
# Pour declarer une methode on utilise le mot cle def
# pour les methodes nous avons deux types de methodes

# les procedures qui ne retournent rien
def ma_procedure():
    print("Je suis une procedure")

# les fonctions qui retournent une valeur
def ma_fonction():
    return "Je suis une fonction"


## on va pouvoir declarer une logique et l'utiliser quand on le souhaite on utilise toujours l'indentation et les deux points


# notre fonction peut recevoir certains parametres et l'on peut leur donner une valeur par defaut
def ma_fonction_parametre(parametre1, parametre2 = "  Je suis un parametre par defaut"):
    print(parametre1, parametre2)
    
ma_fonction_parametre("hello")
ma_fonction_parametre("hello","je suis une valeur")


# on peut effectuer une action sur une liste
def ma_fonction_liste(liste):
    for value in enumerate(liste):
        print(value)

        
# on peut aussi passer une fonction en parametre d'une autre fonction un callback
def ma_fonction_callback(ma_fonction):
    print("Je suis une fonction callback")
    ma_fonction()
    

# petit rappel sur le principe de portée des variables
# une variable definie dans une fonction n'est pas accessible en dehors de cette fonction
# une variable definie en dehors d'une fonction est accessible dans cette fonction

ma_valeur = "Je suis une variable"

def ma_fonction_portee():
    ma_valeur = "Je suis une variable locale"
    print(ma_valeur)


# meme si c'est déconseillé on peut definir une variable globale avec le mot cle global
# mais il est preferable de passer la variable en parametre de la fonction

global ma_variable_globale

ma_variable_globale = "Je suis une variable globale";

# ===========================================================
#lambda 
# ===========================================================

'''
Lambda

    syntaxe -> x =  lambda arg1,arg2 : instruction (ex : arg1 + arg2 )
'''

# METHODE SIMPLE
def exposant(x):
    return x*x

print(exposant(4))


# LAMBDA ( un paramètre)
expoLambda = lambda x : x*x

print(expoLambda(4))

# Addition ( plusieurs paramètres)
addLambda = lambda x,y : x+y

print(addLambda(8,8))


def methode (value , x = lambda y : y*y):
    return x(4)

def methode(x , ma_lambda = lambda y : y*y):
    return ma_lambda(x)

print(methode(4))

print("d")
print(methode(7, expoLambda))