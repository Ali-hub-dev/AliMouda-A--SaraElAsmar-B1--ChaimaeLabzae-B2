"""Adaptation du modèle installé au contrat de l'API."""
from typing import Literal, TypedDict

from sentiment_app.predict import charger_modele
from sentiment_app.predict import predict as _predict

Label = Literal["POSITIVE", "NEGATIVE", "INDETERMINE"]
CORRESPONDANCE: dict[str, Label] = {"positive": "POSITIVE", "negative": "NEGATIVE"}
SEUIL_ABSTENTION = 0.60


class Resultat(TypedDict):
    label: Label
    score: float
    text: str


class SentimentClassifier:
    """Vérifie les classes au démarrage et applique l'abstention."""
    model_name = "tfidf-logreg (TP2, models/sentiment.joblib)"

    def __init__(self) -> None:
        modele = charger_modele()
        if set(modele.classes_) != set(CORRESPONDANCE):
            raise ValueError("Classes du modèle incompatibles avec le contrat")

    def predict(self, text: str) -> Resultat:
        resultat = _predict(text)
        score = resultat["score"]
        label: Label = ("INDETERMINE" if score < SEUIL_ABSTENTION
                        else CORRESPONDANCE[resultat["label"]])
        return {"label": label, "score": score, "text": text[:100]}


def load_model() -> SentimentClassifier:
    return SentimentClassifier()
