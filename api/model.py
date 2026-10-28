
"""Raccord entre l'API et le modèle entraîné au TP2.

L'API n'entraîne rien et ne connaît pas scikit-learn :
elle appelle la fonction predict() de src/predict.py,
qui charge models/sentiment.joblib une seule fois.
"""

import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RACINE / "src"))

from predict import charger_modele  # noqa: E402
from predict import predict as _predict  # noqa: E402

# Seuil d'abstention retenu après analyse de la courbe.
SEUIL_ABSTENTION = 0.60


class SentimentClassifier:
    """Enveloppe du modèle TP2 avec abstention."""

    model_name = "tfidf-logreg (TP2, models/sentiment.joblib)"

    def __init__(self) -> None:
        """Charge le modèle et vérifie sa disponibilité."""
        charger_modele()

    def predict(self, text: str) -> dict:
        """Prédit un sentiment ou s'abstient si le score est faible."""
        resultat = _predict(text)

        score = resultat["score"]

        if score < SEUIL_ABSTENTION:
            label = "INDETERMINE"
        else:
            label = resultat["label"].upper()

        return {
            "label": label,
            "score": score,
            "text": text[:100],
        }


def load_model() -> SentimentClassifier:
    """Construit le classifier avec le modèle mis en cache."""
    return SentimentClassifier()
