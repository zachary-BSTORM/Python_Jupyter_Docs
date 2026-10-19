
# Ensuite on retrouve les types de collections qui sont des listes de valeurs 

##################################################################################################################

# - les listes 

# - liste : [1, 2, 3], ["a", "b", "c"] (liste de valeurs modifiables)
# la liste est indexée de 0 à n-1, c'est-à-dire que le premier élément est à l'index 0
# la liste est ordonnée, c'est-à-dire que l'ordre des éléments est important
# la liste est mutable, c'est-à-dire que l'on peut modifier les éléments de la liste
# la liste est dynamique, c'est-à-dire que l'on peut ajouter ou supprimer des éléments de la liste
# la liste autorise les doublons, c'est-à-dire que l'on peut mettre plusieurs fois le même élément dans la liste


ma_liste = [1, 2, 3]
print(ma_liste[0])
print(ma_liste)


# on peut creer une liste de différentes façons

# en affectant des valeurs directement
ma_liste = [1, 2, 3] # crée une liste de trois éléments


# en utilisant la fonction list()
ma_liste = list((1, 2, 3)) # on utilise des doubles parenthèses car la fonction list() attend un itérable en paramètre


# on peut créer une liste vide
ma_liste = list() # crée une liste vide
ma_liste = [] # crée une liste vide


# une fois que l'on a créé une liste on peut utiliser certaines méthodes pour la manipuler

# append : ajoute un élément à la fin de la liste
ma_liste.append(4) # ajoute l'élément 4 à la fin de la liste


# extend : ajoute plusieurs éléments à la fin de la liste
ma_liste.extend([5, 6]) # ajoute les éléments 5 et 6 à la fin de la liste


# insert : ajoute un élément à une position donnée dans la liste
ma_liste.insert(0, 0) # ajoute l'élément 0 à la position 0 dans la liste


# sort : trie la liste dans l'ordre croissant ou décroissant
# sort(reverse=True) : trie la liste dans l'ordre décroissant
ma_liste.sort() # trie la liste dans l'ordre croissant
ma_liste.sort(reverse=True) # trie la liste dans l'ordre décroissant


# reverse : inverse l'ordre des éléments de la liste
ma_liste.reverse() # inverse l'ordre des éléments de la liste


### certaines methodes ne sont pas uniquement reservées aux listes
### on peut aussi les utiliser sur d'autres types de collections


# remove : supprime le premier élément de la liste qui a la valeur donnée
ma_liste.remove(0) # supprime le premier élément de la liste qui a la valeur 0


# pop : supprime l'élément à la position donnée dans la liste et le renvoie
ma_liste.pop(0) # supprime l'élément à la position 0 dans la liste et le renvoie


# clear : supprime tous les éléments de la liste
ma_liste.clear() # supprime tous les éléments de la liste


# count : renvoie le nombre d'éléments de la liste qui ont la valeur donnée
count = ma_liste.count(1) # renvoie le nombre d'éléments de la liste qui ont la valeur 1


# copy : renvoie une copie de la liste
ma_liste2 = ma_liste.copy() # renvoie une copie de la liste



##################################################################################################################

# Le tuple est une collection ordonnée et immuable de valeurs.
# le tuple est indexé de 0 à n-1, c'est-à-dire que le premier élément est à l'index 0
# le tuple est ordonné, c'est-à-dire que l'ordre des éléments est important
# le tuple est immutable, c'est-à-dire que l'on ne peut pas modifier les éléments du tuple
# l'on ne peut pas ajouter ou supprimer des éléments du tuple
# le tuple autorise les doublons, c'est-à-dire que l'on peut mettre plusieurs fois le même élément dans le tuple
# le tuple est plus rapide que la liste, car il est immutable et ne nécessite pas de gestion de mémoire dynamique

# - tuple : (1, 2, 3), ("a", "b", "c") (collection ordonnée et non modifiable de valeurs)

