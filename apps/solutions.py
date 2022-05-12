from dash import html, dash_table,callback,dcc
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
from app import app
from dash.dependencies import Input, Output
import plotly_express as px


# needed only if running this as a single page app
#external_stylesheets = [dbc.themes.LUX]

#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

####################################################################################################
# 000 - DATA MAPPING
####################################################################################################
#Database mapping

data = pd.read_csv('GHG_projections_2021_EEA.csv')

year_min = data['Year'].min()
year_max = data['Year'].max()



# change to app.layout if running as single page app instead
layout = html.Div([
    dbc.Container([
        dbc.Row([
            html.H1("Explorez vos propres solutions", className="text-center",style={'margin-top':'40px'}),
            html.H5(children=["Choisissez le scénario qui vous paraît le plus efficace"],className="text-center",style={'margin-bottom':'40px'})
        ]),

        # INITIALISATION DE LA PARTIE FILTRAGE#################################################
        dbc.Row([
            # FITLRAGE SUR LE TITRE #################################################
            dbc.Col([], className="text-center", width=3),


            dbc.Col([

                html.H4("Choisissez un ou plusieurs pays", className="text-center"),

                dcc.Dropdown(options=[{'label': l, 'value': l} for l in data["CountryCode"].unique()],value = list(data["CountryCode"].unique()[:3]),id="country_select", placeholder="Quel pays ?", multi = True,className="center-align", style={"margin-bottom":"15px", "width":"100%"}),
                html.P(id='choices',className="center-align", style={"margin-bottom":"15px", "width":"100%"}),
                html.H4("Rechercher une période", className="text-center",style={'margin-top':'20px'}),

                dcc.RangeSlider(id='years-slider',min=year_min,max=year_max,marks=None,tooltip={"placement": "bottom", "always_visible": True},
                                value=[year_min,year_max])

            ], className="text-center", width=6),


            dbc.Col([], className="text-center", width=3),


        ], className="mb-12", style={'margin-bottom': '25px'}),

        dcc.Graph(id='solution-graph')

    ]) #FIN DU DBC CONTAINER

])#FIN DU LAYOUT


# needed only if running this as a single page app
# if __name__ == '__main__':
#     app.run_server(host='127.0.0.1', debug=True)


####################################################################################################
# BACKEND AND CALLBACKS
####################################################################################################


# INPUT ITEM CALLBACK
@app.callback(
    [Output('solution-graph', 'figure'),
    Output('choices','children')],
    [Input('country_select', 'value'),
    Input("years-slider", "value"),
     ])

def update_graph(countries,period):
    
    filtered_data=data[(data['Year']==period[0]) & (data['CountryCode'].isin(countries))]

    fig = px.scatter(filtered_data, x='Year', y='Reported Value', color = 'Gas')
    return fig, countries