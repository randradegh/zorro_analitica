###
# Variable: Ofertas y precios
# Periodo: Febrero 2019
# Proyecto Zorro Abarrotero
# Graph: Barras
# Roberto Andrade Fonseca (c)
# Inicio: mar feb 12 14:33:38 CST 2019
# Para: Avignon
###

# -*- coding: utf-8 -*-
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
data = pd.read_csv("data_febrero_2019.csv")

data_set = data[['Municipio', 'Cadena', 'Tienda', 'Ofertas y precios']]
data_set = data_set.sort_values(by=['Ofertas y precios'], ascending=False)
data_set = data_set.reset_index(drop=True)

# Armamos los promedios por cadena y municipio.
data_scorpion=data_set.loc[data_set['Cadena'] == 'Scorpion']
mean_scorpion=data_scorpion.groupby(['Municipio'], as_index=False)['Ofertas y precios'].mean()
municipios_scorpion = mean_scorpion['Municipio']
data_scorpion= mean_scorpion['Ofertas y precios']

data_zorro=data_set.loc[data_set['Cadena'] == 'Zorro Abarrotero']
mean_zorro=data_zorro.groupby(['Municipio'], as_index=False)['Ofertas y precios'].mean()
municipios_zorro = mean_zorro['Municipio']
data_zorro= mean_zorro['Ofertas y precios']

data_punto=data_set.loc[data_set['Cadena'] == 'Punto de Venta']
mean_punto=data_punto.groupby(['Municipio'], as_index=False)['Ofertas y precios'].mean()
municipios_punto = mean_punto['Municipio']
att_punto= mean_punto['Ofertas y precios']

data_dz=data_set.loc[data_set['Cadena'] == 'DZ']
mean_dz=data_dz.groupby(['Municipio'], as_index=False)['Ofertas y precios'].mean()
municipios_dz = mean_dz['Municipio']
att_dz= mean_dz['Ofertas y precios']

colors = {
    'background': 'black',
    'text': '#a3a3c2'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H3(
        children='Ofertas y Precios por Cadena',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    html.H4(
        children='Febrero 2019',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    dcc.Graph(
        id='example-graph',
        figure={
   'data': [
       {'x': municipios_scorpion,'y': data_scorpion, 'type': 'bar', 'name': 'Scorpion','marker':{'color':'blue'}},
       {'x': municipios_zorro,'y': data_zorro, 'type': 'bar', 'name': 'Zorro Abarrotero','marker':{'color':'red'}},
       {'x': municipios_punto,'y': att_punto, 'type': 'bar', 'name': 'Punto de Venta','marker':{'color':'brown'}},
       {'x': municipios_dz,'y': att_dz, 'type': 'bar', 'name': 'DZ','marker':{'color':'green'}},
            ],
            'layout': {
                'title': 'Promedio de Ofertas y Precios por Cadena y Municipio',
                 'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': { 'color': colors['text'] }
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
