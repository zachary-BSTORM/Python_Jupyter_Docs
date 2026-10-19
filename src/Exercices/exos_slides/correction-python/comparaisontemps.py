secondes_1 = None
minutes_1 = None
heures_1 = None
jours_1 = None

secondes_2 = None
minutes_2 = None
heures_2 = None
jours_2 = None

secondes_1 = int(input("entrez les secondes de la première valeur : "))
minutes_1 = int(input("entrez les minutes de la première valeur : "))
heures_1 = int(input("entrez les heures de la première valeur : "))
jours_1 = int(input("entrez les jours de la première valeur : "))

secondes_2 = int(input("entrez les secondes de la deuxième valeur : "))
minutes_2 = int(input("entrez les minutes de la deuxième valeur : "))
heures_2 = int(input("entrez les heures de la deuxième valeur : "))
jours_2 = int(input("entrez les jours de la deuxième valeur : "))

# Conversion de chaque durée en secondes
secs_1 = secondes_1 + minutes_1 * 60 + heures_1 * 3600 + jours_1 * 86400
secs_2 = secondes_2 + minutes_2 * 60 + heures_2 * 3600 + jours_2 * 86400

# Différence toujours positive : on soustrait la plus petite de la plus grande
if secs_1 > secs_2:
    total_diff = secs_1 - secs_2
else:
    total_diff = secs_2 - secs_1

# Reconversion en jours / heures / minutes / secondes
jours_diff = total_diff // 86400
reste = total_diff % 86400

heures_diff = reste // 3600
reste = reste % 3600

minutes_diff = reste // 60
secondes_diff = reste % 60

print(f"la différence est de {jours_diff}j {heures_diff}h {minutes_diff}m {secondes_diff}s")