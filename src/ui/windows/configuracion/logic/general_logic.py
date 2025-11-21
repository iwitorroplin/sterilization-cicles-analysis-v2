from PySide6.QtWidgets import (
    QFileDialog,
)

from copy import deepcopy
from src.core.app_settings import AppSettings

default_app_config = {
  "general": {
    "printer": "Predeterminada",
    "data_ferlo_dir": "C:/Users/Usuario/Desktop/ferlo",
    "raw_data_ferlo_dir": "C:/Users/Usuario/Desktop/ferlo/raw",
    "process_data_ferlo_dir": "C:/Users/Usuario/Desktop/ferlo/process"
  },
  "cycle_detector": {
    "temperature": 70,
    "auto": True,
    "bad_value": "<<<<<<<<"
  }
}



def initialize(self):

    CONFIG_FILE = "app_config"
    GENERAL_KEY = "general"
    CYCLE_KEY = "cycle_detector"

    """Carga la configuración básica en los campos de la pestaña."""
    loaded_config = AppSettings.get_basic_config() or {}

    general_config = {
        self.default_config[GENERAL_KEY],
        loaded_config.get(GENERAL_KEY, {}),
    }
    cycle_config = {
        **self.default_config[CYCLE_KEY],
        **loaded_config.get(self.CYCLE_KEY, {}),
    }

    self.current_config = {
        self.GENERAL_KEY: deepcopy(general_config),
        self.CYCLE_KEY: deepcopy(cycle_config),
    }
    self.last_loaded_config = deepcopy(self.current_config)

    printer = general_config.get("printer")
    ferlo_dir = general_config.get("data_ferlo_dir")
    raw_dir = general_config.get("raw_data_ferlo_dir")
    process_dir = general_config.get("process_data_ferlo_dir")

    index = self.printer_combo.findText(printer)
    self.printer_combo.setCurrentIndex(index if index >= 0 else 0)
    self.ferlo_dir_edit.setText(ferlo_dir)
    self.raw_path_edit.setText(raw_dir)
    self.process_path_edit.setText(process_dir)

    # Configuracion CYCLE DETECTOR
    temp_c = cycle_config.get("temperature_cycle_detector")
    auto_detection = cycle_config.get("auto_cycle_detection")
    bad_value = cycle_config.get("bad_value_cycle_detector")

    self.temp_c_edit.setText(str(temp_c))
    self.auto_cycle_checkbox.setChecked(bool(auto_detection))
    self.bad_value_edit.setText(bad_value)   

    def browse_raw_path(self):
        directory = QFileDialog.getExistingDirectory(
            self, "Seleccionar directorio RAW", self.raw_path_edit.text()
        )
        if directory:
            self.raw_path_edit.setText(directory)

    def browse_ferlo_dir(self):
        directory = QFileDialog.getExistingDirectory(
            self, "Seleccionar directorio principal", self.ferlo_dir_edit.text()
        )
        if directory:
            self.ferlo_dir_edit.setText(directory)

    def browse_process_path(self):
        directory = QFileDialog.getExistingDirectory(
            self,
            "Seleccionar directorio de datos procesados",
            self.process_path_edit.text(),
        )
        if directory:
            self.process_path_edit.setText(directory)

    # ------------------------------------------------------
    # Validaciones
    # ------------------------------------------------------
    def validate_fields(self):
        errors = []

        if not self.raw_path_edit.text().strip():
            errors.append("El directorio RAW no puede estar vacío.")
        if not self.process_path_edit.text().strip():
            errors.append("El directorio PROCESS no puede estar vacío.")

        return errors

    # ------------------------------------------------------
    # Restaurar valores por defecto
    # ------------------------------------------------------
    def restore_defaults(self):
        reply = QMessageBox.question(
            self,
            "Confirmar",
            "¿Restaurar valores por defecto?",
            QMessageBox.Yes | QMessageBox.No,
        )

        if reply == QMessageBox.Yes:
            self.current_config = self.default_config.copy()
            self.data = self.current_config.copy()
            self.apply_to_ui()

    # ------------------------------------------------------
    # Deshacer
    # ------------------------------------------------------
    def undo_changes(self):
        self.current_config = self.last_loaded_config.copy()
        self.data = self.current_config.copy()
        self.apply_to_ui()

    def save_config(self):
        """
        Valida, actualiza current_config desde la UI,
        y guarda en app_config.json solo la sección 'general'.
        """
        # 1) Actualizamos current_config desde la UI
        self.current_config.update(self.get_ui_values())

        # 2) Validar
        errors = self.validate_fields()
        if errors:
            QMessageBox.warning(self, "Errores", "\n".join(errors))
            return

        # 3) Guardar
        try:
            self.manager.save_section(
                self.CONFIG_FILE,
                self.CONFIG_KEY,
                self.current_config,
            )
            self.last_loaded_config = self.current_config.copy()
            self.data = self.current_config.copy()
            QMessageBox.information(self, "Éxito", "Configuración guardada.")
        except Exception as exc:
            QMessageBox.critical(self, "Error", f"No se pudo guardar:\n{exc}")
