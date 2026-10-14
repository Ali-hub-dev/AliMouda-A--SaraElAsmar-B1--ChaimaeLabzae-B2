# Compte rendu du TP1 — Cadrage et environnement

**Équipe :** Ali Mouda, Sara El Asmar et Chaimae Labzae  
**Dépôt :** https://github.com/Ali-hub-dev/AliMouda-A--SaraElAsmar-B1--ChaimaeLabzae-B2  
**Date :** 14/10/2026  
**Module :** Développement et déploiement d’applications intelligentes

## 1. Le besoin et son cadrage

Une équipe de relation client reçoit de nombreux avis chaque jour et doit traiter rapidement les réclamations. Le projet vise à identifier les avis négatifs afin de les faire remonter en priorité. Le TP1 prépare un dépôt reproductible et justifie les choix techniques pour trois besoins métier.

Pour le **cas 3 (avis négatifs)**, nous avons retenu le **Machine Learning supervisé** : **(a)** les avis peuvent être associés à des étiquettes « positif » et « négatif » ; **(c)** une prédiction locale reste peu coûteuse pour un grand volume. Le critère **(d)** intervient aussi : une erreur peut retarder une réclamation, ce qui impose une évaluation attentive. Pour le cas 1 (ordonnances incomplètes), les règles métier sont privilégiées ; pour le cas 2 (règlement intérieur), le RAG permet de retrouver et citer les articles pertinents.

## 2. L'architecture du dépôt

| Élément | Rôle |
| --- | --- |
| `app/` | Composants applicatifs |
| `data/` | Exemples et données |
| `docs/` | Fiches de cadrage et comptes rendus |
| `models/` | Mesures et artefacts de modèle |
| `scripts/` | Installation et diagnostics |
| `tests/` | Tests automatisés |
| `ui/` | Interface à développer au TP3 |
| `.github/workflows/` | Intégration continue |

Le code et les documents sont versionnés. L'environnement `.venv/`, les données régénérables et le modèle binaire ne le sont pas. `models/metrics.json` est destiné à être versionné car il constitue une preuve des performances ; `models/sentiment.joblib` peut être reconstruit par entraînement et peut être volumineux. Cette distinction devient concrète au TP2.

## 3. Le modèle

Le TP1 ne réalise pas encore l'entraînement : il prépare les fichiers, l'environnement et les choix méthodologiques. Les métriques F1 macro, exactitude, rappel négatif et matrice de confusion sont donc **non applicables à ce TP seul**.

| Jeu | Avis | Vocabulaire | F1 macro | Rappel négatif |
| --- | ---: | ---: | ---: | ---: |
| Démonstration | Non entraîné au TP1 | — | — | — |
| Allociné | Non entraîné au TP1 | — | — | — |

## 4. L'analyse des erreurs

Le TP1 porte sur la fiabilité du dépôt plutôt que sur les erreurs de prédiction. Les erreurs du modèle et les exemples d'avis mal classés seront étudiés au TP2. Un exemple issu des propres données de l’équipe devra être ajouté au compte rendu du TP2.

## 5. L'interface et le seuil d'incertitude

L'interface Streamlit et son seuil d'incertitude relèvent du TP3. Aucun avis n'est envoyé à un agent à cette étape, car le système n'est pas encore entraîné ni lancé.

## 6. Ce qui a échoué

Les vérifications du TP1 portent notamment sur la structure des dossiers, la présence de `.gitignore`, l'environnement virtuel et les contributions Git. **À compléter avec les éventuels incidents réellement rencontrés pendant le TP1** : message exact, cause et correction. Les échanges disponibles ne confirment pas d'incident précis sur cette séance.

## 7. Ce que nous ferions autrement

Nous préparerions dès le départ une procédure d'installation courte, vérifierions la configuration Git des membres et documenterions les exclusions `.gitignore` avant le premier commit. Cela réduirait les écarts entre postes.

## 8. Répartition du travail

*Répartition proposée, à confirmer par les trois membres avant remise.*

| Membre | Ce qu'il a pris en charge |
| --- | --- |
| Ali Mouda | Création du projet `sentiment-app`, configuration de l’environnement Python, initialisation du dépôt Git et organisation des dossiers. |
| Sara El Asmar | Analyse du besoin métier, rédaction des fiches de cadrage et définition des objectifs du projet. |
| Chaimae Labzae | Préparation de la structure documentaire, vérification des fichiers de configuration et participation aux tests initiaux. |

## Outils d'aide à la rédaction

ChatGPT a servi à structurer et reformuler le compte rendu ; les éléments techniques et les contributions doivent être vérifiés par l’équipe avant remise.
