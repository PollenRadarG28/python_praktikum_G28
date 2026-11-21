import pandas as pd

from pollenradar.analysis.preprocessing import prepare


def test_prepare_sorts_and_parses_dates():
    frame = prepare(pd.DataFrame({"date": ["2024-02-01", "2024-01-01"]}))
    assert frame.iloc[0]["date"] == pd.Timestamp("2024-01-01")
