"""Tests d'intégration : l'API telle qu'elle tourne vraiment (TP4, étape D). À COMPLÉTER.

Les tests du TP3 vérifient des réponses ; ceux-ci vérifient le démarrage de l'API
et son comportement quand le modèle manque ou tombe en panne.
"""
from pathlib import Path

import pytest

MODELE = Path(__file__).resolve().parents[1] / "models" / "sentiment.joblib"
pytestmark = pytest.mark.skipif(not MODELE.exists(), reason="modèle non produit : python src/train.py")


def test_demarrage_reel_charge_le_modele():
    """D.1 (donné en exemple) : un client ouvert par « with » exécute le lifespan."""
    from fastapi.testclient import TestClient

    from api.main import app

    with TestClient(app) as client:
        reponse = client.get("/health")
    assert reponse.status_code == 200
    assert "TP2" in reponse.json()["model"]


# À écrire (étape D) :
# D.2 modèle absent : chemin du modèle redirigé (monkeypatch), cache vidé
#     (charger_modele.cache_clear()), l'API refuse de démarrer (FileNotFoundError) ;
# D.3 modèle non chargé : l'API démarrée, modèle retiré de app.state, 503 sur /health et /predict ;
# D.4 modèle en panne : predict lève RuntimeError, puis ValueError("bug interne") :
#     500 dans les deux cas, sans le message interne dans la réponse.
# Utilisez monkeypatch.setattr pour toute modification : il restaure l'état à la fin du test.

def test_modele_absent(monkeypatch, tmp_path):
    """D.2 : l'API refuse de démarrer sans modèle."""
    from fastapi.testclient import TestClient

    import predict as predict_module
    from api.main import app

    monkeypatch.setattr(
        predict_module,
        "MODELE",
        tmp_path / "modele_inexistant.joblib",
    )
    predict_module.charger_modele.cache_clear()

    try:
        with pytest.raises(FileNotFoundError):
            with TestClient(app):
                pass
    finally:
        predict_module.charger_modele.cache_clear()


def test_modele_non_charge(monkeypatch):
    """D.3 : les endpoints répondent 503 sans modèle."""
    from fastapi.testclient import TestClient

    from api.main import app

    with TestClient(app) as client:
        monkeypatch.setattr(app.state, "classifier", None)

        assert client.get("/health").status_code == 503
        assert client.post(
            "/predict",
            json={"text": "Très bon produit"},
        ).status_code == 503


@pytest.mark.parametrize(
    "erreur",
    [
        RuntimeError("panne du modèle"),
        ValueError("bug interne"),
    ],
)
def test_modele_en_panne(monkeypatch, erreur):
    """D.4 : une panne interne renvoie 500."""
    from fastapi.testclient import TestClient

    from api.main import app

    class ModeleEnPanne:
        def predict(self, texte):
            raise erreur

    with TestClient(app) as client:
        monkeypatch.setattr(
            app.state,
            "classifier",
            ModeleEnPanne(),
        )

        reponse = client.post(
            "/predict",
            json={"text": "Très bon produit"},
        )

        assert reponse.status_code == 500
        assert "bug interne" not in reponse.text
        assert "panne du modèle" not in reponse.text
