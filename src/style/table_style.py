from .colors import Colors
from .config import StyleConfig


def apply_table_style(table):
    """
    Estilo moderno para QTableWidget con:

    - Fondo oscuro
    - Encabezado estilizado
    - Hover en filas
    - Selección resaltada
    - Checkbox estilizado
    """

    style = f"""
        QTableWidget {{
            background-color: {Colors.Table.BACKGROUND};
            color: {Colors.Table.TEXT};
            border: {StyleConfig.Border.WIDTH_THIN} solid {Colors.Table.BORDER};
            border-radius: {StyleConfig.Border.RADIUS};
            outline: 0;
            gridline-color: {Colors.Table.GRID};
            selection-background-color: transparent;
        }}

        /* Celdas */
        QTableWidget::item {{
            padding: {StyleConfig.Padding.SM};
            border-bottom: {StyleConfig.Border.WIDTH_THIN} solid {Colors.Table.GRID};
        }}

        /* Hover fila */
        QTableWidget::item:hover {{
            background-color: {Colors.Table.ROW_HOVER};
        }}

        /* Selección */
        QTableWidget::item:selected {{
            background-color: {Colors.Table.SELECTION_BACKGROUND};
            color: {Colors.Table.SELECTION_TEXT};
            font-weight: {StyleConfig.Font.WEIGHT_BOLD};
        }}

        /* Encabezados */
        QHeaderView::section {{
            background-color: {Colors.Table.HEADER_BACKGROUND};
            color: {Colors.Table.HEADER_TEXT};
            padding: {StyleConfig.Padding.SM};
            border: none;
            border-right: {StyleConfig.Border.WIDTH_THIN} solid {Colors.Table.HEADER_BORDER};
            font-weight: {StyleConfig.Font.WEIGHT_BOLD};
        }}

        QHeaderView::section:last {{
            border-right: none;
        }}

        /* Botón esquina (arriba izquierda) */
        QTableCornerButton::section {{
            background-color: {Colors.Table.HEADER_BACKGROUND};
            border: none;
        }}

        /* Checkbox interno */
        QTableWidget::indicator {{
            width: 18px;
            height: 18px;
            border-radius: {StyleConfig.Border.RADIUS_SMALL};
            border: {StyleConfig.Border.WIDTH} solid {Colors.Table.CHECKBOX_BORDER};
            background-color: {Colors.Table.BACKGROUND};
        }}

        QTableWidget::indicator:checked {{
            background-color: {Colors.Table.CHECKBOX_CHECKED};
            border-color: {Colors.Table.CHECKBOX_CHECKED};
        }}

        QTableWidget::indicator:hover {{
            border-color: {Colors.Table.CHECKBOX_HOVER};
        }}
    """

    table.setStyleSheet(style)
