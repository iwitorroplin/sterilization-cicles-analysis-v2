from __future__ import annotations

from modules.base_module import BaseModule
from core.session import Session
from .view import DashboardView


class DashboardController(BaseModule):
    def __init__(self, session: Session) -> None:
        super().__init__("dashboard", "Dashboard", "🏠")
        self.session = session
        self._view = DashboardView()

    def view(self):
        return self._view

    def on_activate(self) -> None:
        data_metadata = self.session.get_data_service().get_data_metadata()
        metadata = data_metadata if data_metadata else None
        self._view.render_data_status(metadata)

        app_config = self.session.get_config_service().get_app_config()
        self._view.render_config(app_config.general.printer, app_config.general.data_ferlo_dir)
