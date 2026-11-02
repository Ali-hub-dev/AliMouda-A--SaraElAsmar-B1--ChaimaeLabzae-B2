"""Frontières et propriétés du contrat HTTP."""
import pytest
from fastapi.testclient import TestClient
from hypothesis import given, settings
from hypothesis import strategies as st

from api.main import app


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as session:
        yield session


def verifier_erreurs(reponse):
    erreurs = reponse.json()["detail"]
    assert isinstance(erreurs, list) and erreurs
    assert all({"loc", "msg", "type"} <= erreur.keys() for erreur in erreurs)


@pytest.mark.parametrize("corps,code", [
    ({"text": ""}, 422), ({"text": "   "}, 422), ({"text": "a"}, 200),
    ({"text": "a" * 2000}, 200), ({"text": "a" * 2001}, 422),
    ({}, 422), ({"text": 42}, 422), (None, 422),
])
def test_frontieres_du_contrat(client, corps, code):
    reponse = (client.post("/predict", json=corps) if corps is not None else
               client.post("/predict", content=b"pas du json",
                           headers={"Content-Type": "application/json"}))
    assert reponse.status_code == code
    if code == 422:
        verifier_erreurs(reponse)


@settings(deadline=None, max_examples=100)
@given(st.text(min_size=1, max_size=2000).filter(lambda texte: bool(texte.strip())))
def test_texte_valide(client, texte):
    reponse = client.post("/predict", json={"text": texte})
    assert reponse.status_code == 200
    resultat = reponse.json()
    assert resultat["label"] in {"POSITIVE", "NEGATIVE", "INDETERMINE"}
    assert 0 <= resultat["score"] <= 1


@settings(deadline=None, max_examples=100)
@given(st.text(alphabet=" \t\n\r\v\f\u0085\u00a0\u2003", min_size=1, max_size=2000))
def test_blancs_refuses(client, texte):
    reponse = client.post("/predict", json={"text": texte})
    assert reponse.status_code == 422
    verifier_erreurs(reponse)
