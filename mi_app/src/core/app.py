from PySide6.QtWidgets import QMainWindow
from .router import Router
from ui.main_window import MainWindow

class Application(QMainWindow):
    def __init__(self, router: Router):
        super().__init__()
        self.router = router
        self.main_window = MainWindow(router)
        self.setCentralWidget(self.main_window)
        self.setWindowTitle("Sistema de Análisis de Datos")
        self.setGeometry(100, 100, 1400, 900)