# Variables de type tuple
g = (1, 2, 3)
print(g[0]) # Affiche le premier élément du tuple
print(g)


# crée un tuple de trois éléments
mon_tuple = (1, 2, 3)


# on peut utiliser le constructeur tuple() pour créer un tuple
mon_tuple = tuple((1, 2, 3))  # ici, on passe un seul argument : un tuple


# et on peut recuperer les valeurs d'un tuple de la même manière que pour une liste
result = mon_tuple[0] # renvoie le premier élément du tuple


# count : renvoie le nombre d'éléments du tuple qui ont la valeur donnée
count = mon_tuple.count(1) # renvoie le nombre d'éléments du tuple qui ont la valeur 1


# index : renvoie l'index du premier élément du tuple qui a la valeur donnée
result = mon_tuple.index(1) # renvoie l'index du premier élément du tuple qui a la valeur 1


### ici aussi on peut utiliser certaines methodes sur les tuples
### on peut aussi les utiliser sur d'autres types de collections
### elles ne sont pas uniquement reservées aux tuples


# len : renvoie le nombre d'éléments dans le tuple
taille = len(mon_tuple) # renvoie le nombre total d'éléments du tuple


# max : renvoie le plus grand élément du tuple
maximum = max(mon_tuple) # renvoie le plus grand élément du tuple


# min : renvoie le plus petit élément du tuple
minimum = min(mon_tuple) # renvoie le plus petit élément du tuple


# sum : renvoie la somme des éléments du tuple
tot = sum(mon_tuple) # renvoie la somme de tous les éléments numériques du tuple


# sorted : renvoie une liste triée contenant les éléments du tuple
ordered_liste = sorted(mon_tuple) # renvoie une nouvelle liste triée dans l'ordre croissant


# reversed : renvoie un itérateur sur les éléments du tuple en ordre inverse
inverse = tuple(reversed(mon_tuple)) # renvoie un nouveau tuple avec les éléments dans l'ordre inverse


# in : vérifie si une valeur est présente dans le tuple
containItem = 2 in mon_tuple # renvoie True si 2 est présent dans le tuple


##################################################################################################################

# Le set est une collection non ordonnée de valeurs uniques.
# Le set n'est pas indexé : on ne peut pas accéder aux éléments avec des indices ([0]).
# Le set est non ordonné, c'est-à-dire que l'ordre des éléments n'est pas garanti.
# Le set est mutable : on peut ajouter ou supprimer des éléments.
# Le set ne permet pas les doublons : toute valeur dupliquée est automatiquement ignorée.
# Le set est optimisé pour tester l'appartenance avec "in" (opération rapide).

# - set : {1, 2, 3}, {"a", "b", "c"} (collection de valeurs uniques non ordonnées)

# Déclaration d'un set
my_set = {1, 2, 3}
print(my_set)

# print(my_set[0])  # Erreur : les sets ne sont pas indexés

# Créer un set vide
my_set = set()  # set vide
# my_set = {}    # dictionnaire vide, pas un set !

# Avec le constructeur set(), les doublons sont supprimés automatiquement
my_set = set([1, 2, 2, 3])
print(my_set)  # Affiche : {1, 2, 3}

# Méthodes de modification
my_set.add(4)        # Ajoute 4 à l’ensemble
my_set.remove(4)     # Supprime 4 (Erreur si 4 n’existe pas)
my_set.discard(10)   # Supprime 10 sans erreur s’il est absent
valeur = my_set.pop()  # Supprime et renvoie un élément aléatoire
my_set.clear()       # Supprime tous les éléments
my_set2 = my_set.copy()  # Copie du set

# Fonctions applicables
taille = len(my_set)       # Nombre d'éléments
existe = 2 in my_set       # True si 2 est dans le set
absent = 9 not in my_set   # True si 9 n’est pas dans le set
liste_triee = sorted(my_set)  # Liste triée à partir du set

# Opérations ensemblistes utiles
set1 = {1, 2, 3}
set2 = {3, 4, 5}

