from dash import html
import dash_bootstrap_components as dbc

# needed only if running this as a single page app
#external_stylesheets = [dbc.themes.LUX]

#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# change to app.layout if running as single page app instead
layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1("Le projet", className="text-center")
                    , className="mb-5 mt-5")
        ]),
        dbc.Row([
            dbc.Col(html.H5(children="Dans le monde des cinémas, la concurrence est rude, surtout pour un petit cinéma de "
                                "quartier comme le nôtre qui face aux grandes chaînes dont le réseau s'étoffe en périphérie des villes."
                                "Constatant le ralentissement de notre activité, nous avons décidé de faire notre révolution numérique"
                                 "en vous propososant cette application dotée d'un système de recommandations de films pour les cinéphages en manque d'"
                                "inspiration. Cette application a été concocté par l'équipe des DATACTORS dont voici une petite présentation:"
                                )
                    , className="mb-4")
            ]),


#######################################################################################################################
    #PRESENTATION DATACTORS
#######################################################################################################################

        dbc.Row([
        # IMAGE #########################################################################################START

            #CARD - ALINE #########################################################################################START

            dbc.Col([

                dbc.Card(
                    [
                        dbc.CardHeader("Product Owner"),
                        dbc.CardBody(
                            [
                                html.H4("Aline", className="text-center"),
                                html.Img(src="/assets/photo_Aline.png", width="210px",
                                         style={'display': 'block', 'margin-left': 'auto',
                                                'margin-right': 'auto',
                                                'margin-bottom': '20px'}),

                                html.P(children=[
                                    "Pendant 12 années dans le secteur des RH, j'ai exploité et analysé de nombreuses données "
                                    "afin d'orienter la Direction dans sa prise de décisions. J'ai souhaité rejoindre la "
                                    "formation Data Analyst de la Wild Code School pour appronfondir"
                                    'mes connaissances en traitement, analyse et visualisation de données. La question du bien-être au travail'
                                    "m'amène à vouloir intégrer une entreprise à taille humaine, soucieuse "
                                    "de l'épanouissement personnel et professionnel de ses salariés. Passionnée par la nature et les animaux, "
                                    "il m' est  essentiel de limiter mon impact environnemental."],
                                    className="card-text"),
                            ]
                        ),
                        dbc.CardFooter(children=[
                            html.P('Rôle dans le projet ', className="text-right", style={'font-size': '15px',
                                                                                          'margin-bottom': '2px',
                                                                                          'color': 'grey'}),
                            html.H6("Exploration des données - Mise en place du Machine Learning - Visualisations", className="text-left"),
                            dbc.Button("LinkedIn", href="https://www.linkedin.com/in/aline-blanck/", color="info",target='blank',style={'display': 'block','margin-left':'auto','margin-right':'auto','margin-top':'15px','margin-bottom':'20px'})

                        ], className="mt-3")

                    ],style={"width": "100%", 'min-height':'870px'})

            ], width=4, className="mb-4"),
            # CARD - GUILLAUME #########################################################################################START

            dbc.Col([

                dbc.Card(
                    [
                        dbc.CardHeader("Team Member"),
                        dbc.CardBody(
                            [
                                html.H4("Guillaume", className="text-center"),
                                html.Img(src="/assets/photo_Guillaume.png", width="170px",
                                         style={'display': 'block', 'margin-left': 'auto',
                                                'margin-right': 'auto',
                                                'margin-bottom': '20px'}),

                                html.P(children=[
                                    "Après 18 ans et différentes expériences en tant que Technicien en Support Informatique, "
                                    "j’ai décidé de pousser mon intérêt dans dans l’analyse de données et de rejoindre la Wild "
                                    "Code School afin de me reconvertir en tant que Data Analyst. Passionné de voyages, membre "
                                    "actif d’un projet d’habitat participatif et de la vie sociale de quartier, j’aimerais mettre "
                                    "à profit mes compétences acquises durant la formation dans le cadre d’actions d'intérêt collectif."],
                                    className="card-text"),
                            ]
                        ),
                        dbc.CardFooter(children=[
                            html.P('Rôle dans le projet ', className="text-right", style={'font-size': '15px',
                                                                                          'margin-bottom': '2px',
                                                                                          'color': 'grey'}),
                            html.H6("Collecte des données (API TMDB) - Exploration, traitement,visualisations.", className="text-left"),
                            dbc.Button("LinkedIn", href=" https://www.linkedin.com/in/guillaume-barry/", color="info",target='blank',style={'display': 'block','margin-left':'auto','margin-right':'auto','margin-top':'15px','margin-bottom':'20px'})

                        ], className="mt-3")

                    ],style={"width": "100%", 'min-height':'870px'})
            ], width=4, className="mb-4"),



            # CARD - JONATHAN #########################################################################################START
            dbc.Col([

                dbc.Card(
                    [
                        dbc.CardHeader("Scrum master"),
                        dbc.CardBody(
                            [
                                html.H4("Jonathan", className="text-center"),
                                html.Img(src="/assets/photo_Jonathan.png", width="300px",
                                         style={'display': 'block', 'margin-left': 'auto',
                                                'margin-right': 'auto',
                                                'margin-bottom': '20px'}),

                                html.P(children=[
                                    "Passionné de sciences et technologies, j'ai orienté mon goût pour ces deux domaines "
                                    "vers l'univers aussi passionnant que complexe qu'est celui de la data. Avec des milliers de "
                                    "domaines d'applications possibles, la data constitue pour moi l'opportunité de travailler sur le fond"
                                    "en étant capable de sélectionner les données pertinentes quelque soit le secteur d'activité."
                                    "Pour la forme (car des belles visualisations ont toujours plus d'impact), ma passion pour la peinture numérique "
                                    "m'a permis de développer ma créativité et une sensibilité sur ce qui touche au visuel."],
                                    className="card-text"),
                            ]
                        ),
                        dbc.CardFooter(children=[
                            html.P('Rôle dans le projet ', className="text-right", style={'font-size': '15px','margin-bottom': '2px','color': 'grey'}),
                            html.H6("Collecte et traitement de données - Visualisations - Montage de l'app Dash", className="text-left"),
                            dbc.Button("LinkedIn", href="lien", color="info",target='blank',style={'display': 'block','margin-left':'auto','margin-right':'auto','margin-top':'15px','margin-bottom':'20px'})

                        ], className="mt-3")

                    ],style={"width": "100%", 'min-height':'870px'})
            ], width=4, className="mb-4"),


    ]),


    dbc.Row([



            #CARD - PABLO #########################################################################################START

        dbc.Col([],width=2),

        dbc.Col([

            dbc.Card(
                [
                    dbc.CardHeader("Team Member"),
                    dbc.CardBody(
                        [
                            html.H4("Pablo", className="text-center"),
                            html.Img(src="/assets/photo_Pablo.png", width="200px",
                                     style={'display': 'block', 'margin-left': 'auto',
                                            'margin-right': 'auto',
                                            'margin-bottom': '20px'}),

                            html.P(children=[
                                "Ancien enseignant et formateur, puis spécialisé dans la politique éducative et l'analyse "
                                "du secteur de l'éducation, j'ai décidé de réorienter ma carrière vers l'analyse des données. "
                                "Grâce à la Wild Code School, je développe des compétences dans la collecte, le traitement et "
                                "la visualisation de données de tout type. Toujours intéressé par l'éducation, ainsi que par le "
                                "sport (je suis arbitre de handball), je veux mettre mes compétences au profit de ces secteurs."],
                                className="card-text"),
                        ]
                    ),
                    dbc.CardFooter(children=[
                        html.P('Rôle dans le projet ', className="text-right", style={'font-size': '15px',
                                                                                      'margin-bottom': '2px',
                                                                                      'color': 'grey'}),

                        html.H6("Collecte (API) - traitement de données -  Machine learning dont intégration Dash", className="text-left"),
                        html.H6(' ', className="text-right"),
                        dbc.Button("LinkedIn", href="lien", color="info",target='blank',style={'display': 'block','margin-left':'auto','margin-right':'auto','margin-top':'15px',
                                                                                                         'margin-bottom':'20px'}),
                        dbc.Button("Github", href="https://github.com/pablomc87", color="secondary",target='blank',style={'display': 'block','margin-left':'auto','margin-right':'auto','margin-top':'15px',
                                                                                                         'margin-bottom':'20px'})

                    ], className="mt-3")

                ],style={"width": "100%", 'min-height':'900px'})
        ], width=4, className="mb-4"),

            # CARD - RAMI #########################################################################################START

        dbc.Col([

            dbc.Card(
                [
                    dbc.CardHeader("Team Member"),
                    dbc.CardBody(
                        [
                            html.H4("Rémy", className="text-center"),
                            html.Img(src="/assets/photo_Remy.png", width="220px",
                                     style={'display': 'block', 'margin-left': 'auto',
                                            'margin-right': 'auto',
                                            'margin-bottom': '20px'}),

                            html.P(children=[
                                "Après 10 ans et différentes expériences en tant que ingénieur de télécommunication dans "
                                "plusieurs pays et étude le MBA à Paris. J’ai décidé de pousser mon intérêt dans l’analyse "
                                "de données qui m’a donné une autre dimension à mes connaissances de l’agilité, design thinking "
                                "et à ma vision du futur de business pour être au courant de business analyses. J’adore le football "
                                "et je suis grand fan de Football club de Barcelona"],
                                className="card-text"),
                        ]
                    ),
                    dbc.CardFooter(children=[
                        html.P('Rôle dans le projet ', className="text-right", style={'font-size': '15px',
                                                                                      'margin-bottom': '2px',
                                                                                      'color': 'grey'}),
                        html.H6("Traitement - Visualisations", className="text-left"),
                        dbc.Button("LinkedIn", href="lien", color="info",style={'display': 'block','margin-left':'auto','margin-right':'auto','margin-top':'15px',
                                                                                                         'margin-bottom':'20px'}),
                        dbc.Button("Github", href="https://github.com/Remydata", color="secondary",target='blank',style={'display': 'block','margin-left':'auto','margin-right':'auto','margin-top':'15px',
                                                                                                         'margin-bottom':'20px'})


                    ], className="mt-3")

                ],style={"width": "100%", 'min-height':'900px'})
        ], width=4, className="mb-4"),

        dbc.Col([],width=2),

    ]),

        ####################################################################################################
        # CREDITS OF USED RESOURCES
        ####################################################################################################

        dbc.Row([

            html.H3("Ressources sur le projet", className="text-center",style={'margin-bottom':'20px','margin-top':'20px'}),


            # CARD - GITHUB #########################################################################################START

            dbc.Col([



                dbc.Card(
                    [
                        dbc.CardHeader("Github du projet"),
                        dbc.CardBody(
                            [
                                html.Img(src="/assets/logo-github.png", width="100em",
                                         style={'display': 'block', 'margin-left': 'auto',
                                                'margin-right': 'auto',
                                                'margin-bottom': '20px'}),

                                html.P(children=["Retrouvez en partage sur Github le code de notre projet."],
                                    className="card-text"),
                            ]
                        ),
                        dbc.CardFooter(children=[

                            dbc.Button("Aller sur Github", href="x", color="secondary",target='blank',style={'display': 'block','margin-left':'auto','margin-right':'auto','margin-top':'15px',
                                                                                                         'margin-bottom':'20px'})

                        ], className="mt-3")

                    ], style={"width": "100%", 'min-height':'350x'})

            ], width=4, className="mb-4"),
            # CARD - NOS CHOIX EXPLIQUES #########################################################################################START

            dbc.Col([

                dbc.Card(
                    [
                        dbc.CardHeader("Nos choix expliqués"),
                        dbc.CardBody(
                            [
                                html.Img(src="/assets/collab_logo.svg", width="150px",
                                         style={'display': 'block', 'margin-left': 'auto',
                                                'margin-right': 'auto',
                                                'margin-bottom': '20px'}),

                                html.P(children=[
                                    "Les grandes étapes de notre projet réunies au sein d'un notebook."],
                                    className="card-text"),
                            ]
                        ),
                        dbc.CardFooter(children=[

                            dbc.Button("Ouvrir le notebook", href="https://colab.research.google.com/drive/18dqRQOiSYkcjz3NiQwr63PdvUPiTbsqp?usp=sharing", color="warning",target='blank',style={'display': 'block','margin-left':'auto','margin-right':'auto','margin-top':'15px',
                                                                                                         'margin-bottom':'20px'})

                        ], className="mt-3")

                    ], style={"width": "100%", 'min-height':'350px'})
            ], width=4, className="mb-4"),

            # CARD - PREZ#########################################################################################START
            dbc.Col([

                dbc.Card(
                    [
                        dbc.CardHeader("Présentation"),
                        dbc.CardBody(
                            [
                                html.Img(src="/assets/Canva-Nouveau-Logo.png", width="100px",
                                         style={'display': 'block', 'margin-left': 'auto',
                                                'margin-right': 'auto',
                                                'margin-bottom': '20px'}),

                                html.P(children=[
                                    "Accédez à la présentation de notre projet sur Canva."],
                                    className="card-text"),
                            ]
                        ),
                        dbc.CardFooter(children=[

                            dbc.Button("Accéder à la présentation",
                                  href="https://www.canva.com/design/DAE_z2Jjndk/VLOmhOitlihnW42Lnq27pw/view?utm_content=DAE_z2Jjndk&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink",
                                       color="info",target='blank',style={'display': 'block','margin-left':'auto','margin-right':'auto','margin-top':'15px','margin-bottom':'20px'})

                        ], className="mt-3")

                    ], style={"width": "100%", 'min-height':'350px'})
            ], width=4, className="mb-4"),

        ]),

    ]),



])

# needed only if running this as a single page app
# if __name__ == '__main__':
#     app.run_server(host='127.0.0.1', debug=True)