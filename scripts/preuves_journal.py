import csv
import json
from pathlib import Path

from fastapi.testclient import TestClient

from api.main import app
from sentiment_app.predict import charger_modele

r = Path.cwd()
evidence = {}
with TestClient(app) as c:
    evidence["health"] = c.get("/health").json()
    for key, body in [
        ("positif", {"text": "Livraison rapide, produit conforme, très satisfait"}),
        ("negatif", {"text": "Produit cassé et service injoignable, à fuir"}),
        ("inconnu", {"text": "xqzvb wlkptr grombu"}),
        ("vide", {"text": ""}),
        ("absent", {}),
        ("entier", {"text": 42}),
        ("espaces", {"text": "   "}),
    ]:
        response = c.post("/predict", json=body)
        evidence[key] = {"status": response.status_code, "body": response.json()}
    evidence["lot"] = [
        {"text": row["text"], **c.post("/predict", json=row).json()}
        for row in csv.DictReader((r / "data/avis_exemple.csv").open(encoding="utf-8"))
    ]
evidence["vocabulaire_demo"] = len(charger_modele().named_steps["tfidf"].vocabulary_)
(r / "docs/preuves-journal.json").write_text(
    json.dumps(evidence, indent=2, ensure_ascii=False), encoding="utf-8"
)
print("Preuves API et lot enregistrées.")
