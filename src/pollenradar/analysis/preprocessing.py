"""Vorverarbeitung von Pollendaten."""

import pandas as pd


def prepare(frame: pd.DataFrame, date_column: str = "date") -> pd.DataFrame:
    """Konvertiert das Datumsfeld und sortiert die Daten chronologisch."""
    result = frame.copy()
    if date_column in result:
        result[date_column] = pd.to_datetime(result[date_column], errors="coerce")
        result = result.dropna(subset=[date_column]).sort_values(date_column)
    return result.reset_index(drop=True)
