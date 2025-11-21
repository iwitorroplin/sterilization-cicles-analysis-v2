"""Estilos compartidos para los diferentes tipos de botones."""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QPushButton

from .colors import Colors
from .config import StyleConfig
from src.core.config import (
    BUTTON_1_SIZE_HEIGHT,
    BUTTON_1_SIZE_WIDTH,
    BUTTON_2_SIZE_HEIGHT,
    BUTTON_2_SIZE_WIDTH,
    BUTTON_3_SIZE_HEIGHT,
    BUTTON_3_SIZE_WIDTH,
)

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
            min-width: {BUTTON_1_SIZE_WIDTH}px;
            max-width: {BUTTON_1_SIZE_WIDTH}px;
            min-height: {BUTTON_1_SIZE_HEIGHT}px;
            max-height: {BUTTON_1_SIZE_HEIGHT}px;
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
            min-width: {BUTTON_2_SIZE_WIDTH}px;
            max-width: {BUTTON_2_SIZE_WIDTH}px;
            min-height: {BUTTON_2_SIZE_HEIGHT}px;
            max-height: {BUTTON_2_SIZE_HEIGHT}px;
        }}
        QPushButton:hover {{
            background-color: {Colors.ButtonSecondary.HOVER};
        }}
        QPushButton:pressed {{
            background-color: {Colors.ButtonSecondary.PRESSED};
        }}
        QPushButton:disabled {{
            background-color: {Colors.ButtonSecondary.DISABLED};
            color: {Colors.ButtonSecondary.DISABLED_TEXT};
            border-color: {Colors.ButtonSecondary.DISABLED_BORDER};
        }}
    """

    button.setStyleSheet(style)
    button.setCheckable(True)
    button.setCursor(Qt.PointingHandCursor)
    
def apply_button_3_style(button: QPushButton):
    """Aplica estilo visual consistente a botones de BUTTON_BROWSE."""

    style = f"""
        QPushButton {{
            background-color: {Colors.ButtonTertiary.BACKGROUND};
            color: {Colors.ButtonTertiary.TEXT};
            border: {StyleConfig.Border.WIDTH} solid {Colors.ButtonTertiary.BORDER};
            border-radius: {StyleConfig.Border.RADIUS};
            padding: {StyleConfig.Padding.MD};
            font-size: {StyleConfig.Font.SIZE_BASE};
            font-weight: {StyleConfig.Font.WEIGHT_BOLD};
            text-align: center;
            min-width: {BUTTON_3_SIZE_WIDTH}px;
            max-width: {BUTTON_3_SIZE_WIDTH}px;
            min-height: {BUTTON_3_SIZE_HEIGHT}px;
            max-height: {BUTTON_3_SIZE_HEIGHT}px;
        }}
        QPushButton:hover {{
            background-color: {Colors.ButtonTertiary.HOVER};
        }}
        QPushButton:pressed {{
            background-color: {Colors.ButtonTertiary.PRESSED};
        }}
        QPushButton:disabled {{
            background-color: {Colors.ButtonTertiary.DISABLED};
            color: {Colors.ButtonTertiary.DISABLED_TEXT};
            border-color: {Colors.ButtonTertiary.DISABLED_BORDER};
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
            min-width: {BUTTON_1_SIZE_WIDTH}px;
            max-width: {BUTTON_1_SIZE_WIDTH}px;
            min-height: {BUTTON_1_SIZE_HEIGHT}px;
            max-height: {BUTTON_1_SIZE_HEIGHT}px;
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



