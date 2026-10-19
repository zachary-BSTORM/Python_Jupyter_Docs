# nous pouvons executer des commandes dans la console directement
# mais le probleme  que nous allons rencontrer est que nous ne pourrons pas reutiliser notre code 

# # il est donc preferable de le mettre dans un fichier et de l'executer
# # pour cela nous allons utiliser la commande python nom_du_fichier.py
# # ou creer un fichier .py et y mettre notre code
# # pour executer le fichier, il faut se placer dans le repertoire ou se trouve le fichier et executer la commande python nom_du_fichier.py

# pour pouvoir nous y retrouver facilement dans notre fichiers nous allons utiliser des commentaires
# # pour cela nous allons utiliser le caractere # pour commenter une ligne

# nous allons aussi utiliser des commentaires multilignes pour expliquer notre code
# # pour cela nous allons utiliser les caracteres """ ou ''' pour definir un commentaire multilignes

'''
pour nous y retrouver facilement dans notre code nous avons la possibilite de definir des sections
# pour cela nous allons utiliser les caracteres # pour definir une section tout simplement 
# idealement il y aurait une section pour : 
# - les imports
# - les variables
# - les fonctions
# - le code principal
'''

# ===================================================================================================================
# # les imports
# ===================================================================================================================
import math

# ===================================================================================================================
# # les variables
# ===================================================================================================================
nb1 = 5
operator = ""
nb2 = 10
again = True
value =[0]
total = 0
index = 0
input_user = 0


# ===================================================================================================================
# # les fonctions
# ===================================================================================================================def
def addition(args: list):
    """
    retourne la somme de deux nombres: 
    """
    somme = 0
    
    for i in args:
        somme += i
    return somme



# ===================================================================================================================
# # le code principal
# ===================================================================================================================

while again:
    
    value[0] = int(input("Enter a number: "))
    
    index += 1
    
    for i in value:
        total += i
    
    print(f"Total: {total}")
    
    input_user = input("Do you want to continue? (y/n): ")
    
    if input_user == "n":
        again = False


