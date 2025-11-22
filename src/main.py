"""
Entrada de la aplicación.

Secuencia de carga:
    1. Configuración básica.
    2. Estilos globales.
    3. Arranque de la ventana principal.
"""

import json
import sys
from pathlib import Path
from PySide6.QtWidgets import QApplication

from src.core.app_settings import AppSettings
from src.core.config import APP_NAME, APP_VERSION
from src.core.loading_manager import LoadingManager
from src.ui.windows.main_window import MainWindow
from src.style import Style


def load_basic_configuration() -> dict:
    """Carga el archivo JSON de configuración básica."""
    config_path = Path(__file__).resolve().parent / "config" / "app_config.json"

    try:
        with config_path.open("r", encoding="utf-8") as config_file:
            return json.load(config_file)
    except FileNotFoundError:
        print(f"No se encontró el archivo de configuración: {config_path}")
    except json.JSONDecodeError as error:
        print(f"Error al leer el archivo de configuración: {error}")

    return {}

def main():
    app = QApplication(sys.argv)

    window = None

    def load_basic_settings():
        basic_config = load_basic_configuration()
        AppSettings.set_basic_config(basic_config)

    def launch_application():
        nonlocal window
        # Aplicar estilo global y nombre de la aplicación
        app.setApplicationDisplayName(f"{APP_NAME} v{APP_VERSION}")
        Style.apply_global(app)

        window = MainWindow()
        window.show()

    loading_manager = LoadingManager()
    loading_manager.start_loading(
        [("Cargando variables básicas...", load_basic_settings, [])],
        on_finished=launch_application,
    )

    sys.exit(app.exec())


if __name__ == "__main__":
    
    main()
