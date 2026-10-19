# Exo 21 — « C'est plus, c'est moins » en boucle jusqu'à trouver le juste prix
# L'ordinateur choisit un nombre entre 1 et 100 ; on compte les tentatives

import random

juste_prix = random.randrange(1, 101, 1)   # un nombre entre 1 et 100
proposition = 0                            # 0 est impossible → on entre forcément dans la boucle
tentatives = 0

while proposition != juste_prix:
    proposition = int(input("Entrez un nombre entre 1 et 100 : "))
    tentatives += 1

    if proposition < juste_prix:
        print("C'est plus")
    elif proposition > juste_prix:
        print("C'est moins")

print(f"C'est gagné en {tentatives} tentatives !")
