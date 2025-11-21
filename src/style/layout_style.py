"""Configuraciones de espaciado y márgenes para layouts."""

from .config import StyleConfig


def get_main_layout_config():
    """Configuración para layouts principales"""
    return {
        "margins": StyleConfig.Layout.MAIN_MARGINS,
        "spacing": StyleConfig.Layout.MAIN_SPACING,
    }


def get_button_layout_config():
    """Configuración para layouts de botones"""
    return {
        "margins": StyleConfig.Layout.BUTTON_MARGINS,
        "spacing": StyleConfig.Layout.BUTTON_SPACING,
    }
