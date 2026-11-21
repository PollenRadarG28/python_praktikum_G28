"""Client für externe Pollen-Datenquellen."""

from typing import Any

import requests


def fetch_json(url: str, *, timeout: float = 10.0) -> Any:
    """Ruft JSON-Daten ab und gibt bei HTTP-Fehlern eine klare Ausnahme aus."""
    response = requests.get(url, timeout=timeout)
    response.raise_for_status()
    return response.json()
