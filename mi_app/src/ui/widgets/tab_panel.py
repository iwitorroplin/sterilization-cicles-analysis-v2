from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QStackedWidget
from PySide6.QtCore import Qt

class TabPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.tab_buttons = []
        self.tab_names = []
        self.setup_ui()
    
    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        # Layout para botones de pestañas
        self.tabs_layout = QHBoxLayout()
        self.tabs_layout.setAlignment(Qt.AlignLeft)
        self.tabs_layout.setSpacing(0)
        
        # Widget para contenido
        self.content_stack = QStackedWidget()
        
        layout.addLayout(self.tabs_layout)
        layout.addWidget(self.content_stack)
    
    def add_tab(self, name: str, widget: QWidget):
        """Añade una nueva pestaña"""
        tab_index = len(self.tab_buttons)
        
        tab_button = QPushButton(name)
        tab_button.setCheckable(True)
        tab_button.setProperty("tab_index", tab_index)
        
        # Estilo
        tab_button.setStyleSheet("""
            QPushButton {
                padding: 8px 16px;
                border: 1px solid #ccc;
                border-bottom: none;
                border-radius: 4px 4px 0 0;
                background-color: #f8f9fa;
                margin-right: 2px;
            }
            QPushButton:checked {
                background-color: white;
                border-color: #007acc;
                color: #007acc;
                font-weight: bold;
            }
            QPushButton:hover:!checked {
                background-color: #e9ecef;
            }
        """)
        
        tab_button.clicked.connect(
            lambda checked, idx=tab_index: self.switch_tab(idx)
        )
        
        self.tab_buttons.append(tab_button)
        self.tab_names.append(name)
        self.tabs_layout.addWidget(tab_button)
        
        self.content_stack.addWidget(widget)
        
        # Activar primera pestaña por defecto
        if len(self.tab_buttons) == 1:
            tab_button.setChecked(True)
    
    def switch_tab(self, index: int):
        """Cambia a la pestaña especificada"""
        if 0 <= index < len(self.tab_buttons):
            for i, button in enumerate(self.tab_buttons):
                button.setChecked(i == index)
            self.content_stack.setCurrentIndex(index)
    
    def get_current_tab_index(self) -> int:
        return self.content_stack.currentIndex()