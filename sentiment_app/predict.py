#!/usr/bin/env python
"""Prédiction unitaire : la fonction que l'API de la semaine 3 appellera.

Usage :
  python src/predict.py "Livraison rapide, très satisfait"
  >>> from predict import predict ; predict("texte")
"""
import os
import sys
from functools import lru_cache
from pathlib import Path
from typing import Literal, TypedDict, cast

import joblib

MODELE = Path(__file__).resolve().parents[1] / "models" / "sentiment.joblib"


class Prediction(TypedDict):
    label: Literal["positive", "negative"]
    score: float


def chemin_modele() -> Path:
    return Path(os.environ.get("SENTIMENT_MODELE") or str(MODELE)).expanduser()


@lru_cache(maxsize=1)
def charger_modele():
    """Chargé une seule fois par processus, pas à chaque appel."""
    if not chemin_modele().exists():
        raise FileNotFoundError(
            f"Modèle introuvable : {chemin_modele()}. Lancez python src/train.py, "
            "ou indiquez son chemin dans SENTIMENT_MODELE."
        )
    return joblib.load(chemin_modele())


def predict(texte: str) -> Prediction:
    """Renvoie {'label': 'positive'|'negative', 'score': float}."""
    if not isinstance(texte, str) or not texte.strip():
        raise ValueError("texte vide")
    pipeline = charger_modele()
    etiquette = cast(Literal["positive", "negative"], pipeline.predict([texte])[0])
    score = float(pipeline.predict_proba([texte]).max())
    return {"label": etiquette, "score": round(score, 4)}


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    resultat = predict(" ".join(sys.argv[1:]))
    print(f"{resultat['label']} (confiance {resultat['score']:.0%})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
