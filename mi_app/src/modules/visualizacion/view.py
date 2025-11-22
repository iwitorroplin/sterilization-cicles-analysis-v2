from __future__ import annotations

from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit


class VisualizacionView(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self._init_ui()

    def _init_ui(self) -> None:
        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(12)

        title = QLabel("Visualización")
        title.setStyleSheet("font-size: 18px; font-weight: 700;")
        layout.addWidget(title)

        self.notes = QTextEdit()
        self.notes.setReadOnly(True)
        self.notes.setText(
            "Configura las vistas que quieras mostrar a partir de los datos cargados.\n"
            "Esta pantalla actúa como plantilla para integrar gráficos o dashboards especializados."
        )

        layout.addWidget(self.notes)
        layout.addStretch()
