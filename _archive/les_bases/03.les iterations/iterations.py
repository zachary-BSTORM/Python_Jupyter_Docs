# les iterations vont permettre d'effectuer des actions un certains nombre de fois en fonction d'une condition 
# cette condition ne doit respecter qu'une seule regle : elle doit renvoyer un booléen (True ou False)

# while
# attention a la condition d'arret de la boucle sinon on se retrouve dans une boucle infinie

i = 0
while i < 10:
    print(i)
    i += 1


#for
# le for est une boucle qui va permettre de parcourir une liste d'éléments (une liste, un tuple, un dictionnaire, un ensemble ou une chaîne de caractères)
# on va retrouver trois cas d'utilisation du for :

# le premier est de parcourir une liste d'éléments

collection = [1, 2, 3, 4, 5]
for value in collection:
    print(value)
    

# le second est de parcourir une liste d'éléments en utilisant la fonction range qui va permettre de créer une liste d'entiers

for i in range(10):
    print(i)
    
# range possède plusieurs arguments :
# - start : le premier entier de la liste (par défaut 0)
# - stop : le dernier entier de la liste (non inclus)
# - step : le pas entre chaque entier de la liste (par défaut 1)

for i in range(1, 10, 2):
    print(i)


# le dernier est de parcourir une liste d'éléments en utilisant la fonction enumerate qui va permettre de créer une liste d'entiers et de les associer à la valeur de l'élément
for i, value in enumerate(collection):
    print(i, value)
    
