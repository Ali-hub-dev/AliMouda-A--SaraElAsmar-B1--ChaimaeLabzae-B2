import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path

from journal_monome import adapter

r = Path.cwd()
source = Path(r"C:\Users\HP\Downloads\journal-tp1-tp6 v-26-10-2026 (1).md")
original = source.read_text(encoding="utf-8-sig")
main, annexes = original.split("## Annexe A", 1)
root = ET.parse(r / "docs/resultats-tests.xml").getroot()
tests = root.findall(".//testcase")


def counts(*modules):
    selected = [t for t in tests if t.attrib["classname"] in ["tests." + m for m in modules]]
    x = sum(t.find("skipped") is not None for t in selected)
    return f"{len(selected) - x} passed" + (f", {x} xfailed" if x else "")


full = "99 passed, 8 xfailed ; 0 failed ; aucun test ignoré hors xfail déclarés"
d = {}


def entry(key, obt, comment, ok=False):
    d[key] = (obt, comment, ok)


entry(
    "Poste du membre A",
    "Python du venv : 3.11.5\ngit version 2.53.0.windows.2\ngit config --global user.name : Ali Mouda\npy -0 : No installed Pythons found!",
    "Python 3.11 fonctionne dans .venv, mais le lanceur py ne détecte pas d'installation. Nous utilisons donc .\\.venv\\Scripts\\python.exe ; le contrôle du lanceur py n'est pas entièrement conforme.",
)
entry(
    "Poste du membre B",
    "Non vérifié sur le poste du membre B.",
    "Le dépôt identifie Sara El Asmar comme membre B, compte @SE909. Les versions et la configuration de son poste doivent être relevées sur sa machine ; celles du poste A ne constituent pas une preuve pour B.",
)
entry(
    "T0",
    "Dossiers présents : app, data, docs, models, scripts, tests, ui, .github.\nFichier .gitignore présent.",
    "La structure initiale demandée est présente. Les dossiers api et sentiment_app complètent cette structure après les TP3 et TP6.",
    True,
)
entry(
    "T1",
    "État initial non conservé.\nContrôle final : Python 3.11.5 ; diagnostic 0 erreur(s), 0 avertissement(s).\n"
    + full,
    "Le résultat initial 3 failed, 31 passed, 4 skipped est celui annoncé par le kit, pas une sortie conservée de notre séance. Les trois échecs réclament les fiches remplies ; les quatre tests ignorés attendent le dépôt Git. Le dépôt étant maintenant complété, nous ne recréons pas artificiellement cet état rouge.",
)
entry(
    "T2",
    counts("test_cadrage") + " (rapport final)\n" + full,
    "Pharmacie : règles métier, car (a) les champs sont connus sans corpus annoté et (d) l'erreur peut toucher la santé. Règlement : RAG, car (a) les documents existent sans questions annotées et (b) les réponses doivent être vérifiables. Avis négatifs : apprentissage supervisé, pour (a) les avis étiquetés et (c) le faible coût par requête. Les nombres globaux dépassent ceux du TP1 car tous les kits sont désormais intégrés.",
    True,
)
entry(
    "T3",
    "Dépôt Git local existant ; origin configuré :\nhttps://github.com/Ali-hub-dev/AliMouda-A--SaraElAsmar-B1--ChaimaeLabzae-B2\nTest de non-suivi de .env et .venv : réussi.\nPremier push et état intermédiaire 37 passed, 1 failed : non conservés.",
    "Le dernier échec décrit dans le kit vérifie qu'au moins deux auteurs ont contribué. L'historique local actuel satisfait ce contrôle ; le premier push et l'affichage GitHub ne sont pas prouvés par cette vérification locale.",
)
entry(
    "T4",
    "Diagnostic sur le poste B non fourni.",
    "Le diagnostic du poste A est sans erreur, mais ne remplace pas une installation indépendante. Le membre B doit exécuter les commandes sur son propre poste.",
)
entry(
    "T5",
    "git shortlog -sn --all :\n4 Ali Mouda\n2 Ali\n2 Sara El Asmar\n" + counts("test_git_history"),
    "Deux noms de membres distincts sont présents dans l'historique local. L'identité « Ali » peut être une variante de « Ali Mouda » ; elle ne doit pas être comptée comme une personne supplémentaire. Aucun commit n'a été créé au nom d'un autre membre.",
    True,
)
entry(
    "T6",
    "Diagnostic : 0 erreur(s), 0 avertissement(s).\n"
    + full
    + "\nCI distante : non vérifiée pour les modifications actuelles.",
    "Les contrôles locaux sont conformes ; les tests TP2 à TP6 expliquent l'écart avec les 38 tests initiaux. La case globale reste ouverte car la CI GitHub ne peut pas être déclarée verte avant le push et sa vérification.",
)
entry(
    "T7",
    "Clone Git frais : non effectué.\nInstallation indépendante de la roue : réussie, voir T40.",
    "Un clone frais prouve que les seuls fichiers versionnés suffisent à reconstruire le projet. T6 peut réussir grâce à des fichiers locaux ignorés ; le contrôle de la roue T40 est distinct et ne remplace pas ce clone.",
)
entry(
    "C1",
    "Kit TP2 déjà installé lors de la reprise.\n"
    + counts("test_model")
    + " pour les tests du modèle (rapport final).\nSortie intermédiaire initiale : non conservée.",
    "Les deux échecs du kit réclament les métriques ; les tests qui nécessitent le modèle sont ignorés tant que le .joblib n'a pas été produit. Les scripts et artefacts requis existent désormais.",
)
entry(
    "C2",
    "290 avis de démonstration : 145 positifs et 145 négatifs.\n100 avis mitigés et 30 neutres.",
    "Exemple affiché par l'évaluation : « Commande jamais reçue et remboursement en attente au début, sauf que ensuite je recommande… ». Deux segments de polarités opposées sont reliés par un retournement ; l'étiquette suit le second segment.",
    True,
)
entry(
    "C3",
    "Démonstration : 232 avis entraînement ; 58 avis test.\nF1 macro : 0.8790 ; exactitude : 0.8793 ; rappel négatif : 0.9310.\nmodels/metrics.json versionnable ; modèle et CSV de démonstration ignorés.",
    "Les métriques sont petites et permettent de comparer les entraînements dans Git. Le binaire est régénérable et suit son propre cycle de vie ; le pipeline est ajusté après la séparation entraînement/test pour éviter une fuite de données.",
    True,
)
entry(
    "C4",
    "Matrice (vérité en ligne ; négatif puis positif en colonne) :\nnegative  27  2\npositive   5 24\n7 erreurs sur 58 avis.\nExemples abrégés affichés :\npositive -> negative : Taille trop petite et retour payant au déballage, sauf que ensuite produit conforme…\npositive -> negative : Commande jamais reçue et remboursement en attente au début, sauf que ensuite je recommande…\nnegative -> positive : Service impeccable et livraison en avance sur le papier, sauf que ensuite produit cassé…",
    "Deux négatifs sont manqués et cinq positifs sont classés négatifs. TF-IDF avec bigrammes capte des termes locaux mais représente mal le changement de polarité et la conclusion d'une longue phrase mitigée.",
    True,
)
entry(
    "C5",
    "Allociné : 20 000 avis, dont 10 204 négatifs.\n16 000 avis entraînement ; 4 000 test ; vocabulaire 149 529 termes.\nF1 macro 0.9205 ; exactitude 0.9205 ; rappel négatif 0.9113.\n"
    + counts("test_model")
    + " ; "
    + full
    + "\nPush et CI actuels : non réalisés/non vérifiés.",
    "Allociné apporte davantage d'exemples et une distribution différente de la démonstration, ce qui peut expliquer son meilleur F1 ; cette comparaison ne permet pas d'isoler une cause unique. Le modèle est sauvegardé séparément dans models/sentiment-allocine.joblib et les mesures dans docs/metrics-allocine.json. Le modèle démo reste actif pour reproduire le TP4.",
)
entry(
    "T14",
    counts("test_api") + " (API) ; " + full + "\nKit API présent ; modèle de démonstration chargé.",
    "La démonstration rétablit le même modèle que la CI et les exemples du cours. Les 48 tests correspondent au kit TP3 seul ; notre suite contient aussi la variante Streamlit historique et les TP4–TP6.",
    True,
)
entry(
    "T15",
    '200\n{"status":"OK","model":"tfidf-logreg (TP2, models/sentiment.joblib)"}',
    "Réponse vérifiée par les tests API et par une véritable requête /health au service lancé depuis la roue indépendante. Aucun clic Swagger ni capture de /docs n'est revendiqué.",
    True,
)
entry(
    "T16",
    "200 ; POSITIVE ; score 0.777",
    "Le score est renvoyé par le modèle chargé. L'API ajoute le contrat de sortie ; le seuil de 0,60 conserve ici la décision positive.",
    True,
)
entry(
    "T17",
    "200 ; NEGATIVE (test API final réussi).",
    "Le test test_predict_negatif confirme la classe négative. Le score précis est consigné dans les preuves API lorsqu'une nouvelle requête est exécutée ; il n'est pas recopié depuis l'attendu sans mesure.",
    True,
)
entry(
    "T18",
    "Texte vide : 422.\nChamp absent : 422.\ntext=42 : 422.\nForme de detail : liste d’erreurs avec loc, msg, type.",
    "Pydantic identifie respectivement une longueur insuffisante, un champ manquant et un type invalide. Le code 422 signale une entrée non conforme ; 500 est réservé à une panne interne, pas à une erreur de saisie.",
    True,
)
entry(
    "T19",
    "Fichier CI présent ; entraînement démo avant tests.\nDernière CI distante : non consultée pour cette reprise.",
    "Le modèle .joblib n'est pas versionné : le runner doit donc le produire avant de tester l'API. Une suite verte en local ne constitue pas une preuve du résultat GitHub Actions.",
)
entry(
    "T20",
    "test_modele_absent : réussi.\nFileNotFoundError au démarrage avec un chemin inexistant.\nRoue sans SENTIMENT_MODELE : code 1 et message « Modèle introuvable … SENTIMENT_MODELE ».",
    "Le lifespan charge le modèle avant de servir des requêtes. Le test redirige temporairement son chemin et vide le cache, sans renommer ni supprimer le modèle utilisé par le reste du projet. Le message a été enrichi au TP6.",
    True,
)
entry(
    "T21",
    "Mesure antérieure conservée dans docs/semaine4.md : 91,89 %.\nÉtat initial exact du kit et nombre de remarques Ruff : non conservés.\nMesure finale : 97,59 % ; Ruff et Mypy passent.",
    "Les anciennes lignes manquantes correspondaient au 503 sans modèle, aux erreurs 500 et au lancement direct Uvicorn. La mesure 91,89 % est reprise du rapport existant ; elle n'a pas été recréée en annulant les corrections.",
)
entry(
    "T22",
    [
        "Sortie avant correction et contre-exemple Hypothesis : non conservés.",
        "Après correction : 422 ; detail est une liste avec loc, msg et type.",
    ],
    "Le validateur Pydantic utilise str.strip(), comme la fonction de prédiction. La forme uniforme permet au client de traiter tous les refus de validation de la même manière. Aucun caractère trouvé historiquement par Hypothesis n'est affirmé sans trace ; la propriété actuelle couvre notamment les blancs Unicode.",
    True,
)
entry(
    "T23",
    "10 passed, trois exécutions réussies (suite complète puis deux exécutions ciblées).",
    "Huit cas paramétrés couvrent les frontières ; deux propriétés explorent les textes valides et les textes blancs. Le rapport final conserve 100 exemples générés pour chaque propriété.",
    True,
)
entry(
    "T24",
    "seuil  répond  exactitude  erreurs  vers humain\n0.50     58      0.879         7       0\n0.60     42      0.952         2      16\n0.70     37      1.000         0      21\nTexte inventé : INDETERMINE ; score 0.5162.",
    "Seuil retenu : 0,60. Il transfère 16/58 avis à un humain (27,6 %) et évite cinq des sept erreurs automatiques. Ce compromis est mesuré sur la démonstration et ne garantit pas la même qualité sur un autre domaine.",
    True,
)
entry(
    "T25",
    "Bilan sur 21 avis : 2 justes, 11 abstentions, 8 erreurs franches déclarées.\n"
    + counts("test_jeu_or"),
    "Le jeu comporte plus que le minimum de 20 avis. Les abstentions expriment une faible confiance ; les huit xfail conservent les erreurs connues au lieu de retirer les avis difficiles. La faiblesse du modèle sur ce jeu reste visible.",
    True,
)
entry(
    "T26",
    counts("test_integration")
    + "\nRequired test coverage of 95% reached. Total coverage: 97.59%\nAPI : 83 instructions, 2 non couvertes (lancement direct Uvicorn).",
    "RuntimeError et ValueError internes donnent 500 sans divulguer le message de panne. Le schéma garantit déjà la validité de l'entrée, donc convertir toute ValueError en 422 cacherait un défaut du serveur. Les classes inconnues, le modèle absent et les 503 sont aussi testés ; aucune exclusion de couverture ajoutée.",
    True,
)
entry(
    "T27",
    "Ruff : All checks passed!\nMypy : Success: no issues found in 4 source files\n"
    + full
    + "\nHooks Ruff et Mypy : Passed.\nSonde volontaire : F401, hook Ruff refusé.\nCI distante : non vérifiée.",
    "Le rapport précédent identifie l'ordre des imports comme le défaut signalé statiquement ; le décompte initial exact n'a pas été conservé. Les erreurs de comportement ont été détectées par les tests. Le refus a été vérifié par pre-commit sur un fichier temporaire, sans créer de faux commit ; la preuve est dans validation-hook.txt.",
)
entry(
    "T28",
    counts("test_client", "test_interface") + " pour les 12 tests TP5.\n" + full,
    "Les sept tests du client vérifient les échanges et la traduction des réponses HTTP. Les cinq tests AppTest vérifient le rendu et les interactions de la page. ui/app.py utilise désormais l'API et ne charge plus directement le modèle.",
    True,
)
entry(
    "T29",
    "AppTest : « API prête : tfidf-logreg (TP2, models/sentiment.joblib) ».\nTest de page réussi ; ouverture manuelle sur localhost:8501 non capturée.",
    "La page a été exécutée par l'outil de test Streamlit avec une API en mémoire. C'est une vérification automatisée du rendu ; elle ne constitue pas une capture d'un navigateur ouvert manuellement.",
    True,
)
entry(
    "T30",
    "Avis positif : score API 0.777, affichage arrondi 78 %.\nAvis négatif : classe NEGATIVE confirmée par le test API.",
    "Les pourcentages proviennent des probabilités de la classe prédite par le pipeline. La page les formate en pourcentages entiers ; ils ne mesurent pas une garantie de justesse sur un nouvel avis.",
    True,
)
entry(
    "T31",
    "Je ne sais pas : à faire vérifier par un humain\nScore 0.5162, affiché 52 % ; message sur le seuil d’abstention.",
    "Les mots inventés ne fournissent presque aucun signal du vocabulaire appris. Le score est inférieur à 0,60 : une intervention humaine est préférable à une décision tranchée et trompeuse.",
    True,
)
entry(
    "T32",
    "Espaces : 422 ; page = avertissement « Texte refusé ».\nConnexion refusée : « API injoignable : lancez d’abord uvicorn api.main:app ».",
    "Le premier cas est un refus de validation renvoyé par l'API. Le second est une erreur de transport : aucun code HTTP n'est reçu. Les tests du client et AppTest couvrent ces deux situations.",
    True,
)
entry(
    "T33",
    "6 avis ; résumé {'INDETERMINE': 1, 'NEGATIVE': 2, 'POSITIVE': 3}.\nBouton CSV implémenté ; téléchargement manuel non capturé.",
    "L'avis « xqzvb wlkptr grombu » est le seul envoyé vers un humain : 1/6, soit 16,7 %. Le lot a été mesuré avec le modèle actif. Le clic d'import et le fichier téléchargé depuis un navigateur restent à documenter.",
)
entry(
    "T34",
    "docs/semaine5.md complété.\n12 tests TP5 réussis localement.\nPush/CI actuels : non effectués/non vérifiés.",
    "La CI installe Streamlit et exécute la suite. La réussite locale est établie ; la case complète reste ouverte tant que l'exécution distante et sa capture ne sont pas disponibles.",
)
entry(
    "T35",
    "Kit TP6 installé depuis la nouvelle archive.\nÉtat rouge intermédiaire : non conservé.\n"
    + counts("test_packaging")
    + " au contrôle final.",
    "Les deux échecs attendus du kit réclament un chemin de modèle configurable et la suppression de sys.path dans l'API. Ces deux points sont maintenant corrigés ; l'état intermédiaire n'est pas présenté comme une sortie réellement enregistrée.",
)
entry(
    "T36",
    counts("test_packaging")
    + " au contrôle final.\nsrc/predict.py : wrapper de compatibilité vers sentiment_app.predict.",
    "La prédiction vit dans le paquet. Le wrapper maintient les anciens imports et scripts, et référence le même module pour que les tests modifiant MODELE touchent bien le module utilisé par l'API. L'échec intermédiaire unique n'a pas été conservé.",
    True,
)
entry(
    "T37",
    full
    + "\nRecherche sys.path dans api/*.py : aucune occurrence.\nRuff : All checks passed!\nMypy : Success: no issues found in 4 source files",
    "api/model.py importe directement sentiment_app.predict. Les types précis et la table de correspondance limitent les étiquettes aux valeurs du contrat, avec vérification des classes au démarrage.",
    True,
)
entry(
    "T38",
    'sentiment-app 0.6.0\nPOSITIVE : 0.777\nINDETERMINE : 0.5162\n/health : {"status":"OK","model":"tfidf-logreg (TP2, models/sentiment.joblib)"}',
    "La commande predict utilise le même adaptateur api.model que le serveur ; elle applique donc le même seuil. Le service a été lancé et interrogé hors du dépôt depuis l'environnement indépendant.",
    True,
)
entry(
    "T39",
    "Successfully built sentiment_app-0.6.0-py3-none-any.whl\n17 entrées : api, sentiment_app, ui et métadonnées.\nNi tests, ni data, ni models, ni src, ni fichier .joblib.",
    "La roue distribue le code utile à l'exécution. Les tests restent dans le dépôt ; données et modèle ont un cycle de vie séparé. La construction finale utilise --no-isolation avec les outils déjà installés.",
    True,
)
entry(
    "T40",
    "Sans SENTIMENT_MODELE : code 1, « Modèle introuvable … SENTIMENT_MODELE ».\nAvec le chemin absolu du modèle : POSITIVE, score 0.777.\nImport : wheel-validation/Lib/site-packages/sentiment_app/__init__.py.\nService indépendant : /health = OK.",
    "La roue a été installée dans un venv neuf, en dehors du dépôt ; pip a installé ses dépendances déclarées. Il a seulement fallu fournir le modèle par son chemin. scikit-learn est limité à la série 1.5 pour rester compatible avec l'entraînement.",
    True,
)
entry(
    "T41",
    "Version du paquet : 0.6.0 ; CHANGELOG.md complété.\nCommit final, étiquette v0.6.0, push et CI distante : non réalisés.",
    "Les livrables sont présents localement. La publication nécessite le commit, le tag et les deux push, puis la vérification de GitHub Actions ; aucune étiquette visible sur GitHub n'est revendiquée.",
)
evidence = json.loads((r / "docs/preuves-journal.json").read_text(encoding="utf-8"))
old = d["C3"]
d["C3"] = (f"Vocabulaire : {evidence['vocabulaire_demo']} termes.\n" + old[0], old[1], old[2])
entry(
    "T17",
    json.dumps(evidence["negatif"], ensure_ascii=False, indent=2),
    "Réponse mesurée avec TestClient sur le modèle actif. La classe est NEGATIVE et la confiance dépasse le seuil de 0,60.",
    True,
)
entry(
    "T18",
    "\n".join(
        k + " : " + json.dumps(evidence[k], ensure_ascii=False)
        for k in ("vide", "absent", "entier")
    ),
    d["T18"][1],
    True,
)
old = d["T22"]
d["T22"] = (
    [old[0][0], json.dumps(evidence["espaces"], ensure_ascii=False, indent=2)],
    old[1],
    old[2],
)
entry(
    "T30",
    f"Avis positif : {evidence['positif']['body']['score']}, affichage 78 %.\nAvis négatif : {evidence['negatif']['body']['score']}, affichage 75 %.",
    d["T30"][1],
    True,
)

