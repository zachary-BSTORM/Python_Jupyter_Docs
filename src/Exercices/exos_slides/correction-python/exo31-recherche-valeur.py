# Exo 31 — rechercher une valeur entrée par l'utilisateur
# Variante de l'exo 28 : avec un DRAPEAU booléen « trouve » —
# l'autre grand classique de la recherche séquentielle

T = [7, 42, 13, 5, 28, 19]

print(f"Tableau : {T}")
valeur = int(input("Quelle valeur cherchez-vous ? "))

trouve = False
for element in T:
    if element == valeur:
        trouve = True

if trouve:
    print(f"{valeur} est bien dans le tableau")
else:
    print(f"{valeur} n'est pas dans le tableau")

# (en Python, le test « valeur in T » fait exactement ça en une ligne)
