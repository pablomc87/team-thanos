import plotly.graph_objects as go
import pandas as pd
import numpy as np
from dash import dcc, html
from dash.dependencies import Input, Output
from dash import dash_table
import dash_bootstrap_components as dbc
from plotly.subplots import make_subplots
from app import app

# needed only if running this as a single page app
#external_stylesheets = [dbc.themes.LUX]

#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


########################################################################################################################
#INITIALISATION DES DATAFRAMES
########################################################################################################################
#1 - Dataframe complet______________________________________________________________________
# df = pd.read_csv('df_app_final_fulltrad.csv', low_memory=False)

#PARTIE GENERALE#######################################################################################################

#Dataframes pour les TOP5 multicritères

#TOP 5 Langue d'origine (création d'index et langue en colonnes)
    #df_langue = pd.DataFrame(df['langue_originale'].value_counts().head(5)).reset_index()  # Changer DF_APP avec le dataframe de Dash
#renommer les colonnes
    #df_langue.rename(columns={'index':'langue', 'langue_originale':'nombre_films'}, inplace=True)
# Création d'un dictionnaire pour renommer les codes ISO
    #trad_dict = {"en": "Anglais", "fr": 'Français', "ja": "Japonais", "it": "Italien", "de": "Allemand"}
#Application du dictionnaire
    #df_langue = df_langue.replace({"langue": trad_dict})


#Dataframe pour le Pie Chart Status
    #df_top_statut = pd.DataFrame((df.loc[:, ['statut']]).apply(pd.value_counts)).sum(axis=1).reset_index()
    #df_top_statut.rename(columns={'index':'val', 0:'count'}, inplace=True)
    #df_top_statut = df_top_statut.sort_values("count", ascending=False)


#3 - Dataframe des films non sortis
    #df_not_released=df.loc[(df['statut']=='Planifié') | (df['statut']=='Rumored') | (df['statut']=='Post-production') | (df['statut']=='En production')]

#PARTIE GENRES##########################################################################################################
    #df_top_genre = pd.DataFrame((df.loc[:, ['genre1', 'genre2', 'genre3']]).apply(pd.value_counts)).sum(axis=1)   # Changer DF_APP avec le dataframe de Dash
# créer un index et mettre la langue en colonne
    #df_top_genre = df_top_genre.reset_index()
# Renommer les colonnes
    #df_top_genre.rename(columns={'index':'genre', 0:'nombre_total'}, inplace=True)
# Tri des valeurs + limiter au top 3
    #df_top_genre = df_top_genre.sort_values("nombre_total", ascending=False)

#PARTIE ACTEURS/ACTRICES##########################################################################################################
#TOP 3
    #df_top_acteur = pd.DataFrame((df.loc[:, ['acteur_1', 'acteur_2', 'acteur_3']]).apply(pd.value_counts)).sum(axis=1)   # Changer DF_APP avec le dataframe de Dash
# créer un index et mettre la langue en colonne
    #df_top_acteur = df_top_acteur.reset_index()
# Renommer les colonnes
    #df_top_acteur.rename(columns={'index':'acteur', 0:'nombre_total_film'}, inplace=True)
# Tri des valeurs + limiter au top 3
    #df_top_acteur = df_top_acteur.sort_values("nombre_total_film", ascending=False)


