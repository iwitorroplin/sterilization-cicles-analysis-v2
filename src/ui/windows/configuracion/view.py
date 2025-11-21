from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from src.style import Style


class ModuleView(QWidget):
    def __init__(self):
        super().__init__()
        self._build_ui()

    def _build_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(12)

        title = QLabel("Configuración")
        Style.label.title(title)
        title.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        status = QLabel("Módulo en construcción")
        status.setAlignment(Qt.AlignCenter)
        Style.label.subtle(status)

        layout.addWidget(title)
        layout.addStretch()
        layout.addWidget(status)
        layout.addStretch()

        self.setLayout(layout)
        Style.widget.apply(self)
