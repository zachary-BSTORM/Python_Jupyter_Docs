# Exo 14 — le lanceur de balles lance tant que le stock n'est pas vide

pret = False
stock_balles = 0

answer_ready = input("Etes vous prêt ? y - n : ")
pret = answer_ready == "y"          # la réponse texte devient un booléen

stock_balles = int(input("Combien de balles sont dans la machine ? "))

if pret:
    while stock_balles > 0:
        stock_balles -= 1
        print(f"Balle lancée ! (il en reste {stock_balles})")
    print("Stock vide, la machine s'arrête")
else:
    print("Revenez quand vous serez prêt")
