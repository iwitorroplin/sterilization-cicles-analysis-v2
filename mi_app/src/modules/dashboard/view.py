from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from ui.widgets.tab_panel import TabPanel

class DashboardView(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
    
    def setup_ui(self):
        layout = QVBoxLayout(self)
        
        self.tab_panel = TabPanel()
        
        # Pestañas
        summary_tab = self.create_summary_tab()
        self.tab_panel.add_tab("Resumen", summary_tab)
        
        metrics_tab = self.create_metrics_tab()
        self.tab_panel.add_tab("Métricas", metrics_tab)
        
        layout.addWidget(self.tab_panel)
    
    def create_summary_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        layout.addWidget(QLabel("Resumen del sistema..."))
        return tab
    
    def create_metrics_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        layout.addWidget(QLabel("Métricas del sistema..."))
        return tab