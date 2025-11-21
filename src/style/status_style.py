"""Estilos reutilizables para cajas de estado o alertas."""

from .colors import Colors
from .config import StyleConfig


def get_status_style(mode: str = "info"):
    """Devuelve el estilo para cajas de estado"""
    colors = {
        "info": f"background:{Colors.Status.INFO_BACKGROUND}; color:{Colors.Status.INFO_TEXT}; border:{StyleConfig.Border.WIDTH_THIN} solid {Colors.Status.INFO_BORDER};",
        "error": f"background:{Colors.Status.ERROR_BACKGROUND}; color:{Colors.Status.ERROR_TEXT}; border:{StyleConfig.Border.WIDTH_THIN} solid {Colors.Status.ERROR_BORDER};",
        "ok": f"background:{Colors.Status.OK_BACKGROUND}; color:{Colors.Status.OK_TEXT}; border:{StyleConfig.Border.WIDTH_THIN} solid {Colors.Status.OK_BORDER};",
        "warning": f"background:{Colors.Status.WARNING_BACKGROUND}; color:{Colors.Status.WARNING_TEXT}; border:{StyleConfig.Border.WIDTH_THIN} solid {Colors.Status.WARNING_BORDER};",
    }

    base_style = f"padding:{StyleConfig.Padding.MD}; border-radius:{StyleConfig.Border.RADIUS_SMALL};"
    return f"{base_style} {colors.get(mode, colors['info'])}"
