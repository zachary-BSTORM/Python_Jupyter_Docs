# --- Correction de Exos_Ennoncés/crud_contacts.md ---
# CRUD « Répertoire de contacts » avec menu interactif.
# Contrainte de l'exercice : SANS classes ni fonctions (def) — uniquement
# variables, conditions, boucles, collections, match/case et input().
# Conséquence assumée : le bloc « afficher la liste numérotée » est copié-collé
# trois fois (options 1, 3 et 4)... c'est exactement ce que les fonctions,
# vues au chapitre suivant, permettront d'éliminer.

contacts = [
    {"nom": "Alice Dupont", "telephone": "0470 11 22 33"},
    {"nom": "Bob Martin", "telephone": "0485 44 55 66"},
]

MENU = """
=== Répertoire de contacts ===
1. Afficher les contacts
2. Ajouter un contact
3. Modifier un numéro
4. Supprimer un contact
0. Quitter
"""

quitter = False

while not quitter:
    print(MENU)
    choix = input("Votre choix : ")

    match choix:
        case "0":
            quitter = True
            print("Au revoir !")

        case "1":
            # --- READ : la liste numérotée à partir de 1 ---
            if len(contacts) == 0:
                print("Le répertoire est vide")
            else:
                for position, contact in enumerate(contacts, start=1):
                    print(f"{position}. {contact['nom']} — {contact['telephone']}")

        case "2":
            # --- CREATE : nom non vide + numéro ---
            nom = input("Nom du contact : ").strip()
            if nom == "":
                print("Le nom ne peut pas être vide")
            else:
                telephone = input("Numéro de téléphone : ").strip()
                contacts.append({"nom": nom, "telephone": telephone})
                print(f"{nom} a été ajouté(e) au répertoire")

        case "3":
            # --- UPDATE : choisir une ligne valide, puis changer le numéro ---
            if len(contacts) == 0:
                print("Le répertoire est vide, rien à modifier")
            else:
                for position, contact in enumerate(contacts, start=1):
                    print(f"{position}. {contact['nom']} — {contact['telephone']}")

                saisie = input("Numéro du contact à modifier : ")
                if not saisie.isdigit():
                    print("Ce n'est pas un nombre !")
                elif int(saisie) < 1 or int(saisie) > len(contacts):
                    print(f"Il n'y a pas de contact n°{saisie}")
                else:
                    index = int(saisie) - 1          # l'utilisateur compte à partir de 1
                    nouveau = input("Nouveau numéro de téléphone : ").strip()
                    contacts[index]["telephone"] = nouveau
                    print(f"Le numéro de {contacts[index]['nom']} a été mis à jour")

        case "4":
            # --- DELETE : choisir une ligne valide, puis retirer avec pop ---
            if len(contacts) == 0:
                print("Le répertoire est vide, rien à supprimer")
            else:
                for position, contact in enumerate(contacts, start=1):
                    print(f"{position}. {contact['nom']} — {contact['telephone']}")

                saisie = input("Numéro du contact à supprimer : ")
                if not saisie.isdigit():
                    print("Ce n'est pas un nombre !")
                elif int(saisie) < 1 or int(saisie) > len(contacts):
                    print(f"Il n'y a pas de contact n°{saisie}")
                else:
                    supprime = contacts.pop(int(saisie) - 1)
                    print(f"{supprime['nom']} a été supprimé(e) du répertoire")

        case _:
            print("Choix invalide")
