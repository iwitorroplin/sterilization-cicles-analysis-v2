from PySide6.QtCore import QObject, Signal
from typing import Dict
from modules.base_module import BaseModule

class Router(QObject):
    module_changed = Signal(str)  # module_name
    
    def __init__(self):
        super().__init__()
        self._modules: Dict[str, BaseModule] = {}
        self._current_module: str = ""
    
    def register_module(self, name: str, module: BaseModule):
        self._modules[name] = module
    
    def navigate_to(self, module_name: str):
        if module_name in self._modules and module_name != self._current_module:
            self._current_module = module_name
            self.module_changed.emit(module_name)
    
    def get_current_module(self) -> str:
        return self._current_module
    
    def get_module(self, name: str) -> BaseModule:
        return self._modules[name]