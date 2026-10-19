# --- Correction de Exos_Ennoncés/collections_mediatheque.md ---
# La médiathèque : dict de dicts + liste de tuples + sets, menu interactif.
# Contrainte : sans classes, sans fonctions (def), sans compréhensions.

catalogue = {                                    # dict de DICTS, clé = titre
    "1984": {"auteur": "George Orwell", "exemplaires": 2},
    "Le Petit Prince": {"auteur": "Antoine de Saint-Exupéry", "exemplaires": 1},
    "Dune": {"auteur": "Frank Herbert", "exemplaires": 3},
    "Fondation": {"auteur": "Isaac Asimov", "exemplaires": 0},
}

abonnes = {"Alice", "Bob", "Chloé"}              # set des abonnés en règle

emprunts = []                                    # liste de TUPLES (abonné, titre)

MENU = """
=== Médiathèque ===
1. Afficher le catalogue
2. Emprunter un livre
3. Rendre un livre
4. Emprunts en cours
5. Statistiques
0. Quitter
"""

quitter = False
while not quitter:
    print(MENU)
    choix = input("Votre choix : ")

    match choix:
        case "0":
            quitter = True
            print("Bonne lecture !")

        case "1":
            # --- le catalogue : un crochet par niveau ---
            for titre, fiche in catalogue.items():
                if fiche["exemplaires"] > 0:
                    print(f"{titre} — {fiche['auteur']} ({fiche['exemplaires']} exemplaire(s) disponible(s))")
                else:
                    print(f"{titre} — {fiche['auteur']} (ÉPUISÉ)")

        case "2":
            # --- emprunter : 3 vérifications dans l'ordre ---
            nom = input("Nom de l'abonné : ").strip()
            titre = input("Titre du livre : ").strip()

            if nom not in abonnes:                              # set : test d'appartenance
                print(f"{nom} n'est pas abonné(e) à la médiathèque")
            elif titre not in catalogue:                        # dict : la clé existe ?
                print(f"« {titre} » n'est pas dans le catalogue")
            elif catalogue[titre]["exemplaires"] == 0:
                print(f"« {titre} » est épuisé pour le moment")
            else:
                catalogue[titre]["exemplaires"] -= 1
                emprunts.append((nom, titre))                   # le tuple trace l'emprunt
                print(f"{nom} emprunte « {titre} »")

        case "3":
            # --- rendre : le tuple complet doit être dans la liste ---
            nom = input("Nom de l'abonné : ").strip()
            titre = input("Titre du livre : ").strip()

            if (nom, titre) in emprunts:        # in compare des tuples ENTIERS
                emprunts.remove((nom, titre))
                catalogue[titre]["exemplaires"] += 1
                print(f"{nom} a rendu « {titre} », merci !")
            else:
                print(f"Aucun emprunt de « {titre} » au nom de {nom}")

        case "4":
            # --- les emprunts en cours ---
            if len(emprunts) == 0:
                print("Aucun emprunt en cours")
            else:
                for nom, titre in emprunts:                     # unpacking
                    print(f"{nom} a emprunté « {titre} »")

        case "5":
            # --- statistiques ---
            print("Titres épuisés :")
            for titre, fiche in catalogue.items():
                if fiche["exemplaires"] == 0:
                    print(f"  - {titre}")

            # le set des emprunteurs actifs, construit depuis la liste de tuples
            actifs = set()
            for nom, titre in emprunts:
                actifs.add(nom)
            print(f"Emprunteurs actifs : {actifs}")
            print(f"Abonnés sans emprunt : {abonnes - actifs}")   # différence de sets
            print(f"Emprunts en cours : {len(emprunts)}")

        case _:
            print("Choix invalide")
