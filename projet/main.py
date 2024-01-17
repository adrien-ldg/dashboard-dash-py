from file import libr_file
from import_py import pip

#installation des librairies manquantes
pip(libr_file("requirements.txt"))


import dash
import dash_bootstrap_components as dbc
from dash import html


app = dash.Dash(__name__,use_pages=True,external_stylesheets=[dbc.themes.YETI])
server = app.server

app.layout = html.Div(children=[
    dash.page_container
])


if __name__ == '__main__':
    app.run_server(port=4050)




