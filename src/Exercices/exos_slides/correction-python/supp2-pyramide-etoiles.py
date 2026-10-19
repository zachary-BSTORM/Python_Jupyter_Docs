# Supplémentaire 2 — autant de lignes d'étoiles que le nombre saisi
# Exemple avec 5 :
# *
# **
# ***
# ****
# *****

nombre = int(input("Entrez un nombre : "))

for i in range(1, nombre + 1):
    print("*" * i)      # l'opérateur * sur une string RÉPÈTE le texte : la ligne i a i étoiles
