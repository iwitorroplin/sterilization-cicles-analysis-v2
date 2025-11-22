from __future__ import annotations

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget, QGroupBox, QGridLayout
from PySide6.QtCore import Qt

from ui.styles import palette


class DashboardView(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self._init_ui()

    def _init_ui(self) -> None:
        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(16)

        self.subtitle = QLabel("Estado general del sistema")
        self.subtitle.setStyleSheet("font-size: 18px; font-weight: 700;")
        layout.addWidget(self.subtitle)

        self.status_group = QGroupBox("Estado de datos")
        status_layout = QGridLayout(self.status_group)

        self.loaded_file_label = QLabel("No hay datos cargados")
        self.loaded_file_label.setStyleSheet(f"color: {palette.MUTED};")
        self.rows_label = QLabel("-")
        self.columns_label = QLabel("-")

        status_layout.addWidget(QLabel("Archivo actual:"), 0, 0)
        status_layout.addWidget(self.loaded_file_label, 0, 1)
        status_layout.addWidget(QLabel("Filas:"), 1, 0)
        status_layout.addWidget(self.rows_label, 1, 1)
        status_layout.addWidget(QLabel("Columnas:"), 2, 0)
        status_layout.addWidget(self.columns_label, 2, 1)

        self.config_group = QGroupBox("Configuración de app")
        config_layout = QGridLayout(self.config_group)
        self.printer_label = QLabel("-")
        self.base_dir_label = QLabel("-")
        config_layout.addWidget(QLabel("Impresora"), 0, 0)
        config_layout.addWidget(self.printer_label, 0, 1)
        config_layout.addWidget(QLabel("Directorio Ferlo"), 1, 0)
        config_layout.addWidget(self.base_dir_label, 1, 1)

        layout.addWidget(self.status_group)
        layout.addWidget(self.config_group)
        layout.addStretch()

    def render_data_status(self, metadata: dict | None) -> None:
        if not metadata:
            self.loaded_file_label.setText("No hay datos cargados")
            self.rows_label.setText("-")
            self.columns_label.setText("-")
            return

        self.loaded_file_label.setText(metadata.get("file_path", ""))
        self.rows_label.setText(str(metadata.get("rows", "-")))
        self.columns_label.setText(", ".join(metadata.get("columns", [])) or "-")

    def render_config(self, printer: str, base_dir: str) -> None:
        self.printer_label.setText(printer)
        self.base_dir_label.setText(base_dir)
