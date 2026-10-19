# Exo 26 — fusionner deux tableaux NON triés dans un troisième, trié
# Le tri se fait PENDANT la fusion : à chaque tour on retire le plus grand
# élément restant des deux tableaux et on l'ajoute à tab3.
# tab3 se construit donc en ordre DÉCROISSANT → l'indice de l'énoncé :
# tab3.reverse() le retourne en croissant (retourner n'est pas trier !).

tab1 = [8, 3, 15, 1]
tab2 = [12, 5, 20, 3, 2]      # un 3 dans chaque tableau : les doublons sont conservés
tab3 = []

# ⚠ cette version VIDE tab1 et tab2 (remove) — c'est le principe de l'algorithme
while len(tab1) > 0 or len(tab2) > 0:

    if len(tab1) == 0:                  # tab1 épuisé → le plus grand est dans tab2
        plus_grand = max(tab2)
        tab2.remove(plus_grand)
    elif len(tab2) == 0:                # tab2 épuisé → le plus grand est dans tab1
        plus_grand = max(tab1)
        tab1.remove(plus_grand)
    elif max(tab1) >= max(tab2):        # les deux ont encore des éléments : on compare
        plus_grand = max(tab1)
        tab1.remove(plus_grand)
    else:
        plus_grand = max(tab2)
        tab2.remove(plus_grand)

    tab3.append(plus_grand)             # tab3 : du plus grand au plus petit

tab3.reverse()                          # décroissant → croissant

print(tab3)                             # [1, 2, 3, 3, 5, 8, 12, 15, 20]


# --- Variante (sans reverse) : insertion à la bonne position ---
# Pour chaque élément, on avance dans tab3 tant que les valeurs sont plus
# petites, puis on insère : tab3 reste trié en permanence.

tab1 = [8, 3, 15, 1]
tab2 = [12, 5, 20, 3, 2]
tab3 = []

for element in tab1 + tab2:             # + concatène : on parcourt les 2 tableaux
    position = 0
    while position < len(tab3) and tab3[position] < element:
        position += 1
    tab3.insert(position, element)      # insère et décale le reste vers la droite

print(tab3)                             # [1, 2, 3, 3, 5, 8, 12, 15, 20]
