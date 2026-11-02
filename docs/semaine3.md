# Semaine 3 : API

## Démarrage sans modèle
Le chargement se fait dans le lifespan, avant de servir les requêtes. Le test d'intégration redirige le chemin vers un fichier absent et constate FileNotFoundError : le déploiement échoue immédiatement au lieu d'annoncer un service disponible. Une perte du classifieur après démarrage reçoit 503 sur health et predict.

## Validation à deux niveaux
Pydantic refuse les corps invalides au niveau HTTP (422 avec detail sous forme de liste). La fonction de prédiction refuse aussi les textes vides lorsqu'elle est appelée directement depuis Python. Ces protections couvrent deux points d'entrée différents ; strip() définit le texte vide aux deux endroits.


## Variante Streamlit initiale et seuil
Le dossier contient deux variantes du TP3 : l'ancien parcours Streamlit et le parcours API utilisé ensuite par TP4–TP6. Les fonctions historiques ui/helpers.py et leurs trois tests sont conservés. L'interface active ui/app.py suit désormais le TP5 et appelle l'API.

À 0,60, 16 avis sur les 58 du test de démonstration partent vers un humain (27,6 %), contre aucun à 0,50 et 21 à 0,70. Les erreurs automatiques diminuent respectivement de 7 à 2 puis 0. Le seuil permet donc de rendre l'incertitude visible ; les résultats ne garantissent pas la qualité sur un autre domaine.
