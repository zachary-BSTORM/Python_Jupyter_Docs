# Exo 27 — déplacer un pion dans un tableau de 10 cases
# g = gauche, d = droite, q = quitter — le pion ne sort jamais du tableau
# (à exécuter dans la console Windows : cls redessine l'écran à chaque tour)
import msvcrt as m
import os

position = 0
commande = ""

while commande != "q":
    os.system("cls")                    # efface l'écran (Windows)

    # dessiner le tableau : [P] pour le pion, [ ] ailleurs
    ligne = ""
    for i in range(10):
        if i == position:
            ligne += "[P]"
        else:
            ligne += "[ ]"
    print(ligne)

    # commande = input("g = gauche | d = droite | q = quitter : ")
    # récupère le caractère sous la forme de byte
    char = m.getch()
    # convertir de bytes en string
    commande = char.decode("ascii")
    print(commande)

    if commande == "d" and position < 9:        # rester dans le tableau !
        position += 1
    elif commande == "q" and position > 0:
        position -= 1

print("Fin de partie")


# ==========================================================
# 2d

# import msvcrt as m
# import os

# # [ligne, colonne] — une LISTE, pas un tuple : 0,0 crée un tuple, immuable,
# # et position[0] = ... planterait en TypeError !
# position = [0, 0]
# commande = ""

# plateau = []

# for _ in range(10):
#     list_to_add = []
#     for _ in range(10):
#         list_to_add.append(0)
#     plateau.append(list_to_add)

# plateau[position[0]][position[1]] = 1   # placer le pion au départ

# # Échap (\x1b) pour quitter — q est pris par « gauche » en ZQSD !
# while commande != "\x1b":
#     os.system("cls")                    # efface l'écran (Windows)

#     for l in plateau:
#         for v in l:
#             print(v , end=" ")
#         print()
#     print("z = haut | s = bas | q = gauche | d = droite | Échap = quitter")

#     # récupère le caractère sous la forme de byte
#     char = m.getch()
#     # convertir de bytes en string — errors="ignore" : les flèches envoient
#     # un octet non-ascii (\xe0) qui ferait planter decode ; .lower() : Z = z
#     commande = char.decode("ascii", errors="ignore").lower()
#     print(commande)

#     plateau[position[0]][position[1]] = 0       # éteindre l'ancienne case

#     if commande == "d" and position[1] < 9:     # droite → colonne + 1
#         position[1] = position[1] + 1
#     elif commande == "q" and position[1] > 0:   # gauche → colonne - 1
#         position[1] = position[1] - 1
#     elif commande == "z" and position[0] > 0:   # haut   → ligne - 1
#         position[0] = position[0] - 1
#     elif commande == "s" and position[0] < 9:   # bas    → ligne + 1
#         position[0] = position[0] + 1

#     plateau[position[0]][position[1]] = 1       # rallumer la nouvelle case

# print("FFin de partie")
