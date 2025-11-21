
import time
from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve, QTimer
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton
from src.ui.widgets.loading_dialog import LoadingDialog
from src.core.loading_manager import LoadingManager

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplicación Principal")
        self.setGeometry(100, 100, 600, 400)
        self.setup_ui()
        
        self.loading_manager = LoadingManager(self)
    
    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        # Botón para loading simple
        btn_simple = QPushButton("Loading Simple")
        btn_simple.clicked.connect(self.show_simple_loading)
        layout.addWidget(btn_simple)
        
        # Botón para loading en serie
        btn_series = QPushButton("Loading en Serie")
        btn_series.clicked.connect(self.show_series_loading)
        layout.addWidget(btn_series)
    
    def show_simple_loading(self):
        """Ejemplo de uso simple"""
        loading = LoadingDialog(self, "Cargando configuración...")
        loading.show()
        
        # Simular proceso y cerrar
        QTimer.singleShot(2000, loading.fade_out_and_close)
    
    def show_series_loading(self):
        """Ejemplo de uso con múltiples procesos"""
        processes = [
            ("Config: Carga y validación...", self.simulate_config, []),
            ("Style: Aplicando estilos...", self.simulate_style, []),
            ("Finalizando...", self.simulate_final, [])
        ]
        
        self.loading_manager.start_loading(processes)
    
    def simulate_config(self):
        time.sleep(1.5)
    
    def simulate_style(self):
        time.sleep(1.2)
    
    def simulate_final(self):
        time.sleep(0.8)