# Fill every control without altering the teaching annexes or executing their instructions.
parts = re.split(r"(?=^### |^## Les difficult)", main, flags=re.M)
for i, section in enumerate(parts):
    if not section.startswith("### "):
        continue
    heading = section.splitlines()[0][4:]
    if heading.startswith("Membre B, après le TP"):
        tp = re.search(r"TP(\d)", heading).group(1)
        item = (
            "Contrôle indépendant du poste B non fourni.",
            "Les résultats locaux du poste A ne doivent pas être recopiés comme preuve du poste B. Sara doit rejouer les commandes sur sa machine et joindre sa propre capture.",
            False,
        )
    else:
        key = heading if heading.startswith("Poste ") else heading.split(" · ")[0]
        if key not in d:
            raise ValueError(heading)
        item = d[key]
    obtained, comment, ok = item
    values = obtained if isinstance(obtained, list) else [obtained]
    counter = [0]

    def fill_obt(m, values=values, counter=counter):
        idx = counter[0]
        counter[0] += 1
        return "```\n" + values[min(idx, len(values) - 1)] + "\n```"

    section = re.sub(r"```\nÀ compléter\n```", fill_obt, section)
    section = section.replace("> À compléter.", "> " + comment)
    if ok:
        section = section.replace("- [ ] Conforme", "- [x] Conforme")
    parts[i] = section
