
nb_1 = None
nb_2 = None
operator = None
operation = ""

nb_1 = int(input("Entrez la première valeur : "))
operator = input("Entrez un opérateur : + - * / % ")
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
        if nb2 != 0:
            print(operation + str(nb_1 / nb_2 ))
        else:
            print("division par zero impossible")
    case "%":
        print(operation + str(nb_1 % nb_2))
    case _:
        print("opération invalide")