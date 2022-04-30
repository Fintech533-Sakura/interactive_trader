import dash_bootstrap_components as dbc
from dash import dcc, html

page_1 = html.Div(
    [
        html.P("Pair Trading Strategy"),
        html.Hr(),
        html.P("Parameters:"),
        dbc.Label('Threshold'),
        dbc.Input(id="threshold", type="number", value=1.5),
        dbc.Label('Hedge Ratio'),
        dbc.Input(id="hedge_ratio", type="number", value=1),
        dbc.Label('Alpha'),
        dbc.Input(id="alpha", type="number", value=1),
        html.Hr(),
        html.Button('Start Pair Trading', id='pair-trade-button', n_clicks=0),
        html.Hr(),
    ]
)
