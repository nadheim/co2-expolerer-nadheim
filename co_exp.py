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
        
    ],
    className = 'dbc'
)

if __name__ == "__main__":
    app.run_server(debug = True)