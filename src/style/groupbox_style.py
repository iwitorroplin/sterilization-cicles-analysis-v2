from PySide6.QtWidgets import QGroupBox

from .colors import Colors
from .config import StyleConfig


def apply_groupbox_style(groupbox: QGroupBox):
    """
    Aplica estilo moderno al QGroupBox:
    - Título destacado con fondo independiente
    - Borde suave redondeado
    - Fondo personalizado
    """

    style = f"""
        QGroupBox {{
            background-color: {Colors.GroupBox.BACKGROUND};
            color: {Colors.GroupBox.TEXT};
            border: {StyleConfig.Border.WIDTH_THIN} solid {Colors.GroupBox.BORDER};
            border-radius: {StyleConfig.Border.RADIUS};
            margin-top: 20px; /* espacio para título */
            font-size: {StyleConfig.Font.SIZE_BASE};
        }}

        /* Título del GroupBox */
        QGroupBox:title {{
            subcontrol-origin: margin;
            subcontrol-position: top left;
            padding: {StyleConfig.Padding.SM} {StyleConfig.Padding.MD};
            background-color: {Colors.GroupBox.HEADER_BACKGROUND};
            color: {Colors.GroupBox.HEADER_TEXT};
            border-radius: {StyleConfig.Border.RADIUS_SMALL};
            font-weight: {StyleConfig.Font.WEIGHT_BOLD};
        }}
    """

    groupbox.setStyleSheet(style)
