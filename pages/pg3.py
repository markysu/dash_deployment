import dash
from dash import dcc, html, callback
from dash.dependencies import Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
import pandas_datareader.data as web
import datetime
import plotly.graph_objects as go


dash.register_page(__name__, path='/compare', title='multistocks', name='Comparision')



df = pd.read_csv("./assets/data.csv")

stocks = ['AMZN','GOOGL','META','MSFT','NVDA']

layout = dbc.Container([
    dbc.Row(
        [
            dbc.Col([
                dcc.Dropdown(id="multi_stock_selector", options=[{"label": stock, "value": stock} for stock in stocks], multi=True, value=stocks[0:2]),
                dcc.Graph(id="multi_stock_selector_graph", figure={})])

            ]
            ),  
                
        ],

    fluid=True)


@callback(
    Output("multi_stock_selector_graph", "figure"),
    Input("multi_stock_selector", "value")
)
def update_graph2(stocks):
    if isinstance(stocks, str):
        stocks = [stocks]
    cols = [f'Close_{stock}' for stock in stocks]

    fig = go.Figure(px.line(df,x="Date", y=cols, labels={"variable":"Stock Price", "value": "Close Price"}))
    
    return fig
