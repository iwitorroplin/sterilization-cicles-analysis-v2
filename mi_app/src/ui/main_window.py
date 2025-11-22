from PySide6.QtWidgets import QMainWindow, QHBoxLayout, QWidget, QStackedWidget
from .sidebar import Sidebar
from core.router import Router

class MainWindow(QMainWindow):
    def __init__(self, router: Router):
        super().__init__()
        self.router = router
        self.setup_ui()
        self.connect_signals()
    
    def setup_ui(self):
        self.setWindowTitle("Sistema de Análisis de Datos")
        self.setGeometry(100, 100, 1400, 900)
        
        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout principal
        layout = QHBoxLayout(central_widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        # Sidebar
        self.sidebar = Sidebar()
        layout.addWidget(self.sidebar)
        
        # Área de contenido
        self.content_stack = QStackedWidget()
        layout.addWidget(self.content_stack, 1)
    
    def connect_signals(self):
        self.sidebar.module_selected.connect(self.router.navigate_to)
        self.router.module_changed.connect(self.on_module_changed)
    
    def on_module_changed(self, module_name: str):
        """Cambia la vista mostrada cuando cambia el módulo"""
        module = self.router.get_module(module_name)
        view = module.get_view()
        
        # Añadir vista si no está en el stack
        if self.content_stack.indexOf(view) == -1:
            self.content_stack.addWidget(view)
        
        # Mostrar vista
        self.content_stack.setCurrentWidget(view)
        self.sidebar.set_active_module(module_name)
        
        # Activar módulo
        module.on_activate()