import dash
from dash import dcc, html, callback
from dash.dependencies import Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
import pandas_datareader.data as web
import datetime
import plotly.graph_objects as go


dash.register_page(__name__, path='/cards', title='Cards', name='Cards_page')

layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dbc.Card(
                dbc.CardBody([
                    html.H4("Stocks", className="card-title text-center"),
                    html.P("The available stocks are 'AMZN','GOOGL','META','MSFT','NVDA", className="card-text"),
                    ]),
                    className="h-100"
                ),
            ],
            width=3),
        dbc.Col([
            dbc.Card(
                dbc.CardBody([
                    html.H4("Time Frame", className="card-title text-center"),
                    html.P("Fiscal year of 2024", className="card-text"),
                ]),
                className="h-100"
            )
        ],
            width=3)
        ]),
    dbc.Row([
        dbc.Col([
            dbc.Card(
                dbc.CardBody([
                    html.H4("Chart", className="card-title"),
                    dcc.Graph(
                        id="stock_selector_graph",
                            #random plotly graph
                            figure=px.line(
                                x=[1, 2, 3, 4],
                                y=[10, 11, 12, 13],
                                title="Random Plotly Graph",
                            ),
                    )
                ])
            )
        ])
    ],
    className="custom_margin"
    )
])