union = set1 | set2           # {1, 2, 3, 4, 5}
intersection = set1 & set2    # {3}
difference = set1 - set2      # {1, 2}
sym_diff = set1 ^ set2        # {1, 2, 4, 5}


##################################################################################################################

# Le dictionnaire est une collection de paires clé:valeur.
# Le dictionnaire n'est pas indexé par position : on accède aux valeurs par leurs clés.
# Avant Python 3.7, l'ordre des éléments n'était pas garanti.
# Depuis Python 3.7, l'ordre d'insertion des éléments est conservé.
# Le dictionnaire est mutable : on peut ajouter, modifier ou supprimer des paires clé:valeur.
# Chaque clé est unique : si une clé est dupliquée, la dernière valeur remplace l'ancienne.
# L'accès à une valeur via sa clé est très rapide (optimisé avec des tables de hachage).

# Exemple de dictionnaire
mon_dict = {1: "a", 2: "b", 3: "c"}

print(mon_dict[1])  # Accès à la valeur associée à la clé 1
print(mon_dict)

# Accès sécurisé avec get : retourne None si la clé n'existe pas (ou une valeur par défaut)
valeur = mon_dict.get(4)  # None
valeur_avec_defaut = mon_dict.get(4, "inconnu")  # "inconnu"

# keys : retourne toutes les clés
cles = mon_dict.keys()

# values : retourne toutes les valeurs
valeurs = mon_dict.values()

# items : retourne toutes les paires clé/valeur
paires = mon_dict.items()

# pop : supprime une clé et retourne sa valeur (KeyError si elle n'existe pas)
valeur = mon_dict.pop(2)  # supprime la clé 2

# popitem : supprime et retourne la dernière paire insérée
cle_valeur = mon_dict.popitem()

# update : ajoute ou met à jour des paires clé/valeur
mon_dict.update({'a': 1, 'b': 2})

# setdefault : retourne la valeur d'une clé, ou l'ajoute avec une valeur par défaut
valeur = mon_dict.setdefault('x', 42)  # ajoute 'x': 42 si 'x' n'existe pas

# clear : supprime tous les éléments du dictionnaire
mon_dict.clear()

# copy : crée une copie du dictionnaire
mon_dict2 = mon_dict.copy()

# Autres fonctions utiles

# len : nombre de paires clé/valeur
taille = len(mon_dict)

# in : teste si une clé existe dans le dictionnaire
existe = 'a' in mon_dict

# not in : teste si une clé n'existe pas
absente = 'z' not in mon_dict

# Création avec dict()
mon_dict = dict([('a', 1), ('b', 2)])

# sorted : trie les clés du dictionnaire (résultat = liste triée des clés)
cles_triees = sorted(mon_dict)

# Ajout / modification directe
mon_dict['nouvelle_cle'] = 'valeur'

# Parcours du dictionnaire
for cle in mon_dict:
    print(cle, mon_dict[cle])

for cle, valeur in mon_dict.items():
    print(f"Clé = {cle}, Valeur = {valeur}")




##################################################################################################################

# range est un générateur de suites de nombres entiers
# range permet de créer une séquence de nombres sans les stocker tous en mémoire
# range est souvent utilisé dans les boucles for pour répéter une action un certain nombre de fois
# range est itérable, mais ce n'est pas une liste, ni un type modifiable
# pour afficher les valeurs générées par un range, on doit le convertir en liste ou en tuple

# on a aussi la possibilité d'utiliser un slice (plage d’indices) pour récupérer un ensemble de valeurs d'une liste

# ici on va récupérer les valeurs de 0 à 3 (non inclus) dans la liste
ma_liste2 = ma_liste[0:3]  # renvoie les éléments de la liste de l'index 0 à 3 (non inclus)

# on peut préciser que l'on veut récupérer les valeurs jusqu'à un certain index
ma_liste2 = ma_liste[:3]  # renvoie les éléments de la liste de l'index 0 à 3 (non inclus)

