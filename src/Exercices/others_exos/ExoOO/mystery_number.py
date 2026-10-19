import random

# --- Jeu du nombre mystère ---
# Le jeu tire un nombre aléatoire entre 1 et 100.
# Le joueur dispose d'un nombre de tentatives choisi au départ (1–50).
# Après chaque tentative, on indique si le nombre mystère est plus grand ou plus petit.
# On mémorise les nombres déjà essayés pour éviter les doublons.
# Le jeu se termine par une victoire (bon nombre) ou une défaite (tentatives épuisées).

def mystery_number_start():
    mystery_number = random.randint(1, 100)
    tried_numbers = []  # Historique des tentatives pour éviter les doublons

    # --- Phase 1 : choix du nombre de vies ---
    # Boucle de validation : on répète jusqu'à obtenir une entrée valide
    while True:
        try:
            life = int(input("How many tries do you want (1-50)? "))
            if 1 <= life <= 50:
                break
            else:
                print("Please enter a number between 1 and 50")
        except ValueError:
            print("Invalid input, please enter a number")

    # --- Phase 2 : boucle de jeu principale ---
    while life > 0:
        print(f"Your previous numbers: {tried_numbers}")

        try:
            choice = int(input("Enter a number between 1 and 100: "))
        except ValueError:
            print("Invalid input, please enter a number")
            continue  # On ne consomme pas une vie sur une entrée invalide

        if not 1 <= choice <= 100:
            print("Number must be between 1 and 100")
            continue

        if choice in tried_numbers:
            print("You already tried this number")
            continue  # Doublon : on ne consomme pas une vie non plus

        tried_numbers.append(choice)
        life -= 1  # On consomme une vie uniquement sur une tentative valide et nouvelle

        if choice == mystery_number:
            print("Correct! YOU WIN!")
            return
        elif choice < mystery_number:
            print("Incorrect, the number is bigger!")
        else:
            print("Incorrect, the number is smaller!")

    print(f"You lose! The number was {mystery_number}")