# --- Menu principal ---
# Affiche les options disponibles et retourne le choix de l'utilisateur (entier validé).
# La boucle while + try/except assure que show_menu() ne retourne JAMAIS une valeur invalide :
#   - ValueError si l'entrée n'est pas un entier (ex: "abc")
#   - Vérification de la plage [0-6] avant de retourner

def show_menu():
    print("\n=== Menu ===")
    print("0. Quit")
    print("1. Calculator")
    print("2. Mystery Number")
    print("3. Library Manager")
    print("4. Todo App")
    print("5. Minesweeper")
    print("6. Algorithmes")

    while True:
        try:
            answer = int(input("What is your choice? "))
            if 0 <= answer <= 6:
                return answer
            else:
                print("Please enter a number between 0 and 6")
        except ValueError:
            print("Invalid input, please enter a number")