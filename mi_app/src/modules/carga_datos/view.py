from __future__ import annotations

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QFileDialog,
    QGroupBox,
    QGridLayout,
    QTextEdit,
)


class CargaDatosView(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self._init_ui()

    def _init_ui(self) -> None:
        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(16)

        title = QLabel("Carga de datos")
        title.setStyleSheet("font-size: 18px; font-weight: 700;")
        layout.addWidget(title)

        self.load_button = QPushButton("Seleccionar CSV")
        layout.addWidget(self.load_button)

        self.metadata_group = QGroupBox("Resumen del archivo")
        meta_layout = QGridLayout(self.metadata_group)
        self.file_label = QLabel("-")
        self.rows_label = QLabel("-")
        self.columns_label = QLabel("-")

        meta_layout.addWidget(QLabel("Archivo:"), 0, 0)
        meta_layout.addWidget(self.file_label, 0, 1)
        meta_layout.addWidget(QLabel("Filas:"), 1, 0)
        meta_layout.addWidget(self.rows_label, 1, 1)
        meta_layout.addWidget(QLabel("Columnas:"), 2, 0)
        meta_layout.addWidget(self.columns_label, 2, 1)

        self.preview_box = QTextEdit()
        self.preview_box.setReadOnly(True)
        self.preview_box.setMinimumHeight(160)

        layout.addWidget(self.metadata_group)
        layout.addWidget(QLabel("Vista previa"))
        layout.addWidget(self.preview_box)
        layout.addStretch()

    def ask_for_file(self) -> str:
        file_path, _ = QFileDialog.getOpenFileName(self, "Seleccionar archivo CSV", filter="CSV (*.csv)")
        return file_path

    def render_metadata(self, metadata: dict | None) -> None:
        if not metadata:
            self.file_label.setText("-")
            self.rows_label.setText("-")
            self.columns_label.setText("-")
            self.preview_box.setText("No hay datos cargados")
            return

        self.file_label.setText(metadata.get("file_path", "-"))
        self.rows_label.setText(str(metadata.get("rows", "-")))
        self.columns_label.setText(", ".join(metadata.get("columns", [])))

    def render_preview(self, text: str) -> None:
        self.preview_box.setText(text)
