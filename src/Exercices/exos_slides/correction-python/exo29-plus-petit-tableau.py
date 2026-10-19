# Exo 29 — le plus petit de 10 entiers, version TABLEAU
# Deux phases bien séparées : 1) tout stocker, 2) chercher le minimum
# (on ne retient RIEN pendant la saisie, contrairement à l'exercice précédent)

# Phase 1 : la saisie — on se contente de remplir la liste
T = []
for i in range(1, 11):
    valeur = int(input(f"Entier {i}/10 : "))
    T.append(valeur)

# Phase 2 : la recherche — le premier élément est le minimum provisoire
plus_petit = T[0]
for valeur in T:
    if valeur < plus_petit:
        plus_petit = valeur

print(f"Le plus petit est {plus_petit}")
# (en Python : min(T) — mais ici on fait L'ALGORITHME)
