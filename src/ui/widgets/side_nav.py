from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel
)
from PySide6.QtCore import Signal
from src.style import Style
from src.core.config import SIDEBAR_WIDTH

class SidebarWidget(QWidget):
    module_changed = Signal(str)
    
    def __init__(self):
        super().__init__()
        self.current_button = None
        self.buttons = {}  # Diccionario: nombre_módulo -> botón
        self._build_sidebar()
        
    def _build_sidebar(self):
        """Construye el sidebar"""
        self.setFixedWidth(SIDEBAR_WIDTH)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(5, 10, 5, 10)
        
        # Título
        title = QLabel("Navegación")
        title.setStyleSheet("font-size: 16px; font-weight: bold; margin: 10px;")
        layout.addWidget(title)
        
        layout.addStretch()
        self.setLayout(layout)
        
        Style.widget.apply(layout)
    
    def add_module(self, module_name, icon_text="»"):
        """Añade un módulo al sidebar"""
        btn = QPushButton(f"{icon_text} {module_name}")
        btn.setCheckable(True)       
        btn.clicked.connect(lambda: self._on_module_clicked(module_name, btn))
        
        # Insertar antes del stretch
        self.layout().insertWidget(self.layout().count() - 1, btn)
        self.buttons[module_name] = btn
    
    def _on_module_clicked(self, module_name, button):
        """Maneja el clic en un módulo"""
        if self.current_button:
            self.current_button.setChecked(False)
        
        button.setChecked(True)
        self.current_button = button
        self.module_changed.emit(module_name)
    
    def set_active_module(self, module_name):
        """Establece un módulo como activo"""
        if module_name in self.buttons:
            self._on_module_clicked(module_name, self.buttons[module_name])