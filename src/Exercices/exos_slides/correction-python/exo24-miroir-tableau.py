# Exo 24 — inverser un tableau (effet miroir)
# Échanges deux à deux : le premier avec le dernier, etc., jusqu'au milieu

taille = int(input("Combien d'éléments ? "))

T = []
for i in range(1, taille + 1):
    valeur = int(input(f"Élément {i} : "))
    T.append(valeur)

# échanges jusqu'au MILIEU seulement (sinon on ré-inverse tout !)
for i in range(taille // 2):
    T[i], T[taille - 1 - i] = T[taille - 1 - i], T[i]   # échange sans variable temporaire

print(f"Tableau inversé : {T}")

# Versions « tout Python » équivalentes :
#   T.reverse()   → inverse la liste sur place
#   T[::-1]       → renvoie une NOUVELLE liste inversée (slicing à pas -1)
