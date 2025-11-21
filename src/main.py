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
from src.ui.widgets.loading_dialog import LoadingDialog
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

    loading_dialog = LoadingDialog(text="Cargando variables básicas...", show_progress=False)
    loading_dialog.show()
    QApplication.processEvents()

    basic_config = load_basic_configuration()
    AppSettings.set_basic_config(basic_config)

    loading_dialog.fade_out_and_close()

    # Aplicar estilo global y nombre de la aplicación
    app.setApplicationDisplayName(f"{APP_NAME} v{APP_VERSION}")
    Style.apply_global(app)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
