# --- Calculatrice simple ---
# Saisit deux nombres et un opérateur, effectue l'opération et affiche le résultat.
# Gère la division par zéro et les entrées non numériques via try/except.
# Le match/case remplace une chaîne de if/elif → plus lisible et "Pythonic".

def calculator():
    try:
        nb1 = float(input("Entrez un premier nombre : "))
        op = input("Entrez un opérateur (+, -, *, /) : ")
        nb2 = float(input("Entrez un deuxième nombre : "))

        match op:
            case "+":
                result = nb1 + nb2
            case "-":
                result = nb1 - nb2
            case "*":
                result = nb1 * nb2
            case "/":
                if nb2 == 0:
                    print("Division par zéro impossible")
                    return
                result = nb1 / nb2
            case _:
                print("Opérateur invalide")
                return

        print(f"Le résultat de {nb1} {op} {nb2} = {result}")

    except ValueError:
        # float() lève ValueError si la saisie n'est pas convertible en nombre
        print("Veuillez entrer des nombres valides")