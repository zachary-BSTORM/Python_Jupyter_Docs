# Exo 15 — les tables de multiplication de 1 à 9, avec deux boucles

for table in range(1, 10):
    print(f"--- Table de {table} ---")
    for i in range(1, 11):
        print(f"{table} x {i} = {table * i}")