main = "".join(parts)
main = (
    main.replace("| Nom | *à compléter* | *à compléter* |", "| Nom | Ali Mouda | Sara El Asmar |")
    .replace(
        "| Compte GitHub | *à compléter* | *à compléter* |",
        "| Compte GitHub | @Ali-hub-dev | @SE909 |",
    )
    .replace(
        "*adresse du dépôt GitHub, à compléter*",
        "https://github.com/Ali-hub-dev/AliMouda-A--SaraElAsmar-B1--ChaimaeLabzae-B2",
    )
)
notice = """\n**Mise à jour : 28/10/2026 — résultats locaux vérifiés.**\n\nCe journal est rempli à partir des exécutions et rapports conservés. Les états initiaux non enregistrés, le poste B, le clone frais, les captures et la CI distante sont signalés explicitement ; les sorties attendues du modèle pédagogique ne sont pas présentées comme des mesures. Les nombres finaux diffèrent des états intermédiaires puisque les six TP sont intégrés. Une case cochée confirme le comportement local décrit, sans attester une capture ou un clic manuel non réalisé.\n\nLes rapports existants mentionnent aussi **Chaimae Labzae** comme troisième membre de l'équipe ; le tableau A/B du canevas reprend les rôles du README. La répartition individuelle reste à faire confirmer par les membres.\n"""
main = main.replace("## Comment remplir ce journal", notice + "\n## Comment remplir ce journal", 1)
# Use explicit missing-capture entries instead of broken image links or fabricated screenshots.
missing = []


