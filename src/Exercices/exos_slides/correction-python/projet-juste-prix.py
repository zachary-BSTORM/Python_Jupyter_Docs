# Projet — Le juste prix complet
#   - 10 essais maximum ; après, c'est perdu et l'ordinateur affiche le juste prix
#   - 3 niveaux : facile (1-10), moyen (1-100), difficile (1-1000)
#   - on rejoue tant que la personne le désire (niveau redemandé, nombre régénéré)
#   - toute saisie est vérifiée avec .isdigit() : le programme ne plante jamais

import os
import random

rejouer = "y"

while rejouer == "y":
    os.system("cls")    # efface l'écran (Windows)

    # --- choix du niveau (redemandé tant qu'il est incorrect) ---
    niveau = ""
    while niveau not in ("1", "2", "3"):
        niveau = input("Niveau : 1 facile (1-10) | 2 moyen (1-100) | 3 difficile (1-1000) : ")

    if niveau == "1":
        maximum = 10
    elif niveau == "2":
        maximum = 100
    else:
        maximum = 1000

    # --- la partie ---
    juste_prix = random.randrange(1, maximum + 1, 1)
    essais_restants = 10
    trouve = False

    while essais_restants > 0 and not trouve:
        saisie = input(f"Votre proposition (1 à {maximum}) — {essais_restants} essais restants : ")

        if saisie.isdigit():                  # la saisie est bien un nombre
            proposition = int(saisie)
            essais_restants -= 1

            if proposition < juste_prix:
                print("C'est plus")
            elif proposition > juste_prix:
                print("C'est moins")
            else:
                trouve = True
                print(f"C'est gagné en {10 - essais_restants} tentatives !")
        else:
            print("Ce n'est pas un nombre !")  # ne consomme pas d'essai

    if not trouve:
        print(f"Perdu ! Le juste prix était {juste_prix}")

    rejouer = input("Voulez-vous rejouer ? y - n : ")

print("Merci d'avoir joué !")
