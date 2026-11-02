# Compte rendu TP3 : API et variante Streamlit

L'équipe indiquée dans les rapports existants est Ali Mouda, Sara El Asmar et Chaimae Labzae. Les ressources locales contiennent deux parcours TP3 : interface directe et API. Le projet final suit l'API, nécessaire aux TP4–TP6 ; les helpers et tests de l'interface initiale sont conservés.

FastAPI charge le modèle au démarrage, sert /health et /predict, refuse les entrées invalides et masque les erreurs internes. Les tests couvrent aussi le modèle absent, non chargé et en panne. La page Streamlit finale passe par HTTP ; voir docs/semaine5.md.

Le modèle de démonstration donne F1 macro 0,8790, exactitude 0,8793, rappel négatif 0,9310 ; matrice [[27, 2], [5, 24]]. Les sept erreurs incluent des retournements de sentiment mal compris. À 0,60, 16/58 avis partent vers un humain et les erreurs automatiques passent de sept à deux. L'entraînement Allociné a ensuite été vérifié séparément au TP2 : voir docs/metrics-allocine.json.

Les observations techniques et la validation figurent dans docs/semaine3.md et docs/ETAT-TP1-TP6.md. La répartition historique individuelle ne peut pas être reconstruite par les tests ; elle reste à attester par l'équipe.
