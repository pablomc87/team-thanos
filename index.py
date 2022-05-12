from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

# must add this line in order for the app to be deployed successfully on Heroku
from app import server
from app import app
# import all pages in the app
from apps import home, cinematheque_catalog,cinematheque_kpi,movision,projet

# building the navigation bar
# https://github.com/facultyai/dash-bootstrap-components/blob/master/examples/advanced-component-usage/Navbars.py


navbar = dbc.NavbarSimple(


    children=[
        dbc.NavItem(dbc.NavLink("Cinémathèque", href="/cinematheque_catalog")),
        dbc.NavItem(dbc.NavLink("Dataviz", href="/cinematheque_kpi")),
        dbc.NavItem(dbc.NavLink("Movision", href="/movision")),
        dbc.NavItem(dbc.NavLink("Le projet", href="/projet")),

    ],
    brand="Les Bobines creuses",
    brand_href="/home",
    color="warning",
    dark=False,
    style={"font-weight":"bold"}
)

# embedding the navigation bar
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/home':
        return home.layout
    elif pathname == '/cinematheque_catalog':
        return cinematheque_catalog.layout
    elif pathname == '/cinematheque_kpi':
        return cinematheque_kpi.layout
    elif pathname == '/movision':
        return movision.layout
    elif pathname == '/projet':
        return projet.layout
    else:
        return home.layout

if __name__ == '__main__':
    app.run_server(debug=True)