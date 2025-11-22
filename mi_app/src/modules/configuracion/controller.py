from __future__ import annotations

from PySide6.QtWidgets import QMessageBox

from modules.base_module import BaseModule
from core.session import Session
from shared.validators import ConfigValidators, ProgramValidators
from .view import ConfigView


class ConfigController(BaseModule):
    def __init__(self, session: Session) -> None:
        super().__init__("configuracion", "Configuración", "⚙️")
        self.session = session
        self._view = ConfigView()
        self._connect()

    def _connect(self) -> None:
        self._view.config_updated.connect(self._update_config)
        self._view.program_added.connect(self._add_program)
        self._view.program_deleted.connect(self._delete_program)

    def view(self):
        return self._view

    def on_activate(self) -> None:
        self._reload()

    def _reload(self) -> None:
        config_service = self.session.get_config_service()
        self._view.load_app_config(config_service.get_app_config())
        self._view.load_programs(config_service.get_programs_config().programs)
        self._view.clear_program_form()

    def _update_config(self, section: str, payload: dict) -> None:
        if section == "general":
            validations = [
                ConfigValidators.validate_directory(payload["data_ferlo_dir"]),
                ConfigValidators.validate_directory(payload["raw_data_ferlo_dir"]),
                ConfigValidators.validate_directory(payload["process_data_ferlo_dir"]),
            ]
            if not all(v.is_valid for v in validations):
                self._alert("Revisa que las rutas no estén vacías.")
                return

        self.session.get_config_service().update_app_config(section, payload)
        self._alert("Configuración guardada correctamente", QMessageBox.Information)

    def _add_program(self, program_data: dict) -> None:
        validation = ProgramValidators.validate_program(program_data)
        if not validation.is_valid:
            self._alert("\n".join(validation.errors))
            return
        service = self.session.get_config_service()
        service.add_program(program_data)
        self._reload()

    def _delete_program(self, program_id: int) -> None:
        service = self.session.get_config_service()
        service.delete_program(program_id)
        self._reload()

    def _alert(self, message: str, icon=QMessageBox.Warning) -> None:
        QMessageBox(icon, "Configuración", message, parent=self._view).exec()
