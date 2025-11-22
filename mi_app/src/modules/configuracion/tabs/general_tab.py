from __future__ import annotations

from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QCheckBox,
    QComboBox,
    QDoubleSpinBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)

from src.style import Style


class GeneralTab(QWidget):
    """Sección de configuración general y detector de ciclos."""

    general_saved = Signal(dict)
    detector_saved = Signal(dict)

    def __init__(self):
        super().__init__()
        self._build_ui()

    def _build_ui(self) -> None:
        layout = QVBoxLayout(self)
        main_layout = Style.layout.main()
        layout.setContentsMargins(*main_layout["margins"])
        layout.setSpacing(main_layout["spacing"])

        layout.addWidget(self._build_general_section())
        layout.addWidget(self._build_cycle_section())
        layout.addStretch()
        layout.addLayout(self._build_actions())

        Style.widget.apply(self)

    def _build_general_section(self) -> QWidget:
        container = QWidget()
        container.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        section_layout = QVBoxLayout(container)
        section_layout.setContentsMargins(0, 0, 0, 0)
        section_layout.setSpacing(Style.config.Layout.MAIN_SPACING)

        section_layout.addLayout(self._build_printer_row())
        section_layout.addLayout(self._build_dir_row("Directorio principal:", "ferlo_dir_edit"))
        section_layout.addLayout(self._build_dir_row("Directorio RAW:", "raw_path_edit"))
        section_layout.addLayout(self._build_dir_row("Directorio Process:", "process_path_edit"))

        return container

    def _build_printer_row(self) -> QHBoxLayout:
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(Style.config.Layout.BUTTON_SPACING)

        self.printer_combo = QComboBox()
        self.printer_combo.addItems(["Predeterminada", "Impresora 1", "Impresora 2"])

        label = QLabel("Impresora:")
        layout.addWidget(label)
        layout.addWidget(self.printer_combo)

        Style.label.apply(label)
        Style.combobox.apply(self.printer_combo)
        return layout

    def _build_dir_row(self, label_text: str, attr_name: str) -> QHBoxLayout:
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(Style.config.Layout.BUTTON_SPACING)

        label = QLabel(label_text)
        edit = QLineEdit()
        edit.setPlaceholderText("Selecciona la ruta correspondiente...")

        setattr(self, attr_name, edit)

        browse_btn = QPushButton("...")

        layout.addWidget(label)
        layout.addWidget(edit)
        layout.addWidget(browse_btn)

        Style.label.apply(label)
        Style.input.apply(edit)
        Style.button.terciary(browse_btn)
        return layout

    def _build_cycle_section(self) -> QWidget:
        container = QWidget()
        container.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        layout = QVBoxLayout(container)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(Style.config.Layout.MAIN_SPACING)

        self.temperature_input = QDoubleSpinBox()
        self.temperature_input.setRange(0, 300)
        self.temperature_input.setSuffix(" °C")
        self.auto_checkbox = QCheckBox("Detección automática de ciclos")
        self.bad_value_input = QLineEdit()
        self.bad_value_input.setPlaceholderText("Marcador de error en los datos")

        temp_row = QHBoxLayout()
        temp_row.setContentsMargins(0, 0, 0, 0)
        temp_row.setSpacing(Style.config.Layout.BUTTON_SPACING)
        temp_label = QLabel("Temperatura umbral:")
        temp_row.addWidget(temp_label)
        temp_row.addWidget(self.temperature_input)

        bad_value_row = QHBoxLayout()
        bad_value_row.setContentsMargins(0, 0, 0, 0)
        bad_value_row.setSpacing(Style.config.Layout.BUTTON_SPACING)
        bad_label = QLabel("Marcador de error:")
        bad_value_row.addWidget(bad_label)
        bad_value_row.addWidget(self.bad_value_input)

        Style.label.apply(temp_label)
        Style.label.apply(bad_label)
        Style.input.apply(self.bad_value_input)
        Style.checkbox.apply(self.auto_checkbox)

        layout.addLayout(temp_row)
        layout.addWidget(self.auto_checkbox)
        layout.addLayout(bad_value_row)

        return container

    def _build_actions(self) -> QHBoxLayout:
        layout = QHBoxLayout()
        buttons_layout = Style.layout.buttons()
        layout.setContentsMargins(*buttons_layout["margins"])
        layout.setSpacing(buttons_layout["spacing"])

        self.save_general_btn = QPushButton("Guardar general")
        self.save_detector_btn = QPushButton("Guardar detector")

        self.save_general_btn.clicked.connect(self._emit_general)
        self.save_detector_btn.clicked.connect(self._emit_detector)

        Style.button.secondary(self.save_general_btn)
        Style.button.secondary(self.save_detector_btn)

        layout.addStretch()
        layout.addWidget(self.save_general_btn)
        layout.addWidget(self.save_detector_btn)
        return layout

    # Public API
    def load_app_config(self, app_config) -> None:
        index = self.printer_combo.findText(app_config.general.printer)
        self.printer_combo.setCurrentIndex(index if index >= 0 else 0)
        self.ferlo_dir_edit.setText(app_config.general.data_ferlo_dir)
        self.raw_path_edit.setText(app_config.general.raw_data_ferlo_dir)
        self.process_path_edit.setText(app_config.general.process_data_ferlo_dir)

        self.temperature_input.setValue(app_config.cycle_detector.temperature)
        self.auto_checkbox.setChecked(app_config.cycle_detector.auto)
        self.bad_value_input.setText(app_config.cycle_detector.bad_value)

    # Emitters
    def _emit_general(self) -> None:
        payload = {
            "printer": self.printer_combo.currentText(),
            "data_ferlo_dir": self.ferlo_dir_edit.text(),
            "raw_data_ferlo_dir": self.raw_path_edit.text(),
            "process_data_ferlo_dir": self.process_path_edit.text(),
        }
        self.general_saved.emit(payload)

    def _emit_detector(self) -> None:
        payload = {
            "temperature": self.temperature_input.value(),
            "auto": self.auto_checkbox.isChecked(),
            "bad_value": self.bad_value_input.text(),
        }
        self.detector_saved.emit(payload)
