
# Entwicklungsrichtlinien – PollenRadar Analytics

Dieses Dokument beschreibt die Regeln für die gemeinsame Entwicklung im Projektteam.

## 1. Git-Workflow

Wir verwenden einen vereinfachten GitHub Flow.

- `main` enthält den gemeinsamen Projektstand.
- Für jedes Issue wird ein eigener Branch erstellt.
- Änderungen an `main` erfolgen ausschließlich über Pull Requests.
- Jeder Pull Request wird von mindestens einem anderen Teammitglied überprüft.

## 2. Branch-Konventionen

Branches werden nach folgendem Schema benannt:

`typ/issue-nummer-beschreibung`

Beispiele:

- `feature/12-api-client`
- `fix/18-api-error`
- `docs/21-readme`
- `test/15-statistics`
- `chore/3-git-workflow`

Branch-Namen werden kleingeschrieben und verwenden Bindestriche.

## 3. Commit-Konventionen

Wir verwenden einfache Conventional-Commit-Präfixe:

| Präfix | Verwendung |
|---|---|
| `feat:` | Neue Funktion |
| `fix:` | Fehlerbehebung |
| `docs:` | Dokumentation |
| `test:` | Tests |
| `refactor:` | Umstrukturierung ohne Funktionsänderung |
| `chore:` | Projektkonfiguration und Wartung |

Beispiel:

`feat: implement pollen API client`

Commits sollen möglichst kleine, zusammengehörige Änderungen enthalten.

## 4. Pull-Request-Prozess

1. GitHub-Issue auswählen und sich zuweisen.
2. Issue im Project Board auf **In Progress** setzen.
3. Aktuellen Stand von `main` abrufen.
4. Eigenen Branch erstellen.
5. Änderungen implementieren und testen.
6. Änderungen committen und pushen.
7. Pull Request gegen `main` erstellen.
8. Issue im Project Board auf **In Review** setzen.
9. Review durch mindestens ein anderes Teammitglied durchführen lassen.
10. Nach erfolgreicher Prüfung den PR mergen und das Issue abschließen.

Der Pull Request enthält eine kurze Beschreibung, die Änderungen, die durchgeführten Tests und die zugehörige Issue-Nummer.

Zum automatischen Schließen eines Issues wird `Closes #NUMMER` verwendet.

## 5. Code Reviews

Bei jedem Review achten wir auf:

- Korrektheit und Verständlichkeit
- Einhaltung der Projektarchitektur
- Einhaltung der Python-Codekonventionen
- Fehlerbehandlung
- Sinnvolle Tests
- Keine unnötigen Dateien oder Zugangsdaten

Fehler und Verbesserungsvorschläge werden direkt im Pull Request kommentiert.

## 6. Python-Codekonventionen

- Python-Code folgt PEP 8.
- Variablen und Funktionen verwenden `snake_case`.
- Klassen verwenden `PascalCase`.
- Konstanten verwenden `UPPER_CASE`.
- Imports stehen am Dateianfang.
- Funktionen sollen möglichst eine klar abgegrenzte Aufgabe erfüllen.
- Ruff wird zur Prüfung der Codequalität verwendet.

Vor einem Pull Request:

```bash
python -m ruff check .
python -m ruff format --check .
python -m pytest
```

## 7. Projektorganisation

GitHub Issues dienen zur Aufgabenverwaltung.

Das GitHub Project Board verwendet folgende Status:

- Backlog
- Ready
- In Progress
- Help
- In Review
- Done

Jedes Issue soll eine verständliche Beschreibung und überprüfbare Akzeptanzkriterien enthalten.

## 8. Sicherheit

- Keine Passwörter, Tokens oder API-Schlüssel committen.
- Keine virtuellen Umgebungen (`.venv`) hochladen.
- Lokale Konfigurationen über `.gitignore` ausschließen.
- Änderungen an der Projektarchitektur im Team abstimmen.
