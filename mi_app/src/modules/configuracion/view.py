from __future__ import annotations

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QFormLayout,
    QLineEdit,
    QPushButton,
    QGroupBox,
    QHBoxLayout,
    QDoubleSpinBox,
    QCheckBox,
    QTableWidget,
    QTableWidgetItem,
)
from PySide6.QtCore import Signal, Qt

from shared.validators import ConfigValidators
from .models import ProgramFormData


class ConfigView(QWidget):
    config_updated = Signal(str, dict)  # section, payload
    program_added = Signal(dict)
    program_selected = Signal(int)
    program_deleted = Signal(int)

    def __init__(self) -> None:
        super().__init__()
        self._init_ui()

    def _init_ui(self) -> None:
        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(12)

        title = QLabel("Configuración")
        title.setStyleSheet("font-size: 18px; font-weight: 700;")
        layout.addWidget(title)

        layout.addWidget(self._build_general_group())
        layout.addWidget(self._build_cycle_group())
        layout.addWidget(self._build_programs_group())
        layout.addStretch()

    def _build_general_group(self) -> QGroupBox:
        group = QGroupBox("General")
        form = QFormLayout(group)
        self.printer_input = QLineEdit()
        self.ferlo_dir_input = QLineEdit()
        self.raw_dir_input = QLineEdit()
        self.process_dir_input = QLineEdit()
        self.save_general_btn = QPushButton("Guardar general")
        self.save_general_btn.clicked.connect(self._emit_general)

        form.addRow("Impresora", self.printer_input)
        form.addRow("Directorio Ferlo", self.ferlo_dir_input)
        form.addRow("Directorio Raw", self.raw_dir_input)
        form.addRow("Directorio Process", self.process_dir_input)
        form.addRow(self.save_general_btn)
        return group

    def _emit_general(self) -> None:
        payload = {
            "printer": self.printer_input.text(),
            "data_ferlo_dir": self.ferlo_dir_input.text(),
            "raw_data_ferlo_dir": self.raw_dir_input.text(),
            "process_data_ferlo_dir": self.process_dir_input.text(),
        }
        self.config_updated.emit("general", payload)

    def _build_cycle_group(self) -> QGroupBox:
        group = QGroupBox("Detector de ciclos")
        form = QFormLayout(group)
        self.temperature_input = QDoubleSpinBox()
        self.temperature_input.setRange(0, 300)
        self.auto_checkbox = QCheckBox("Detección automática")
        self.bad_value_input = QLineEdit()
        self.save_cycle_btn = QPushButton("Guardar detector")
        self.save_cycle_btn.clicked.connect(self._emit_cycle)

        form.addRow("Temperatura umbral", self.temperature_input)
        form.addRow("Auto", self.auto_checkbox)
        form.addRow("Marcador de error", self.bad_value_input)
        form.addRow(self.save_cycle_btn)
        return group

    def _emit_cycle(self) -> None:
        payload = {
            "temperature": self.temperature_input.value(),
            "auto": self.auto_checkbox.isChecked(),
            "bad_value": self.bad_value_input.text(),
        }
        self.config_updated.emit("cycle_detector", payload)

    def _build_programs_group(self) -> QGroupBox:
        group = QGroupBox("Programas")
        layout = QVBoxLayout(group)
        self.table = QTableWidget(0, 6)
        self.table.setHorizontalHeaderLabels([
            "ID",
            "Nombre",
            "Producto",
            "Formato",
            "Tiempo",
            "Temp. objetivo",
        ])
        self.table.horizontalHeader().setStretchLastSection(True)
        layout.addWidget(self.table)

        # Formulario compacto para nuevas filas
        form_layout = QFormLayout()
        self.program_name_input = QLineEdit()
        self.product_input = QLineEdit()
        self.format_input = QLineEdit()
        self.target_time_input = QDoubleSpinBox()
        self.target_time_input.setRange(0, 1000)
        self.target_temp_input = QDoubleSpinBox()
        self.target_temp_input.setRange(0, 300)
        self.enabled_checkbox = QCheckBox("Habilitado")
        self.enabled_checkbox.setChecked(True)

        form_layout.addRow("Nombre", self.program_name_input)
        form_layout.addRow("Producto", self.product_input)
        form_layout.addRow("Formato", self.format_input)
        form_layout.addRow("Tiempo objetivo", self.target_time_input)
        form_layout.addRow("Temperatura objetivo", self.target_temp_input)
        form_layout.addRow(self.enabled_checkbox)

        self.add_program_btn = QPushButton("Añadir programa")
        self.delete_program_btn = QPushButton("Eliminar seleccionado")

        buttons = QHBoxLayout()
        buttons.addWidget(self.add_program_btn)
        buttons.addWidget(self.delete_program_btn)

        layout.addLayout(form_layout)
        layout.addLayout(buttons)

        self.add_program_btn.clicked.connect(self._emit_program_add)
        self.delete_program_btn.clicked.connect(self._emit_program_delete)

        return group

    def _emit_program_add(self) -> None:
        payload = ProgramFormData(
            program_name=self.program_name_input.text(),
            product_name=self.product_input.text(),
            format=self.format_input.text(),
            target_time=self.target_time_input.value(),
            target_temperature=self.target_temp_input.value(),
            enabled=self.enabled_checkbox.isChecked(),
        )
        self.program_added.emit(payload.to_dict())

    def _emit_program_delete(self) -> None:
        current_row = self.table.currentRow()
        if current_row < 0:
            return
        program_id = int(self.table.item(current_row, 0).text())
        self.program_deleted.emit(program_id)

    # Render helpers
    def load_app_config(self, app_config) -> None:
        self.printer_input.setText(app_config.general.printer)
        self.ferlo_dir_input.setText(app_config.general.data_ferlo_dir)
        self.raw_dir_input.setText(app_config.general.raw_data_ferlo_dir)
        self.process_dir_input.setText(app_config.general.process_data_ferlo_dir)

        self.temperature_input.setValue(app_config.cycle_detector.temperature)
        self.auto_checkbox.setChecked(app_config.cycle_detector.auto)
        self.bad_value_input.setText(app_config.cycle_detector.bad_value)

    def load_programs(self, programs) -> None:
        self.table.setRowCount(len(programs))
        for row, program in enumerate(programs):
            self.table.setItem(row, 0, QTableWidgetItem(str(program.program_id)))
            self.table.setItem(row, 1, QTableWidgetItem(program.program_name))
            self.table.setItem(row, 2, QTableWidgetItem(program.product_name))
            self.table.setItem(row, 3, QTableWidgetItem(program.format))
            self.table.setItem(row, 4, QTableWidgetItem(str(program.target_time)))
            self.table.setItem(row, 5, QTableWidgetItem(str(program.target_temperature)))

        if not programs:
            self.table.setRowCount(1)
            self.table.setItem(0, 0, QTableWidgetItem("-"))
            self.table.setItem(0, 1, QTableWidgetItem("No hay programas"))

    def clear_program_form(self) -> None:
        self.program_name_input.clear()
        self.product_input.clear()
        self.format_input.clear()
        self.target_time_input.setValue(0)
        self.target_temp_input.setValue(0)
        self.enabled_checkbox.setChecked(True)
