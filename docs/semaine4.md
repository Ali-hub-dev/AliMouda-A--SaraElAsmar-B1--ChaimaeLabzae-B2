# Semaine 4 : tests approfondis et qualité, notes du binôme

## 1. Couverture

- **Avant (étape A) :** la première mesure disponible était de **91,89 %**, avec 6 instructions non couvertes sur 74. La mesure initiale exacte de l'étape A n'a pas été conservée. Les lignes non exécutées étaient `api/main.py` : 49, 75–77 et 83–85.
- **Pour chacune, le comportement qu'aucun test ne vérifiait :**
  - Ligne 49 : réponse HTTP 503 lorsque le modèle n'est pas chargé.
  - Lignes 75–77 : réponse HTTP 500 lorsqu'une exception survient pendant la prédiction.
  - Lignes 83–85 : lancement direct de l'application avec Uvicorn.
- **Après (étape D) :** couverture de **97,50 %** (78 instructions couvertes sur 80), supérieure à l'objectif de 95 %. Les deux instructions restantes concernent le lancement direct avec Uvicorn. Elles ne sont pas couvertes par les tests `TestClient`, mais n'ont pas été explicitement exclues de la mesure.

## 2. Défauts trouvés

| Symptôme | Test qui l'a révélé | Correction |
| --- | --- | --- |
| Les textes contenant uniquement des espaces n'étaient pas rejetés correctement. | `test_predict_texte_vide_422` | Ajout d'une validation Pydantic dans `api/schemas.py`. |
| Le comportement HTTP 503 sans modèle n'était pas vérifié. | `test_modele_non_charge` | Ajout de tests sur `/health` et `/predict`. |
| Les exceptions internes du modèle n'étaient pas couvertes. | `test_modele_en_panne` | Ajout de tests vérifiant la réponse HTTP 500. |
| Le modèle renvoyait une classe même avec une confiance faible. | Analyse de `courbe_seuil.py` et du jeu d'or | Ajout du seuil d'abstention de 0,60 et de `INDETERMINE`. |
| Quatre tests du jeu d'or devenaient `XPASS(strict)`. | `test_pas_d_erreur_franche` | Adaptation des tests pour distinguer les abstentions des erreurs franches. |
| Imports non conformes à la règle I001. | `ruff check .` | Réorganisation des imports dans `api/model.py`. |

## 3. Seuil d'abstention

- **Deux ou trois points de la courbe (`python src/courbe_seuil.py`) :**
  - Seuil 0,50 : 58 avis traités sur 58, exactitude de 87,9 %, 7 erreurs et aucune intervention humaine.
  - Seuil 0,60 : 42 avis traités, exactitude de 95,2 %, 2 erreurs et 16 avis envoyés à un humain.
  - Seuil 0,70 : 37 avis traités, exactitude de 100 %, aucune erreur parmi les avis traités et 21 avis envoyés à un humain.
- **Seuil retenu :** **0,60** ; **part des avis envoyés à un humain :** 16/58, soit **27,6 %** ; **justification :** ce seuil permet de réduire les erreurs de 7 à 2 tout en conservant 72,4 % des avis en traitement automatique sur le jeu de démonstration.

## 4. Jeu d'or

- **Bilan (`python src/bilan_jeu_or.py`) :** **2 justes, 11 abstentions, 8 erreurs franches déclarées**, sur 21 avis.
- **Ce que ces chiffres disent du modèle :** avant l'intégration du seuil, le modèle produisait 9 prédictions correctes et 12 erreurs franches. Après intégration, 4 erreurs franches sont évitées grâce à l'abstention. Cependant, seulement 2 des 10 avis traités automatiquement sont correctement classés. Le modèle présente donc encore des difficultés importantes sur les avis complexes, notamment les négations, les formulations ironiques et les avis mixtes.

## 5. Outils statiques

- **Remarques au départ :** Ruff avait signalé plusieurs problèmes de qualité, notamment des imports mal placés (`E402`), des variables ambiguës (`E741`), des règles concernant les exceptions (`B904`) et l'utilisation de `zip` (`B905`). Mypy ne signalait pas d'erreur dans l'API lors des vérifications disponibles.
- **Parmi les défauts de la partie 2, combien Ruff et Mypy avaient-ils signalés ? Qu'en concluez-vous ?** Parmi les six défauts présentés, **un défaut (l'ordre des imports) a été signalé par Ruff**, tandis qu'aucun n'a été signalé par Mypy. Les autres défauts ont été identifiés par les tests ou l'analyse du comportement du modèle. Nous concluons que l'analyse statique complète les tests fonctionnels, mais ne les remplace pas.

**Vérification finale :** 72 tests réussis, 8 échecs attendus, couverture de 97,50 %, Ruff validé, Mypy validé et hooks pre-commit validés.
