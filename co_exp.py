#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 09:50:27 2023

@author: magnusnadheim
"""

# Import packages
import pandas as pd
import plotly.express as px
from pandas_datareader import wb

from dash import dcc, html, Dash
from dash.dependencies import Input, Output

import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template

# URL and set templates
dbc_css = 'https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.2/dbc.min.css'
load_figure_template('bootstrap')

# Read dataframe
df = pd.read_csv('world_1960_2021.csv')

df_update = df[df.year > 1990]

# Set year as index
df_update.set_index('year', inplace = True)


fig_kt = px.line(
    df_update, 
    y = 'EN.ATM.CO2E.KT',                                
)

fig_kt.update_layout(
    yaxis_title = None,                          
    xaxis_title = None,                         
    title = 'CO2 emmisions (kt)',  
    title_x = 0.5,   
    margin = {'l' : 0, 'r' : 0}
)

fig_pc = px.line(
    df_update, 
    y = 'EN.ATM.CO2E.PC',                                
)

fig_pc.update_layout(
    yaxis_title = None,                          
    xaxis_title = None,                         
    title = 'CO2 emissions (metric tons per capita)',  
    title_x = 0.5,   
    margin = {'l' : 0, 'r' : 0}
)

# Create application
app = Dash(__name__, external_stylesheets = [dbc.themes.BOOTSTRAP, dbc_css])
server = app.server

app.layout = dbc.Container(
    children = [
        
        # Header
        html.H1('CO2 emissions around the world'),
        dcc.Markdown(
            """Data on emissions and potential drivers are extracted from the 
               [World Development Indicators](https://datatopics.worldbank.org/world-development-indicators/) 
               database."""
        ),
        
        # Place plots side by side
        dbc.Row(
            children = [
            
            # Column 1: price plot
            dbc.Col(dcc.Graph(figure = fig_kt), width = 6),
            
            # Column 2: volume plot
            dbc.Col(dcc.Graph(figure = fig_pc), width = 6)
            ]
        )  
        
    ],
    className = 'dbc'
)

if __name__ == "__main__":
    app.run_server(debug = True)
