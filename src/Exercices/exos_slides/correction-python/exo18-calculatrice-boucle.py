# Exo 18 — la calculatrice refait un calcul tant que l'utilisateur le désire

encore = "y"

while encore == "y":
    nb_1 = int(input("Entrez la première valeur : "))
    operator = input("Entrez un opérateur : + - * / % : ")
    nb_2 = int(input("Entrez la deuxième valeur : "))

    operation = f"{nb_1} {operator} {nb_2} = "

    match operator:
        case "+":
            print(operation + str(nb_1 + nb_2))
        case "-":
            print(operation + str(nb_1 - nb_2))
        case "*":
            print(operation + str(nb_1 * nb_2))
        case "/":
            if nb_2 != 0:
                print(operation + str(nb_1 / nb_2))
            else:
                print("division par zero impossible")
        case "%":
            print(operation + str(nb_1 % nb_2))
        case _:
            print("opération invalide")

    encore = input("Voulez-vous faire un autre calcul ? y - n : ")
