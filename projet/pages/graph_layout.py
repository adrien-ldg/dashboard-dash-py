import plotly_express as px
import pandas as pd
import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from dataset.data import df
import navigation
from plotly.subplots import make_subplots



country = df.Pays.unique()
dict_country = [{'label': x, 'value': x} for x in country]

var_dist = [{'label': x, 'value': x} for x in df.columns[6:]]

var_barplot = [{'label': x, 'value': x} for x in df.columns[3:]]

var_scat = [{'label': x, 'value': x} for x in df.columns[6:]]


var_X = [{'label': x, 'value': x} for x in df.columns[6:15]]


var_Y = [{'label': x, 'value': x} for x in df.columns[15:]]



dash.register_page(__name__,path="/graph", title="Graphiques")

layout = html.Div(children=[
    navigation.navbar,
    html.Br(),
    html.H2(children=html.Span("Graphiques:", style={'font-weight': 'bold', 'text-decoration': 'underline'}),),
    html.Br(),
    html.Div(
        dbc.Select(
                    id='input_dist',
                    options=var_dist,
                    value=var_dist[1]["value"]
                ),
            style={'width': '90%', 'margin-left': '5%'} 
    ),

    dcc.Graph(id="output_dist",
              style={'text-align': 'center', 'display':'inline-block', 'width': '100%'}),

    html.Br(),
    html.Br(),
    html.Br(),

    html.Div([
        html.Div(
        dbc.Select(
                id='input_bar',
                options=var_barplot,
                value=var_barplot[1]["value"]
            ),
        style={'width': '30%'} 
        ),

        html.Div(
            dcc.Slider(
                id='input_bar_an',
                min=2000,
                max=2019,
                value=2000,
                step=1,
                marks={i: str(i) for i in range(2000, 2020)},
            ),
            style={'width': '50%'} 
        )], 
        style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center', 'gap': '75px'}
    ),

    html.Br(),

    dcc.Graph(id="output_bar",
        style={'text-align': 'center', 'display':'inline-block', 'width': '100%'}),

    html.Br(),
    html.Br(),
    html.Br(),

    html.Div([
        html.Div(
        dbc.Select(
                id='input_scat',
                options=var_scat,
                value=var_scat[1]["value"]
            ),
        style={'width': '40%'} 
        ),

        html.Div(
            dbc.Select(
                id='input_scat_pays',
                options=dict_country,
                value=dict_country[1]["value"]
            ),
            style={'width': '40%'} 
        )], 
        style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center', 'gap': '75px'}
    ),

    html.Br(),

    dcc.Graph(id="output_scat",
        style={'text-align': 'center', 'display':'inline-block', 'width': '100%'}),

    html.Br(),
    html.Br(),
    html.Br(),


    html.Div([
        html.Div(
        dbc.Select(
                id='input_X',
                options=var_X,
                value=var_X[1]["value"]
            ),
        style={'width': '40%'} 
        ),

        html.Div(
            dbc.Select(
                id='input_Y',
                options=var_Y,
                value=var_Y[1]["value"]
            ),
            style={'width': '40%'} 
        )], 
        style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center', 'gap': '75px'}
    ),

    html.Br(),

    html.Div([ 
        dcc.RadioItems(
            id='radio-items',
            options=[
                {'label': 'lowess', 'value': 'lowess'},
                {'label': 'ols', 'value': 'ols'}
            ],
            value='ols' 
        ),
    ], style={'display': 'flex','justify-content': 'center', 'flex-direction': 'row'}),  
    

    html.Br(),

    dcc.Graph(id="output_tendance",
        style={'text-align': 'center', 'display':'inline-block', 'width': '100%'}),

    html.Br(),
    html.Br(),
    html.Br(),

    html.Div([
        html.Div(
        dbc.Select(
                id='input_pie_pays',
                options=dict_country,
                value=dict_country[0]["value"]
            ),
        style={'width': '30%'} 
        ),

        html.Div(
            dcc.Slider(
                id='input_pie_an',
                min=2000,
                max=2019,
                value=2000,
                step=1,
                marks={i: str(i) for i in range(2000, 2020)},
            ),
            style={'width': '50%'} 
        )], 
        style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center', 'gap': '75px'}
    ),

    html.Br(),

    dcc.Graph(id="output_pie",
        style={'text-align': 'center', 'display':'inline-block', 'width': '100%'}),
    
    ],
    style={'text-align': 'center', 'display':'inline-block', 'width': '100%'}
    )


