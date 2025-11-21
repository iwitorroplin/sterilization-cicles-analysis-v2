
from typing import Dict, Optional, Type

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QLabel,
    QMessageBox,
    QPushButton,
    QHBoxLayout,
    QMainWindow,
    QSizePolicy,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)
import importlib

from src.core.config import (
    APP_NAME,
    APP_VERSION,
    WINDOW_MIN_WIDTH,
    WINDOW_MIN_HEIGHT,
)

from src.core.module_manager import ModuleManager

from src.ui.widgets.header import HeaderWidget
from src.ui.widgets.footer import FooterWidgetWidget
from src.ui.widgets.side_nav import SideWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # ❌ Quitar la X de la ventana
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        
        self.setWindowTitle(f"{APP_NAME}  v{APP_VERSION}")
        self.setMinimumSize(WINDOW_MIN_WIDTH, WINDOW_MIN_HEIGHT)
        
        # Inicializar gestor de módulos
        self.module_manager = ModuleManager()
        
        # Configurar UI
        self._setup_ui()
        
        
        # Cargar módulo inicial
        self._load_module("Dashboard")
    
    
    
    
    def _setup_ui(self):
        """Configura la interfaz de usuario"""
        # Contenedor principal
        root_container = QWidget()
        root_container.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        app_layout = QVBoxLayout()
        app_layout.setContentsMargins(0, 0, 0, 0)
        app_layout.setSpacing(0)
        
        # Header
        app_layout.addWidget(self._create_header(), stretch=0)
        
        # Body: nav + content
        self.body_widget = QWidget()
        self.body_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        self.body_layout = QHBoxLayout()
        self.body_layout.setContentsMargins(0, 0, 0, 0)
        self.body_layout.setSpacing(0)
        
        # Side Navigation
        self.side_nav = self._create_side_nav()
        self.body_layout.addWidget(self.side_nav, stretch=0)
        
        # Content Area con QStackedWidget
        self.content_stack = self._create_content_stack()
        self.body_layout.addWidget(self.content_stack, stretch=1)
        
        self.body_widget.setLayout(self.body_layout)
        app_layout.addWidget(self.body_widget, stretch=1)
        
        # Footer
        app_layout.addWidget(self._create_footer(), stretch=0)
        
        root_container.setLayout(app_layout)
        self.setCentralWidget(root_container)