
    
"""
ini app:

dialog de loading
    1º: config: 
        carga y validacion
    2º: style
        carga
"""


import sys
from PySide6.QtWidgets import QApplication
from src.ui.windows.main_window import MainWindow

def main():
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()