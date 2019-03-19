###
# Variable: Trato amable
# Periodo: Enero 2019
# Proyecto Zorro Abarrotero
# Graph: Barras
# Roberto Andrade Fonseca (c)
# Inicio: mar feb 12 17:25:05 CST 2019
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
data = pd.read_csv("data_enero_2019.csv")

data_set = data[['Municipio', 'Cadena', 'Tienda', 'Trato amable']]
data_set = data_set.sort_values(by=['Trato amable'], ascending=False)
data_set = data_set.reset_index(drop=True)

# Armamos los promedios por cadena y municipio.
data_scorpion=data_set.loc[data_set['Cadena'] == 'Scorpion']
mean_scorpion=data_scorpion.groupby(['Municipio'], as_index=False)['Trato amable'].mean()
municipios_scorpion = mean_scorpion['Municipio']
data_scorpion= mean_scorpion['Trato amable']

data_zorro=data_set.loc[data_set['Cadena'] == 'Zorro Abarrotero']
mean_zorro=data_zorro.groupby(['Municipio'], as_index=False)['Trato amable'].mean()
municipios_zorro = mean_zorro['Municipio']
data_zorro= mean_zorro['Trato amable']

##data_zorro=data_set.loc[data_set['Cadena'] == 'Zorro Abarrotero']
colors = {
    'background': 'black',
    'text': '#a3a3c2'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H3(
        children='Trato Amable por Cadena',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    html.H3(
        children='Enero 2019',
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
            ],
            'layout': {
                'title': 'Promedio de Trato Amable por Cadena y Municipio',
                 'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': { 'color': colors['text'] }
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
