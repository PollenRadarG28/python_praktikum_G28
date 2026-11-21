"""Einlesen und Validieren von Pollendaten im CSV-Format."""

from pathlib import Path

import pandas as pd


def load_csv(path: str | Path) -> pd.DataFrame:
    """Lädt eine CSV-Datei und prüft, dass sie nicht leer ist."""
    frame = pd.read_csv(path)
    if frame.empty:
        raise ValueError(f"Die CSV-Datei ist leer: {path}")
    return frame
