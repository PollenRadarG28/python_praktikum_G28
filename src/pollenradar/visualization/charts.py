"""Diagramme für Pollendaten."""

import matplotlib.pyplot as plt
import pandas as pd


def plot_series(frame: pd.DataFrame, date_column: str, value_column: str):
    """Erstellt ein Liniendiagramm für eine Pollenmessreihe."""
    figure, axis = plt.subplots(figsize=(10, 5))
    axis.plot(frame[date_column], frame[value_column])
    axis.set(
        xlabel="Datum", ylabel=value_column, title=f"{value_column} im Zeitverlauf"
    )
    figure.tight_layout()
    return figure
