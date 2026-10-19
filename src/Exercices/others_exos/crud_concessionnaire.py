# --- Correction de Exos_Ennoncés/crud_concessionnaire.md ---
# CRUD « Concessionnaire automobile » avec persistance JSON.
# Architecture :  démarrage → charger_voitures() → boucle de menu
#                 chaque changement (3/4/5) → sauvegarder_voitures() écrase le fichier
# Les explications détaillées sont dans crud_concessionnaire_explications.md

import json
import os

FICHIER = "concessionnaire.json"

# Le stock de départ : utilisé uniquement au tout premier lancement,
# quand le fichier JSON n'existe pas encore.
STOCK_DEPART = {
    "1-ABC-123": {"marque": "Renault", "modele": "Clio", "annee": 2019,
                  "prix": 11500, "kilometrage": 68000},
    "1-DEF-456": {"marque": "Peugeot", "modele": "208", "annee": 2021,
                  "prix": 15900, "kilometrage": 32000},
    "1-GHI-789": {"marque": "Toyota", "modele": "Yaris", "annee": 2017,
                  "prix": 9200, "kilometrage": 95000},
}


def sauvegarder_voitures(voitures):
    """Écrase le fichier JSON avec l'état actuel du stock.

    Appelée après CHAQUE changement : le fichier est donc toujours à jour,
    même si le programme est fermé brutalement.
    """
    with open(FICHIER, "w", encoding="utf-8") as f:          # "w" : écrase tout
        json.dump(voitures, f, ensure_ascii=False, indent=4)


def charger_voitures():
    """Charge le stock depuis le JSON — exécutée UNE fois, au démarrage.

    Tout premier lancement (pas de fichier) : on crée le fichier avec le
    stock de départ, puis on le lit — un seul chemin de lecture.
    """
    if not os.path.exists(FICHIER):
        sauvegarder_voitures(STOCK_DEPART)
    with open(FICHIER, "r", encoding="utf-8") as f:
        return json.load(f)                       # texte JSON → dictionnaire Python


def demander_entier(question):
    """Repose la question jusqu'à obtenir un entier valide (saisie robuste)."""
    while True:
        try:
            return int(input(question))           # ça marche → return sort de la boucle
        except ValueError:
            print("⚠ Veuillez entrer un nombre entier")


def afficher_liste(voitures):
    """La liste résumée du parc — réutilisée par les options 1, 4 et 5."""
    if len(voitures) == 0:
        print("Le parc est vide")
    else:
        print(f"{len(voitures)} voiture(s) en stock :")
        for plaque, voiture in voitures.items():
            print(f"  {plaque} — {voiture['marque']} {voiture['modele']} ({voiture['annee']})")


MENU = """
=== Concessionnaire AutoStorm ===
1. Afficher les voitures
2. Afficher le détail d'une voiture
3. Ajouter une voiture
4. Modifier une voiture
5. Supprimer une voiture
0. Quitter
"""

# --- Le chargement est exécuté directement au démarrage ---
voitures = charger_voitures()
print(f"{len(voitures)} voiture(s) chargée(s) depuis {FICHIER}")

quitter = False
while not quitter:
    print(MENU)
    choix = input("Votre choix : ")

    match choix:
        case "0":
            quitter = True
            print("À bientôt !")
            # Rien à sauvegarder ici : le fichier est déjà à jour
            # après chaque changement.

        case "1":
            # --- READ (liste) ---
            afficher_liste(voitures)

        case "2":
            # --- READ (détail) ---
            plaque = input("Plaque de la voiture : ").strip().upper()
            if plaque in voitures:
                voiture = voitures[plaque]
                print(f"--- {plaque} ---")
                print(f"Marque      : {voiture['marque']}")
                print(f"Modèle      : {voiture['modele']}")
                print(f"Année       : {voiture['annee']}")
                print(f"Prix        : {voiture['prix']} €")
                print(f"Kilométrage : {voiture['kilometrage']} km")
            else:
                print(f"Aucune voiture avec la plaque {plaque}")

        case "3":
            # --- CREATE ---
            plaque = input("Plaque (ex: 1-ABC-123) : ").strip().upper()
            if plaque == "":
                print("La plaque ne peut pas être vide")
            elif plaque in voitures:
                print(f"La plaque {plaque} existe déjà dans le parc")
            else:
                marque = input("Marque : ").strip()
                modele = input("Modèle : ").strip()
                annee = demander_entier("Année : ")
                prix = demander_entier("Prix (€) : ")
                kilometrage = demander_entier("Kilométrage : ")

                voitures[plaque] = {
                    "marque": marque,
                    "modele": modele,
                    "annee": annee,
                    "prix": prix,
                    "kilometrage": kilometrage,
                }
                sauvegarder_voitures(voitures)    # le fichier reflète le nouvel état
                print(f"{marque} {modele} ajoutée au parc ({plaque})")

        case "4":
            # --- UPDATE : saisie vide = conserver la valeur actuelle ---
            afficher_liste(voitures)
            plaque = input("Plaque de la voiture à modifier : ").strip().upper()
            if plaque not in voitures:
                print(f"Aucune voiture avec la plaque {plaque}")
            else:
                voiture = voitures[plaque]        # référence vers le dict interne :
                print("Laissez vide pour conserver la valeur actuelle.")

                marque = input(f"Marque [{voiture['marque']}] : ").strip()
                if marque != "":
                    voiture["marque"] = marque    # ... le modifier modifie voitures !

                modele = input(f"Modèle [{voiture['modele']}] : ").strip()
                if modele != "":
                    voiture["modele"] = modele

                # Ici, pas de demander_entier : « vide = conserver » impose
                # de tester la saisie nous-mêmes avec .isdigit()
                prix = input(f"Prix [{voiture['prix']} €] : ").strip()
                if prix != "":
                    if prix.isdigit():
                        voiture["prix"] = int(prix)
                    else:
                        print("Prix ignoré (ce n'est pas un nombre)")

                kilometrage = input(f"Kilométrage [{voiture['kilometrage']} km] : ").strip()
                if kilometrage != "":
                    if kilometrage.isdigit():
                        voiture["kilometrage"] = int(kilometrage)
                    else:
                        print("Kilométrage ignoré (ce n'est pas un nombre)")

                sauvegarder_voitures(voitures)
                print(f"La voiture {plaque} a été mise à jour")

        case "5":
            # --- DELETE : avec confirmation ---
            afficher_liste(voitures)
            plaque = input("Plaque de la voiture à supprimer : ").strip().upper()
            if plaque not in voitures:
                print(f"Aucune voiture avec la plaque {plaque}")
            else:
                voiture = voitures[plaque]
                reponse = input(f"Supprimer {voiture['marque']} {voiture['modele']} ({plaque}) ? o/n : ")
                if reponse.strip().lower() == "o":
                    del voitures[plaque]
                    sauvegarder_voitures(voitures)
                    print(f"La voiture {plaque} a été retirée du parc")
                else:
                    print("Suppression annulée")

        case _:
            print("Choix invalide")
