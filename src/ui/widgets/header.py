from PySide6.QtWidgets import (
    QLabel,
    QVBoxLayout,
    QWidget
    )

from PySide6.QtCore import Qt

from src.core.config import APP_TITLE
from src.style import Style

class HeaderWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        self._build_header()
        
    def _build_header(self):
        """Crea el header de la aplicación"""

        self.setFixedHeight(60)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        header_label = QLabel(APP_TITLE)
        header_label.setAlignment(Qt.AlignCenter)

        Style.label.title(header_label)

        layout.addWidget(header_label)
        self.setLayout(layout)
        Style.widget.apply(self)