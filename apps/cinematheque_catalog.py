from dash import html, dash_table,callback,dcc
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
from app import app
from dash.dependencies import Input, Output


# needed only if running this as a single page app
#external_stylesheets = [dbc.themes.LUX]

#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

####################################################################################################
# 000 - DATA MAPPING
####################################################################################################
#Database mapping

df_movies = pd.read_csv('df_app_final_fulltrad.csv', low_memory=False)
df_movies.set_index('id', inplace=True, drop=False)


annee_min = df_movies['annee'][df_movies['annee']!=0].min()
annee_max = df_movies['annee'].max()



# change to app.layout if running as single page app instead
layout = html.Div([
    dbc.Container([
        dbc.Row([
            html.H1("Cinémathèque: notre catalogue de films", className="text-center",style={'margin-top':'40px'}),
            html.H5(children=["Parcourez notre catalogue et visualisez-les informations sur les films de votre choix."],className="text-center",style={'margin-bottom':'40px'})
        ]),

        #INITIALISATION DE LA PARTIE CATALOGUE (module type DATATABLE)#################################################

        # INITIALISATION DE LA PARTIE FILTRAGE#################################################
        dbc.Row([
            # FITLRAGE SUR LE TITRE #################################################
            dbc.Col([], className="text-center", width=3),


            dbc.Col([

                html.H4("Rechercher un film", className="text-center"),

                dbc.Input(id="movie_input", placeholder="Saisissez votre recherche", size="lg", className="center-align", style={"margin-bottom":"15px", "width":"100%"}),

                dbc.RadioItems(
                    id="data_selector",
                    className="btn-group",
                    inputClassName="btn-check",
                    labelClassName="btn btn-outline-warning",
                    labelCheckedClassName="active",
                    options=[
                        {"label": "Titres", "value": 1},
                        {"label": "Réalisateurs", "value": 2},
                        {"label": "Acteurs/actrices", "value": 3},
                    ],
                    value=1,
                ),


                html.H4("Rechercher une période", className="text-center",style={'margin-top':'20px'}),

                dcc.RangeSlider(id='years-slider',min=annee_min,max=annee_max,marks=None,tooltip={"placement": "bottom", "always_visible": True},
                                value=[annee_min,annee_max])

            ], className="text-center", width=6),


            dbc.Col([], className="text-center", width=3),


        ], className="mb-12", style={'margin-bottom': '25px'}),

        dbc.Row(children=[],id='movie_table_container', className="mb-12",style={'margin-top':'10px'}), # FIN DE LA ROW  FILTRES + DATAFRAME

        dbc.Card(children=[],id="movie_id_card",
                             body=True, color="dark", outline=True),


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
    Output('movie_table_container', 'children'),
    [Input('movie_input', 'value'),
    Input("data_selector", "value"),
    Input("years-slider", "value"),
     ])

def update_data_table(text_input,radio_item_value,period):
    
    df_movies_filtered=df_movies

    try:

        if text_input != None:
            text_input = str(text_input).lower()
            if radio_item_value==1:
                df_movies_filtered = df_movies_filtered.dropna(subset='titre')
                df_movies_filtered = df_movies_filtered.loc[df_movies_filtered['titre'].str.lower().str.contains(text_input)]
                df_movies_filtered = df_movies_filtered[(df_movies_filtered['annee'] > period[0]) & (df_movies_filtered['annee'] < period[1])]

                return [dash_table.DataTable(data=df_movies_filtered.to_dict('records'),
                                         columns=[{"name": i, "id": i}
                                                  for i in df_movies_filtered.loc[:,['titre',
                                                                            'realisateur',
                                                                            'duree',
                                                                            'annee',
                                                                            'acteurs',
                                                                            'genres_fr',
                                                                            'notation']]],
                                         style_data={
                                                    'backgroundColor': 'transparent',
                                                     'color':'white',
                                                     'whiteSpace': 'normal', 'height': 'auto',
                                                     'lineHeight': '20px'
                                                    },
                                        style_header={
                                                'backgroundColor': 'black',
                                                'fontWeight': 'bold',
                                                'height':'35px'},
                                        page_size=10,
                                        style_as_list_view=True,
                                        fill_width=True,
                                        style_cell={'fontSize':15, 'font-family':'cursive'},
                                        id="datatable-row-ids"
                                    )]

            elif radio_item_value==2:
                
                df_movies_filtered = df_movies_filtered.dropna(subset='realisateur')
                df_movies_filtered = df_movies_filtered.loc[df_movies_filtered['realisateur'].str.lower().str.contains(text_input)]
                df_movies_filtered = df_movies_filtered[(df_movies_filtered['annee'] > period[0]) & (df_movies_filtered['annee'] < period[1])]
                return [dash_table.DataTable(data=df_movies_filtered.to_dict('records'),
                                         columns=[{"name": i, "id": i}
                                                  for i in df_movies_filtered.loc[:,['titre',
                                                                            'realisateur',
                                                                            'duree',
                                                                            'annee',
                                                                            'acteurs',
                                                                            'genres_fr',
                                                                            'notation']]],
                                         style_data={
                                                    'backgroundColor': 'transparent',
                                                     'color':'white',
                                                     'whiteSpace': 'normal', 'height': 'auto',
                                                     'lineHeight': '20px'
                                                    },
                                        style_header={
                                                'backgroundColor': 'black',
                                                'fontWeight': 'bold',
                                                'height':'35px'},
                                        page_size=10,
                                        style_as_list_view=True,
                                        fill_width=True,
                                        style_cell={'fontSize':15, 'font-family':'cursive'},
                                        id="datatable-row-ids"
                                    )]

            elif radio_item_value==3:
                df_movies_filtered = df_movies_filtered.dropna(subset='acteurs')
                df_movies_filtered = df_movies_filtered.loc[df_movies_filtered['acteurs'].str.lower().str.contains(text_input)]
                df_movies_filtered = df_movies_filtered[(df_movies_filtered['annee'] > period[0]) & (df_movies_filtered['annee'] < period[1])]
                return [dash_table.DataTable(data=df_movies_filtered.to_dict('records'),
                                         columns=[{"name": i, "id": i}
                                                  for i in df_movies_filtered.loc[:,['titre',
                                                                            'realisateur',
                                                                            'duree',
                                                                            'annee',
                                                                            'acteurs',
                                                                            'genres_fr',
                                                                            'notation']]],
                                         style_data={
                                                    'backgroundColor': 'transparent',
                                                     'color':'white',
                                                     'whiteSpace': 'normal', 'height': 'auto',
                                                     'lineHeight': '20px'
                                                    },
                                        style_header={
                                                'backgroundColor': 'black',
                                                'fontWeight': 'bold',
                                                'height':'35px'},
                                        page_size=10,
                                        style_as_list_view=True,
                                        fill_width=True,
                                        style_cell={'fontSize':15, 'font-family':'cursive'},
                                        id="datatable-row-ids"
                                    )]

        else:
            return html.H4(children=["Votre sélection"])

    except:
        return ''

@app.callback(
    Output('movie_id_card', 'children'),
    Input('datatable-row-ids', 'active_cell'))

def return_movie_info(active_cell):
    try:
        return [
            dbc.Container([
            #TITRE DU BLOC DE PRESENTATION
                dbc.Row([
                    html.H3("Informations sur votre film", className="text-left", style={'border-bottom':'solid',
                                                                                         'border-size':'0.3px',
                                                                                         'border-color':'white',
                                                                                         'margin-bottom':'10px'
                                                                                         })
                ]),

                # PREMIERE LIGNE DU BLOC DE PRESENTATION
                dbc.Row([
                    # COLONNE POUR AFFICHAGE DE L'AFFICHE DU FILM
                    dbc.Col(children=[], id="image_container",width=3, className = 'align-self-center', style={'margin-top':'10px'}),

                    # COLONNE POUR AFFICHAGE DES INFORMATIONS DU FILM___________________________________________________
                    # Titre du film_____________________________________________________________________________________
                    dbc.Col(children=[

                        dbc.Row(children=[
                            html.H3(df_movies.loc[active_cell['row_id'], "titre"],className="text-left"),
                        ]),

                        dbc.Row(children=[
                            html.P('Titre original: ', className="text-right", style={'font-size': '15px',
                                                                                 'margin-bottom': '2px',
                                                                                 'color': 'grey'}),
                            html.H6(df_movies.loc[active_cell['row_id'], "titre_original"], className="text-left")
                        ]),

                        # LIGNE POUR LES METADONNES DU FILM

                        dbc.Row(children=[
                            # Données de statue / année de sortie / durée______________________________________________
                            dbc.Col(children=[
                                html.P('Statut : ', className="text-right", style={'font-size':'15px',
                                                                                    'margin-bottom':'2px',
                                                                                    'color':'grey'}),
                                html.P(df_movies.loc[active_cell['row_id'], "statut"], className="text-left")
                            ],width=2),

                            dbc.Col(children=[
                                html.P('Année de sortie: ', className="text-right", style={'font-size':'15px',
                                                                                           'margin-bottom':'2px',
                                                                                           'color':'grey'}),
                                html.P(df_movies.loc[active_cell['row_id'], "annee"], className="text-left")
                            ],width=2),

                            dbc.Col(children=[
                                html.P('Durée : ', className="text-right", style={'font-size':'15px',
                                                                                  'margin-bottom': '2px',
                                                                                'color':'grey'}),
                                html.P("{:} min".format(df_movies.loc[active_cell['row_id'], "duree"]), className="text-left")
                            ],width=2),

                            dbc.Col(children=[
                                html.P('Genre(s): ', className="text-right", style={'font-size': '15px',
                                                                                  'margin-bottom': '2px',
                                                                                  'color': 'grey'}),
                                html.P(df_movies.loc[active_cell['row_id'], "genres_fr"], className="text-left")
                            ],width=6),

                        ],style={'border-top':'0.3px solid grey','height': '55px','border-bottom': '0.3px solid grey'
                                 }),


                        # Données de réalisateur/ au casting / au scénario_____________________________________________
                        dbc.Row(children=[

                            dbc.Col(children=[
                                html.P('A la réalisation : ', className="text-right", style={'font-size': '15px',
                                                                                   'margin-bottom': '2px',
                                                                                   'color': 'grey'}),
                                html.P(df_movies.loc[active_cell['row_id'], "realisateur"],  className="text-left")
                            ],width=3),

                            dbc.Col(children=[
                                html.P('Au casting : ', className="text-right", style={'font-size': '15px',
                                                                                    'margin-bottom': '2px',
                                                                                    'color': 'grey'}),
                                html.P(df_movies.loc[active_cell['row_id'], "acteurs"], className="text-left")
                            ],width=9),


                        ], style={'height': '55px','border-bottom': '0.3px solid grey','margin-bottom':'10px'
                                  }),

                        # Partie Synopsys______________________________________________________________________________
                        dbc.Row(children=[
                            html.P('Synopsys : ', className="text-right", style={'font-size': '15px',
                                                                                   'margin-bottom': '2px',
                                                                                   'color': 'grey'}),
                            html.H6(df_movies.loc[active_cell['row_id'], "synopsys"],className="text-left")
                                ]),

                        # Production / Composition ______________________________________________________________________________
                        dbc.Row(children=[

                            dbc.Col(children=[
                                html.P('A la production :', className="text-right", style={'font-size': '15px',
                                                                                             'margin-bottom': '2px',
                                                                                             'color': 'grey'}),
                                html.P(df_movies.loc[active_cell['row_id'], "producteur"], className="text-left")
                            ]),

                            dbc.Col(children=[
                                html.P('A la bande-originale : ', className="text-right", style={'font-size': '15px',
                                                                                            'margin-bottom': '2px',
                                                                                            'color': 'grey'}),
                                html.P(df_movies.loc[active_cell['row_id'], "compositeur"], className="text-left")
                            ]),



                        ], style={'height': '55px', 'border-top': '0.3px solid grey', 'margin-top': '10px'
                                  }),

                    ], width=8, className="mb-4", style={'margin-left':'20px'})
                ], className="mb-12", style={'margin-bottom':'20px'}),


                # PARTIE STATISTIQUES ________________________________________________________________________________
                dbc.Row(children=[

                    dbc.Col(children=[
                        html.H5("Statistiques", className="text-left", style={'padding-top': '8px',
                                                                                     'color': 'grey'}),
                    ]),

                    dbc.Col(children=[
                        html.P('Budget : ', className="text-right", style={'font-size': '15px',
                                                                                     'margin-bottom': '2px',
                                                                                     'color': 'grey'}),
                        html.P("${:,.2f}".format(df_movies.loc[active_cell['row_id'], "budget"]), className="text-left")
                    ]),

                    dbc.Col(children=[
                        html.P('Recettes : ', className="text-right", style={'font-size': '15px',
                                                                                    'margin-bottom': '2px',
                                                                                    'color': 'grey'}),
                        html.P("${:,.2f}".format(df_movies.loc[active_cell['row_id'], "recettes"]), className="text-left")
                    ]),

                    dbc.Col(children=[
                        html.P('Notation IMDB : ', className="text-right", style={'font-size': '15px',
                                                                               'margin-bottom': '2px',
                                                                               'color': 'grey'}),
                        html.P(df_movies.loc[active_cell['row_id'], "notation"], className="text-left")
                    ]),

                    dbc.Col(children=[
                        html.P('Notation TMDB : ', className="text-right", style={'font-size': '15px',
                                                                                  'margin-bottom': '2px',
                                                                                  'color': 'grey'}),
                        html.P(df_movies.loc[active_cell['row_id'], "popularité"], className="text-left")
                    ]),


                ], style={'height': 'auto','border-top': '0.3px solid grey', 'margin-bottom': '10px'
                          }),

                # PARTIE VIDEO________________________________________________________________________________

                    dbc.Row(children=[
                        html.H3("Vidéo (bande-annonce, trailer, etc)", className="text-left", style={'border-bottom': 'solid',
                                                                                     'border-size': '0.3px',
                                                                                     'border-color': 'white',
                                                                                     'margin-bottom': '10px'
                                                                                     }),
                    ]),



                 dbc.Row(children=[],id="video_container"),


            ])#FIN DU DBC CONTAINER
         ] #FIN DU RETURN
    except:
        return ''

@app.callback(
    Output('image_container', 'children'),
    Input('datatable-row-ids', 'active_cell'))

def return_movie_poster1(active_cell):
    try:
        if df_movies.loc[active_cell['row_id'], 'url_affiche'] !='0':
            return [
                html.Img(
                    src="https://image.tmdb.org/t/p/w500/" + str(df_movies.loc[active_cell['row_id'], "url_affiche"]),
                    width="300px")
                    ]
        else:
            return [
                html.H5("Pas d'affiche pour ce film", className="text-center", style={'padding-top': '8px', 'color': 'grey'}),
            ]
    except:
        return ''



@app.callback(
    Output('video_container', 'children'),
    Input('datatable-row-ids', 'active_cell'))

def return_movie_video(active_cell):
    try:
        if df_movies.loc[active_cell['row_id'], 'site_vid'] =='YouTube':
            return [
                     html.Iframe(
                       src="https://www.youtube.com/embed/" + str(df_movies.loc[active_cell['row_id'], 'key_vid']),
                       style={'width': '1000px',
                              'height': '600px',
                              'display':'block',
                              'margin-left':'auto',
                              'margin-right': 'auto',
                              'margin-top': '20px'
                              }),

                        html.H4(df_movies.loc[active_cell['row_id'], "nom_vid"], className="text-center",
                            style={
                                   'margin-top': '10px',
                                    'margin-bottom': '25px'
                                   })
                    ]

        elif df_movies.loc[active_cell['row_id'], 'site_vid'] =='Vimeo':
            return [
                     html.Video(
                       src="https://vimeo.com" + str(df_movies.loc[active_cell['row_id'], 'key_vid']),
                                style={'width': '80%',
                                       'height': 'auto',
                                       'display': 'block',
                                       'margin-left': 'auto',
                                       'margin-right': 'auto',
                                       'margin-top': '20px'
                                       }),


                        html.H3(df_movies.loc[active_cell['row_id'], "nom_vid"], className="text-center",
                            style={
                                   'margin-top': '10px',
                                    'margin-bottom': '25px'
                                   })

                ]
        else:
            return [
                html.H5("Aucun contenu vidéo pour ce film", className="text-left", style={'padding-top': '8px', 'color': 'grey','margin-bottom': '25px'}),
            ]
    except:
        return ''


