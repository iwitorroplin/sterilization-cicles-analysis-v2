"""Estilos reutilizables para widgets de entrada (QLineEdit, QTextEdit)."""

from .colors import Colors
from .config import StyleConfig


def apply_input_style(input_widget):
    """
    Aplica estilo visual consistente a widgets de entrada (QLineEdit, QTextEdit).

    Maneja:
        ✓ Estado normal
        ✓ Placeholder o vacío
        ✓ Estado de enfoque (focus)
        ✓ TextEdit o LineEdit (comparten mismo diseño)
    """

    style = f"""
        QLineEdit, QTextEdit {{
            background-color: {Colors.Input.BACKGROUND};
            color: {Colors.Input.TEXT};
            border: {StyleConfig.Border.WIDTH} solid {Colors.Input.BORDER};
            border-radius: {StyleConfig.Border.RADIUS};
            padding: {StyleConfig.Padding.SM};
            font-size: {StyleConfig.Font.SIZE_BASE};
            selection-background-color: {Colors.Tab.ACTIVE_BACKGROUND};
        }}

        /* Placeholder text */
        QLineEdit[empty="true"], QTextEdit[empty="true"] {{
            background-color: {Colors.Input.PLACEHOLDER_BACKGROUND};
            color: {Colors.Input.PLACEHOLDER_TEXT};
            border-color: {Colors.Input.PLACEHOLDER_BORDER};
        }}

        /* Cuando está seleccionado/en foco */
        QLineEdit:focus, QTextEdit:focus {{
            border-color: {Colors.Input.FOCUS_BORDER};
        }}
    """

    input_widget.setStyleSheet(style)

    # Extra: etiqueta interna para saber si está vacío (permite cambiar color)
    if hasattr(input_widget, "textChanged"):
        input_widget.textChanged.connect(lambda: _update_empty_state(input_widget))
    _update_empty_state(input_widget)


def _update_empty_state(widget):
    """Actualiza la propiedad Qt 'empty' para modificar el estilo si no hay texto."""
    text = widget.toPlainText() if hasattr(widget, "toPlainText") else widget.text()
    widget.setProperty("empty", text.strip() == "")
    widget.style().unpolish(widget)
    widget.style().polish(widget)
    widget.update()
