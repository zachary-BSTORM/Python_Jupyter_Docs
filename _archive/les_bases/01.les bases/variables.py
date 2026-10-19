# Declaration de variables 

# les variables sont des espaces de stockage qui permettent de conserver des valeurs
# le type permet de determiner l'espace de stockage utilisé pour la variable

# leurs noms doivent commencer par une lettre ou un underscore et ne peuvent pas contenir d'espace
# les variables peuvent contenir des lettres, des chiffres et des underscores
# la convention est d'utiliser le "snake_case" pour les noms de variables
# les variables ne peuvent pas commencer par un chiffre
# par exemple : ma_variable, ma_variable_2, ma_variable_3

# les variables sont sensibles à la casse, c'est à dire que "a" et "A" sont deux variables différentes
# les constantes n'existent pas en python

# le type de la variable est déterminé par la valeur qu'elle contient et permet de savoir quel type d'opération on peut effectuer sur cette variable
# (par exemple on ne peut pas additionner une chaine de caracteres avec un entier)

# l'affectation d'une valeur à une variable se fait avec le signe égal (=)
# python permet l'affectation multiple, c'est à dire qu'on peut affecter plusieurs valeurs à plusieurs variables en une seule ligne
# par exemple : a, b, c = 1, 2, 3

# ################################################################################################################

# les variables peuvent contenir des valeurs de differents types

# pour declarer une variable, on utilise le nom de la variable suivi du signe égal (=) et de la valeur à affecter

# par exemple :
ma_variable = 1
ma_variable_2 = "a"
ma_variable_3 = True


# on peut aussi affecter plusieurs valeurs à plusieurs variables en une seule ligne

# par exemple : 
a, b, c = 1, 2, 3
j,k,l = "a", "b", "c"

# les types de base sont :

# - entier : 1, 2, 3, 4, 5
value_int = 1


# - flottant : 1.0, 2.5, 3.14, 4.0 ( un point  à cause de la norme internationale qui impose d'utiliser le point comme séparateur décimal)
value_float = 1.0


# - chaine de caracteres : "a", "b", "c", "d"
value_string = "a"


# - valeur Unicode : "a", "b", "c", "d" (permet d'utiliser des caracteres spéciaux comme les accents ou les caracteres chinois)
value_unicode = "\U0001F44B"


# - booleen : True, False
value_bool = True


# - chaine de caracteres multilignes : """a""" ou '''a''' (permet d'écrire des chaines de caracteres sur plusieurs lignes)
value_string = """a
b
c
"""


# - chaine de caracteres formatée : f"Hello {name}" ou "Hello {}".format(name) 
# (permet d'insérer des variables dans une chaine de caracteres)

message = "chimichanga"
value_string_2 = f"Hello {message}"


# - chaine de caracteres brut : r"Hello {name}" ou r"Hello {}".format(name) 
# (permet d'écrire des chaines de caracteres sans interpréter les caractères spéciaux comme les \n ou les \t)

adresse = r"C:\Users\user\Documents\file.txt"


# - None : None (représente une valeur nulle ou l'absence de valeur)
value_none = None


# - type qui nous permet de renvoyer le type de la variable

value_inconnu = 5
print(type(value_inconnu)) 
# Affiche <class 'int'>, ce qui signifie que value_inconnu est de type entier


# function qui permet d'enregistrer une action specifique afin de la rappeler plus tard
func = print("Hello world") # Affiche "Hello world" dans la console



##################################################################################################################

#pour verifier le type d'une variable, on peut utiliser la fonction type()

value_test = 5
print(type(value_test))

# affiche <class 'int'>, 
# ce qui signifie que value_test est de type entier
#les chevrons <> indiquent que c'est une classe
#Le format <...> permet de distinguer rapidement l'information d’un simple texte.


##################################################################################################################

# utilisation de la console pour afficher ou récuperer des informations

# afficher la valeur d'une variable dans la console
value_to_display = "Hello world"
print(value_to_display)


#recuperer une valeur dans la console
input_value = input("Entrez une valeur : ") 


# Demande à l'utilisateur de saisir une valeur
text = input("Entrez une valeur : ")

text = text + " hello "
print(text)


# python offre la possibilité d'ajouter des arguments , un separateur et un séparateur de fin de ligne
# pour cela on utilise les arguments sep et end de la fonction print()
# sep : permet de définir le séparateur entre les valeurs à afficher
# end : permet de définir le séparateur de fin de ligne (par défaut c'est \n)
# exemple d'utilisation de sep et end

nb = 5
print("le nombre est", nb, sep=" - ", end="!")


##################################################################################################################

# Tout ce que nous allons recuperer ou afficher dans la console est de type chaîne de caractères
# il n'est pas necessaire de convertir une valeur pour l'afficher dans la console
# mais dans certains cas , nous avons besoin de convertir une valeur de type str en int ou float

# pour convertir une valeur d'un type à un autre, on peut utiliser les fonctions int(), float(), str(), bool()

# on remarque que l'on utilise le type dans lequel on veut convertir la valeur comme methode de conversion


# int() : convertit une valeur en entier
value_str = input("Entrez une valeur : ")
value_int = int(value_str) # Convertit la valeur saisie en entier
print(type(value_int))


# float() : convertit une valeur en flottant
value_str_2 = input("Entrez une valeur : ")
value_float = float(value_str_2) # Convertit la valeur saisie en flottant
print(type(value_float))


# str() : convertit une valeur en chaine de caracteres
value_int = int(input("Entrez une valeur : "))
value_str = str(value_int) # Convertit la valeur entière en chaine de caracteres
print(type(value_str))


# bool() : convertit une valeur en booleen
value_str_3 = input("Entrez une valeur : ")
value_bool = bool(value_str_3) # Convertit la valeur saisie en booleen
print(type(value_bool))


# unicode() : convertit une valeur en unicode
# les chaines de caracteres sont déjà en unicode, donc pas besoin de conversion depuis python 3
# value_unicode = unicode(value_str) # Convertit la valeur saisie en unicode etait utilisé avant python 3
# mais n'est plus nécessaire depuis python 3
# Unicode est une norme internationale (ISO 10646) qui définit un système de codage universel pour représenter tous les caractères des langues du monde, 
# ainsi que des symboles, emojis, ponctuations, etc.