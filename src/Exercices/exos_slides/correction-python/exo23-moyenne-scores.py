# Exo 23 — moyenne des scores (max 10 joueurs)
# On stocke les scores dans une liste, puis on calcule la moyenne

nb_joueurs = 0

# redemander tant que le nombre n'est pas entre 1 et 10
while nb_joueurs < 1 or nb_joueurs > 10:
    nb_joueurs = int(input("Combien de joueurs ? (1 à 10) : "))

scores = []
for i in range(1, nb_joueurs + 1):
    score = int(input(f"Score du joueur {i} : "))
    scores.append(score)

total = 0
for score in scores:
    total += score

print(f"Moyenne des scores : {total / nb_joueurs}")
# (en Python, sum(scores) / len(scores) donne le même résultat en une ligne)
