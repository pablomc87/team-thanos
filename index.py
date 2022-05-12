from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

# must add this line in order for the app to be deployed successfully on Heroku
from app import server
from app import app
# import all pages in the app
from apps import contexte, home, projet, solutions

# building the navigation bar
# https://github.com/facultyai/dash-bootstrap-components/blob/master/examples/advanced-component-usage/Navbars.py


navbar = dbc.NavbarSimple(


    children=[
        dbc.NavItem(dbc.NavLink("Le contexte", href="/contexte")),
        dbc.NavItem(dbc.NavLink("Les solutions", href="/solutions")),
        dbc.NavItem(dbc.NavLink("Team Thanos", href="/projet")),

    ],
    brand="Team Thanos",
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
    elif pathname == '/solutions':
        return solutions.layout
    elif pathname == '/contexte':
        return contexte.layout
    elif pathname == '/projet':
        return projet.layout
    else:
        return home.layout

if __name__ == '__main__':
    app.run_server(debug=True)