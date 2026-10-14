# Compte rendu du TP2 — Entraînement et évaluation

**Équipe :** Ali Mouda, Sara El Asmar et Chaimae Labzae  
**Dépôt :** https://github.com/Ali-hub-dev/AliMouda-A--SaraElAsmar-B1--ChaimaeLabzae-B2  
**Date :** 14/10/2026  
**Module :** Développement et déploiement d’applications intelligentes

## 1. Le besoin et son cadrage

Le besoin métier est de repérer rapidement les avis négatifs parmi un volume important de commentaires. Le TP2 transforme ce besoin en une tâche de classification binaire, afin de fournir une prédiction reproductible et mesurable. L'approche retenue est le **Machine Learning supervisé**, justifiée par **(a)** la disponibilité d'avis étiquetés et **(c)** le coût limité d'une prédiction après entraînement. Le critère **(d)** rend essentiel le suivi des avis négatifs manqués.

## 2. L'architecture du dépôt

| Élément | Rôle |
| --- | --- |
| `src/make_demo.py` | Génération des avis de démonstration |
| `src/train.py` | Entraînement et sauvegarde du pipeline |
| `src/evaluate.py` | Évaluation et analyse des erreurs |
| `src/predict.py` | Prédiction sur un nouvel avis |
| `tests/test_model.py` | Contrôles des métriques et du modèle |
| `models/metrics.json` | Résultats chiffrés versionnés |
| `models/sentiment.joblib` | Modèle binaire local, non versionné |
| `docs/semaine2.md` | Analyse des erreurs |

Le fichier `models/metrics.json` doit être conservé dans Git pour tracer les performances et le seuil de validation. Le modèle `models/sentiment.joblib` n'est pas versionné car il est généré par l'entraînement et peut être volumineux. Le CSV de démonstration et `.venv/` sont également régénérables.

## 3. Le modèle

La commande `python src\make_demo.py` a produit **290 avis**, dont **145 positifs et 145 négatifs** ; le jeu contient **100 avis mitigés et 30 neutres**, volontairement difficiles. Le découpage de référence est de 80 % pour l'entraînement et 20 % pour le test. Le pipeline associe une vectorisation du texte et un classificateur ; la séparation doit précéder la vectorisation pour éviter la fuite de données.

L'entraînement sur Allociné a également été réalisé, comme l'indique la réussite des **42 tests du TP2**. Cependant, les sorties chiffrées de `train.py`, `evaluate.py` et `models/metrics.json` n'ont pas été transmises : il faut donc les reporter avant remise.

| Jeu | Avis | Vocabulaire | F1 macro | Rappel négatif |
| --- | ---: | ---: | ---: | ---: |
| Démonstration | 290 | **À relever** | **À relever** | **À calculer** |
| Allociné | 20 000 (jeu prévu) | **À relever** | **À relever** | **À calculer** |

**Exactitude, démonstration :** à relever.  
**Exactitude, Allociné :** à relever.

**Matrice de confusion issue de votre exécution :**

```text
                  Prédit négatif   Prédit positif
Réel négatif          [   ]             [   ]
Réel positif          [   ]             [   ]
```

**Commentaire ligne 1 :** parmi les avis réellement négatifs, indiquer ceux correctement détectés et ceux classés à tort positifs.  
**Commentaire ligne 2 :** parmi les avis réellement positifs, indiquer ceux classés à tort négatifs et ceux correctement détectés.

## 4. L'analyse des erreurs

Le jeu de démonstration comporte des avis mitigés avec des changements de sentiment. Une représentation en sac de mots peut confondre « bon puis mauvais » et « mauvais puis bon » puisqu'elle ne conserve pas l'ordre des mots. Les avis négatifs prédits positifs sont particulièrement préoccupants pour la relation client.

**Nombre réel d'erreurs :** à relever dans `python src\evaluate.py`.  
**Exemple d'un avis effectivement mal classé :** à copier depuis les sorties d'évaluation.  
**Classe réelle / prédite :** à compléter.

Une amélioration possible serait un modèle sensible à l'ordre et au contexte des mots. La priorité du TP2 reste toutefois la reproductibilité et la qualité de l'évaluation, non la recherche d'un modèle complexe.

## 5. L'interface et le seuil d'incertitude

Le TP2 fournit la fonction de prédiction réutilisée au TP3. Le seuil de vérification humaine et le nombre d'avis envoyés à un agent seront mesurés dans l'interface du TP3 ; ils ne sont pas établis par les résultats communiqués pour ce TP.

## 6. Ce qui a échoué

Juste après l'installation du kit, les tests ont affiché **`2 failed, 38 passed, 2 skipped`**. Les deux échecs concernaient l'absence de `models/metrics.json` et les deux tests ignorés signalaient l'absence de `models/sentiment.joblib`. C'était un état attendu avant entraînement. L'exécution de `python src\make_demo.py` a ensuite généré correctement les 290 avis. Après la suite du travail, les tests du TP2 ont atteint **42 réussites**.

## 7. Ce que nous ferions autrement

Nous enregistrerions systématiquement les métriques et les exemples d'erreurs dès chaque exécution, comparerions plusieurs jeux de données et suivrions particulièrement le rappel de la classe négative. Nous automatiserions également la conservation d'un jeu de test stable.

## 8. Répartition du travail

*Répartition proposée, à confirmer par les trois membres avant remise.*

| Membre | Ce qu'il a pris en charge |
| --- | --- |
| Ali Mouda | Installation du kit TP2, génération du jeu de démonstration et exécution des scripts d’entraînement. |
| Sara El Asmar | Préparation des données, analyse des métriques et interprétation de la matrice de confusion. |
| Chaimae Labzae | Vérification des tests automatisés, analyse des erreurs de prédiction et rédaction de la documentation du TP2. |

## Outils d'aide à la rédaction

ChatGPT a aidé à comprendre les erreurs de tests et à structurer ce compte rendu ; les métriques et exemples doivent être vérifiés sur les sorties du projet.
