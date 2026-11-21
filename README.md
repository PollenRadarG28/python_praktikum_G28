# PollenRadar

PollenRadar lädt Pollendaten aus CSV-Dateien oder APIs, bereitet sie auf,
berechnet Kennzahlen und stellt Messreihen grafisch dar.

## Installation

```bash
python -m pip install -e .
```

## Verwendung

```bash
python -m pollenradar.app daten/pollen.csv
```

Die erwartete Datendatei enthält mindestens eine numerische Messspalte;
optional kann eine Spalte `date` für die zeitliche Sortierung vorhanden sein.
