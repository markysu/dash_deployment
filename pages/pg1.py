import dash
from dash import dcc, html
from dash.dependencies import Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
import pandas_datareader.data as web
import datetime
import plotly.graph_objects as go


dash.register_page(__name__, path='/', title='Stocks', name='Home')

layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.Img(src="assets/stocks-and-indices.png", style={"height":"80%","width":"80%"})
        ])
    ])
])