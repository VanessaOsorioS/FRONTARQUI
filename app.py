from dash import Dash, html, dcc

# Inicializa la aplicación
app = Dash(__name__)

# Layout de la aplicación
app.layout = html.Div(
    className="main-container",
    children=[
        # Contenedor ALU y controles
        html.Div(
            className="alu-and-controls-container",
            children=[
                # Contenedor ALU
                html.Div(
                    className="alu-container",
                    children=[
                        html.Div("ALU", className="alu-title"),
                        html.Div(
                            children=[
                                html.Div(
                                    children=[
                                        html.Div("OPERANDO 1", className="alu-title-square"),
                                        dcc.Textarea(className="alu-square", id="operando-1", value=""),
                                    ],
                                    className="alu-item",
                                ),
                                html.Div(
                                    children=[
                                        html.Div("OPERANDO 2", className="alu-title-square"),
                                        dcc.Textarea(className="alu-square", id="operando-2", value=""),
                                    ],
                                    className="alu-item",
                                ),
                                html.Div(
                                    children=[
                                        html.Div("RESULTADO", className="alu-title-result"),
                                        dcc.Textarea(className="alu-result", id="resultado", value=""),
                                    ],
                                    className="alu-result-item",
                                ),
                            ],
                            className="alu-grid",
                        ),
                    ],
                ),
                # Contenedor PSW, PC, UNIDAD DE CONTROL, UNIDAD DE CONTROL CABLEADA
                html.Div(
                    className="control-units-container",
                    children=[
                        html.Div(
                            children=[
                                html.Div(
                                    children=[
                                        html.Div("PSW", className="alu-title-square"),
                                        dcc.Textarea(className="control-square", id="psw", value=""),
                                    ],
                                    className="control-item",
                                ),
                                html.Div(
                                    children=[
                                        html.Div("PC", className="alu-title-square"),
                                        dcc.Textarea(className="control-square", id="pc", value=""),
                                    ],
                                    className="control-item",
                                ),
                            ],
                            className="control-left-column",
                        ),
                        html.Div(
                            children=[
                                html.Div(
                                    children=[
                                        html.Div("UNIDAD DE CONTROL", className="alu-title-square"),
                                        dcc.Textarea(className="control-square", id="unidad-control", value=""),
                                    ],
                                    className="control-item",
                                ),
                                html.Div(
                                    children=[
                                        html.Div("UNIDAD DE CONTROL C", className="alu-title-square"),
                                        dcc.Textarea(className="control-square", id="unidad-control-c", value=""),
                                    ],
                                    className="control-item",
                                ),
                            ],
                            className="control-right-column",
                        ),
                    ],
                ),
            ],
        ),
        # MAR, MBR, IR y Banco de Registros
        html.Div(
            className="mar-mbr-ir-container",
            children=[
                html.Div(
                    children=[
                        html.Div(
                            children=[
                                html.Div("MAR", className="alu-title-square"),
                                dcc.Textarea(className="mar-mbr-ir-square", id="mar", value=""),
                            ],
                            className="mar-mbr-ir-item",
                        ),
                        html.Div(
                            children=[
                                html.Div("MBR", className="alu-title-square"),
                                dcc.Textarea(className="mar-mbr-ir-square", id="mbr", value=""),
                            ],
                            className="mar-mbr-ir-item",
                        ),
                        html.Div(
                            children=[
                                html.Div("IR", className="alu-title-square"),
                                dcc.Textarea(className="mar-mbr-ir-square", id="ir", value=""),
                            ],
                            className="mar-mbr-ir-item",
                        ),
                    ],
                    className="mar-mbr-ir-grid",
                ),
                html.Div(
                    className="bank-of-registers-container",
                    children=[
                        html.Div("BANCO DE REGISTROS", className="registers-title"),
                        dcc.Textarea(className="registers-square", id="banco-registros", value=""),
                    ],
                ),
                # Bloque para ingresar información
                html.Div(
                    className="bank-of-registers-container",
                    children=[
                        html.Div("Ingrese la Información", className="registers-title"),
                        dcc.Textarea(
                            className="info-square",
                            id="ingrese-informacion",
                            value="",
                            style={"resize": "none"},  # Evita el redimensionamiento
                        ),
                    ],
                ),
            ],
        ),
        # Buses
        html.Div(
            className="buses-container",
            children=[
                html.Div(
                    children=[
                        html.Div("BUS DE CONTROL", className="alu-title-square"),
                        dcc.Textarea(className="content-box", id="bus-control", value=""),
                    ],
                    className="bus",
                ),
                html.Div(
                    children=[
                        html.Div("BUS DE DATOS", className="alu-title-square"),
                        dcc.Textarea(className="content-box", id="bus-datos", value=""),
                    ],
                    className="bus",
                ),
                html.Div(
                    children=[
                        html.Div("BUS DE DIRECCIONES", className="alu-title-square"),
                        dcc.Textarea(className="content-box", id="bus-direcciones", value=""),
                    ],
                    className="bus",
                ),
            ],
        ),
        # Memorias y botones
        html.Div(
            className="memory-button-container",
            children=[
                html.Div(
                    className="memory-container",
                    children=[
                        html.Div("MEMORIAS", className="memory-title"),
                        html.Div(
                            id="memory-columns-container",
                            className="memory-columns-container",
                            children=[
                                html.Div(
                                    className="memory-column",
                                    children=[
                                        html.Div("Instrucciones", className="memory-subtitle"),
                                        html.Div(className="memory-content"),
                                    ],
                                ),
                                html.Div(
                                    className="memory-column",
                                    children=[
                                        html.Div("Datos", className="memory-subtitle"),
                                        html.Div(className="memory-content"),
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
                html.Div(
                    className="button-container",
                    children=[
                        html.Button("Cargar", className="memory-button"),
                        html.Button("Ejecutar", className="memory-button"),
                        html.Button("Siguiente", className="memory-button"),
                    ],
                ),
            ],
        ),
    ],
)

# Ejecutar la aplicación
if __name__ == "__main__":
    app.run_server(debug=True)
