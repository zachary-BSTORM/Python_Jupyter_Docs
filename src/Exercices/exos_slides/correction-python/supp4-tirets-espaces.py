# Supplémentaire 4 — nbRep, nbTiret, nbEspace :
# nbTiret tirets suivis de nbEspace espaces, le tout répété nbRep fois
# Exemple : nbRep = 2, nbTiret = 1, nbEspace = 3  →  |-   -   |
# (les barres | ne sont là que pour visualiser les espaces en fin de ligne)

nb_rep = int(input("Entrez nbRep : "))
nb_tiret = int(input("Entrez nbTiret : "))
nb_espace = int(input("Entrez nbEspace : "))

motif = "-" * nb_tiret + " " * nb_espace    # un bloc : les tirets puis les espaces
print(motif * nb_rep)                       # ... répété nbRep fois
