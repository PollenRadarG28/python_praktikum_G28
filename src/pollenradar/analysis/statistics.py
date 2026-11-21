"""Statistische Auswertungen von Pollendaten."""

import pandas as pd


def summary(frame: pd.DataFrame) -> pd.DataFrame:
    """Erzeugt deskriptive Kennzahlen für numerische Spalten."""
    return frame.describe(include="number").T
