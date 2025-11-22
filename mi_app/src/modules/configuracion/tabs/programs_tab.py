from __future__ import annotations

from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QAbstractItemView,
    QHeaderView,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
    QDoubleSpinBox,
    QCheckBox,
)

from src.style import Style
from modules.configuracion.models import ProgramFormData


class ProgramsTab(QWidget):
    """Gestión de programas en una tabla dedicada."""

    program_added = Signal(dict)
    program_deleted = Signal(int)

    def __init__(self):
        super().__init__()
        self._build_ui()

    def _build_ui(self) -> None:
        layout = QVBoxLayout(self)
        main_layout = Style.layout.main()
        layout.setContentsMargins(*main_layout["margins"])
        layout.setSpacing(main_layout["spacing"])

        layout.addWidget(self._build_table())
        layout.addLayout(self._build_form())
        layout.addLayout(self._build_actions())

        Style.widget.apply(self)

    def _build_table(self) -> QWidget:
        container = QWidget()
        table_layout = QVBoxLayout(container)
        table_layout.setContentsMargins(0, 0, 0, 0)
        table_layout.setSpacing(Style.config.Layout.MAIN_SPACING)

        title = QLabel("Programas configurados")
        Style.label.apply(title, "normal")
        table_layout.addWidget(title)

        self.table = QTableWidget(0, 6)
        self.table.setHorizontalHeaderLabels(
            [
                "ID",
                "Nombre",
                "Producto",
                "Formato",
                "Tiempo",
                "Temp. objetivo",
            ]
        )
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.verticalHeader().setVisible(False)
        self.table.itemSelectionChanged.connect(self._update_actions_state)

        Style.table.apply(self.table)

        table_layout.addWidget(self.table)
        return container

    def _build_form(self) -> QHBoxLayout:
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(Style.config.Layout.MAIN_SPACING)

        self.program_name_input = QLineEdit()
        self.product_input = QLineEdit()
        self.format_input = QLineEdit()
        self.target_time_input = QDoubleSpinBox()
        self.target_time_input.setRange(0, 1000)
        self.target_temperature_input = QDoubleSpinBox()
        self.target_temperature_input.setRange(0, 300)
        self.enabled_checkbox = QCheckBox("Habilitado")
        self.enabled_checkbox.setChecked(True)

        fields = [
            ("Nombre", self.program_name_input),
            ("Producto", self.product_input),
            ("Formato", self.format_input),
            ("Tiempo objetivo", self.target_time_input),
            ("Temperatura objetivo", self.target_temperature_input),
        ]

        for label_text, widget in fields:
            column = QVBoxLayout()
            column.setContentsMargins(0, 0, 0, 0)
            column.setSpacing(6)

            label = QLabel(label_text)
            Style.label.apply(label)
            column.addWidget(label)

            if isinstance(widget, QLineEdit):
                Style.input.apply(widget)
            else:
                Style.input.apply(widget)

            column.addWidget(widget)
            layout.addLayout(column)

        layout.addWidget(self.enabled_checkbox)
        Style.checkbox.apply(self.enabled_checkbox)

        return layout

    def _build_actions(self) -> QHBoxLayout:
        layout = QHBoxLayout()
        buttons_layout = Style.layout.buttons()
        layout.setContentsMargins(*buttons_layout["margins"])
        layout.setSpacing(buttons_layout["spacing"])

        self.add_program_btn = QPushButton("Añadir")
        self.delete_program_btn = QPushButton("Eliminar")

        self.add_program_btn.clicked.connect(self._emit_add)
        self.delete_program_btn.clicked.connect(self._emit_delete)

        Style.button.secondary(self.add_program_btn)
        Style.button.secondary(self.delete_program_btn)

        layout.addStretch()
        layout.addWidget(self.add_program_btn)
        layout.addWidget(self.delete_program_btn)

        self._update_actions_state()
        return layout

    # Public API
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
            self.table.setSpan(0, 1, 1, 5)

        self._update_actions_state()

    def clear_program_form(self) -> None:
        self.program_name_input.clear()
        self.product_input.clear()
        self.format_input.clear()
        self.target_time_input.setValue(0)
        self.target_temperature_input.setValue(0)
        self.enabled_checkbox.setChecked(True)

    # Emitters
    def _emit_add(self) -> None:
        payload = ProgramFormData(
            program_name=self.program_name_input.text(),
            product_name=self.product_input.text(),
            format=self.format_input.text(),
            target_time=self.target_time_input.value(),
            target_temperature=self.target_temperature_input.value(),
            enabled=self.enabled_checkbox.isChecked(),
        )
        self.program_added.emit(payload.to_dict())

    def _emit_delete(self) -> None:
        current_row = self.table.currentRow()
        if current_row < 0:
            return

        program_id_item = self.table.item(current_row, 0)
        if not program_id_item:
            return

        self.program_deleted.emit(int(program_id_item.text()))

    def _update_actions_state(self) -> None:
        has_selection = len(self.table.selectedIndexes()) > 0
        self.delete_program_btn.setEnabled(has_selection)
