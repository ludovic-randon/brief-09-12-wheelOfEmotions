#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 12:04:54 2020

@author: randon
"""

import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import dash_table
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import SGDClassifier
import pickle
#-----------------------------------------
# - Function -
def print_table(res):
    # Compute mean and std
    final = {}
    for model in res:
        arr = np.array(res[model])
        final[model] = {
            "name" : model,
            "time" : arr[:, 0].mean().round(2),
            "f1": [arr[:,1].mean().round(3), arr[:,1].std().round(3)],
            "recall": [arr[:,2].mean().round(3), arr[:,1].std().round(3)],
            "precision": [arr[:,3].mean().round(3), arr[:,1].std().round(3)],}
    df = pd.DataFrame.from_dict(final, orient="index").round(3)
    return df
#
#-----------------------------------------
# - Define df -
filename1 = "data/saveRes/LOGREGmodel.sav"
res1 = pickle.load(open(filename1, 'rb'))
res1 = print_table(res1)

#filename2 = "data/saveRes/SVCmodel.sav"
#res2 = pickle.load(open(filename2, 'rb'))
#res2 = print_table(res2)

filename3 = "data/saveRes/SGDmodel.sav"
res3 = pickle.load(open(filename3, 'rb'))
res3 = print_table(res3)

filename4 = "data/saveRes/KNNmodel.sav"
res4 = pickle.load(open(filename4, 'rb'))
res4 = print_table(res4)

filename5 = "data/saveRes/DTREEmodel.sav"
res5 = pickle.load(open(filename5, 'rb'))
res5 = print_table(res5)

#-----------------------------------------
# - Tabs - 
tab1_content2 = dbc.Row([html.H4(children='Logistic Regression', className="mt-4"),

            dash_table.DataTable(id='container-button-timestamp',
            data=res1.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in res1.columns],
            style_header={'backgroundColor': 'rgb(30, 30, 30)'},
            style_table={'overflowX': 'auto',
                         'width' : '1200px',
                         'margin-bot': '100px'},
            style_cell={
                'backgroundColor': 'rgb(50, 50, 50)',
                'color': 'white',
                'textAlign':'left',
                'padding-left':'5px'
                },
            css=[ {'selector': '.row', 'rule': 'margin: 0'}]
            ),
            html.H6(children='On these different optimizations of the Logistic Regression model, we see that it is the vectorization with stopworld and ngramm which obtains the best result with an F1 at 0.892, despite the longer execution speed,', className="mt-4"),
            ])
# ------
"""
tab2_content2 = dbc.Row([html.H4(children='Super Vector Classifier', className="mt-4"),

            dash_table.DataTable(id='container-button-timestamp',
            data=res2.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in res2.columns],
            style_header={'backgroundColor': 'rgb(30, 30, 30)'},
            style_table={'overflowX': 'auto',
                         'width' : '1200px',
                         'margin-bot': '100px'},
            style_cell={
                'backgroundColor': 'rgb(50, 50, 50)',
                'color': 'white',
                'textAlign':'left',
                'padding-left':'5px'
                },
            css=[ {'selector': '.row', 'rule': 'margin: 0'}]
            ),
            html.H6(children='On these different optimizations of the Logistic Regression model, we see that it is the vectorization with stopworld and ngramm which obtains the best result with an F1 at 0.892, despite the longer execution speed,', className="mt-4"),
            ])