def capture(m):
    label, path = m.groups()
    missing.append((label, path))
    return f"**Capture non fournie — {label}** : `{path}`."


main = re.sub(r"!\[([^\]]*)\]\((captures/[^)]+)\)", capture, main)
start = main.index("## Les difficultés rencontrées")
end = main.index("## La répartition du travail", start)
main = (
    main[:start]
    + """## Les difficultés rencontrées

| TP | Commande / contrôle | Message ou symptôme | Cause | Solution |
| --- | --- | --- | --- | --- |
| TP1 | py -0 | No installed Pythons found! | Le lanceur ne détecte pas Python, mais le venv fonctionne. | Utiliser .venv/Scripts/python.exe (3.11.5). |
| TP4 | Audit des tests | Seulement deux frontières, propriétés absentes | Fichier du kit resté partiellement complété. | Huit frontières, deux propriétés Hypothesis et forme standard des 422. |
| TP4 | Audit du modèle | .upper() et retour dict non précis ; classes inconnues non rejetées | Contrat d'étiquettes insuffisamment explicite. | TypedDict/Literal, table de correspondance et validation au démarrage. |
| TP5 | Audit ui/app.py | Ancienne interface chargée directement sur le modèle | Le kit n'écrase pas les fichiers existants. | Intégrer la page cliente HTTP, conserver les helpers historiques. |
| TP6 | pip install -e . dans le sandbox | WinError 5, accès refusé sur les métadonnées temporaires | Restriction d'écriture de l'environnement d'exécution. | Réexécuter avec autorisation hors sandbox ; installation réussie. |
| TP4 | pre-commit install dans le sandbox | OperationalError: attempt to write a readonly database | Cache pre-commit protégé. | Réexécuter avec autorisation ; hooks installés et validés. |
| TP4 | Jeu d'or | 8 erreurs franches sur 21 avis | Limites du modèle sur négation, ironie et formulations inconnues. | Conserver et déclarer les erreurs ; 11 abstentions, sans prétendre corriger le modèle. |

"""
    + main[end:]
)
start = main.index("## La répartition du travail")
end = main.index("## Le bilan", start)
main = (
    main[:start]
    + """## La répartition du travail

Les rôles A/B du README sont Ali Mouda et Sara El Asmar. Les contributions historiques détaillées ci-dessous ne sont pas attestées par les traces techniques ; l'équipe doit les confirmer. La reprise technique du 28/10/2026 a été réalisée avec l'assistance de Codex, sans attribuer artificiellement ces actions à un membre.

| TP | Travaux présents ou complétés | Attribution individuelle |
| --- | --- | --- |
| TP1 | Fiches et structure déjà présentes ; vérification de l'environnement et des auteurs ; lock généré. | Création/cadrage A et installation B indiqués dans le README ; détail à confirmer. |
| TP2 | Scripts existants ; évaluation démo et entraînement Allociné séparé vérifiés ; rapport complété. | Non déductible des seules sorties de commandes. |
| TP3 | API et helpers historiques présents ; tests et notes vérifiés. | Non déductible des seules sorties de commandes. |
| TP4 | Frontières/propriétés, typage et classes inconnues complétés ; qualité et couverture validées. | Compléments lors de la reprise assistée ; rôles humains à confirmer. |
| TP5 | Intégration du client HTTP et de la page ; douze tests et résultats du lot vérifiés. | Compléments lors de la reprise assistée ; rôles humains à confirmer. |
| TP6 | Paquet/CLI, roue, environnement indépendant et documentation complétés. | Compléments lors de la reprise assistée ; rôles humains à confirmer. |

"""
    + main[end:]
)
bilan = {
    1: "Le cadrage, la structure, l'environnement et l'historique sont vérifiés. Le lanceur py, le second poste, le clone frais et les captures restent à documenter.",
    2: "Le F1 macro est de 0,8790 sur la démonstration et de 0,9205 sur Allociné. Les deux modèles sont séparés ; les sept erreurs démo révèlent les limites des retournements de sentiment.",
    3: "L'API charge le modèle au démarrage, applique les contrats et distingue refus de validation et pannes. Les anciennes fonctions Streamlit restent testées ; le parcours final passe par l'API.",
    4: "Les tests aux frontières, les propriétés et les pannes sont couverts. La couverture atteint 97,59 %, Ruff/Mypy passent ; huit erreurs du jeu d'or restent explicitement déclarées.",
    5: "Le client et la page passent leurs douze tests. Un avis sur les six du fichier exemple reçoit une abstention ; le téléchargement manuel et les captures restent à joindre.",
    6: "La roue 0.6.0 fonctionne hors du dépôt avec SENTIMENT_MODELE et installe ses dépendances. Le commit final, le tag, le push et la CI distante restent les étapes de publication.",
}
for tp, text in bilan.items():
    main = main.replace(f"**TP{tp}** :\n\n> À compléter.", f"**TP{tp}** :\n\n> {text}")
assert "À compléter" not in main
(r / "docs/captures").mkdir(exist_ok=True)
(r / "docs/captures/LISEZ-MOI.md").write_text(
    "# Captures restant à joindre\n\nAucune capture historique n’a été fabriquée. Les résultats textuels sont dans le journal et les rapports associés.\n\n"
    + "\n".join(f"- `{path.split('/', 1)[1]}` — {label}" for label, path in missing)
    + "\n",
    encoding="utf-8",
)
(r / "docs/journal-tp1-tp6.md").write_text(main + "## Annexe A" + annexes, encoding="utf-8")
print(
    f"Journal rempli : {len(d)} blocs spécifiques ; {len(missing)} captures signalées comme non fournies. Annexes conservées sans modification."
)



adapter(r)