# on peut aussi préciser que l'on veut récupérer les valeurs à partir d'un certain index
ma_liste2 = ma_liste[3:]  # renvoie les éléments de la liste de l'index 3 à la fin de la liste

# on peut aussi créer un clone facilement
ma_liste2 = ma_liste[:]  # copie superficielle (shallow copy) de la liste

# === Copie par valeur ou par référence ? ===
# Cette syntaxe [:] crée une nouvelle liste → donc la liste est copiée **par valeur**
# MAIS : les éléments à l'intérieur restent **par référence**
# → si les éléments sont des objets mutables (ex : listes, dictionnaires), ils ne sont pas clonés.
# Exemple :
# ma_liste = [[1, 2], [3, 4]]
# ma_liste2 = ma_liste[:]
# ma_liste2[0][0] = 99
# print(ma_liste)  # affiche [[99, 2], [3, 4]] → l'objet interne a été modifié

# on peut aussi préciser un pas pour récupérer les valeurs
# on va donner trois informations : le début, la fin et le pas
ma_liste2 = ma_liste[0:6:2]  # renvoie les éléments aux indices 0, 2, 4

# --- Utilisation de range ---

# range(stop) : génère les nombres de 0 jusqu'à stop (exclu)
list_value = range(5)  # génère 0, 1, 2, 3, 4
print(list(list_value))  # [0, 1, 2, 3, 4]

# range(start, stop) : génère les nombres de start jusqu'à stop (exclu)
list_value = range(2, 6)  # génère 2, 3, 4, 5
print(list(list_value))  # [2, 3, 4, 5]

# range(start, stop, step) : génère les nombres de start jusqu'à stop (exclu) avec un pas
list_value = range(0, 10, 2)  # génère 0, 2, 4, 6, 8
print(list(list_value))  # [0, 2, 4, 6, 8]

# range avec un pas négatif
list_value = range(10, 0, -2)  # génère 10, 8, 6, 4, 2
print(list(list_value))  # [10, 8, 6, 4, 2]

# convertir un range en liste
liste = list(range(4))  # [0, 1, 2, 3]

# convertir un range en tuple
list_value = tuple(range(3, 6))  # (3, 4, 5)

# === Copie ou pas avec range ? ===
# Attention : range() lui-même ne génère pas une liste en mémoire → c'est un objet itérable
# Quand on fait list(range(...)), on crée une **nouvelle liste** contenant les valeurs → donc **copie par valeur**


##################################################################################################################

import copy
# La fonction copy() permet de créer une copie superficielle (shallow copy) d'un objet.
# Cela signifie que les objets imbriqués (comme les listes à l'intérieur d'une liste) ne sont pas copiés, mais référencés.
# Si vous modifiez un objet imbriqué dans la copie, cela affectera également l'original.
# Pour créer une copie profonde (deep copy), utilisez copy.deepcopy().
# Cela crée une copie complète de l'objet, y compris tous les objets imbriqués.
# Cela signifie que les modifications apportées à la copie n'affecteront pas l'original.

# Exemple de copie superficielle
ma_liste = [[1, 2], [3, 4]]
ma_liste2 = copy.copy(ma_liste)  # copie superficielle
# ma_liste2[0][0] = 99  # modifie l'élément à l'index 0 de la première liste
# print(ma_liste)  # affiche [[99, 2], [3, 4]] → l'objet interne a été modifié

# Exemple de copie profonde
ma_liste = [[1, 2], [3, 4]]
ma_liste2 = copy.deepcopy(ma_liste)  # copie profonde
ma_liste2[0][0] = 99  # modifie l'élément à l'index 0 de la première liste
# print(ma_liste)  # affiche [[1, 2], [3, 4]] → l'objet interne n'a pas été modifié
# print(ma_liste2)  # affiche [[99, 2], [3, 4]] → l'objet interne a été modifié dans la copie profonde

