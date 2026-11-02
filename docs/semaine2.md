# Semaine 2 : entraînement et erreurs

Vérification du 28/10/2026 sur le modèle de démonstration : 232 avis pour entraîner, 58 pour tester, F1 macro 0,8790, exactitude 0,8793, rappel négatif 0,9310. Le pipeline est ajusté après séparation des données.

Matrice (vérité en ligne, prédiction en colonne ; négatif puis positif) : [[27, 2], [5, 24]]. Deux avis négatifs sont manqués et cinq positifs sont classés négatifs.

Les sept erreurs concernent des formulations mitigées. Par exemple, « Commande jamais reçue et remboursement en attente au début, sauf que ensuite je recommande… » est positif mais prédit négatif : TF-IDF ne représente pas correctement le retournement final. Le modèle de démonstration ne prouve pas une généralisation à Allociné ; aucune nouvelle mesure Allociné n'est revendiquée.


## Contrôle Allociné réalisé le 28/10/2026

Entraînement indépendant terminé sur 20 000 avis publics (10 204 négatifs) : 16 000 pour entraîner, 4 000 pour tester ; vocabulaire de 149 529 termes. F1 macro **0,9205**, exactitude **0,9205**, rappel négatif **0,9113**, au-dessus du seuil F1 de 0,85. Les mesures sont sauvegardées dans docs/metrics-allocine.json ; le modèle indépendant est models/sentiment-allocine.joblib (ignoré par Git). Le modèle de démonstration reste actif pour reproduire les contrôles et le jeu d'or du TP4. Ces mesures complètent la vérification antérieure limitée à la démonstration.
