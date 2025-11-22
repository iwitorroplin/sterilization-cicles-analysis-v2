from modules.base_module import BaseModule
from .view import DashboardView

class DashboardController(BaseModule):
    def __init__(self):
        super().__init__("Dashboard")
        self._view = DashboardView()
    
    def get_view(self):
        return self._view
    
    def get_controller(self):
        return self