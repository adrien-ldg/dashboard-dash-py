import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from dataset.data import df
import navigation


var = [{'label': x, 'value': x} for x in [  "Population",
                                                "Densite(P/Km2)",
                                                "Superficie(Km2)",
                                                "Electricite d'origine fossile(TWh)",
                                                "Electricite d'origine nucleaire(TWh)",
                                                "Electricite d'origine renouvelable(TWh)",
                                                "Electricite d'origine fossile / hab(KWh/pers)",
                                                "Electricite d'origine nucleaire / hab(KWh/pers)",
                                                "Electricite d'origine renouvelable / hab(KWh/pers)",
                                                "Part energie renouvelable(%)",
                                                "Part energie fossile(%)",
                                                "Part autres energies(%)",
                                                "Intensite energetique(MJ/$2017 PIB PPA)",
                                                "Emissions CO2(kt)",
                                                "Croissance PIB(%)",
                                                "PIB/habitant($)"
                                            ]
]



dash.register_page(__name__,path="/map", title="Carte chloroplète")

layout = html.Div([
    navigation.navbar,
    html.Br(),
    html.H2(children=html.Span("Carte de l'Europe:", style={'font-weight': 'bold', 'text-decoration': 'underline'}),
            style={'text-align': 'center', 'display':'inline-block', 'width': '100%'}),
    
    html.Br(),
    html.Br(),
    html.Br(),

    html.Div([
        html.Div(
        dbc.Select(
                id='input_map',
                options=var,
                value=var[0]["value"]
            ),
        style={'width': '30%'} 
        ),

        html.Div(
            dcc.Slider(
                id='input_map_an',
                min=2000,
                max=2019,
                value=2000,
                step=1,
                marks={i: str(i) for i in range(2000, 2020)},
            ),
            style={'width': '50%'} 
        )
        ], style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center', 'gap': '75px'}
    ),

    html.Br(),
    html.Br(),
    html.Br(),

    html.H5(id="title_max_min", 
            style={'text-align': 'center', 'display':'inline-block', 'width': '100%'}),

    html.Br(),
    html.Br(),
    
    html.Div([ 
        html.Div(id='top5-list'),

        html.Div(id='low5-list'),
        ], style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center', 'gap': '300px'}
    ),
    

    html.Br(),
    html.Br(),
    html.Br(),


    dcc.Graph(id="output_map",
              style={'text-align': 'center', 'display':'inline-block', 'width': '100%'})

])

@dash.callback(
    [Output('output_map', 'figure'),
    Output('top5-list', 'children'),
    Output('low5-list', 'children'),
    Output('title_max_min', 'children')],
    [Input('input_map', 'value'),
    Input('input_map_an', 'value')]
)
def update_map_callback(selected_variable, selected_year):

    df_an = df[df["Annee"] == selected_year]

    # Les limites géographiques pour l'Europe
    europe_lon = [-25, 45]  # Longitude de l'ouest à l'est
    europe_lat = [30, 80]   # Latitude du sud au nord

    fig = go.Figure(data=go.Choropleth(
        locations=df_an['Code'],
        z=df_an[selected_variable],
        text=df_an['Pays'],
        colorscale=["#79B2D8", "#226C9C"],
        autocolorscale=False,
        marker_line_color='darkgray',
        marker_line_width=0.5,
    ))

    fig.update_geos(
        lonaxis_range=europe_lon,  # Limite de longitude
        lataxis_range=europe_lat   # Limite de latitude
    )

    fig.update_layout(
        title=dict(
        text=f"Carte chloroplète de l'Union Européenne représentant en {selected_year} la répartition de : {selected_variable}",
        x=0.5  # Centrer le titre horizontalement
    ),
        geo=dict(
            lonaxis_range=europe_lon,  # Limite de longitude
            lataxis_range=europe_lat,  # Limite de latitude
            showframe=False,
            showcoastlines=False,
            projection_type='equirectangular'
        ),
        width=1200,  # Largeur souhaitée en pixels
        height=700   # Hauteur souhaitée en pixels
    )

    
    top5_df = df_an.sort_values(by=selected_variable, ascending=False).head(5)
    top5_df['Classement'] = range(1, 6)
    top5_list = html.Ul([html.Li(f"{row['Classement']}. {row['Pays']} - {row[selected_variable]}") for _, row in top5_df.iterrows()])


    low5_df = df_an.sort_values(by=selected_variable).head(5)
    low5_df['Classement'] = range(27, 22 , -1)
    low5_list = html.Ul([html.Li(f"{row['Classement']}. {row['Pays']} - {row[selected_variable]}") for _, row in low5_df.iterrows()])

    title = html.Span(f"Top/Low 5 des pays en {selected_year} pour: {selected_variable} ", style={'font-weight': 'bold', 'text-decoration': 'underline'})
    return fig, top5_list, low5_list, title

