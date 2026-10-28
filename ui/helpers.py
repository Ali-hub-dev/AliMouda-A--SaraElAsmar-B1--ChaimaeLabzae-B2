"""Fonctions pures de l'interface : chargement du modÃ¨le, prÃ©diction, rÃ©sumÃ©.

SÃ©parÃ©es de app.py pour Ãªtre testables sans lancer Streamlit.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

RACINE = Path(__file__).resolve().parents[1]
MODELE = RACINE / "models" / "sentiment.joblib"
SEUIL_INCERTITUDE = 0.60   # en dessous, on affiche Â« Ã  vÃ©rifier Â»


def charger_predicteur():
    """Renvoie la fonction predict() du TP2, ou lÃ¨ve FileNotFoundError."""
    if not MODELE.exists():
        raise FileNotFoundError(
            "models/sentiment.joblib absent : lancez d'abord python src/train.py"
        )
    sys.path.insert(0, str(RACINE / "src"))
    from predict import predict  # noqa: E402  (import tardif : le modÃ¨le doit exister)
    return predict


def classer(texte: str, predicteur) -> dict:
    """PrÃ©diction enrichie d'un verdict lisible par un non-spÃ©cialiste."""
    if not isinstance(texte, str) or not texte.strip():
        raise ValueError("texte vide")
    resultat = predicteur(texte)
    incertain = resultat["score"] < SEUIL_INCERTITUDE
    resultat["verdict"] = "Ã  vÃ©rifier" if incertain else resultat["label"]
    resultat["incertain"] = incertain
    return resultat


def predire_lot(df: pd.DataFrame, predicteur, colonne: str = "review") -> pd.DataFrame:
    """Ajoute les colonnes prediction, confiance et verdict Ã  un tableau d'avis."""
    if colonne not in df.columns:
        raise KeyError(f"colonne '{colonne}' absente du fichier")
    lignes = [classer(str(t), predicteur) for t in df[colonne].fillna("")  if str(t).strip()]
    if not lignes:
        raise ValueError("aucun avis exploitable dans le fichier")
    sortie = df.loc[df[colonne].fillna("").astype(str).str.strip() != ""].copy()
    sortie["prediction"] = [ligne["label"] for ligne in lignes]
    sortie["confiance"] = [round(ligne["score"], 3) for ligne in lignes]
    sortie["verdict"] = [ligne["verdict"] for ligne in lignes]
    return sortie


def resumer(df: pd.DataFrame) -> dict:
    """Les trois chiffres que l'Ã©quipe relation client regarde en premier."""
    negatifs = int((df["prediction"] == "negative").sum())
    a_verifier = int((df["verdict"] == "Ã  vÃ©rifier").sum())
    return {
        "total": len(df),
        "negatifs": negatifs,
        "part_negatifs": round(100 * negatifs / len(df), 1) if len(df) else 0.0,
        "a_verifier": a_verifier,
        "confiance_moyenne": round(float(df["confiance"].mean()), 3) if len(df) else 0.0,
    }

