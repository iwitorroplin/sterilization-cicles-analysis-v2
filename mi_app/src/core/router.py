from __future__ import annotations

from typing import Dict, Iterable, List
from PySide6.QtCore import QObject, Signal

from modules.base_module import BaseModule


class Router(QObject):
    """Orquesta la navegación entre módulos visuales."""

    module_changed = Signal(str)

    def __init__(self) -> None:
        super().__init__()
        self._modules: Dict[str, BaseModule] = {}
        self._order: List[str] = []
        self._current_module: str | None = None

    # Registro y consulta
    def register_module(self, module: BaseModule) -> None:
        slug = module.slug()
        self._modules[slug] = module
        if slug not in self._order:
            self._order.append(slug)

    def registered_modules(self) -> Iterable[BaseModule]:
        for slug in self._order:
            yield self._modules[slug]

    # Navegación
    def navigate_to(self, module_slug: str) -> None:
        if module_slug not in self._modules:
            return
        if self._current_module == module_slug:
            return

        self._current_module = module_slug
        self.module_changed.emit(module_slug)

    # Utilidades
    def current(self) -> BaseModule | None:
        if self._current_module is None:
            return None
        return self._modules.get(self._current_module)

    def get(self, slug: str) -> BaseModule:
        return self._modules[slug]
