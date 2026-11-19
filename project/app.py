# Import libraries
from shiny import ui, render, App
import pandas as pd
import numpy as np
import requests
import matplotlib.pyplot as plt
from pathlib import Path
import plotly.express as px
from shinywidgets import output_widget, render_widget

# Import analysisData csv file
dataPath = Path(__file__).parent / "data" / "analysisData.csv"
analysisData = pd.read_csv(dataPath)
# Add valid circuit data
noRacesPerCircuit = analysisData.groupby("circuitName")["raceId"].nunique()
validCircuits = noRacesPerCircuit[noRacesPerCircuit >= 5].index

# Spearman correlation calculation function
def calculateSpearman(group):
    spearmanCorr = group["qualiPosition"].corr(group["position"],method="spearman")
    return spearmanCorr

# Correlations per circuit
circuitCorr = analysisData[analysisData["circuitName"].isin(validCircuits)].groupby("circuitName").apply(calculateSpearman, include_groups=False).sort_values(ascending=False)

# Absolute position difference  and average calculations 
analysisData["absPositionDiff"] = analysisData["positionDiff"].abs()
circuitAbsDiff = (analysisData.groupby("circuitName")["absPositionDiff"].mean().loc[validCircuits].sort_values())

# UI
app_ui = ui.page_fluid(
    ui.h2("Formula 1: Qualifying & Race Results"), # Title
    ui.p("Exploring the relationship between F1 qualifying and finishing positions between 2014-2024"), # Subtitle
    # Circuit drop down
    ui.input_select(
            "circuit",
            "Select a circuit:",
            choices=sorted(validCircuits)
        ),
    # Circuit scatter plot card
    ui.card(
        ui.card_header('Scatter Plot'),
        output_widget("qualiScatter"),
    ),
    
    ui.h3("Comparing circuits"), # Subtitle
    
    # Graph type drop down
    ui.input_select(
        "metric",
        "Choose graph:",
        choices={
            "correlation": "Spearman Correlation",
            "difference": "Mean Absolute Position Difference"
        }
    ),
    # Bar chart card
    ui.card(
            ui.card_header('Bar Chart'),
            output_widget("circuitComparison"),
        ) 
)

# SERVER
def server(input, output, session):

    @render.text
    def selectedCircuit():
        return f"Selected circuit: {input.circuit()}"
    
    @render.text
    def correlation(): 
        circuitData = analysisData[analysisData["circuitName"] == input.circuit()]
        correlation = circuitData["qualiPosition"].corr(circuitData["position"], method="spearman")
        return f"Correlation: {correlation:.3f}"
    
    @render_widget
    def qualiScatter():
        circuitData = analysisData[analysisData["circuitName"] == input.circuit()]
        fig = px.scatter(
            circuitData,
            x="qualiPosition",
            y="position",
            title=f"Qualifying vs Finishing Position for {input.circuit()}",
            labels={"qualiPosition": "Qualifying Position",
                    "position": "Finishing Position"},
                    opacity=0.4
        )
        return fig

    @render_widget
    def circuitComparison():
        if input.metric() == "correlation":
            values = circuitCorr
            chartTitle = "Qualifying vs Finishing Correlation by Circuit"
            xlabel = "Spearman Correlation"
        else:
            values = circuitAbsDiff
            chartTitle = "Mean Absolute Position Difference by Circuit"
            xlabel = "Mean Absolute Difference"

        fig = px.bar(
            x=values.values,
            y=values.index,
            orientation="h",
            labels={
                "x": xlabel,
                "y": "Circuit"
            },
            title=chartTitle
        )
        fig.update_layout(height=650)
        return fig

# INITIALISE APP
app = App(app_ui,server)