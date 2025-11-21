"""Estilos compartidos para los diferentes tipos de botones."""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QPushButton

from .colors import Colors
from .config import StyleConfig


def apply_button_1_style(button: QPushButton):
    """Aplica estilo visual consistente a botones primarios."""

    style = f"""
        QPushButton {{
            background-color: {Colors.ButtonPrimary.BACKGROUND};
            color: {Colors.ButtonPrimary.TEXT};
            border: {StyleConfig.Border.WIDTH} solid {Colors.ButtonPrimary.BORDER};
            border-radius: {StyleConfig.Border.RADIUS};
            padding: {StyleConfig.Padding.MD};
            font-size: {StyleConfig.Font.SIZE_BASE};
            font-weight: {StyleConfig.Font.WEIGHT_BOLD};
            text-align: center;
        }}
        QPushButton:hover {{
            background-color: {Colors.ButtonPrimary.HOVER};
        }}
        QPushButton:pressed {{
            background-color: {Colors.ButtonPrimary.PRESSED};
        }}
        QPushButton:checked {{
            background-color: {Colors.ButtonPrimary.CHECKED};
            border: {StyleConfig.Border.WIDTH} solid {Colors.Text.INVERTED};
        }}
    """

    button.setStyleSheet(style)
    button.setCheckable(True)
    button.setCursor(Qt.PointingHandCursor)

# los botones 2 y exit sin checked

def apply_button_2_style(button: QPushButton):
    """Aplica estilo visual consistente a botones secundarios."""

    style = f"""
        QPushButton {{
            background-color: {Colors.ButtonSecondary.BACKGROUND};
            color: {Colors.ButtonSecondary.TEXT};
            border: {StyleConfig.Border.WIDTH} solid {Colors.ButtonSecondary.BORDER};
            border-radius: {StyleConfig.Border.RADIUS};
            padding: {StyleConfig.Padding.MD};
            font-size: {StyleConfig.Font.SIZE_BASE};
            font-weight: {StyleConfig.Font.WEIGHT_BOLD};
            text-align: center;
        }}
        QPushButton:hover {{
            background-color: {Colors.ButtonSecondary.HOVER};
        }}
        QPushButton:pressed {{
            background-color: {Colors.ButtonSecondary.PRESSED};
        }}
    """

    button.setStyleSheet(style)
    button.setCheckable(True)
    button.setCursor(Qt.PointingHandCursor)

def apply_button_exit_style(button: QPushButton):
    """Aplica estilo visual para botones de salida/peligro."""

    style = f"""
        QPushButton {{
            background-color: {Colors.ButtonDanger.BACKGROUND};
            color: {Colors.ButtonDanger.TEXT};
            border: {StyleConfig.Border.WIDTH} solid {Colors.ButtonDanger.BORDER};
            border-radius: {StyleConfig.Border.RADIUS};
            padding: {StyleConfig.Padding.MD};
            font-size: {StyleConfig.Font.SIZE_BASE};
            font-weight: {StyleConfig.Font.WEIGHT_BOLD};
            text-align: center;
        }}
        QPushButton:hover {{
            background-color: {Colors.ButtonDanger.HOVER};
        }}
        QPushButton:pressed {{
            background-color: {Colors.ButtonDanger.PRESSED};
        }}
    """

    button.setStyleSheet(style)
    button.setCheckable(True)
    button.setCursor(Qt.PointingHandCursor)



