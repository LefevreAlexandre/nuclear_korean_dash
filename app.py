# create a dash app layout in dash 2

# app contains a main graph with timeseries data by countries id = 'timeseries-graph-by-countries'
#a graph with timeseries data by products id = 'timeseries-graph-by-products'


# and a dropdown menu to select the data
# a country dropdown: id = 'country'
# a product dropdown: id = 'product'

# the data is stored in a dataframe data

# import the necessary libraries
import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd

# load the data
from data import df
from layout import layout


# create a dash app
app = dash.Dash(__name__)

# create a dash app layout
app.layout = layout

# create a callback for the timeseries graph
@app.callback(
    dash.dependencies.Output('timeseries-graph-by-countries', 'figure'),
    [
        dash.dependencies.Input('country', 'value'),
        dash.dependencies.Input('product', 'value')
    ])
def update_countries_graph(countries, products):
    # filter the data
    dff = df[(df.PartnerName.isin(countries)) & (df.ProductCode.isin(products))]
    dff = dff.groupby(['Year','PartnerName']).Value.sum().reset_index()
    # create a timeseries graph
    fig = px.line(dff, 
        x='Year', 
        y='Value', 
        color='PartnerName', 
        title='Timeseries by Countries'
    )
    return fig

# create a callback for the timeseries graph
@app.callback(
    dash.dependencies.Output('timeseries-graph-by-products', 'figure'),
    [
        dash.dependencies.Input('country', 'value'),
        dash.dependencies.Input('product', 'value')
    ])
def update_products_graph(countries, products):
    # filter the data
    dff = df[(df.PartnerName.isin(countries)) & (df.ProductCode.isin(products))]
    dff = dff.groupby(['Year','ProductCode']).Value.sum().reset_index()
    # create a timeseries graph
    fig = px.line(dff, 
        x='Year', 
        y='Value', 
        color='ProductCode', 
        title='Timeseries by Products'
    )
    return fig

# create a callback for the map graph
@app.callback(
    dash.dependencies.Output('map-graph', 'figure'),
    [
        dash.dependencies.Input('product', 'value'),
        dash.dependencies.Input('year', 'value'),

    ])
def update_map_graph(products, year):
    # filter the data
    dff = df[df['Year'] == year]
    dff = dff[(dff.ProductCode.isin(products))]
    dff = dff.groupby(['Year','PartnerISO3','PartnerName']).Value.sum().reset_index()
    # create a map graph
    fig = px.scatter_geo(dff, 
        locations='PartnerISO3', 
        hover_name='PartnerName', 
        locationmode = 'ISO-3',
        size='Value',

    )
    fig.update_layout(
        title='Map by Countries',
        geo_showcountries = True)

    return fig

# run the app
if __name__ == '__main__':
    app.run_server()


