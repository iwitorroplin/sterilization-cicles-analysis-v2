from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget
from PySide6.QtCore import Qt
from src.style import Style

class FooterWidget(QWidget):
    def __init__(self, initial_text="Listo"):
        super().__init__()
        self.footer_label = None
        self._build_footer(initial_text)
        
    def _build_footer(self, initial_text):
        """Construye el footer de la aplicación"""
        self.setFixedHeight(30)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.footer_label = QLabel(initial_text)
        self.footer_label.setAlignment(Qt.AlignCenter)

        Style.label.subtle(self.footer_label)

        layout.addWidget(self.footer_label)
        self.setLayout(layout)
        Style.widget.apply(self)
    
    def update_status(self, text):
        """Actualiza el texto del footer"""
        if self.footer_label:
            self.footer_label.setText(text)