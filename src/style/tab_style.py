from PySide6.QtWidgets import QTabWidget

from .colors import Colors
from .config import StyleConfig


def apply_tab_style(tab_widget: QTabWidget):
    """
    Aplica un estilo visual moderno al sistema de pestañas (QTabWidget).

    Incluye:
        - Fondo oscuro
        - Pestaña activa destacada
        - Hover elegante
        - Bordes suaves
        - Tipografía consistente
    """

    style = f"""
        QTabWidget::pane {{
            border: {StyleConfig.Border.WIDTH_THIN} solid {Colors.Tab.BORDER};
            background: {Colors.Tab.BACKGROUND};
            border-radius: {StyleConfig.Border.RADIUS};
        }}

        /* Contenedor de las pestañas */
        QTabBar::tab {{
            background: {Colors.Tab.BACKGROUND};
            color: {Colors.Tab.TEXT};
            padding: {StyleConfig.Tab.LABEL_PADDING};
            font-size: {StyleConfig.Font.SIZE_BASE};
            border: {StyleConfig.Border.WIDTH_THIN} solid {Colors.Tab.BORDER};
            border-bottom: none;
            border-top-left-radius: {StyleConfig.Border.RADIUS};
            border-top-right-radius: {StyleConfig.Border.RADIUS};
            margin-right: 3px;
        }}

        /* Pestaña activa */
        QTabBar::tab:selected {{
            background: {Colors.Tab.ACTIVE_BACKGROUND};
            color: {Colors.Tab.ACTIVE_TEXT};
            font-weight: {StyleConfig.Font.WEIGHT_BOLD};
            border-color: {Colors.Tab.ACTIVE_BACKGROUND};
        }}

        /* Hover */
        QTabBar::tab:hover {{
            background: {Colors.Tab.HOVER_BACKGROUND};
            color: {Colors.Text.INVERTED};
        }}

        /* Pestaña deshabilitada */
        QTabBar::tab:disabled {{
            color: {Colors.Tab.DISABLED_TEXT};
            background: {Colors.Tab.DISABLED_BACKGROUND};
        }}
    """

    tab_widget.setStyleSheet(style)
