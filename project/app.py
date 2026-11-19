from shiny import ui, render, App
import pandas as pd
import numpy as np
import requests
import matplotlib.pyplot as plt
from pathlib import Path

dataPath = Path(__file__).parent / "data" / "analysisData.csv"
analysisData = pd.read_csv(dataPath)
print(analysisData.shape)

app_ui = ui.page_fluid(
    ui.h2("Formula 1: Qualifying & Race Results"),
    ui.p("Exploring the relationship between F1 qualifying and finishing positions between 2014-2024"),
    ui.input_select(
        "circuit",
        "select a circuit:",
        choices=sorted(analysisData["circuitName"].unique())
    ),
    ui.output_text("selectedCircuit")
)

def server(input, output, session):
    @render.text
    def selectedCircuit():
        return f"Selected circuit: {input.circuit()}"

app = App(app_ui,server)