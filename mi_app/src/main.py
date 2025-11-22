import sys
from PySide6.QtWidgets import QApplication

from core.app import Application
from core.router import Router
from core.session import Session
from modules.dashboard.controller import DashboardController
from modules.carga_datos.controller import CargaDatosController
from modules.analisis.controller import AnalisisController
from modules.visualizacion.controller import VisualizacionController
from modules.reportes.controller import ReportesController
from modules.configuracion.controller import ConfigController


def main() -> None:
    app = QApplication(sys.argv)
    session = Session()
    router = Router()

    # Registro de módulos en el orden deseado
    router.register_module(DashboardController(session))
    router.register_module(CargaDatosController(session))
    router.register_module(AnalisisController(session))
    router.register_module(VisualizacionController(session))
    router.register_module(ReportesController(session))
    router.register_module(ConfigController(session))

    main_window = Application(router, session)
    main_window.show()

    # Primer módulo
    router.navigate_to("dashboard")

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
