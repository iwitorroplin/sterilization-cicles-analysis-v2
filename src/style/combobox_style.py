from PySide6.QtWidgets import QComboBox

from .colors import Colors
from .config import StyleConfig


def apply_combobox_style(combo: QComboBox):
    """
    Aplica estilo consistente al QComboBox incluyendo:
        - Visual base (fondo, bordes, texto)
        - Hover
        - Focus
        - Dropdown estilizado
    """

    style = f"""
        QComboBox {{
            background-color: {Colors.ComboBox.BACKGROUND};
            color: {Colors.ComboBox.TEXT};
            border: {StyleConfig.Border.WIDTH} solid {Colors.ComboBox.BORDER};
            border-radius: {StyleConfig.Border.RADIUS};
            padding: {StyleConfig.Padding.SM} {StyleConfig.Padding.MD};
            font-size: {StyleConfig.Font.SIZE_BASE};
        }}

        /* Botón del desplegable (flecha) */
        QComboBox::drop-down {{
            border: none;
            width: 24px;
        }}

        QComboBox::down-arrow {{
            image: none;
            width: 0px;
            height: 0px;
            border-left: 6px solid transparent;
            border-right: 6px solid transparent;
            border-top: 8px solid {Colors.ComboBox.ARROW};
            margin-right: 6px;
        }}

        /* Hover */
        QComboBox:hover {{
            border-color: {Colors.ComboBox.HOVER_BORDER};
        }}

        /* Focus */
        QComboBox:focus {{
            border-color: {Colors.ComboBox.FOCUS_BORDER};
        }}

        /* Estilo del menú desplegable */
        QComboBox QAbstractItemView {{
            background-color: {Colors.ComboBox.POPUP_BACKGROUND};
            color: {Colors.ComboBox.POPUP_TEXT};
            border: {StyleConfig.Border.WIDTH_THIN} solid {Colors.ComboBox.BORDER};
            selection-background-color: {Colors.ComboBox.FOCUS_BORDER};
            selection-color: {Colors.Text.INVERTED};
        }}
    """

    combo.setStyleSheet(style)
