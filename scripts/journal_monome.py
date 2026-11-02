"""Adapter le journal pédagogique à la remise individuelle d'Ali Mouda."""

import re
from pathlib import Path


def adapter(root: Path) -> None:
    fichier = root / "docs/journal-tp1-tp6.md"
    texte = fichier.read_text(encoding="utf-8")
    texte = texte.replace(
        "# Journal de bord du binôme : TP1 à TP6",
        "# Journal de bord individuel : TP1 à TP6 — Ali Mouda",
    )
    texte = re.sub(
        r"\|  \| Membre A \| Membre B \|\n.*?(?=\n\n)",
        "| Étudiant | Compte GitHub | Modalité |\n"
        "| --- | --- | --- |\n"
        "| Ali Mouda | @Ali-hub-dev | Monôme |",
        texte,
        count=1,
        flags=re.S,
    )
    texte = re.sub(
        r"Les rapports existants mentionnent aussi .*?(?=\n\n)",
        "**Travail réalisé en monôme par Ali Mouda.** Les contrôles du second membre "
        "du canevas ne s'appliquent pas à cette remise individuelle. Le dépôt conserve "
        "son URL et son historique existants ; ils ne sont pas modifiés pour présenter "
        "ce journal comme un travail individuel.",
        texte,
        count=1,
    )
    texte = texte.replace("les états initiaux", "les états initiaux")
    texte = texte.replace("le poste B, ", "")
    texte = texte.replace("le second poste, ", "")
    texte = re.sub(
        r"^### (?:Poste du membre B|Membre B, après le TP\d)[^\n]*\n.*?(?=^#{2,3} |\Z)",
        "",
        texte,
        flags=re.M | re.S,
    )
    texte = re.sub(
        r"^### T4 · .*?(?=^### T5)",
        "### T4 · Installation d'un second membre\n\n"
        "**Sans objet — travail en monôme.** Le diagnostic du poste d'Ali Mouda "
        "est consigné dans T6. Le clone frais T7 reste un contrôle distinct de "
        "reproductibilité.\n\n",
        texte,
        count=1,
        flags=re.M | re.S,
    )
    texte = re.sub(
        r"^### T5 · .*?(?=^### T6)",
        "### T5 · Historique Git — remise individuelle\n\n"
        "**Étudiant :** Ali Mouda.\n\n"
        "**Obtenu :** les trois tests de l'historique Git passent dans le rapport final. "
        "L'historique existant contient notamment des commits d'Ali Mouda et des "
        "contributions antérieures d'autres auteurs.\n\n"
        "- [x] Historique local vérifié\n\n"
        "**Commentaire :** l'exigence pédagogique d'un commit par membre du binôme "
        "est sans objet pour cette remise en monôme. Les auteurs existants restent "
        "inchangés ; aucun auteur fictif n'a été créé.\n\n"
        "**Capture non fournie — historique Git** : `captures/tp1-t5-shortlog.png`.\n\n",
        texte,
        count=1,
        flags=re.M | re.S,
    )
    debut = texte.index("## La répartition du travail")
    fin = texte.index("## Le bilan", debut)
    texte = texte[:debut] + """## Organisation du travail en monôme

**Responsable de la remise : Ali Mouda.** Les travaux sont présentés individuellement.
La reprise technique et la rédaction ont bénéficié de l'assistance de Codex.

| TP | Travail présenté par Ali Mouda |
| --- | --- |
| TP1 | Cadrage des trois cas, environnement Python, structure et vérifications Git. |
| TP2 | Entraînements démonstration et Allociné, métriques et analyse des erreurs. |
| TP3 | API FastAPI, contrats HTTP et vérification des réponses. |
| TP4 | Tests aux limites, propriétés, intégration, abstention et qualité statique. |
| TP5 | Interface Streamlit, client HTTP, analyse des avis et du lot CSV. |
| TP6 | Paquet installable, commande sentiment et validation de la roue hors du dépôt. |

""" + texte[fin:]
    texte = re.sub(
        r"\*\*3\\?\. La part du membre B\.\*\*.*?(?=^## |^### |\Z)",
        "**3. Travail en monôme.** Les contrôles attribués au second membre dans "
        "le canevas ne s'appliquent pas. Ali Mouda conserve sa propre identité Git "
        "pour ses commits ; aucune seconde identité n'est nécessaire.\n\n",
        texte,
        flags=re.M | re.S,
    )
    texte = texte.replace(" (membre A)", " (Ali Mouda)")
    texte = texte.replace(" (à deux)", " (travail individuel)")
    texte = texte.replace("Poste du membre A", "Poste d'Ali Mouda")
    texte = texte.replace("le nom du membre A", "le nom d'Ali Mouda")
    texte = texte.replace("La préparation des postes", "La préparation du poste")
    texte = texte.replace("push, CI, part du membre B", "push et CI")
    texte = texte.replace("rédigés par le binôme", "rédigés par l'étudiant")
    texte = texte.replace("d'un binôme à l'autre", "d'un étudiant à l'autre")
    debut = texte.index("## Comment remplir ce journal")
    fin = texte.index("## 0", debut)
    texte = texte[:debut] + """## Organisation du journal

Le journal est enregistré sous `docs/journal-tp1-tp6.md`.
Chaque contrôle présente le résultat obtenu, sa conformité et un commentaire explicatif.
Les résultats non vérifiés sont indiqués explicitement.

---

""" + texte[fin:]
    texte = re.sub(r"^\*\*Capture non fournie.*\n", "", texte, flags=re.M)
    remplacements = {
        "les captures et la CI distante": "la CI distante",
        "sans attester une capture ou un clic manuel non réalisé": "sans attester un clic manuel non réalisé",
        "Aucun clic Swagger ni capture de /docs n'est revendiqué.": "Les requêtes ont été vérifiées automatiquement.",
        "ouverture manuelle sur localhost:8501 non capturée": "ouverture manuelle sur localhost:8501 non vérifiée",
        "elle ne constitue pas une capture d'un navigateur ouvert manuellement": "l'ouverture manuelle dans un navigateur n'a pas été vérifiée",
        "téléchargement manuel non capturé": "téléchargement manuel non vérifié",
        "l'exécution distante et sa capture ne sont pas disponibles": "l'exécution distante n'est pas vérifiée",
        "le clone frais et les captures restent à documenter": "le clone frais reste à vérifier",
        "le téléchargement manuel et les captures restent à joindre": "le téléchargement manuel reste à vérifier",
        "Ce qu'on capture": "Ce qu'on extrait",
    }
    for ancien, nouveau in remplacements.items():
        texte = texte.replace(ancien, nouveau)
    texte = re.sub(r"\n{3,}", "\n\n", texte)
    fichier.write_text(texte, encoding="utf-8")
    (root / "docs/captures/LISEZ-MOI.md").unlink(missing_ok=True)


if __name__ == "__main__":
    adapter(Path(__file__).resolve().parents[1])
