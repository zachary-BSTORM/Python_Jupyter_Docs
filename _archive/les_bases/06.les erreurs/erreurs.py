# la gestion des erreurs
# le try, except, else et finally
# le try permet de tester un bloc de code
# le except permet de gerer les erreurs
# le else s'execute si aucune erreur n'est survenue
# le finally s'execute toujours

# on va  pouvoir tester un code qui peut generer une erreur
# le try contient le code a tester
# le except contient le code a executer si une erreur est survenue
# le else contient le code a executer si aucune erreur n'est survenue
# le finally contient le code a executer dans tous les cas

try:
    print("action a realiser")
except:
    print("une erreur s'est produite")
else:
    print("le bloc else s'execute si aucune erreur n'est survenue")
finally:
    print("le bloc finally s'execute toujours")
    
    
# on a la possibilite de gerer plusieurs types d'erreurs
# on peut preciser le type d'erreur a gerer

try:
    print("action a realiser")
except ValueError:
    print("une erreur de type ValueError s'est produite")
except TypeError:
    print("une erreur de type TypeError s'est produite")
except:
    print("une erreur de type inconnu s'est produite")
    

# on peut recuperer les informations sur l'erreur avec as
# cela permet d'afficher le message exact de l'erreur

try:
    x = int("abc")
except ValueError as e:
    print("une erreur ValueError s'est produite :", e)

# on peut lever volontairement une exception avec raise
# cela permet d'indiquer qu'une situation anormale doit interrompre le programme

def division(a , b):
    if b == 0:
        raise ZeroDivisionError("division par zero interdite")
    return a / b


# on peut definir ses propres types d'exceptions en creant une classe
# elle doit heriter de la classe Exception
class MonErreur(Exception):
    pass

# exemple d'utilisation d'une exception personnalisée
try:
    raise MonErreur("erreur personnalisée")
except MonErreur as e:
    print("exception personnalisee :", e)
