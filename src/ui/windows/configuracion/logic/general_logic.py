from copy import deepcopy

from PySide6.QtWidgets import QFileDialog, QMessageBox

from src.core.app_settings import AppSettings


default_app_config = {
    "general": {
        "printer": "Predeterminada",
        "data_ferlo_dir": "C:/Users/Usuario/Desktop/ferlo",
        "raw_data_ferlo_dir": "C:/Users/Usuario/Desktop/ferlo/raw",
        "process_data_ferlo_dir": "C:/Users/Usuario/Desktop/ferlo/process",
    },
    "cycle_detector": {
        "temperature_cycle_detector": 70,
        "auto_cycle_detection": True,
        "bad_value_cycle_detector": "<<<<<<<<",
    },
}


class GeneralLogicMixin:
    CONFIG_FILE = "app_config"
    GENERAL_KEY = "general"
    CYCLE_KEY = "cycle_detector"

    def initialize(self):
        """Carga la configuración básica en los campos de la pestaña."""
        loaded_config = AppSettings.get_basic_config() or {}

        general_config = {
            **self.default_config[self.GENERAL_KEY],
            **loaded_config.get(self.GENERAL_KEY, {}),
        }
        cycle_config = {
            **self.default_config[self.CYCLE_KEY],
            **loaded_config.get(self.CYCLE_KEY, {}),
        }

        self.current_config = {
            self.GENERAL_KEY: deepcopy(general_config),
            self.CYCLE_KEY: deepcopy(cycle_config),
        }
        self.last_loaded_config = deepcopy(self.current_config)

        self.apply_to_ui()

    # ------------------------------------------------------
    # Aplicación en la UI
    # ------------------------------------------------------
    def apply_to_ui(self):
        general_config = self.current_config.get(self.GENERAL_KEY, {})
        cycle_config = self.current_config.get(self.CYCLE_KEY, {})

        printer = general_config.get("printer")
        index = self.printer_combo.findText(printer)
        self.printer_combo.setCurrentIndex(index if index >= 0 else 0)

        self.ferlo_dir_edit.setText(general_config.get("data_ferlo_dir", ""))
        self.raw_path_edit.setText(general_config.get("raw_data_ferlo_dir", ""))
        self.process_path_edit.setText(general_config.get("process_data_ferlo_dir", ""))

        temp_c = cycle_config.get("temperature_cycle_detector", "")
        self.temp_c_edit.setText(str(temp_c))
        self.auto_cycle_checkbox.setChecked(bool(cycle_config.get("auto_cycle_detection")))
        self.bad_value_edit.setText(cycle_config.get("bad_value_cycle_detector", ""))

    def get_ui_values(self):
        return {
            self.GENERAL_KEY: {
                "printer": self.printer_combo.currentText(),
                "data_ferlo_dir": self.ferlo_dir_edit.text().strip(),
                "raw_data_ferlo_dir": self.raw_path_edit.text().strip(),
                "process_data_ferlo_dir": self.process_path_edit.text().strip(),
            },
            self.CYCLE_KEY: {
                "temperature_cycle_detector": self.temp_c_edit.text().strip(),
                "auto_cycle_detection": self.auto_cycle_checkbox.isChecked(),
                "bad_value_cycle_detector": self.bad_value_edit.text().strip(),
            },
        }

    # ------------------------------------------------------
    # Eventos de navegación
    # ------------------------------------------------------
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

        temp_value = self.temp_c_edit.text().strip()
        if not temp_value:
            errors.append("La temperatura de inicio de ciclos es obligatoria.")
        else:
            try:
                float(temp_value)
            except ValueError:
                errors.append("La temperatura de inicio de ciclos debe ser numérica.")

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
            self.current_config = deepcopy(self.default_config)
            self.apply_to_ui()

    # ------------------------------------------------------
    # Deshacer
    # ------------------------------------------------------
    def undo_changes(self):
        self.current_config = deepcopy(self.last_loaded_config)
        self.apply_to_ui()

    def save_config(self):
        """
        Valida, actualiza current_config desde la UI,
        y guarda en AppSettings la sección 'general'.
        """
        self.current_config = self.get_ui_values()

        errors = self.validate_fields()
        if errors:
            QMessageBox.warning(self, "Errores", "\n".join(errors))
            return

        AppSettings.set_basic_config(self.current_config)
        self.last_loaded_config = deepcopy(self.current_config)
        QMessageBox.information(self, "Éxito", "Configuración guardada.")
