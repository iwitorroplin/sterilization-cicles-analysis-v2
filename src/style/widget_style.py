"""Estilo base para contenedores (QWidget)."""

from .colors import Colors
from .config import StyleConfig


def apply_widget_style(widget):
    """Aplica el estilo base a un contenedor estándar (ej: header, footer, panel)."""

    style = f"""
        QWidget {{
            background-color: {Colors.App.SURFACE};
            color: {Colors.Text.PRIMARY};
            font-family: {StyleConfig.Font.FAMILY};
        }}
        QLabel {{
            background-color: transparent;
            color: {Colors.Text.PRIMARY};
        }}
    """

    widget.setStyleSheet(style)
