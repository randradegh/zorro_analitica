###
# Variable: Atención en cajas
# Periodo: Febrero de 2019
# Proyecto Zorro Abarrotero
# Graph: Sectores
# Roberto Andrade Fonseca (c)
# Inicio: lun mar 11 12:42:01 CST 2019 
# Para: Avignon
###
# -*- coding: utf-8 -*-
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
data = pd.read_csv("data_febrero_2019.csv")

data_set = data[['Cadena', 'Tienda', 'Atención en cajas']]
data_set = data_set.sort_values(by=['Atención en cajas'], ascending=False)
data_set = data_set.reset_index(drop=True)

atencion_cajas=pd.Series(data_set['Atención en cajas'])
tiendas=pd.Series(data_set['Tienda'])
cadenas=pd.Series(data_set['Cadena']).sort_values()
promedios = data_set.groupby(['Cadena'])['Atención en cajas'].mean()
#print(promedios)

values = [
        data[data['Cadena'] == 'DZ']['Atención en cajas'].mean(), 
        data[data['Cadena'] == 'Punto de Venta']['Atención en cajas'].mean(), 
        data[data['Cadena'] == 'Scorpion']['Atención en cajas'].mean(), 
        data[data['Cadena'] == 'Zorro Abarrotero']['Atención en cajas'].mean()
        ]

print('Scorpion: ')
print(data[data['Cadena'] == 'Scorpion']['Atención en cajas'].mean())
print('Zorro: ')
print(data[data['Cadena'] == 'Zorro Abarrotero']['Atención en cajas'].mean())

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
        }),
    html.H4(
        children='Febrero 2019',
        style={
            'textAlign': 'center',
            'color': colors['text']
    }),

    dcc.Graph(
        id='example-graph-2',
        figure={
            'data': [
                {
                'labels': pd.Series(data_set['Cadena'].sort_values().unique()), 
                'values': values,
                'marker': {'colors':['green','brown','blue', 'red']},
                'hole': 0.6,
                'type':'pie'},
            ],
            'layout': {
                'title': 'Calificación promedio de la atención en cajas.',
                 'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': { 'color': colors['text'] }
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)


