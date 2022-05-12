from dash import html
import dash_bootstrap_components as dbc

# needed only if running this as a single page app
#external_stylesheets = [dbc.themes.LUX]

#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# change to app.layout if running as single page app instead
layout = html.Div([
    dbc.Container([

        dbc.Row([
            dbc.Carousel(
                            items=[
                                {
                                    "key": "1",
                                    "src": "/assets/cinema_photo_XL.jpg",
                                    "header": "6 salles , 450 sièges ",
                                    "caption": "Un confort garanti à chacune de vos séances",
                                },
                                {
                                    "key": "2",
                                    "src": "/assets/salle_4dx.jpg",
                                    "header": "En 2021, 120 000 personnes ont fréquenté nos salles obscures",
                                    "caption": "En 2022, nous ouvrons notre première salle 4DX, une première pour un "
                                               "cinéma de petite exploitation",
                                },
                                {
                                    "key": "3",
                                    "src": "assets/clap.jpg",
                                    "header": "Vous êtes maître de notre programmation",
                                    "caption": "Utilisez notre application de recommandation pour voir diffuser vos films"
                                               "favoris sur grand écran.",
                                },
                            ],style={'height':'550px', 'width':'auto',"margin-bottom":"150px"}
                        )
        ]),


        dbc.Row([
            dbc.Col(html.H1("Bienvenue aux Bobines Creuses, votre cinéma de quartier", className="text-center")
                    )
        ]),

        dbc.Row([
            dbc.Col(html.H5(children="Depuis 1990, votre cinéma de quartier Les Bobines Creuses s'engage à allier "
                                     "programmation de qualité et conditions de visionnage optimales pour votre confort. "
                                      "Animé depuis tout petit par la passion du cinéma, Alexandre Martin, son directeur, "
                                     "n'a cessé de travailler avec les meilleurs distributeurs afin de conférer à son "
                                     "établissement son ADN si particulier."
                                     )
                    , className="mb-4")
            ]),


        dbc.Row([
            dbc.Col(html.P(children="Depuis plusieurs années, le cinéma n'a cessé de se moderniser pour afin de vous offrir "
                                     "toujours plus de services tout en savourant vos films préférés. Avec les progrès du numérique, "
                                    "nous poursuivrons notre transition numériques en vous proposant de devenir partie prenante de "
                                    "la vie de votre cinéma."
                                                 )
                                , className="mb-4")
                ]),

        dbc.Row([]),

        dbc.Row([
            dbc.Col(html.H2("Nos ressources", className="text-center")
                    , className="mb-5 mt-5"),
                ]),
        ####################################################################################################
        # CREDITS OF USED RESOURCES
        ####################################################################################################

        dbc.Row([

            # CARD - DATABASE IMDB #####################################################################################
            dbc.Col(dbc.Card(children=[html.H4(children='La base de données IMDB',
                                               className="text-center"),
                                       # PHOTO###################################################################
                                       dbc.Row([dbc.Col(html.Img(src="/assets/IMDB_logo.png", width="130px",style={
                                                                                                         'display':'block',
                                                                                                         'margin-left':'auto',
                                                                                                         'margin-right':'auto',
                                                                                                         'margin-top': '15px',
                                                                                                         'margin-bottom':'20px'})

                                                        )]
                                               ),
                                       # TEXT###################################################################

                                       dbc.Row([dbc.Col(
                                           html.P(
                                               children="Les données d'Imdb, la plus importante base de données cinématographique"
                                                        "ont été la colonne vertébrale de ce projet. L'API fournie nous a permis "
                                                        "de collecter une partie des informations nécessaires à la construction "
                                                        "de notre cinémathèque.")
                                           , style={'margin-bottom':'0px'})
                                                ]
                                       ),
                                       # LINKS###################################################################
                                       dbc.Row([dbc.Col(dbc.Button("Aller sur IMDB", href="https://www.imdb.com",
                                                                   color="warning",target='blank',style={'display': 'block','margin-left':'auto','margin-right':'auto','margin-top':'15px',
                                                                                                         'margin-bottom':'20px'}),
                                                        className="mt-3")])

                                       ],
                             body=True, color="dark", outline=True, style={'height':'460px'})
                    , width=4, className="mb-4"),

            # CARD - DATABASE TMDB  ####################################################################################

            dbc.Col(dbc.Card(children=[html.H4(children='La base de données TMDB',
                                               className="text-center", style={"margin-bottom":"20px"}),
                                       # PHOTO###################################################################
                                       dbc.Row([dbc.Col(html.Img(
                                           src="https://www.themoviedb.org/assets/2/v4/logos/v2/blue_square_2-d537fb228cf3ded904ef09b136fe3fec72548ebc1fea3fbbd1ad9e36364db38b.svg",
                                           width="150px",style={
                                                                 'display':'block',
                                                                 'margin-left':'auto',
                                                                 'margin-right':'auto',
                                                                 'margin-top': '15px',
                                                                 'margin-bottom':'25px'}),
                                                        )]
                                               ),
                                       # TEXT###################################################################
                                       dbc.Row([
                                           html.P(
                                               children="La base de données TMDB est une autre base de données cinématographique."
                                                        "Son contenu, plus francisé, nous a permis d'avoir plus d'informations "
                                                        "dans notre langue. Une étape nécessaire pour vous permettre de consulter "
                                                        "notre base sans traducteur.")
                                       ],style={'margin-bottom':'0px'}
                                       ),
                                       # LINKS###################################################################
                                       dbc.Row([dbc.Col(
                                           dbc.Button("Aller sur TMDB", href="https://www.themoviedb.org/?language=fr",
                                                      color="info",target='blank',style={'display': 'block','margin-left':'auto','margin-right':'auto','margin-top':'15px',
                                                                                                         'margin-bottom':'20px'}),
                                           className="mt-3")], justify="center")

                                       ],
                             body=True, color="dark", outline=True, style={'height':'460px'})
                    , width=4, className="mb-4"),

            # CARD - WILD CODE SCHOOL  #################################################################################

            dbc.Col(dbc.Card(children=[html.H4(children='Wild Code School',
                                               className="text-center"),
                                       # PHOTO###################################################################
                                       dbc.Row([
                                           dbc.Col(
                                               html.Img(src="/assets/WCS_logo.png", width="250x",style={
                                                                                                         'display': 'block',
                                                                                                         'margin-left':'auto',
                                                                                                         'margin-right':'auto',
                                                                                                         'margin-top':'15px',
                                                                                                         'margin-bottom':'20px'})
                                                    )
                                                ]),
                                       # TEXT###################################################################
                                       dbc.Row([dbc.Col(
                                           html.P(children="Ce projet est un scénario fictif donné dans le cadre d'une formation "
                                                           "Data Analyst dispensé par la Wild Code School. L'objectif est "
                                                           "de proposer une application de recommandations de films grâce au machine learning."
                                                           "Rendez-vous dans la rubrique pour >Le projet< pour en savoir plus.")
                                           , style={'margin-bottom':'0px'})]
                                       ),
                                       # LINKS###################################################################
                                       dbc.Row([dbc.Col(
                                           dbc.Button("Aller sur le site de la WCS", href="https://www.wildcodeschool.com/fr-FR",
                                                      color="danger",target='blank',style={'display': 'block','margin-left':'auto','margin-right':'auto','margin-top':'15px',
                                                                                                         'margin-bottom':'20px'}),
                                           className="mt-3")], )

                                       ],
                             body=True, color="dark", outline=True,style={'height':'460px'})
                    , width=4, className="mb-4")

                ], className="mb-5"),


        ####################################################################################################
        # FOOTER
        ####################################################################################################
        dbc.Row([

            dbc.Col((html.H3(children='Coordonnées', className="text-left",style={'padding-top':'10px'}),
                     html.H5(children='Cinéma - Les bobines creuses', className="text-left"),
                     html.P("120 rue des Cinéphiles", className="text-left"),
                     html.P("23000 GUERET", className="text-left",style={'margin-top':'-2px'}),
                     html.P("Tel : 0X 25 24 89 64", className="text-left",style={'margin-top':'-2px'}),
                     html.P("Mail : contact@bobines-creuses.fr", className="text-left")
                     ), width=4, className="mb-4"),

            dbc.Col((), width=4, className="mb-4"),

            dbc.Col((html.H5(children='Crédits', className="text-right",style={'padding-top':'10px'}),
                    html.A("Attributions des photos : Pexels.com",

                            href="https://www.flaticon.com/free-icon/coronavirus_2913604")


            ), width=4, className="mb-4"),

        ], className="mb-12", style={#'background': 'rgb(48,48,48)',
                                     'border-top':'solid',
                                     'border-size': '1px',
                                     'height': '250px',
                                     'width': '100%',
                                     'margin-bottom': '0px',
                                     }
        ),

        ]),#fin du DBC container



    ])


# needed only if running this as a single page app
# if __name__ == '__main__':
#     app.run_server(host='127.0.0.1', debug=True)