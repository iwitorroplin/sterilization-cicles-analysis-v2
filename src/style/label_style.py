"""Estilos centralizados para etiquetas (QLabel)."""

from PySide6.QtWidgets import QLabel

from .colors import Colors
from .config import StyleConfig


def apply_label_style(label: QLabel, variant: str = "normal"):
    """
    Aplica estilo visual uniforme a etiquetas (QLabel).

    Variantes disponibles:
        - normal        → texto estándar
        - subtle        → texto menos dominante (descripciones, hints)
        - title         → tipo título (más grande y fuerte)
        - disabled      → estilo apagado
    """

    variants = {
        "normal": {
            "color": Colors.Label.BODY,
            "font_size": StyleConfig.Font.SIZE_BASE,
            "bold": StyleConfig.Font.WEIGHT_NORMAL,
        },
        "subtle": {
            "color": Colors.Label.SUBTLE,
            "font_size": StyleConfig.Font.SIZE_SMALL,
            "bold": StyleConfig.Font.WEIGHT_NORMAL,
        },
        "title": {
            "color": Colors.Label.TITLE,
            "font_size": StyleConfig.Font.SIZE_TITLE,
            "bold": StyleConfig.Font.WEIGHT_BOLD,
        },
        "disabled": {
            "color": Colors.Label.DISABLED,
            "font_size": StyleConfig.Font.SIZE_BASE,
            "bold": StyleConfig.Font.WEIGHT_NORMAL,
        },
    }

    config = variants.get(variant, variants["normal"])

    style = f"""
        QLabel {{
            color: {config['color']};
            background-color: {Colors.Label.BACKGROUND};
            font-size: {config['font_size']};
            font-weight: {config['bold']};
            font-family: {StyleConfig.Font.FAMILY};
        }}
    """

    label.setStyleSheet(style)
