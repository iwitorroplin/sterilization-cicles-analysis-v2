from __future__ import annotations

from abc import ABC, abstractmethod
from PySide6.QtCore import QObject
from PySide6.QtWidgets import QWidget


class BaseModule(QObject, ABC):
    """Contratos comunes para cada módulo de la aplicación."""

    def __init__(self, slug: str, title: str, icon: str = "") -> None:
        super().__init__()
        self._slug = slug
        self._title = title
        self._icon = icon

    @abstractmethod
    def view(self) -> QWidget:
        ...

    def controller(self) -> QObject:
        return self

    def slug(self) -> str:
        return self._slug

    def title(self) -> str:
        return self._title

    def icon(self) -> str:
        return self._icon

    def on_activate(self) -> None:
        """Hook opcional ejecutado al activar el módulo."""
        return None
