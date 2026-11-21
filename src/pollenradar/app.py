"""Kleiner CLI-Einstiegspunkt für PollenRadar."""

import argparse

from pollenradar.analysis.preprocessing import prepare
from pollenradar.analysis.statistics import summary
from pollenradar.data.csv_loader import load_csv


def main() -> None:
    parser = argparse.ArgumentParser(description="Pollen-Daten analysieren")
    parser.add_argument("csv", help="Pfad zur CSV-Datei")
    args = parser.parse_args()
    print(summary(prepare(load_csv(args.csv))))


if __name__ == "__main__":
    main()
