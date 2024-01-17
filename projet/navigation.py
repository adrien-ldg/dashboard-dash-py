import dash_bootstrap_components as dbc

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="/")),
        dbc.NavItem(dbc.NavLink("Graphiques", href="/graph")),
        dbc.NavItem(dbc.NavLink("Map", href="/map")),
        dbc.NavItem(dbc.NavLink("Conclusion", href="/ccl"))
    ],
    brand="Projet: Evolution de la répartion des différents types d'énergie chez les pays de l'UE:",
    brand_href="/",
    color="#379E54",
    dark=True,
    fluid=True,
    links_left=True,
    sticky='Top'
)