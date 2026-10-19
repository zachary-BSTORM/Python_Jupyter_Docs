# Exo 28 — rechercher une valeur et afficher sa POSITION
# Recherche séquentielle avec un indice : on avance tant qu'on n'a pas trouvé

T = [12, 5, 8, 20, 8, 3]

print(f"Tableau : {T}")
valeur = int(input("Quelle valeur cherchez-vous ? "))

i = 0
while i < len(T) and T[i] != valeur:
    i += 1

# en sortie de boucle : soit T[i] == valeur (trouvé),
# soit i == len(T) (tout parcouru sans trouver)
if i < len(T):
    print(f"{valeur} se trouve en position {i}")    # position de la 1re occurrence
else:                                               # (les positions commencent à 0)
    print(f"{valeur} n'est pas dans le tableau")

# (en Python, T.index(valeur) donne la position — mais ici on fait L'ALGORITHME)
