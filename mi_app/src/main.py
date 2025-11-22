import sys
from PySide6.QtWidgets import QApplication
from core.app import Application
from core.router import Router

# Importar controladores
from modules.dashboard.controller import DashboardController
from modules.carga_datos.controller import CargaDatosController
from modules.analisis.controller import AnalisisController
from modules.visualizacion.controller import VisualizacionController
from modules.reportes.controller import ReportesController
from modules.configuracion.controller import ConfigController

def main():
    app = QApplication(sys.argv)
    
    # Configurar router
    router = Router()
    
    # Registrar módulos
    router.register_module("dashboard", DashboardController())
    router.register_module("carga_datos", CargaDatosController())
    router.register_module("analisis", AnalisisController())
    router.register_module("visualizacion", VisualizacionController())
    router.register_module("reportes", ReportesController())
    router.register_module("configuracion", ConfigController())
    
    # Crear aplicación
    main_app = Application(router)
    main_app.show()
    
    # Navegar al dashboard
    router.navigate_to("dashboard")
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()