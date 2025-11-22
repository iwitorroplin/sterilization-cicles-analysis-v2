from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QButtonGroup, QLabel, QFrame
from PySide6.QtCore import Signal, Qt

class Sidebar(QWidget):
    module_selected = Signal(str)
    
    def __init__(self):
        super().__init__()
        self.setup_ui()
    
    def setup_ui(self):
        self.setFixedWidth(200)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 20, 10, 20)
        layout.setSpacing(10)
        
        # Título
        title = QLabel("Sistema de Análisis")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 16px; font-weight: bold; margin-bottom: 20px;")
        layout.addWidget(title)
        
        # Separador
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        layout.addWidget(separator)
        
        # Grupo de botones
        self.button_group = QButtonGroup()
        self.button_group.setExclusive(True)
        
        # Módulos
        modules = [
            ("Dashboard", "dashboard"),
            ("Carga de Datos", "carga_datos"),
            ("Análisis", "analisis"),
            ("Visualización", "visualizacion"),
            ("Reportes", "reportes"),
            ("Configuración", "configuracion")
        ]
        
        for text, name in modules:
            btn = QPushButton(text)
            btn.setCheckable(True)
            btn.setStyleSheet("""
                QPushButton {
                    text-align: left;
                    padding: 10px;
                    border: none;
                    border-radius: 5px;
                    font-size: 14px;
                }
                QPushButton:hover {
                    background-color: #e0e0e0;
                }
                QPushButton:checked {
                    background-color: #007acc;
                    color: white;
                }
            """)
            btn.clicked.connect(lambda checked, n=name: self.module_selected.emit(n))
            self.button_group.addButton(btn)
            layout.addWidget(btn)
        
        layout.addStretch()
    
    def set_active_module(self, module_name: str):
        """Marca un módulo como activo"""
        for btn in self.button_group.buttons():
            if btn.text().lower().replace(" ", "_") == module_name:
                btn.setChecked(True)
                break