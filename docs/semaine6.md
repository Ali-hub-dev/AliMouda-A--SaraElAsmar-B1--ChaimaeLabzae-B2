# Semaine 6 : paquet installable

## 1. Modèle externe
La roue contient le code sentiment_app, api et ui, sans tests, données ni modèle. Le modèle est un artefact d'entraînement avec son propre cycle de mise à jour. SENTIMENT_MODELE indique son chemin ; dans le dépôt, le chemin par défaut reste models/sentiment.joblib. La fonction chemin_modele() et son test vérifient cette configuration.

## 2. Imports
api/model.py importe maintenant sentiment_app.predict directement, sans sys.path. src/predict.py reste un module de compatibilité pour les anciens scripts et tests ; il référence le même objet Python pour préserver les modifications du chemin par monkeypatch. TypedDict et Literal précisent le contrat et une correspondance explicite vérifie les classes dès le démarrage.

## 3. Roue hors du dépôt
La roue sentiment_app-0.6.0-py3-none-any.whl a été construite avec python -m build --wheel --no-isolation. Son installation nécessite les dépendances déclarées ; la prédiction nécessite également le chemin absolu du modèle dans SENTIMENT_MODELE. Le code et le modèle doivent utiliser des versions compatibles de scikit-learn : le projet et la CI utilisent la série 1.5 (localement 1.5.2).

Les résultats de la validation indépendante sont consignés dans docs/ETAT-TP1-TP6.md.

Validation indépendante réussie : sans variable, code 1 et message indiquant SENTIMENT_MODELE ; avec variable, POSITIVE (0,777) et INDETERMINE (0,5162). Le module importé appartient à wheel-validation/Lib/site-packages ; le service lancé depuis cet environnement répond /health avec status OK. Voir validation-roue.json.