"""#TOP 5 ACTEURS PAR DECENIE

    #work_base_act = df
# Ajout decade
work_base_act['decenie'] = work_base_act['annee'].dropna().astype(int)//10*10

# Création d'un dataframe par colonne acteur
df_acteur1 = work_base_act [['acteur_1', 'decenie', 'tconst']]
df_acteur1 = df_acteur1.rename(columns={'acteur_1':'acteur'})
df_acteur2 = work_base_act [['acteur_2', 'decenie', 'tconst']]
df_acteur2 = df_acteur2.rename(columns={'acteur_2':'acteur'})
df_acteur3 = work_base_act [['acteur_3', 'decenie', 'tconst']]
df_acteur3 =df_acteur3.rename(columns={'acteur_3':'acteur'})
# Concatener les 3 dataframes
df_actors123 = pd.concat([df_acteur1, df_acteur2, df_acteur3])
# Creation pivot table par décennie
work_base_actor = pd.pivot_table(df_actors123,index=["decenie", "acteur"], values=["acteur"],aggfunc=len)
# tri par nombre de tconst
work_base_actor = work_base_actor.sort_values(by=['tconst'], ascending=False)
# reset index
work_base_actor.reset_index(['acteur'], inplace=True)
# sort value
work_base_actor = work_base_actor.sort_values(by=['tconst'], ascending=False)
# Dataframes par décennie
df_top5_act1950 = work_base_actor[work_base_actor.index==1950].head()
df_top5_act1960 = work_base_actor[work_base_actor.index==1960].head()
df_top5_act1970 = work_base_actor[work_base_actor.index==1970].head()
df_top5_act1980 = work_base_actor[work_base_actor.index==1980].head()
df_top5_act1990 = work_base_actor[work_base_actor.index==1990].head()
df_top5_act2000 = work_base_actor[work_base_actor.index==2000].head()
df_top5_act2010 = work_base_actor[work_base_actor.index==2010].head()
df_top5_act2020 = work_base_actor[work_base_actor.index==2020].head()
# concat en un seul + attribution d'un ordre
df_top5_act = pd.concat([df_top5_act1950, df_top5_act1960, df_top5_act1970, df_top5_act1980, df_top5_act1990, df_top5_act2000, df_top5_act2010, df_top5_act2020])
df_top5_act = df_top5_act.reset_index()
df_top5_act ["number"]=[1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]

#TOP ACTEURS SELON MOYENNE DES NOTES
df_top_actors_avgRating = pd.read_csv('df_top5_actor_average.csv')

#PARTIE GENRES##########################################################################################################
#
work_base=pd.read_csv('Gui_Evolution_Genres.csv')
work_base['decenie'] = work_base['annee'].dropna().astype(int)//10*10

df_Action = work_base[(work_base['genre1'] == 'Action') | (work_base['genre2'] == 'Action') | (work_base['genre3'] == 'Action')]
df_Aventure = work_base[(work_base['genre1'] == 'Aventure') | (work_base['genre2'] == 'Aventure') | (work_base['genre3'] == 'Aventure')]
df_Comédie = work_base[(work_base['genre1'] == 'Comédie') | (work_base['genre2'] == 'Comédie') | (work_base['genre3'] == 'Comédie')]
df_Crime = work_base[(work_base['genre1'] == 'Crime') | (work_base['genre2'] == 'Crime') | (work_base['genre3'] == 'Crime')]
df_Drame = work_base[(work_base['genre1'] == 'Drame') | (work_base['genre2'] == 'Drame') | (work_base['genre3'] == 'Drame')]
df_Horreur = work_base[(work_base['genre1'] == 'Horreur') | (work_base['genre2'] == 'Horreur') | (work_base['genre3'] == 'Horreur')]
df_Mystère = work_base[(work_base['genre1'] == 'Mystère') | (work_base['genre2'] == 'Mystère') | (work_base['genre3'] == 'Mystère')]
df_Romance = work_base[(work_base['genre1'] == 'Romance') | (work_base['genre2'] == 'Romance') | (work_base['genre3'] == 'Romance')]
df_Thriller = work_base[(work_base['genre1'] == 'Thriller') | (work_base['genre2'] == 'Thriller') | (work_base['genre3'] == 'Thriller')]

df_Action = df_Action.groupby("decenie").size()
df_Aventure = df_Aventure.groupby("decenie").size()
df_Comédie = df_Comédie.groupby("decenie").size()
df_Crime = df_Crime.groupby("decenie").size()
df_Drame = df_Drame.groupby("decenie").size()
df_Horreur = df_Horreur.groupby("decenie").size()
df_Mystère = df_Mystère.groupby("decenie").size()
df_Romance = df_Romance.groupby("decenie").size()
df_Thriller = df_Thriller.groupby("decenie").size()

#PARTIE MONEY TALKS####################################################################################################

#Dataframe pour le TOP FILM par RECETTES_________________________________________________________
df_top_recettes = df[["titre", "recettes"]]    # Changer DF_APP avec le dataframe de Dash
df_top_recettes = pd.DataFrame(df_top_recettes.sort_values("recettes", ascending = False).head(5))


#Dataframes de la partie Money Talks_________________________________________________________
df_movies_ROI=df[(df['recettes']!=0)&(df['budget']!=0)]
ROI_ratio=pd.DataFrame(df_movies_ROI['recettes']/df_movies_ROI['budget'],columns=['br_ratio'])

work_base_money=pd.read_csv('Gui_Budget-Revenu.csv')
work_base_money_mean = pd.pivot_table(work_base_money,index=["decenie"], values=["budget", "recettes"],aggfunc=np.mean)"""

