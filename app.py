import dash
from dash import dcc, html
from dash.dependencies import Output, Input, State
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
import pandas_datareader.data as web
import datetime
import plotly.graph_objects as go


app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.SPACELAB])
# print(dash.page_registry.keys())
# print(dash.page_registry.values())

server = app.server


toggle_button = dbc.Button(
    "☰",color="primary", className="ms-2", id="toggle-button", n_clicks=0
)

sidebar = dbc.Nav(
    [
        dbc.NavLink(
            [
                html.Div(page["name"], className="ms-2")   
            ],
            href=page["path"],
            active="exact"
        )
        for page in dash.page_registry.values()
    ],
    vertical=True,
    pills=True,
    className="bg-light",
    id="sidebar"

)

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.Div([html.H1("Multipage Stock App", className="text-center"),
                         toggle_button]
                         ),
                         )
    ]),

    html.Hr(),

    dbc.Row(
        [
            dbc.Col(
                [
                    sidebar
                ], 
                width=2,
                id="sidebar-col"
                ),
                # xs=4, sm=4, md=4, lg=2, xl=2, xxl=2),

            dbc.Col(
                [
                    dash.page_container
                ], 
                width=10,
                # xs=8, sm=8, md=8, lg=10, xl=10, xxl=10,
                id="content-col")
        ]
    )
], fluid=True)


@app.callback(
    Output("sidebar-col", "width"),
    Output("content-col", "width"),
    Output("sidebar-col", "style"),
    Input("toggle-button", "n_clicks"),
    State("sidebar-col", "width"),
)
def toggle_sidebar(n_clicks, sidebar_width):
    if n_clicks:
        if sidebar_width == 2:
            return 0, 12, {"display": "none"}
        else:
            return 2, 10, {}
    
    return sidebar_width, 10, {}


if __name__ == '__main__':
    app.run_server(debug=True)