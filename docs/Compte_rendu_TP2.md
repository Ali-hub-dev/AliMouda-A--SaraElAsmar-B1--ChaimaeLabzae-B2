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

Les mesures vérifiées le 28/10/2026 concernent le modèle de démonstration présent : 232 avis d'entraînement et 58 de test, F1 macro 0,8790, exactitude 0,8793 et rappel négatif 0,9310. Aucune mesure Allociné conservée ne permet de confirmer cet entraînement ; ses résultats ne sont donc pas inventés.

Matrice de confusion (ordre négatif, positif) : [[27, 2], [5, 24]]. Sur 29 négatifs, 27 sont correctement reconnus et 2 manqués. Sur 29 positifs, 24 sont reconnus et 5 classés négatifs.

## 4. Analyse des erreurs

Sept erreurs sont observées. « Commande jamais reçue et remboursement en attente au début, sauf que ensuite je recommande… » est réellement positif et prédit négatif. Les avis mitigés révèlent la difficulté du sac de mots à comprendre quel sentiment conclut la phrase. Le détail reproductible figure dans docs/semaine2.md et python src/evaluate.py.

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


## Contrôle Allociné réalisé le 28/10/2026

Entraînement indépendant terminé sur 20 000 avis publics (10 204 négatifs) : 16 000 pour entraîner, 4 000 pour tester ; vocabulaire de 149 529 termes. F1 macro **0,9205**, exactitude **0,9205**, rappel négatif **0,9113**, au-dessus du seuil F1 de 0,85. Les mesures sont sauvegardées dans docs/metrics-allocine.json ; le modèle indépendant est models/sentiment-allocine.joblib (ignoré par Git). Le modèle de démonstration reste actif pour reproduire les contrôles et le jeu d'or du TP4. Ces mesures complètent la vérification antérieure limitée à la démonstration.