########################################################################################################################
#STYLISATION DES TABS
########################################################################################################################

tabs_styles = {
    'height': '100px',
    'backgroundColor':'rgba(235,157,15,0)',
    'borderBottom': '1px solid #d6d6d6',
}
tab_style = {
     'padding': '6px',
    'fontWeight': 'bold',
    'backgroundColor':'rgba(48,48,48,1)'
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': 'rgba(235,157,15,1)',
    'color': 'white',
    'padding': '6px'
}


###############################################################################################################
#INITIALISATION DES GRAPHS STATIQUES
###############################################################################################################
"""
# PARTIE GENERALITES#######################################
# SUBPLOTS TOP 5
keyfacts_subplot=make_subplots(rows=1,cols=4,subplot_titles=("TOP 5 Acteurs", "TOP 5 Genres", "TOP 5 langue d'origine", "TOP 5 Box-office"))

keyfacts_subplot.add_trace(go.Bar(x=df_top_acteur["acteur"].head(5), y=df_top_acteur["nombre_total_film"], hovertemplate="<br>Nom de l'acteur : %{x}<br>Nombre de films : %{y}" '<extra></extra>'),row=1, col=1)
keyfacts_subplot.add_trace(go.Bar(x=df_top_genre["genre"].head(5), y=df_top_genre["nombre_total"], hovertemplate="<br>Genre : %{x}<br>Nombre de films : %{y}" '<extra></extra>'),row=1, col=2)
keyfacts_subplot.add_trace(go.Bar(x=df_langue["langue"], y=df_langue["nombre_films"], hovertemplate="<br>Langue : %{x}<br>Nombre de films : %{y}" '<extra></extra>'),row=1, col=3)
keyfacts_subplot.add_trace(go.Bar(x=df_top_recettes["titre"], y=df_top_recettes["recettes"],customdata=df_top_recettes["recettes"]/1000000000, hovertemplate="<br>Titre : %{x}<br>Recettes :$%{customdata:,.2f}B" '<extra></extra>'),row=1, col=4)
keyfacts_subplot.update_traces(marker_color='rgba(235,157,15,1)')

keyfacts_subplot.update_layout(
                               autosize=True,
                               paper_bgcolor='rgba(0,0,0,0)',
                               plot_bgcolor='rgba(0,0,0,0)',
                               font=dict(color='white'),
                               showlegend=False
                               )

# STATUT DES FILMS


movie_status=go.Figure()
movie_status.add_trace(go.Pie(labels=df_top_statut['val'], values=df_top_statut['count']))
movie_status.update_layout(
                               autosize=True,
                               paper_bgcolor='rgba(0,0,0,0)',
                               plot_bgcolor='rgba(0,0,0,0)',
                               font=dict(color='white'),
                               )
# GENRE DES FILMS##############################################################################################

fig_barplot_evo_genres=go.Figure()
fig_barplot_evo_genres.add_trace(go.Bar(x=df_Action.index, y=df_Action.values, name="Action",marker_color='#EB9D0F', hovertemplate="Genre : Action<br>Décennie : %{x}<br>Nombre de films : %{y}" '<extra></extra>'))
fig_barplot_evo_genres.add_trace(go.Bar(x=df_Aventure.index, y=df_Aventure.values, name="Aventure",marker_color='#EB710F', hovertemplate="Genre : Aventure<br>Décennie : %{x}<br>Nombre de films : %{y}" '<extra></extra>'))
fig_barplot_evo_genres.add_trace(go.Bar(x=df_Comédie.index, y=df_Comédie.values, name="Comédie",hovertemplate="Genre : Comédie<br>Décennie : %{x}<br>Nombre de films : %{y}" '<extra></extra>'))
fig_barplot_evo_genres.add_trace(go.Bar(x=df_Crime.index, y=df_Crime.values,name="Crime",hovertemplate="Genre : Crime<br>Décennie : %{x}<br>Nombre de films : %{y}" '<extra></extra>'))
fig_barplot_evo_genres.add_trace(go.Bar(x=df_Drame.index, y=df_Drame.values, name="Drame",hovertemplate="Genre : Drame<br>Décennie : %{x}<br>Nombre de films : %{y}" '<extra></extra>'))
fig_barplot_evo_genres.add_trace(go.Bar(x=df_Horreur.index, y=df_Horreur.values, name="Horreur", hovertemplate="Genre : Horreur<br>Décennie : %{x}<br>Nombre de films : %{y}" '<extra></extra>'))
fig_barplot_evo_genres.add_trace(go.Bar(x=df_Mystère.index, y=df_Mystère.values, name="Mystère", hovertemplate="Genre : Mystère<br>Décennie : %{x}<br>Nombre de films : %{y}" '<extra></extra>'))
fig_barplot_evo_genres.add_trace(go.Bar(x=df_Romance.index, y=df_Romance.values, name="Romance", hovertemplate="Genre : Romance<br>Décennie : %{x}<br>Nombre de films : %{y}" '<extra></extra>'))
fig_barplot_evo_genres.add_trace(go.Bar(x=df_Thriller.index, y=df_Thriller.values, name="Thriller",hovertemplate="Genre : Thriller<br>Décennie : %{x}<br>Nombre de films : %{y}" '<extra></extra>'))

fig_barplot_evo_genres.update_layout(legend_title_text = "Genre")
fig_barplot_evo_genres.update_yaxes(title_text="Nombre de films")
fig_barplot_evo_genres.update_xaxes(categoryorder='category ascending')
fig_barplot_evo_genres.update_layout(
                               autosize=True,
                               paper_bgcolor='rgba(0,0,0,0)',
                               plot_bgcolor='rgba(0,0,0,0)',
                               font=dict(color='white'),
                               legend=dict(
                                    orientation="h",
                                    yanchor="bottom",
                                    y=1.02,
                                    xanchor="right",
                                    x=1
                                ),
                                xaxis = dict(
                                    tickmode = 'linear',
                                    tick0 = 1930,
                                    dtick = 10,
                                    title="Décennie"
                                    ),
                               )

# PARTIE ACTEURS ##########################################


# TOP 5 ACTEUR PAR DECENIE EN NOMBRE DE FILMS
def Bar_Color(i):
    if (i == 1):
        return "#E57F4D"
    elif (i == 2):
        return "#D5655F"
    elif (i == 3):
        return "#F6B931"
    elif (i == 4):
        return "#F3DB32"
    elif (i == 5):
        return "#F2F233"


fig_barplot_actors_decade = go.Figure()
fig_barplot_actors_decade.add_trace(go.Bar(x=df_top5_act["decenie"], y=df_top5_act["tconst"], text=df_top5_act["acteur"] + "<br>Nombre de films : " + df_top5_act["tconst"].astype(str),
                    hovertemplate="Decenie : %{x}" '<extra></extra>',
                    textangle=0,
                    marker_color=list(map(Bar_Color, df_top5_act['number']),
                    )))

fig_barplot_actors_decade.update_layout(xaxis_title="Décennie", yaxis_title="Nombre de films cumulés pour les 5 acteurs",
                  height=1000,
                  autosize=True,
                  paper_bgcolor='rgba(0,0,0,0)',
                  plot_bgcolor='rgba(0,0,0,0)',
                  font=dict(color='white'),
                  )

# TOP 5 ACTEURS SELON LA MOYENNE D'EVAL DES FILMS
fig_scatter_actorsAvg_decade= go.Figure(data=[go.Scatter(
    x=df_top_actors_avgRating['year'], y=round(df_top_actors_avgRating['average'],2),
    hovertemplate =
    '<b>Acteur</b> : %{text}'+
    '<br><i>Moyenne </i>: %{y}<br>'+
    '<i>Nombre de films :</i> %{marker.size}'
    '<extra></extra>',
    mode='markers',
    text = df_top_actors_avgRating['index'],
    marker=dict(size=df_top_actors_avgRating['frequency'], color=df_top_actors_avgRating['average'],showscale=True, colorbar=dict(
            title="Note moyenne"
            )
        ),
    )
])

fig_scatter_actorsAvg_decade.update_layout(
    autosize=False,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    width=1200,
    height=1000,
    font=dict(color='white'),
    margin=dict(
        l=50,
        r=50,
        b=100,
        t=100,
        pad=4
                ),
    xaxis = dict(
        tickmode = 'linear',
        tick0 = 1920,
        dtick = 10,
        title="Décennie"
                ),
    yaxis= dict(
        tickmode = 'linear',
        tick0 = 6.6,
        dtick = 0.1,
        title="Note moyenne des films",
                )
            )


# PARTIE MONEY TALKS#######################################
# BOXPLOT BUDGET
fig_boxplot_ROI_budget= go.Figure()
fig_boxplot_ROI_budget.add_trace(go.Box(x=df_movies_ROI['budget'],
                                 name="",
                                 text=df_movies_ROI['titre'],
                                 marker_color='rgba(235,157,15,1)',
                                 
                                 ))


fig_boxplot_ROI_budget.update_layout(paper_bgcolor='rgba(0,0,0,0)',
                            plot_bgcolor='rgba(0,0,0,0)',
                            xaxis_title="Budget",
                            autosize=False,
                            width=290,
                            height=150,
                            font=dict(color='white'),
                            margin = dict(l=0,r=0,b=8,t=8,pad=4)
                              )


# BOXPLOT RECETTES
fig_boxplot_ROI_recettes= go.Figure()
fig_boxplot_ROI_recettes.add_trace(go.Box(x=df_movies_ROI['recettes'],
                                 name="",
                                 text=df_movies_ROI['titre'],
                                 marker_color='rgba(235,157,15,1)'
                                 ))


fig_boxplot_ROI_recettes.update_layout(paper_bgcolor='rgba(0,0,0,0)',
                            plot_bgcolor='rgba(0,0,0,0)',
                            xaxis_title="Recettes",
                            autosize=False,
                            width=290,
                            height=150,
                            font=dict(color='white'),
                            margin = dict(l=0,r=0,b=15,t=15,pad=10)
                              )

# PARTIE MONEY TALKS - RECETTES VS BUDGET - FILM

fig_scatter_ROI= go.Figure()
fig_scatter_ROI.add_trace(go.Scatter(x=df_movies_ROI['budget'],
                                     y=df_movies_ROI['recettes'],
                                    text=df_movies_ROI['titre']
                                     ))


fig_scatter_ROI.update_traces(go.Scatter(mode='markers',
                                         marker=dict(
                                         color=df_movies_ROI['notation'],
                                         colorbar=dict(
                                                        title="Score IMDB"
                                                    ),
                                        colorscale="Solar"
                                             ),

                                        ))

fig_scatter_ROI.update_layout(paper_bgcolor='rgba(0,0,0,0)',
                            plot_bgcolor='rgba(0,0,0,0)',
                            xaxis_title="Budget",
                            yaxis_title="Recettes",
                            autosize=False,
                            width=800,
                            height=600,
                            font=dict(color='white'),
                            margin=dict(l=0, r=0, b=15, t=15, pad=10)
                              )

# PARTIE MONEY TALKS - RATIO RECETTES/ BUDGET


fig_barplot_evo_br=go.Figure()
fig_barplot_evo_br.add_trace(go.Bar(x=work_base_money_mean.index, y=work_base_money_mean['budget'], name='Budget',marker_color='rgba(235,157,15,1)', customdata=work_base_money_mean['budget']/1000000, hovertemplate="Décennie : %{x} <br>Budget : $%{customdata:,.2f}M" '<extra></extra>'))
fig_barplot_evo_br.add_trace(go.Scatter(x=work_base_money_mean.index, y=work_base_money_mean['recettes'], name='Recettes',line=dict(width=6,color='#EB9D0F'), customdata=work_base_money_mean['recettes']/1000000,hovertemplate="Décennie : %{x} <br>Recettes : $%{customdata:,.2f}M" '<extra></extra>'))

fig_barplot_evo_br.update_layout(paper_bgcolor='rgba(0,0,0,0)',
                            plot_bgcolor='rgba(0,0,0,0)',
                            xaxis = dict(
                                tickmode = 'linear',
                                tick0 = 1910,
                                dtick = 10,
                                title="Décennie"
                                        ),
                            yaxis_title="Montant en dollars",
                            autosize=True,
                            height=600,
                            font=dict(color='white'),
                            margin=dict(l=0, r=0, b=15, t=15, pad=10)
                            )"""

