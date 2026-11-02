# Semaine 5 : interface Streamlit

## 1. Séparation du client et du modèle
La page utilise ui.client pour GET /health et POST /predict, et ne charge pas le modèle. Un modèle réentraîné peut être remplacé côté serveur sans modifier la page. Les tests remplacent la session HTTP par TestClient : ils vérifient ainsi le vrai contrat API sans serveur externe.

## 2. Abstention
Pour « xqzvb wlkptr grombu », l'API répond INDETERMINE. La page affiche « Je ne sais pas : à faire vérifier par un humain » et explique le seuil d'abstention, plutôt que de forcer une décision.

## 3. Panne et fichier d'exemple
Une connexion refusée produit « API injoignable : lancez d'abord uvicorn api.main:app ». Un 422 donne un avertissement sur le texte ; un 503 signale le modèle non chargé. Ces comportements sont vérifiés par les tests du client et AppTest.

Mesure du fichier data/avis_exemple.csv avec le modèle local : 6 avis, 3 POSITIVE, 2 NEGATIVE et 1 INDETERMINE, soit 1/6 (16,7 %) envoyé à un humain. La page présente le tableau, le résumé et le téléchargement CSV.
