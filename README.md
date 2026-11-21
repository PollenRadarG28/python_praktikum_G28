# PollenRadar Analytics

Python-Projekt im Rahmen des Informatik-Praktikums an der TH Lübeck.

Ziel ist es, Pollendaten über eine REST-API abzurufen, statistisch auszuwerten und mit Streamlit grafisch darzustellen.

## Voraussetzungen

- Python 3.13
- Git
- VS Code oder eine andere Python-IDE

## 1. Repository klonen

Öffne ein Terminal und führe folgende Befehle aus:

```bash
git clone https://github.com/PollenRadarG28/python_praktikum_G28.git
cd python_praktikum_G28
```

## 2. Virtuelle Umgebung erstellen

Jeder Entwickler erstellt eine eigene virtuelle Python-Umgebung.

**Windows (PowerShell):**

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Linux / macOS:**

```bash
python3.13 -m venv .venv
source .venv/bin/activate
```

Nach der Aktivierung sollte `(.venv)` im Terminal angezeigt werden.

## 3. Abhängigkeiten installieren

```bash
python -m pip install -r requirements.txt
python -m pip install -e .
```

Alle benötigten Python-Bibliotheken werden dadurch installiert.

## 4. Anwendung starten

Sobald das Streamlit-Grundgerüst implementiert ist:

```bash
streamlit run src/pollenradar/app.py
```

Die Anwendung ist anschließend normalerweise unter `http://localhost:8501` erreichbar.

## 5. Git-Workflow

Für jede Aufgabe wird ein eigener Branch erstellt.

```bash
git switch main
git pull
git switch -c feature/ISSUE-NUMMER-beschreibung
```

Nach der Bearbeitung:

```bash
git add .
git commit -m "feat: kurze Beschreibung"
git push -u origin feature/ISSUE-NUMMER-beschreibung
```

Anschließend auf GitHub einen Pull Request gegen `main` erstellen und das zugehörige Issue verknüpfen.

**Wichtig:** Nicht direkt auf `main` entwickeln.

## Projektstruktur

```text
src/
└── pollenradar/
    ├── app.py
    ├── data/
    ├── analysis/
    └── visualization/
tests/
docs/
requirements.txt
pyproject.toml
README.md
```

## Hinweise

- `.venv/` wird nicht in Git hochgeladen.
- Neue Bibliotheken müssen in `requirements.txt` eingetragen werden.
- Änderungen werden über Pull Requests zusammengeführt.
- Aufgaben und Fortschritt werden über GitHub Issues und Projects verwaltet.
- Bei Problemen oder Fragen ein GitHub Issue beziehungsweise einen Kommentar erstellen.

## Projektteam

PollenRadarG28 – TH Lübeck