###############################################################################################################
#INITIALISATION DU LAYOUT
###############################################################################################################
layout = html.Div([
    dbc.Container([

        dbc.Row([
            dbc.Col(html.H2(children='Dataviz'), className="text-center", style={'margin-top':'25px'})
        ]),


        ###############################################################################################################
        #INITIALISATION DES VISUALISATIONS
        ###############################################################################################################

        #VISUALISATIONS GLOBALES#######################################################################################
        dbc.Row([
        html.H3(children='Chiffres clés',className="text-left "),
        html.P(children="Notre base de données cinématographique regroupe quelques 60 000 titres d'une grande "
                        "diversité de genres capables de plaire au plus grand nombre. Notre moteur de recommandations s'appuie"
                        "quant à lui sur environ 11 000 titres pour vous proposer les alternatives les plus pertinentes!"
               ,className="text-left text-light"),
                ]),


        ###############################################################################################################
        #INITIALISATION DES TABS
        ###############################################################################################################
        dcc.Tabs(id="tabs", value='tab_overview', children=[
            dcc.Tab(label='Généralités', value='tab_overview',style=tab_style, selected_style=tab_selected_style),
            dcc.Tab(label='Genres', value='tab_genres',style=tab_style, selected_style=tab_selected_style),
            dcc.Tab(label='Acteurs & actrices', value='tab_acteurs',style=tab_style, selected_style=tab_selected_style),
            dcc.Tab(label='Money talks', value='tab_money',style=tab_style, selected_style=tab_selected_style),

        ]),

        html.Div(id='tab_content_output'),


        ]),

    ]) #FIN DE LA DIV LAYOUT
