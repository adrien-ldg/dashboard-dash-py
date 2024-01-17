import dash
from dash import html
import navigation

txt = """
La qualité et la quantité des données disponibles dans notre jeu de données nous permettent de poser une problématique pertinente : Y a-t-il une tendance énergétique dans les pays d'Europe au cours des 20 dernières années ? Celle-ci a-t-elle une quelconque corrélation avec le nombre d'habitants de ces pays, ainsi que leur PIB ou encore leurs émissions de CO2 ?
\n\n
Nous avons réalisé plusieurs graphiques dans notre tableau de bord (dashboard) qui nous permettent d'établir des conclusions pour répondre à cette problématique.
\n\n
Notre bar chart nous permet de visualiser, pour une année précise entre 2000 et 2020, la quantité des données que l'on définit en ordonnée pour tous les pays d'Europe. Par exemple, on remarque que, au cours des 20 dernières années, les seuls vrais producteurs d'énergie fossile sont l'Allemagne, l'Espagne, l'Italie et la Pologne. En ce qui concerne le nucléaire, seul la France en produit énormément, avec l'Allemagne loin derrière, et donc la production a nettement baissé au cours des dernières années. Pour ce qui est des énergies renouvelables, de nombreux pays se démarquent, mais on remarque une forte hausse dans toute l'Europe de la production de cette nouvelle forme d'énergie.
\n\n
Sur un autre onglet, notre scatter plot nous permet d'observer plus clairement la formation de tendances au fil du temps. En effet, on remarque que les émissions de CO2 en Europe sont en quasi-constante baisse depuis 2005. On observe également que c'est à partir de cette époque que le PIB par habitant a commencé à croître de manière significative (malgré une croissance du PIB relativement stable) et que l'intensité énergétique a commencé à baisser.
\n\n
Par ailleurs, sur notre onglet intitulé 'Courbe de tendance', on peut réaliser des observations en examinant spécifiquement la corrélation entre deux variables. Ce graphique nous permet, entre autres, de voir l'importance du PIB par habitant dans l'optique d'une potentielle transition énergétique, car bien que plus responsable pour la planète, les nouvelles technologies et sources d'énergie sont bien plus coûteuses que les sources plus traditionnelles.
\n\n
Notre jeu de données met donc en avant ici que la situation économique globale des habitants d'Europe s'améliorant au cours des deux dernières décennies tandis que les énergies renouvelables commencent à se populariser aussi de plus en plus tandis que le nucléaire et les énergies fossiles continuent lentement mais sûrement à être mises de côté.
"""

dash.register_page(__name__,path="/ccl", title="Conclusion")

layout = html.Div(children=[
    navigation.navbar,
    html.Br(),
    html.H2(children=html.Span("Conclusion:", style={'font-weight': 'bold', 'text-decoration': 'underline'}),),

    html.Br(),
    html.Br(),

    html.Div(children=[
        html.P(children=txt),

    ],
    style={'text-align': 'center', 'display':'inline-block', 'width': '85%'}
    )
],
style={'text-align': 'center', 'display':'inline-block', 'width': '100%'}
)