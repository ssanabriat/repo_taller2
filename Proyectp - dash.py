import numpy as np
import tqdm as tqdm
import pandas as pd
import scipy as scipy
import joblib as joblib
#import pyparsing as pyparsing
import statsmodels as statsmodels

from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy . estimators import BayesianEstimator
from pgmpy . sampling import BayesianModelSampling
from pgmpy . estimators import MaximumLikelihoodEstimator

import dash
from dash import dcc  # dash core components
from dash import html # dash html components
import plotly.express as px
from dash.dependencies import Input, Output
import base64
from PIL import Image
#from Modelo_Proyecto_1 import prob_desercion

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

image_path = "C:/Users/lj.sanchezd/OneDrive - Universidad de los andes/Maestría/2023 - 20/Analítica Computacional/saturno.jpg"

#Using Pillow to read the the image
pil_img = Image.open(image_path)

# Using base64 encoding and decoding
def b64_image(image_filename):
    with open(image_filename, 'rb') as f:
        image = f.read()
    return 'data:image/jpg;base64,' + base64.b64encode(image).decode('utf-8')

app.layout = html.Div(children=[
    html.Img(src=b64_image(image_path), style={'display':'inline-block', 'height':'10%', 'width':'10%'}),
    html.H1(children='Saturno', style={'marginLeft':400, 'display':'inline-block', 'color': 'orange', 'font-family': 'cursive', 'font-weight': '550'}),

    html.Div(html.P(['Saturno es un aplicativo que le permite al orientador visualizar el desempeño del estudiante.','Esta herramienta le ayudará a tomar mejores decisiones en el proceso de acompañamiento a sus estudiantes.']),
             
             style={'font-family': 'sans-serif', 'font-size': 18, 'text-align': 'justify'})
             ,
    
    html.Br(),
     html.Div(children='''
        A continuación complete la información del estudiante para conocer sus posibilidades.
    ''', 
    style={'font-family': 'sans-serif', 'font-size': 18, 'font-weight': 'bold'}
    ),

    html.Div(["Edad del estudiante: ",
              dcc.Input(id='edad', value='0', type='number')], style={'display':'table-cell','padding':5, 'verticalAlign':'middle'}),
    html.Br(),
    #html.Div(id='edad-output'),

    #LISTA DESPLEGABLE 0,1,2,3 --> FOTO WHATSAPP
    html.Div(["Edad a la que ingresó a la universidad: ",
              dcc.RadioItems(options=[
       {'label': 'Menos de 25 años', 'value': 0},
       {'label': 'Entre 25 y 30 años', 'value': 1},
       {'label': 'Entre 30 y 35', 'value': 2},
       {'label': 'Más de 35', 'value': 3} ])
   ],),
              #dcc.Input(id='edad_ingreso', value='0', type='number')]),
    html.Br(),

    html.Div(["Nota en la prueba de admisión: ",
              dcc.Input(id='prueba', value='Malo', type='text')]),
    html.Br(),

    html.Div(["Costo actual de la matrícula: ",
              dcc.Input(id='tuition_fees', value='0', type='number')]),
    html.Br(),

    html.Div(["Es deudor: ",
              dcc.Input(id='debtor', value='0', type='number')]),
    html.Br(),

    html.Div(["El estudiante es becado: ",
              dcc.Input(id='scholarship', value='0', type='number')]),
    html.Br(),

    html.Div(["Semestre que cursa: ",
              dcc.Input(id='semestre', value='0', type='number')]),
    html.Br(),

    html.Div(["Promedio académico de primer semestre: ",
              dcc.Input(id='sem1_gpa', value='0', type='number')]),
    html.Br(),

    html.Div(["El estudiante aprobó más del 50% de las materias de primer semestre: ",
              dcc.Input(id='sem1_aprobado', value='0', type='number')]),
    html.Br(),

    html.Div(["Promedio académico de segundo semestre: ",
              dcc.Input(id='sem2_gpa', value='0', type='number')]),
    html.Br(),

    html.Div(["El estudiante aprobó más del 50% de las materias de segundo semestre: ",
              dcc.Input(id='sem2_aprobado', value='0', type='number')]),
    html.Br(),

    ],
   
    style={'marginLeft': 50, 'marginRight': 50, 'marginTop': 25}

)

#datos = prob_desercion(prueba.value, debtor, tuition_fees, scholarship, edad_ingreso, sem1_aprobado, sem2_aprobado, sem1_gpa, sem2_gpa)
#print(datos)

#@app.callback(
#    Output(component_id='edad-output', component_property='children'),
#    [Input(component_id='edad', component_property='value')]
#)


#El parámetro es lo que se quiere mostrar
def update_output_div(input_value):
    return 'Output: {}'.format(input_value*2)


if __name__ == '__main__':
    app.run_server(debug=True)
