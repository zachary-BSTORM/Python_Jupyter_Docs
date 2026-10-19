# Supplémentaire 1 — connexion par mot de passe : 3 erreurs de suite → compte bloqué

MOT_DE_PASSE = "python123"   # « constante » : convention des majuscules

essais = 0
connecte = False

while essais < 3 and not connecte:
    saisie = input("Entrez votre mot de passe : ")

    if saisie == MOT_DE_PASSE:
        connecte = True
    else:
        essais += 1
        print(f"Mot de passe incorrect ({essais}/3)")

if connecte:
    print("Bonjour, content de vous revoir !")
else:
    print("Votre compte est bloqué")
