import dash
from dash import html
from dash.dash_table import DataTable
from dataset.data import df
import navigation


columns = [{'name': x, 'id': x} for x in df.columns]

table = DataTable(
    columns=columns, 
    data = df.to_dict('records'),
    cell_selectable=True,
    sort_action='native',
    filter_action='native',
    page_action='native',
    page_current=0,
    page_size=10,
    style_table={'overflowX': 'auto'} 
)

dash.register_page(__name__,path="/", title="Home")

layout = html.Div(children=[
    navigation.navbar,
    html.Br(),
    html.H2(children = html.Span("Accueil:", style={'font-weight': 'bold', 'text-decoration': 'underline'}),),
    html.Br(),
    html.Div([
            html.Img(src="https://fr.cdn.v5.futura-sciences.com/buildsv6/images/wide1920/2/e/1/2e13386c85_100685_01-intro-642.jpg",
                    width=800, height=400),
            html.Br(),
        ], style={'text-align': 'center'}),

    html.Div([
        html.Br(),
        html.P("À l'aide de ce jeu de données, notre objectif est d'analyser et de visualiser comment la production d'énergie est répartie au sein des pays de l'Union Européenne sur une période allant de l'année 2000 à 2019. Nous souhaitons comprendre comment cette répartition de la production d'énergie a évolué au fil du temps et quel impact elle a eu sur les économies des pays membres de l'Union Européenne, ainsi que sur la densité de leur population. En examinant les tendances de production d'énergie au sein de l'UE, nous cherchons à identifier des corrélations potentielles entre la production d'énergie, la croissance économique et la densité de la population, et à mieux comprendre les défis liés à l'utilisation de l'énergie au sein de cette région géographique clé.")
    ],
    style={'text-align': 'center', 'display':'inline-block', 'width': '85%'}),
    html.Br(),
    html.H3(children = "Dataset montrant la répartition de l'énergie dans chaque pays de l'union européenne depuis les années 200:"),
    html.Div(children = [table], style={'width':'850px', 'height': '750px', 'margin': '0 auto'}),
    html.Br()
],
style={'text-align': 'center', 'display':'inline-block', 'width': '100%'}
)