"""
# ------
tab3_content2 = dbc.Row([html.H4(children='Stochastic Gradient Descent', className="mt-4"),

            dash_table.DataTable(id='container-button-timestamp',
            data=res3.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in res3.columns],
            style_header={'backgroundColor': 'rgb(30, 30, 30)'},
            style_table={'overflowX': 'auto',
                         'width' : '1200px'},
            style_cell={
                'backgroundColor': 'rgb(50, 50, 50)',
                'color': 'white',
                'textAlign':'left',
                'padding-left':'5px'
                },
            css=[ {'selector': '.row', 'rule': 'margin: 0'}]
            ),
            html.H6(children='On the Stochastic Gradient descent models, it is the vectorization with stop_world and Ngram which obtains the best result with an F1 of 0.90, even if the other optimization attempts are very good', className="mt-4"),
            ])
# ------
tab4_content2 = dbc.Row([html.H4(children='KNNeighbor', className="mt-4"),

            dash_table.DataTable(id='container-button-timestamp',
            data=res4.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in res4.columns],
            style_header={'backgroundColor': 'rgb(30, 30, 30)'},
            style_table={'overflowX': 'auto',
                         'width' : '1200px'},
            style_cell={
                'backgroundColor': 'rgb(50, 50, 50)',
                'color': 'white',
                'textAlign':'left',
                'padding-left':'5px'
                },
            css=[ {'selector': '.row', 'rule': 'margin: 0'}]
            ),
            html.H6(children='The KNN model is a basic model. We get mediocre results, regardless of the optimization, at best we get 0.757 with all the TFIDF vectorization criteria included', className="mt-4"),
            ])
# ------
tab5_content2 = dbc.Row([html.H4(children='Decision Tree', className="mt-4"),
            dash_table.DataTable(id='container-button-timestamp',
            data=res5.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in res5.columns],
            style_header={'backgroundColor': 'rgb(30, 30, 30)'},
            style_table={'overflowX': 'auto',
                         'width' : '1200px'},
            style_cell={
                'backgroundColor': 'rgb(50, 50, 50)',
                'color': 'white',
                'textAlign':'left',
                'padding-left':'5px'
                },
            css=[ {'selector': '.row', 'rule': 'margin: 0'}]
            ),
            html.H6(children='Decision Tree has average results, we see that it is the optimization with NGram & stop word which dominates with 0.867, however it is followed by ready by the model without NGram with 0.863, in view of the execution time, which with 10x higher with NGram, it is better to keep the model without, so we will keep the model without Ngram with 0.863', className="mt-4"),
            ])

# ----------------------------------------
# - Figure - 


#-----------------------------------------
# - Layout -

layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1(children='Machine learning'), className="mb-2")
        ]),
        dbc.Row([
            dbc.Col(html.H6(children='We will compare and analyse different model for Kaggle Data'), className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.H6(children='First, we try some vectorizing data, we compared the results of 5 machine learning models, Logistique regression, Super Vector Classifier, SGradientDescent, KNNeighbort, DecisionTree, for the Kaggle Dataset to determine the best vectorizing of each'), className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.H6(children='Vectorizer keyword : SW=StopWorld, NG=ngram_range, idf=TFidf '), className="mb-2")
        ]),
        dbc.Row([dbc.Tabs(
    [
        dbc.Tab(tab1_content2, label="Logistic Reg",label_style={"color":"#810303"}),
        dbc.Tab(tab3_content2, label="SGradient Descent", label_style={"color":"#11337E"}),
        dbc.Tab(tab4_content2, label="KNNeighbor",label_style={"color":"#810303"}),
        dbc.Tab(tab5_content2, label="Decision Tree",label_style={"color":"#11337E"}),
    ],
),   
        ], className="mb-4"),
        dbc.Row([
            dbc.Col(html.H4(children='Lets compare the best model of each classifier with classification report to determine the best model for the kaggle data'), className="mt-4 mb-4")
        ]),
        dbc.Row([
              dbc.Col(html.Img(src="/assets/saveCr/LOGREGcr.png", height="240px"), width=4.5 ),
              dbc.Col(html.Img(src="/assets/saveCr/SGDcr.png", height="240px"),width=4.5),
              dbc.Col(html.H5(children='As we can see, the distribution of the scores on the different emotions is homogeneous on all the models, we have "Love" and "Surprised" which are lower, so our models give us the same type of result, if we are focused on score, we can deduce that the Stochastic Descent Gradient model is really the best in addition to being the fastest.'),)
            ], className="mt-4"),
        dbc.Row([
             dbc.Col(html.Img(src="/assets/saveCr/KNNcr.png", height="240px"),width=4.5),
             dbc.Col(html.Img(src="/assets/saveCr/DTREEcr.png", height="240px"),width=4.5),
             ], className="mb-4"),
                dbc.Row([
        dbc.Col(html.H4(children='Lets compare the best model of each classifier with classification report to determine the best model for the kaggle data'), className="mt-4 mb-4")
        ]),
        
    ])
])