"""
Entrada de la aplicación.

Secuencia de carga:
    1. Configuración básica.
    2. Estilos globales.
    3. Arranque de la ventana principal.
"""

import sys
from PySide6.QtWidgets import QApplication

from src.core.config import APP_NAME, APP_VERSION
from src.ui.windows.main_window import MainWindow
from src.style import Style

def main():
    app = QApplication(sys.argv)

    # Aplicar estilo global y nombre de la aplicación
    app.setApplicationDisplayName(f"{APP_NAME} v{APP_VERSION}")
    Style.apply_global(app)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
