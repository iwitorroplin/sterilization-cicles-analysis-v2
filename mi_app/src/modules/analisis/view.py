from __future__ import annotations

from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem
from PySide6.QtCore import Qt


class AnalisisView(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self._init_ui()

    def _init_ui(self) -> None:
        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(12)

        title = QLabel("Análisis de datos cargados")
        title.setStyleSheet("font-size: 18px; font-weight: 700;")
        layout.addWidget(title)

        self.summary_table = QTableWidget(0, 2)
        self.summary_table.setHorizontalHeaderLabels(["Métrica", "Valor"])
        self.summary_table.horizontalHeader().setStretchLastSection(True)

        layout.addWidget(self.summary_table)
        layout.addStretch()

    def render_summary(self, summary: dict[str, str]) -> None:
        self.summary_table.setRowCount(len(summary))
        for row, (metric, value) in enumerate(summary.items()):
            self.summary_table.setItem(row, 0, QTableWidgetItem(metric))
            self.summary_table.setItem(row, 1, QTableWidgetItem(value))

        if not summary:
            self.summary_table.setRowCount(1)
            self.summary_table.setItem(0, 0, QTableWidgetItem("Sin datos"))
            self.summary_table.setItem(0, 1, QTableWidgetItem("Carga un CSV en 'Carga de Datos'"))
