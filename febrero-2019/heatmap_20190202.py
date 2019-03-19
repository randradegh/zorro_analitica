###
# Variable: Todas 
# Periodo: Febrero de 2019
# Proyecto Zorro Abarrotero
# Graph: Barras
# Roberto Andrade Fonseca (c)
# Inicio: jue mar 14 13:23:59 CST 2019
# Para: Avignon
###
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as ff
import plotly.offline as offline
import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# read in data from csv file
df = pd.read_csv('data_febrero_2019.csv',index_col=2)
df = df.sort_values(by=['Tienda'])
#df = df.loc[df['Cadena'] == 'Scorpion']
#df = df.loc[df['Cadena'] == 'Zorro Abarrotero']

df = df.loc[:, ['Cadena','Trato amable','Rapidez','Atención en cajas','Ofertas y precios','Surtido y existencias','Orden y Limpieza','Seguridad Industrial']].reindex()
df = df.reindex()
df = df.T.iloc[::-1] 		# transform and reverse rows (to get caps in right order for heat map)
df = df.T 							# and then transform it back again.
#df 
app = dash.Dash(__name__)
server = app.server
app.config.supress_callback_exceptions = True

# Change the title of the page from the default "Dash"
app.title = "Application heatmap"

# Using external css from chriddyp from plotly for ease
app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

left_margin = 200
right_margin = 100

colors = {
    'background': 'white',
    'text': 'gray'
}

app.layout = html.Div([

    html.H1('Zorro Abarrotero'),
    html.H2('Mapa de Calor de Dimensiones'),
    dcc.RadioItems(
        id='cadena',
        options=[{'label': i, 'value': i} for i in ['Zorro Abarrotero', 'Scorpion','Punto de Venta', 'DZ']],
        value='Zorro Abarrotero',
        labelStyle={'display': 'inline-block'}
     ),
    html.Div(id='display-cadena'),
    dcc.Graph(id='heatmap_output')
    ], style = {'textAlign':'center','backgroundColor': colors['background'], 'color': colors['text']}
    )

id ='isv_select'

@app.callback(
        Output('display-cadena', 'children'),
        [Input('cadena', 'value')])
def set_cadena_valor(value):
    return 'La cadena mostrada es {}'.format(value)

@app.callback(
    Output('heatmap_output', 'figure'),
    [Input('cadena', 'value')])

def update_figure(cadena):
    dff = df.loc[df['Cadena'] == cadena]
    dff = dff.loc[:, ['Trato amable','Rapidez','Atención en cajas','Ofertas y precios','Surtido y existencias','Orden y Limpieza','Seguridad Industrial']].reindex()
    return {
        'data': [{
            'z': dff.values.T.tolist(),
            'y': dff.columns.tolist(),
            'x': dff.index.tolist(),
            'ygap': 1,
            'reversescale': 'true',
            'colorscale': [[0, '#FCF3CF'], [1, 'green']],
            'type': 'heatmap',
            'text':'Hola mundo',
        }],
        'layout': {
            'plot_bgcolor': colors['background'],
            'paper_bgcolor': colors['background'],
            'font': { 'color': colors['text'] },
            'height': 1000,
            'width': 1500,
            'xaxis': {'side':'top'},
            'margin': {
             	'l': left_margin,
               	'r': right_margin,
               	'b': 150,
               	't': 200
               }
           }
        }

if __name__ == '__main__':
    app.run_server(debug=True)
