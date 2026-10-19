# Exo 19 — N^10 avec une boucle while : on multiplie 10 fois le résultat par N

n = int(input("Entrez un nombre N : "))

resultat = 1
compteur = 0

while compteur < 10:
    resultat = resultat * n
    compteur += 1

print(f"{n}^10 = {resultat}")
