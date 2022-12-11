from dash import dcc
from dash import html

from data import countries, products, years

# create a dash app layout
layout = html.Div([
    html.H1('Dash app with multiple graphs'),
    html.Div([
        html.Div([
            dcc.Dropdown(
                id='country', 
                options=[{'label': i, 'value': i} for i in countries], 
                value=countries, 
                multi=True
            ),
            dcc.Dropdown(
                id='product', 
                options=[{'label': i, 'value': i} for i in products], 
                value=products, 
                multi=True
            ),
            dcc.Dropdown(
                id='year', 
                options=[{'label': i, 'value': i} for i in years], 
                value=max(years), 
            ),
        ]),
        html.Div([
            dcc.Graph(id='map-graph'), 
            dcc.Graph(id='timeseries-graph-by-countries'),
            dcc.Graph(id='timeseries-graph-by-products'), 
        ])
    ], className='row'),
])
