from PySide6.QtWidgets import QLineEdit, QDoubleSpinBox
from PySide6.QtCore import Signal
from typing import Callable, Optional

class ValidatedLineEdit(QLineEdit):
    validation_changed = Signal(bool)
    
    def __init__(self, validator: Optional[Callable] = None, parent=None):
        super().__init__(parent)
        self._validator = validator
        self._is_valid = True
        self.textChanged.connect(self._validate)
    
    def set_validator(self, validator: Callable):
        self._validator = validator
        self._validate()
    
    def _validate(self):
        if self._validator is None:
            self._is_valid = True
        else:
            self._is_valid = self._validator(self.text())
        
        self._update_style()
        self.validation_changed.emit(self._is_valid)
    
    def _update_style(self):
        if self._is_valid:
            self.setStyleSheet("border: 1px solid #cccccc;")
        else:
            self.setStyleSheet("border: 1px solid red;")
    
    def is_valid(self) -> bool:
        return self._is_valid

class ValidatedDoubleSpinBox(QDoubleSpinBox):
    validation_changed = Signal(bool)
    
    def __init__(self, min_val: float, max_val: float, parent=None):
        super().__init__(parent)
        self.setRange(min_val, max_val)
        self._is_valid = True
        self.valueChanged.connect(self._validate)
    
    def _validate(self):
        value = self.value()
        self._is_valid = (self.minimum() <= value <= self.maximum())
        self._update_style()
        self.validation_changed.emit(self._is_valid)
    
    def _update_style(self):
        if self._is_valid:
            self.setStyleSheet("border: 1px solid #cccccc;")
        else:
            self.setStyleSheet("border: 1px solid red;")
    
    def is_valid(self) -> bool:
        return self._is_valid