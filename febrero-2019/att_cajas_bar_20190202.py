###
# Variable: Atención en cajas
# Periodo: Febrero de 2019
# Proyecto Zorro Abarrotero
# Graph: Barras
# Roberto Andrade Fonseca (c)
# Inicio: jue mar 14 11:04:46 CST 2019
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

data_set = data[['Municipio', 'Cadena', 'Tienda', 'Atención en cajas']]
data_set = data_set.sort_values(by=['Atención en cajas'], ascending=False)
data_set = data_set.reset_index(drop=True)

# Armamos los promedios por cadena y municipio.
data_scorpion=data_set.loc[data_set['Cadena'] == 'Scorpion']
mean_scorpion=data_scorpion.groupby(['Municipio'], as_index=False)['Atención en cajas'].mean()
municipios_scorpion = mean_scorpion['Municipio']
att_scorpion= mean_scorpion['Atención en cajas']

data_zorro=data_set.loc[data_set['Cadena'] == 'Zorro Abarrotero']
mean_zorro=data_zorro.groupby(['Municipio'], as_index=False)['Atención en cajas'].mean()
municipios_zorro = mean_zorro['Municipio']
att_zorro= mean_zorro['Atención en cajas']

data_punto=data_set.loc[data_set['Cadena'] == 'Punto de Venta']
mean_punto=data_punto.groupby(['Municipio'], as_index=False)['Atención en cajas'].mean()
municipios_punto = mean_punto['Municipio']
att_punto= mean_punto['Atención en cajas']

data_dz=data_set.loc[data_set['Cadena'] == 'DZ']
mean_dz=data_dz.groupby(['Municipio'], as_index=False)['Atención en cajas'].mean()
municipios_dz = mean_dz['Municipio']
att_dz= mean_dz['Atención en cajas']

colors = {
    'background': 'black',
    'text': '#a3a3c2'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H3(
        children='Atención en Cajas por Cadena',
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
       {'x': municipios_scorpion,'y': att_scorpion, 'type': 'bar', 'name': 'Scorpion','marker':{'color':'blue'}},
       {'x': municipios_zorro,'y': att_zorro, 'type': 'bar', 'name': 'Zorro Abarrotero','marker':{'color':'red'}},
       {'x': municipios_punto,'y': att_punto, 'type': 'bar', 'name': 'Punto de Venta','marker':{'color':'brown'}},
       {'x': municipios_dz,'y': att_dz, 'type': 'bar', 'name': 'DZ','marker':{'color':'green'}},
            ],
            'layout': {
                'title': 'Promedio de Atención en Cajas por Cadena y Municipio.',
                 'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': { 'color': colors['text'] }
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
