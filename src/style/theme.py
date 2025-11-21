"""
Configuración global del tema de la aplicación
"""

from .colors import Colors
from .config import StyleConfig


class Theme:
    font_family = StyleConfig.Font.FAMILY
    font_size = StyleConfig.Font.SIZE_BASE
    background = Colors.App.BACKGROUND
    text_color = Colors.Text.PRIMARY


def get_app_style():
    """Estilo global de la aplicación"""
    return f"""
        QWidget {{
            font-family: {Theme.font_family};
            font-size: {Theme.font_size};
            color: {Theme.text_color};
            background-color: {Theme.background};
        }}
    """
