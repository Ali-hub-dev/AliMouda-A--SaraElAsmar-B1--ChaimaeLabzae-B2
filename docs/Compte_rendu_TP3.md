# Compte rendu du TP3 — Interface Streamlit

**Équipe :** Ali Mouda, Sara El Asmar et Chaimae Labzae  
**Dépôt :** https://github.com/Ali-hub-dev/AliMouda-A--SaraElAsmar-B1--ChaimaeLabzae-B2  
**Date :** 14/10/2026  
**Module :** Développement et déploiement d’applications intelligentes

## 1. Le besoin et son cadrage

L'équipe relation client a besoin d'un outil accessible sans terminal pour repérer et prioriser les avis négatifs. Le TP3 met le modèle du TP2 à disposition dans une interface web Streamlit. Le Machine Learning supervisé reste l'approche du cas 3, motivée par **(a)** les données étiquetées et **(c)** le coût limité des prédictions ; le critère **(d)** justifie l'intervention humaine lorsque le modèle hésite.

## 2. L'architecture du dépôt

| Élément | Rôle |
| --- | --- |
| `ui/app.py` | Présentation de l'interface Streamlit |
| `ui/helpers.py` | Fonctions de chargement, classement et résumé |
| `src/predict.py` | Prédiction réutilisée depuis le TP2 |
| `tests/test_ui.py` | Tests automatisés de l'interface |
| `docs/semaine3.md` | Justification du seuil d'incertitude |
| `models/metrics.json` | Métriques conservées dans Git |
| `models/sentiment.joblib` | Modèle local non versionné |

La séparation entre `ui/app.py` et `ui/helpers.py` rend la logique testable sans démarrer le serveur. `models/metrics.json` est versionné pour garder la preuve des performances, alors que `models/sentiment.joblib` est reconstructible par entraînement et n'est pas poussé dans Git.

## 3. Le modèle

L'interface réutilise le modèle entraîné au TP2 : elle n'introduit pas un nouveau classificateur. Le jeu de démonstration comporte 290 avis (145 de chaque classe) ; le jeu Allociné prévu comporte 20 000 avis. Les métriques exactes de vos exécutions sont à recopier depuis `models/metrics.json` et les sorties d'évaluation.

| Jeu | Avis | Vocabulaire | F1 macro | Rappel négatif |
| --- | ---: | ---: | ---: | ---: |
| Démonstration | 290 | **À relever** | **À relever** | **À relever** |
| Allociné | 20 000 (jeu prévu) | **À relever** | **À relever** | **À relever** |

**Exactitude :** à relever pour chaque jeu.  
**Matrice de confusion :** à insérer depuis l'évaluation du TP2 ; commenter séparément les lignes « réel négatif » et « réel positif ».

## 4. L'analyse des erreurs

Les avis mitigés restent difficiles, notamment lorsque le sens de la phrase change après « mais ». La vectorisation en sac de mots ne représente pas directement cet ordre. Le TP3 vise donc à rendre l'incertitude visible plutôt qu'à masquer ces limites.

**Nombre d'erreurs :** à reporter depuis `python src\evaluate.py`.  
**Exemple réel mal classé :** à ajouter à partir de vos données, avec la classe réelle et la prédiction.  
**Amélioration possible :** un modèle tenant compte du contexte ; ce n'était pas l'objectif de la séance d'interface.

## 5. L'interface et le seuil d'incertitude

L'application Streamlit a été lancée avec succès. Elle comporte trois onglets : **Un avis**, **Un fichier CSV** et **Comment ça marche**. Le premier affiche la prédiction et sa confiance ; le deuxième permet d'analyser un lot, de visualiser sa répartition, de prioriser les négatifs et d'exporter les résultats.

Le seuil par défaut retenu est **0,60** : une confiance inférieure à 60 % entraîne le verdict **« À vérifier par un agent »**. C'est un compromis entre traitement automatique et prudence face aux prédictions incertaines.

**Nombre d'avis effectivement envoyés à un agent sur votre jeu de test :** **à mesurer** (le test manuel de l'onglet CSV a été passé). Ce chiffre ne doit pas être inventé.

## 6. Ce qui a échoué

L'installation du kit TP3 a été suivie de **45 tests réussis**. En revanche, la commande `python -m streamlit run ui\app.py` a échoué avec **`PackageNotFoundError: No package metadata was found for streamlit`**. La correction a consisté à installer Streamlit dans l'environnement virtuel avec `python -m pip install streamlit`. Après cela, l'interface s'est ouverte correctement. Les essais manuels détaillés des trois onglets n'ont pas été réalisés dans les échanges disponibles.

## 7. Ce que nous ferions autrement

Nous ajouterions des tests de bout en bout pour l'import CSV, mesurerions le nombre de vérifications humaines à plusieurs seuils et recueillerions les retours d'agents du service client. Nous prévoirions aussi un déploiement contrôlé et un suivi des prédictions après mise en service.

## 8. Répartition du travail

*Répartition proposée, à confirmer par les trois membres avant remise.*

| Membre | Ce qu'il a pris en charge |
| --- | --- |
| Ali Mouda | Installation du kit TP3, configuration de Streamlit et lancement de l’application. |
| Sara El Asmar | Conception fonctionnelle des trois onglets : avis individuel, fichier CSV et explication du modèle. |
| Chaimae Labzae | Intégration du seuil d’incertitude, vérification des tests automatisés et documentation de l’interface. |

## Outils d'aide à la rédaction

ChatGPT a servi au dépannage de l'installation Streamlit et à la rédaction structurée ; le fonctionnement de l'interface et les 45 tests ont été vérifiés sur le poste de développement.
