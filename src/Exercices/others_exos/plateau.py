import os

plate = [[0] * 10 for _ in range(10)]   # 10 lignes indépendantes de 10 zéros
x = 0                                   # ligne   (0 = en haut de l'écran)
y = 0                                   # colonne (0 = à gauche)
plate[x][y] = 1

direction = ""
while direction != "Q":
    os.system('cls')
    for ligne in plate:
        print(ligne)

    direction = input("Direction : N - S - E - O (Q pour quitter) : ").strip().upper()

    plate[x][y] = 0                     # éteindre l'ancienne position...
    match direction:
        case "N":
            if x > 0:                   # le nord = MONTER = ligne - 1
                x -= 1
        case "S":
            if x < 9:
                x += 1
        case "E":
            if y < 9:
                y += 1
        case "O":
            if y > 0:
                y -= 1
        case "Q":
            print("Fin de partie")
        case _:
            print("Direction inconnue")
    plate[x][y] = 1 