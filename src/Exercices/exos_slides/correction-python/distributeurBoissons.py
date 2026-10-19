user_choice = -1

coca = 5
fanta = 4
water = 6
coffee = 8

menu = """
coca   : 1
fanta  : 2
eau  : 3
café : 4
"""


print(menu)
user_choice = int(input("Entrez votre selection"))

match user_choice:
    case 1 :
        if coca > 0:
            print("voici votre coca")
            coca -= 1
        else :
            print("cette boisson n'est pas disponible")
    case 2 :
        if fanta > 0:
            print("voici votre fanta")
            fanta -= 1
        else :
            print("cette boisson n'est pas disponible")
    case 3 :
        if fanta > 0:
            print("voici votre eau")
            water -= 1
        else :
            print("cette boisson n'est pas disponible")
    case 4 :
        if fanta > 0:
            print("voici votre café")
            coffee -= 1
        else :
            print("cette boisson n'est pas disponible")