
"""Tests du jeu d'or : TP4, étape C.

Une erreur franche correspond à une prédiction POSITIVE au lieu de
NEGATIVE, ou inversement.

Une abstention INDETERMINE n'est pas une erreur franche.
Les erreurs connues encore présentes sont marquées xfail(strict=True).
"""

import csv
from pathlib import Path

import pytest

RACINE = Path(__file__).resolve().parents[1]
JEU_OR = RACINE / "data" / "jeu_or.csv"
MODELE = RACINE / "models" / "sentiment.joblib"

FRANCHES = {"POSITIVE", "NEGATIVE"}
MINIMUM_AVIS = 20
MINIMUM_DIFFICILES = 5


def lire_jeu_or() -> list[dict[str, str]]:
    """Lit les avis du jeu d'or."""
    if not JEU_OR.exists():
        return []

    with JEU_OR.open(encoding="utf-8", newline="") as f:
        return [
            ligne
            for ligne in csv.DictReader(f)
            if (ligne.get("text") or "").strip()
        ]


LIGNES = lire_jeu_or()


def cas_du_jeu_or():
    """Prépare les tests et les erreurs connues encore actives."""
    from api.model import SEUIL_ABSTENTION
    from predict import predict

    for numero, ligne in enumerate(LIGNES, start=2):
        raison = (ligne.get("erreur_connue") or "").strip()
        marques = []

        if raison and MODELE.exists():
            resultat = predict(ligne["text"])
            score = resultat["score"]
            label = resultat["label"].upper()

            if score >= SEUIL_ABSTENTION and label != ligne["attendu"]:
                marques.append(
                    pytest.mark.xfail(
                        strict=True,
                        reason=raison,
                    )
                )

        yield pytest.param(
            ligne["text"],
            ligne["attendu"],
            id=f"ligne-{numero}",
            marks=marques,
        )


def test_jeu_or_complet():
    """Vérifie au moins 20 avis, dont 5 difficiles."""
    assert len(LIGNES) >= MINIMUM_AVIS, (
        f"jeu d'or incomplet : {len(LIGNES)} avis sur {MINIMUM_AVIS}"
    )

    difficiles = [
        ligne
        for ligne in LIGNES
        if (ligne.get("difficulte") or "").strip()
    ]

    assert len(difficiles) >= MINIMUM_DIFFICILES, (
        f"{len(difficiles)} avis difficiles sur {MINIMUM_DIFFICILES}"
    )

    for ligne in LIGNES:
        assert ligne["attendu"] in FRANCHES, (
            f"étiquette attendue invalide : {ligne['attendu']!r}"
        )


@pytest.fixture(scope="module")
def client():
    """Démarre l'API avec le modèle réel."""
    if not MODELE.exists():
        pytest.skip("modèle non produit : python src/train.py")

    from fastapi.testclient import TestClient

    from api.main import app

    with TestClient(app) as c:
        yield c


@pytest.mark.parametrize("texte, attendu", list(cas_du_jeu_or()))
def test_pas_d_erreur_franche(client, texte, attendu):
    """Vérifie l'absence d'erreur franche non déclarée."""
    reponse = client.post(
        "/predict",
        json={"text": texte},
    )

    assert reponse.status_code == 200

    label = reponse.json()["label"]

    assert label in FRANCHES | {"INDETERMINE"}

    assert not (
        label in FRANCHES and label != attendu
    ), f"erreur franche : {label} au lieu de {attendu}"
