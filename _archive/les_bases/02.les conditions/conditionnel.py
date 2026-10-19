# en python on utilise pas d'accolades pour definir un bloc de code, mais l'indentation
# on utilise des deux points pour definir le debut d'un bloc de code
from unittest.mock import DEFAULT

# Nous retrouvons les structures conditionnelles qui permettent de tester une ou plusieurs conditions
# et d'exécuter du code en fonction du resultat de cette ou ces conditions.

# Les structures conditionnelles sont les suivantes :

# - if : si la condition est vraie, on exécute le code qui suit
# - elif : si la premiere condition est fausse , on exécute le code dans le elif
# - else : si aucune des conditions précédentes n'est vraie, on exécute le code present dans le else
# - match : ici on tiens compte de la valeur d'une variable pour effectuer une action en fonction de sa valeur  (utilisé en Python 3.10 et supérieur)


# if 
# on peut ajouter les parenteses ou pas, mais c'est plus lisible avec les parenthèses


nb = 10
if nb > 0:
    print("Le nombre est positif")
    
if nb < 0:
    print("Le nombre est négatif")

if nb == 0 & 10/2 == 2:
    print("Le nombre est positif")

if nb == 0 | 10/2 == 2:
    print("Le nombre est positif")

# elif
# meme principe que le if, on peut ajouter les parenteses
# ce code ne sera exécuté que si la condition du if est fausse

if nb > 0:
    print("Le nombre est positif")
elif nb < 0:
    print("Le nombre est négatif")
    

# else
# le else est executé si aucune des conditions précédentes n'est vraie
if (nb > 0):
    print("Le nombre est positif")
elif nb < 0:
    print("Le nombre est négatif")
else:
    print("Le nombre est zero")

# match
# Le match permet d'effectuer plusieurs comparaison sur une seule variable
match nb:
    case 0:
        print("Le nombre est 0")
    case 1:
        print("Le nombre est 1")
    case _:
        print("Le nombre est différent")