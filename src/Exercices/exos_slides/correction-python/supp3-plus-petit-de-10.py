# Supplémentaire 3 — lire 10 entiers et afficher le plus petit
# Le premier entier devient le plus petit provisoire,
# puis chaque nouvel entier plus petit prend sa place

nombre = int(input("Entier 1/10 : "))
plus_petit = nombre

for i in range(2, 11):
    nombre = int(input(f"Entier {i}/10 : "))
    if nombre < plus_petit:
        plus_petit = nombre

print(f"Le plus petit est {plus_petit}")
