# État vérifié TP1–TP6 — 28/10/2026

## Point de reprise

Le dépôt actif est sentiment-app. L'historique s'arrêtait au commit TP4 (0ce182e). TP1–TP3 étaient largement réalisés, mais certains comptes rendus étaient des canevas ; TP4 manquait les huit frontières, les deux propriétés Hypothesis, les types précis et le rejet des classes inconnues. TP5 n'était pas intégré. TP6 était dans le nouveau fichier ressources-etudiants (1).zip, pas dans le dossier ressources déjà extrait.

L'inventaire docs/audit-fichiers.json liste les fichiers du projet et les ressources pédagogiques ainsi que les membres des archives, avec tailles et empreintes. Les environnements, caches et sorties générées sont exclus de cet inventaire.

## Résultats par TP

| TP | Livrables et vérification locale |
| --- | --- |
| TP1 | Trois fiches remplies ; historique avec plusieurs auteurs ; diagnostic : 0 erreur, 0 avertissement ; requirements.lock généré. |
| TP2 | Démonstration : 232/58 avis, F1 0,8790. Allociné : 16 000/4 000 avis, F1 0,9205, rappel négatif 0,9113 ; modèle séparé et métriques dans docs/metrics-allocine.json. |
| TP3 | API, contrats, santé et prédiction validés ; anciens helpers Streamlit et leurs tests conservés ; les deux variantes du cours sont expliquées dans docs/semaine3.md. |
| TP4 | Huit frontières HTTP et forme des erreurs ; deux propriétés Hypothesis, trois exécutions réussies ; pannes et classes inconnues testées ; typage, abstention, jeu d'or conservé. Ruff/Mypy et hooks passent ; un fichier temporaire invalide est refusé par le hook (preuve : validation-hook.txt). |
| TP5 | Client HTTP, page Streamlit, prédiction individuelle, abstention, erreurs, lot et export ; 12 tests du kit passent. Fichier d'exemple : 3 positifs, 2 négatifs, 1 abstention sur 6. |
| TP6 | Paquet 0.6.0, commande sentiment, modèle configurable, compatibilité des anciens imports ; roue construite sans tests/données/modèle ; installation indépendante dans ../wheel-validation, prédictions POSITIVE et INDETERMINE, erreur explicite sans modèle et véritable API /health=OK hors du dépôt. Preuve : docs/validation-roue.json. |

Suite complète : **99 passed, 8 xfailed, aucun failed ni skipped**, couverture API **97,59 %**, objectif 95 % atteint. Les huit xfail sont les erreurs connues existantes sur le jeu d'or, autorisées par l'énoncé ; elles ne signifient pas que le modèle classe correctement ces avis. Bilan du jeu d'or : 2 justes, 11 abstentions, 8 erreurs franches déclarées sur 21 avis.

Un avertissement de dépréciation Starlette/AnyIO apparaît sans échec de test. Les deux instructions non couvertes correspondent au lancement direct d'Uvicorn ; aucune exclusion de couverture n'a été ajoutée.

## Rejouer les contrôles (PowerShell, depuis sentiment-app)

```powershell
.\.venv\Scripts\python.exe scripts/check_setup.py
.\.venv\Scripts\python.exe -m pytest -q --cov=api --cov-report=term-missing --cov-fail-under=95
.\.venv\Scripts\python.exe -m ruff check .
.\.venv\Scripts\python.exe -m mypy api
.\.venv\Scripts\sentiment.exe --version
.\.venv\Scripts\sentiment.exe serve
# Dans un deuxième terminal :
.\.venv\Scripts\sentiment.exe ui
```

Le modèle actif reste celui de démonstration pour correspondre à la CI et au TP4. Le modèle Allociné est disponible séparément : définir SENTIMENT_MODELE avec le chemin absolu models/sentiment-allocine.joblib, puis redémarrer l'API. Les résultats du jeu d'or peuvent différer avec ce modèle.

## Remise sur GitHub

La CI locale a été complétée avec Ruff, Mypy, couverture minimale et installation de la roue hors du dépôt. Les modifications restent locales, sans commit ni push ; aucune CI distante verte ni étiquette publiée n'est revendiquée. La création du commit final, l'étiquette v0.6.0 et leur push restent les étapes de remise. Les contributions individuelles historiques doivent être attestées par les membres, pas déduites des tests.
