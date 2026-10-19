# Exo 30 — insérer une valeur dans un tableau TRIÉ, directement à la bonne place
# Interdit d'insérer à la fin puis de trier : on cherche la position, puis insert

T = [2, 5, 9, 14, 20]           # trié dans l'ordre croissant

print(f"Tableau : {T}")
valeur = int(input("Valeur à insérer ? "))

# avancer tant que les éléments sont plus petits que la valeur
position = 0
while position < len(T) and T[position] < valeur:
    position += 1

# insérer À cette position : insert décale les suivants vers la droite
# (si la valeur est plus grande que tout, position == len(T) → insertion en fin)
T.insert(position, valeur)

print(f"Tableau après insertion : {T}")
