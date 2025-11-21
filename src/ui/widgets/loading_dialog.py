import time
from PySide6.QtWidgets import (QDialog, QVBoxLayout, QLabel, QProgressBar, QApplication)
from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve, QTimer
from PySide6.QtGui import QPixmap, QPainter, QColor
from PySide6.QtWidgets import QSizePolicy

class LoadingDialog(QDialog):
    """Dialog de carga modal reutilizable - Widget independiente"""
    
    def __init__(self, parent=None, text="Procesando...", show_progress=True):
        super().__init__(parent)
        self.setup_ui(text, show_progress)
        self.setup_animations()
        
    def setup_ui(self, text, show_progress):
        """Configura la interfaz de usuario"""
        self.setWindowFlags(Qt.Dialog | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_DeleteOnClose, False)
        self.setModal(True)
        self.setFixedSize(350, 200)
        self.setStyleSheet(self.get_stylesheet())
        
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)
        
        # Spinner
        self.spinner = QLabel()
        self.spinner.setAlignment(Qt.AlignCenter)
        self.spinner.setFixedSize(64, 64)
        
        # Texto
        self.label = QLabel(text)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 14px; font-weight: bold;")
        
        # Barra de progreso
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setTextVisible(True)
        self.progress_bar.setVisible(show_progress)
        
        if not show_progress:
            self.progress_bar.setFixedHeight(0)
        
        layout.addStretch()
        layout.addWidget(self.spinner, alignment=Qt.AlignCenter)
        layout.addWidget(self.label, alignment=Qt.AlignCenter)
        layout.addWidget(self.progress_bar)
        layout.addStretch()
        
        self.setLayout(layout)
        self.center_on_screen()
    
    def get_stylesheet(self):
        """Retorna el stylesheet del diálogo"""
        return """
            QWidget {
                background-color: #2c3e50;
                border-radius: 10px;
                color: #ecf0f1;
            }
            QProgressBar {
                border: 2px solid #34495e;
                border-radius: 5px;
                text-align: center;
                color: #2c3e50;
                font-weight: bold;
            }
            QProgressBar::chunk {
                background-color: #3498db;
                border-radius: 3px;
            }
        """
    
    def setup_animations(self):
        """Configura las animaciones"""
        self.start_time = None
        self.minimum_display_time = 1000
        self._rotation_angle = 0
        
        self.close_timer = QTimer()
        self.close_timer.setSingleShot(True)
        self.close_timer.timeout.connect(self.force_close)
        
        self.fade_in()
        self.start_spinner_animation()
    
    def center_on_screen(self):
        """Centra la ventana en la pantalla"""
        screen = QApplication.primaryScreen().availableGeometry()
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2
        self.move(x, y)
    
    def fade_in(self):
        """Animación de entrada con desvanecimiento"""
        self.setWindowOpacity(0)
        self.anim = QPropertyAnimation(self, b"windowOpacity")
        self.anim.setDuration(400)
        self.anim.setStartValue(0)
        self.anim.setEndValue(1)
        self.anim.setEasingCurve(QEasingCurve.OutCubic)
        self.anim.start()
    
    def showEvent(self, event):
        super().showEvent(event)
        self.start_time = time.time() * 1000
    
    def fade_out_and_close(self):
        """Animación de salida respetando tiempo mínimo"""
        current_time = time.time() * 1000
        elapsed_time = current_time - self.start_time
        
        if elapsed_time >= self.minimum_display_time:
            self.force_close()
        else:
            remaining_time = self.minimum_display_time - elapsed_time
            self.close_timer.start(int(remaining_time))
    
    def force_close(self):
        """Cierra el diálogo forzadamente"""
        if hasattr(self, 'rotation_timer') and self.rotation_timer.isActive():
            self.rotation_timer.stop()
            
        self.anim_close = QPropertyAnimation(self, b"windowOpacity")
        self.anim_close.setDuration(400)
        self.anim_close.setStartValue(1)
        self.anim_close.setEndValue(0)
        self.anim_close.setEasingCurve(QEasingCurve.InCubic)
        self.anim_close.finished.connect(self.accept)
        self.anim_close.start()
    
    def start_spinner_animation(self):
        """Animación de rotación del spinner"""
        self._rotation_angle = 0
        self.rotation_timer = QTimer()
        self.rotation_timer.timeout.connect(self.rotate_spinner)
        self.rotation_timer.start(30)
    
    def rotate_spinner(self):
        """Rotar el spinner"""
        self._rotation_angle = (self._rotation_angle + 8) % 360
        self.update_spinner()
    
    def update_spinner(self):
        """Actualiza la apariencia del spinner"""
        pixmap = QPixmap(64, 64)
        pixmap.fill(Qt.transparent)
        
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.Antialiasing)
        
        pen = painter.pen()
        pen.setWidth(4)
        pen.setColor(QColor(52, 152, 219))
        painter.setPen(pen)
        painter.setBrush(Qt.NoBrush)
        painter.translate(32, 32)
        painter.rotate(self._rotation_angle)
        painter.drawArc(-24, -24, 48, 48, 0, 270 * 16)
        
        painter.end()
        self.spinner.setPixmap(pixmap)
    
    def update_progress(self, value):
        """Actualiza el progreso de la barra"""
        self.progress_bar.setValue(value)
    
    def update_text(self, text):
        """Actualiza el texto de la ventana"""
        self.label.setText(text)