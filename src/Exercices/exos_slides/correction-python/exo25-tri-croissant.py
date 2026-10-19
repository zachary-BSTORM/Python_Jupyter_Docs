# Exo 25 — trier un tableau d'entiers dans l'ordre croissant (tri à bulles)
# Comparer chaque paire de voisins, échanger s'ils sont dans le mauvais ordre :
# à chaque passage, le plus grand « remonte » à la fin comme une bulle.

T = [29, 3, 15, 8, 22, 1]
taille = len(T)

print(f"Avant : {T}")

for passage in range(1, taille):
    # après chaque passage, la fin du tableau est déjà en place :
    # inutile d'y repasser → on s'arrête à taille - passage
    for i in range(taille - passage):
        if T[i] > T[i + 1]:                     # mauvais ordre → échange
            T[i], T[i + 1] = T[i + 1], T[i]

print(f"Après : {T}")        # [1, 3, 8, 15, 22, 29]

# (T.sort() fait le travail en une ligne — mais l'exercice demande L'ALGORITHME)
