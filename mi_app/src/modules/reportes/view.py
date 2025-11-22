from __future__ import annotations

from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton


class ReportesView(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self._init_ui()

    def _init_ui(self) -> None:
        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(12)

        title = QLabel("Reportes")
        title.setStyleSheet("font-size: 18px; font-weight: 700;")
        layout.addWidget(title)

        self.description = QTextEdit()
        self.description.setReadOnly(True)
        self.description.setText(
            "Genera PDFs con resúmenes de los ciclos, métricas básicas y trazabilidad.\n"
            "Esta sección deja preparado el espacio para conectar motores de plantillas como Jinja2 y reportlab."
        )

        self.generate_button = QPushButton("Generar reporte de ejemplo")

        layout.addWidget(self.description)
        layout.addWidget(self.generate_button)
        layout.addStretch()

    def render_report_message(self, text: str) -> None:
        self.description.setText(text)
