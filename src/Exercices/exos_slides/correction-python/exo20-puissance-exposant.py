# Exo 20 — reprise de l'exo 19 : l'utilisateur entre aussi l'exposant

n = int(input("Entrez un nombre N : "))
exposant = int(input("Entrez l'exposant : "))

resultat = 1
compteur = 0

while compteur < exposant:
    resultat = resultat * n
    compteur += 1

print(f"{n}^{exposant} = {resultat}")