@dash.callback(
    Output('output_dist', 'figure'),
    Input('input_dist', 'value')
)
def update_dist_callback(variable):

    
    fig1 = px.histogram(df, x=variable)
    fig2 = px.box(df, x=variable, boxmode='overlay')

    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.1)

    fig.add_trace(fig2['data'][0], row=1, col=1)
    fig.add_trace(fig1['data'][0], row=2, col=1)

    fig.update_yaxes(title_text="Frequency", row=1, col=1)
    fig.update_xaxes(title_text=variable, row=2, col=1)

    fig.update_layout(
        title_text=f"Histogramme et Boxplot de la colonne: {variable}",
        title_x=0.5,
        showlegend=False,
        paper_bgcolor='white',  # Fond de page blanc
        plot_bgcolor='white'    # Fond du graphique blanc
    )

    return fig


@dash.callback(
    Output('output_bar', 'figure'),
    [Input('input_bar', 'value'),
    Input('input_bar_an', 'value')]
)
def update_bar_callback(input_v, selected_year):

    df_an = df[df["Annee"] == selected_year]

    fig = px.bar(df_an, x='Pays', y=input_v)
    fig.update_traces(marker_color="#0487B5")
    fig.update_layout(
    title = f"Barplot représentant pour chaque pays de l'Union Européenne en {selected_year}: {input_v}",
    xaxis_title="Pays", yaxis_title=input_v,
    title_x=0.5  
    )

   
    return fig


@dash.callback(
    Output('output_scat', 'figure'),
    [Input('input_scat', 'value'),
    Input('input_scat_pays', 'value')]
)
def update_scat_callback(input_var, selected_country):

    df_pays = df[df["Pays"] == selected_country]
    
    
    fig = px.line(df_pays, x='Annee', y=input_var, markers=True, line_shape='linear')

    # Personnalisez le line plot selon vos besoins
    fig.update_traces(line=dict(color="#0487B5", width=2), marker=dict(size=8))  # Personnalisation des lignes et des marqueurs
    fig.update_layout(
    title = f"Graphique pour {input_var} en {selected_country}:",
    xaxis_title="Année",
    yaxis_title=input_var,
    title_x=0.5
    )

    return fig


@dash.callback(
    Output('output_tendance', 'figure'),
    [Input('input_X', 'value'),
    Input('input_Y', 'value'),
    Input('radio-items', 'value')]
)
def update_tendance_callback(input_X, input_Y, strat):

    # Remplacez 'df' par le nom de votre DataFrame
    fig = px.scatter(df, x=input_X, y=input_Y,
                    labels={"x": input_X, "y": input_Y})

    # Ajoutez une ligne de tendance
    fig.add_trace(px.scatter(df, x=input_X, y=input_Y, trendline=strat).data[1])

    # Personnalisez la couleur de la ligne de tendance
    fig.data[1].line.color = 'red'  # Définissez la couleur de la ligne de tendance

    # Personnalisez le titre du graphique
    fig.update_layout(title=f"Graphique représentant {input_X} en fonction {input_Y} pour tous de l'Union  Européenne:", title_x=0.5)

    return fig


@dash.callback(
    Output('output_pie', 'figure'),
    [Input('input_pie_pays', 'value'),
    Input('input_pie_an', 'value')]
)
def update_pie_callback(selected_pays, selected_an):
    data = df[(df['Pays'] == selected_pays) & (df['Annee'] == selected_an)]

    if data.empty:
        # Gérez le cas où aucune donnée n'est trouvée pour les valeurs sélectionnées
        return {}

    # Créez un DataFrame pour le Pie Chart
    pie_data = pd.DataFrame({'Catégorie': ["Part energie renouvelable(%)", "Part energie fossile(%)", "Part autres energies(%)"],
                            'Valeurs': [data["Part energie renouvelable(%)"].values[0], 
                                        data["Part energie fossile(%)"].values[0], 
                                        data["Part autres energies(%)"].values[0]]})

    # Définissez des couleurs spécifiques pour chaque catégorie
    colors = ['#00FF00', '#FF0000', '#0000FF']

    # Tracez le Pie Chart avec des couleurs spécifiques
    fig = px.pie(pie_data, names='Catégorie', values='Valeurs', 
                 title=f"Répartition des différents types d'énergie en {selected_pays} en {selected_an}",
                 color='Catégorie',
                 color_discrete_map={'Part energie renouvelable(%)': colors[0],
                                     'Part energie fossile(%)': colors[1],
                                     'Part autres energies(%)': colors[2]})

    fig.update_layout(
        title_x=0.5
    )

    return fig