"""
@app.callback(Output('tab_content_output', 'children'),
              Input('tabs', 'value'))
def render_content(tab):
    ###############################################################################################################
    # TAB GENERALITES
    ###############################################################################################################
    if tab == 'tab_overview':
        return html.Div([

            #INTRODUCTION###############################################################################################
            dbc.Row([
                html.H3(children='Généralités!',className="text-left",style={'margin-top':'25px'}),
                html.P(children="Découvrez en quelques indicateurs et graphs bien choisis les grandes caractéristiques  et "
                                "tendances de notre cinémathèque",className="text-left text-light")
                    ]),
            #CHIFFRES CLES##############################################################################################
            dbc.Row([
                dbc.Col(dbc.Card(
                    children=[html.P(children='61 000', className="text-center", style={'color': 'rgba(235,157,15,1)',
                                                                                        'font-size': "45px",
                                                                                        'font-weight': 'bold',
                                                                                        'margin': '0 0 0 0',
                                                                                        'padding': '0 0 0 0'}),
                              html.H4(children='films', className="text-center"),

                              ],
                    body=True, color="dark", outline=True)
                        , width=4, className="mb-4"),

                dbc.Col(dbc.Card(
                    children=[html.P(children='50 620', className="text-center", style={'color': 'rgba(235,157,15,1)',
                                                                                        'font-size': "45px",
                                                                                        'font-weight': 'bold',
                                                                                        'margin': '0 0 0 0',
                                                                                        'padding': '0 0 0 0'}),
                              html.H4(children='acteurs & actrices', className="text-center"),

                              ],
                    body=True, color="dark", outline=True)
                    , width=4, className="mb-4"),

                dbc.Col(dbc.Card(
                    children=[html.P(children='604', className="text-center", style={'color': 'rgba(235,157,15,1)',
                                                                                        'font-size': "45px",
                                                                                        'font-weight': 'bold',
                                                                                        'margin': '0 0 0 0',
                                                                                        'padding': '0 0 0 0'}),
                              html.H4(children='films non diffusés', className="text-center")

                                           ],
                                 body=True, color="dark", outline=True)
                        , width=4, className="mb-4")
            ], className="mb-5"),

            #TOP 5 MULTICRITERES#######################################################################################

            html.H3(children='TOP 5 multicritères', className="text-left", style={'margin-top': '25px'}),

            dbc.Row([

                dcc.Graph(figure=keyfacts_subplot)

           ], className="mb-5"),

            # Répartition des films par statut et tableau###############################################################
            dbc.Row([

                dbc.Col(children=[

                    html.H4(children="Répartition des films par statut", className="text-center",
                            style={'margin-bottom': '15px'}),

                    dcc.Graph(figure=movie_status),

                     ], width=5, className="mb-4"),

                dbc.Col(
                    dbc.Row([
                        html.H4(children="Overview des films non sortis", className="text-center",
                                style={'margin-bottom': '15px'}),

                        dash_table.DataTable(id='non_released_movies',
                                             data=df_not_released.to_dict('records'),
                                             columns=[{"name": i, "id": i}
                                                      for i in df_not_released.loc[:, ['titre',
                                                                                'realisateur',
                                                                                 'annee',
                                                                                 'statut']]],
                                             style_data={'background': 'rgba(235,157,15,0)',
                                                         'color': 'white'
                                                         },
                                             style_header={
                                                 'backgroundColor': 'black',
                                                 'fontWeight': 'bold',
                                                 'height': '35px'},
                                             page_size=10,
                                             fill_width=True,
                                             style_cell={'fontSize': 14, 'font-family': 'monospace','overflow':'hidden'},

                                             )

                    ])

                    , width=7, className="mb-4")
            ], className="mb-5"),

        ])
    ###############################################################################################################
    # TAB ACTEURS
    ###############################################################################################################
    elif tab == 'tab_acteurs':
        return html.Div([
            dbc.Row([
            html.H3(children='Acteurs et actrices en statistiques!',className="text-left",style={'margin-top':'25px'}),
            html.P(children="Découvrez ces quelques visualisation pour voir qui sont les principaux acteurs et actrices"
                            "de notre cinémathèque.",className="text-left text-light"),

                    ]),

            dbc.Row([
                html.H4(children="TOP 5 Acteurs/actrices par décenies", className="text-center",
                        style={'margin-top': '25px'}),
                html.P(children="Selon le nombre de films", className="text-center"),
                dcc.Graph(figure=fig_barplot_actors_decade),
                ]),

            dbc.Row([
                html.H4(children="TOP 5 Acteurs/actrices selon la notation moyenne de leur filmographie", className="text-center",
                        style={'margin-top': '25px'}),
                html.P(children="Pour les acteurs et actrices ayant plus de 10 films à leur actif", className="text-center",style={'margin-bottom':'0px'}),
                dcc.Graph(figure=fig_scatter_actorsAvg_decade),
            ]),

        ]),


    ###############################################################################################################
    # TAB GENRES
    ###############################################################################################################
    elif tab == 'tab_genres':
        return html.Div([
            dbc.Row([
            html.H3(children='Une vingtaine de genres!',className="text-left",style={'margin-top':'25px'}),
            html.P(children="Notre cinémathèque contient de films catégorisés dans une vingtaine de genres allant de la comédie"
                   "au film noir. Plusieurs genres peuvent être adossés à un même film.",className="text-left text-light"),

                    ]),

            dbc.Row([
                html.H4(children="Evolution du nombre de films par genre", className="text-center",
                        style={'margin-top': '25px'}),
                html.P(children="Pour les 9 genres principaux de notre base de données, regroupés par décennie", className="text-center"),
                dcc.Graph(figure=fig_barplot_evo_genres),

            ])

            ]),

    ###############################################################################################################
    # TAB MONEY TALKS
    ###############################################################################################################
    elif tab == 'tab_money':
        return html.Div([
            dbc.Row([
            html.H3(children='Money talks!',className="text-left",style={'margin-top':'25px'}),
            html.P(children="Parce que le cinéma est aussi une affaire de gros sous, voici quelques indicateurs confrontant "
                            "des données aux recettes cinématographiques et budgets des films. Notre cinémathèque contient environ 7 500 films "
                            "pour lesquels nous disposons de ces deux données. Les présents chiffres sont établis sur la base de "
                            "cet échantillon",className="text-left text-light"),

                    ]),

            dbc.Row([
                        dbc.Col(

                            dbc.Card(children=[html.H4(children='Indicateurs statistiques',className="text-center"),

                                dbc.Row([

                                    html.H5("Budget des films",className="text-center"),
                                    dbc.Col(children=[

                                        html.H6(children='Moyenne', className="text-center"),
                                        html.H4(children="${:,.0f}".format(df_movies_ROI['budget'].mean()), className="text-center"),

                                         ]),

                                    dbc.Col(children=[
                                        html.H6(children='Médiane',className="text-center"),
                                        html.H4(children="${:,.0f}".format(df_movies_ROI['budget'].median()),className="text-center"),

                                            ])

                                    ], style={'border-bottom':'solid 0.3px grey',
                                              "margin":"0px 5px 5px 5px"}),

                                dbc.Row([

                                    html.H5("Recettes cinématographiques",className="text-center"),
                                    dbc.Col(children=[

                                       html.H6(children='Moyenne', className="text-center"),
                                       html.H4(children="${:,.0f}".format(df_movies_ROI['recettes'].mean()), className="text-center"),

                                                    ]),

                                    dbc.Col(children=[
                                        html.H6(children='Médiane', className="text-center"),
                                        html.H4(children="${:,.0f}".format(df_movies_ROI['recettes'].median()), className="text-center"),

                                                 ])

                                    ], style={'border-bottom': 'solid 0.3px grey',
                                              "margin":"0px 5px 5px 5px"}),



                        dbc.Row([

                            dcc.Graph(figure=fig_boxplot_ROI_budget)

                                ], style={"margin":"10px 0px 10px 0px"}),

                        dbc.Row([

                               dcc.Graph(figure=fig_boxplot_ROI_recettes)

                           ], style={"margin":"10px 0px 10px 0px"}),

                        dbc.Badge("Lecture",id='boxplot_tt', color="warning", className="ms-1"),
                        dbc.Tooltip(
                                    "Lecture: "
                                    "La plupart des valeurs dans les boxplots sont concentrées entre 5M$ et 35M$ pour les budgets,"
                                    "et entre 5M$ et 85M$ pour les recettes. On note la présence de nombeux outliers des deux côtés"
                                    "avec des super productions à très haut budget et des gros scores au box office. ",
                                    target="boxplot_tt",)

                                ], body=True, color="dark", outline=True)
                                        , width=4, className="mb-4"),


                        dbc.Col(
                                dbc.Row([
                                    html.H4(children="Recettes cinématographiques versus budgets engagés",className="text-center",
                                            style={'margin-top':'15px'}),
                                    dcc.Graph(figure=fig_scatter_ROI)

                                ])

                            ,width=8, className="mb-4")
                    ],className="mb-5"),

            dbc.Row([
                html.H4(children="Evolution de la moyenne des recettes et budgets par décennie", className="text-center",
                        style={'margin-top': '25px'}),
                dcc.Graph(figure=fig_barplot_evo_br),

            ])

            ]),

"""
# needed only if running this as a single page app
# if __name__ == '__main__':
#     app.run_server(host='127.0.0.1', debug=True)