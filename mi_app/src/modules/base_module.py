from abc import ABC, abstractmethod
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QObject

class BaseModule(QObject, ABC):
    def __init__(self, name: str, icon: str = ""):
        super().__init__()
        self._name = name
        self._icon = icon
    
    @abstractmethod
    def get_view(self) -> QWidget:
        pass
    
    @abstractmethod
    def get_controller(self) -> QObject:
        pass
    
    def get_name(self) -> str:
        return self._name
    
    def get_icon(self) -> str:
        return self._icon
    
    def on_activate(self):
        """Se ejecuta cuando el módulo se activa"""
        pass