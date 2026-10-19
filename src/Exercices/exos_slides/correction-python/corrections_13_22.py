"""
exo13-À l’aide d’une boucle, afficher la table de multiplication par 2. 
Ensuite, coder votre algorithme en Python.
- récupérer la table à afficher 
- récupérer le nombre d'éléments à afficher
"""
# =====================================================================
# exo13 - Table de multiplication
# =====================================================================
table = int(input("Quelle table voulez-vous afficher ? "))
nb_elements = int(input("Combien d'éléments afficher ? "))

for i in range(1, nb_elements + 1):
    print(f"{i} x {table} = {i * table}")


"""
exo14-Reprenez l’algorithme du lanceur de balles de tennis et
faites en sorte qu’il lance une balle tant que le stock n’est pas vide.
Il y a donc 2 variables stock_balles et pret , panier_vide

- afficher à chaque balle lancé le nombre de balle restante
- afficher un message lors de l'arret
"""
# =====================================================================
# exo14 - Lanceur de balles de tennis
# =====================================================================
stock_balles = int(input("Nombre de balles dans le stock : "))
pret = True
panier_vide = stock_balles == 0

while pret and not panier_vide:
    stock_balles -= 1
    print(f"Balle lancée ! Il reste {stock_balles} balle(s).")
    if stock_balles == 0:
        panier_vide = True

print("Arrêt du lanceur : le panier est vide.")


"""
• exo15-À l’aide de deux boucles, 
afficher les tables de multiplication de 1 à 9. 
Ensuite, coder votre algorithme en Python.
"""
# =====================================================================
# exo15 - Tables de multiplication de 1 à 9 (deux boucles imbriquées)
# =====================================================================
for table in range(1, 10):
    print(f"--- Table de {table} ---")
    for i in range(1, 11):
        print(f"{i} x {table} = {i * table}")
    print()


"""
Jeu du plus ou moins

Génération d'un nombre aléatoire 
- from random import randint
result = randint(1,10)

dans une boucle 
    - demander à l'utilisateur d'entrez une valeur
    - afficher plus ou moins 
    - compter le nombre coups
    
    - afficher un message lorsqu'il à trouvez le nombre avec le nombre de coups
"""
# =====================================================================
# Jeu du plus ou moins (1 à 10)
# =====================================================================
from random import randint

result = randint(1, 10)
nb_coups = 0
proposition = 0

while proposition != result:
    proposition = int(input("Entrez un nombre entre 1 et 10 : "))
    nb_coups += 1
    if proposition < result:
        print("C'est plus !")
    elif proposition > result:
        print("C'est moins !")

print(f"Bravo, vous avez trouvé {result} en {nb_coups} coup(s) !")

"""
exo17-À l’aide d’une boucle TantQue … Faire, améliorez l’algorithme du distributeur
de boissons pour qu’il demande au client s’il désire une autre boisson (Tant qu’il en a
envie).
"""
# =====================================================================
# exo17 - Distributeur de boissons en boucle
# =====================================================================
continuer = "o"

while continuer == "o":
    print("1. Café")
    print("2. Thé")
    print("3. Chocolat chaud")
    choix = input("Votre choix : ")

    if choix == "1":
        print("Voici votre café.")
    elif choix == "2":
        print("Voici votre thé.")
    elif choix == "3":
        print("Voici votre chocolat chaud.")
    else:
        print("Choix invalide.")

    continuer = input("Désirez-vous une autre boisson ? (o/n) : ").lower()

print("Merci, à bientôt !")


"""
• exo18-À l’aide d’une boucle TantQue … Faire, améliorez l’algorithme de la
calculatrice afin qu’elle demande à l’utilisateur s’il veut faire un autre calcul (tant
qu’il le désire).
"""
# =====================================================================
# exo18 - Calculatrice en boucle
# =====================================================================
continuer = "o"

while continuer == "o":
    a = float(input("Premier nombre : "))
    operateur = input("Opérateur (+, -, *, /) : ")
    b = float(input("Second nombre : "))

    if operateur == "+":
        print(f"Résultat : {a + b}")
    elif operateur == "-":
        print(f"Résultat : {a - b}")
    elif operateur == "*":
        print(f"Résultat : {a * b}")
    elif operateur == "/":
        if b == 0:
            print("Erreur : division par zéro impossible.")
        else:
            print(f"Résultat : {a / b}")
    else:
        print("Opérateur inconnu.")

    continuer = input("Voulez-vous faire un autre calcul ? (o/n) : ").lower()

print("Fin de la calculatrice.")


"""
• exo19-À l’aide de la boucle TantQue … Faire, réalisez un algorithme calculant le
résultat de N10. N étant un nombre saisi par l’utilisateur.
"""
# =====================================================================
# exo19 - Calcul de N^10 avec une boucle while
# =====================================================================
n = int(input("Entrez un nombre N : "))
resultat = 1
compteur = 0

while compteur < 10:
    resultat *= n
    compteur += 1

print(f"{n}^10 = {resultat}")


"""
• exo20-Reprenez l’exercice précédent et modifiez-le pour que l’utilisateur entre
également l’exposant qu’il désire calculer.
"""
# =====================================================================
# exo20 - Calcul de N^exposant
# =====================================================================
n = int(input("Entrez un nombre N : "))
exposant = int(input("Entrez l'exposant (entier positif) : "))
resultat = 1
compteur = 0

while compteur < exposant:
    resultat *= n
    compteur += 1

print(f"{n}^{exposant} = {resultat}")


"""
• exo21-Améliorez le "C'est plus, c'est moins, c'est gagné" pour qu'il tourne en boucle tant que le juste_prix n'a pas été trouvé.
L'ordinateur choisit un nombre aléatoirement entre 1 et 100. L'utilisateur est invité à entrer un nombre et l'algorithme nous
répond "C'est plus" ou "C'est moins". Lorsqu'on a trouvé le bon nombre, l'algorithme affiche le nombre de tentatives
effectuées pour trouver le résultat
"""
# =====================================================================
# exo21 - Juste prix (1 à 100) en boucle
# =====================================================================
from random import randint

juste_prix = randint(1, 100)
tentatives = 0
proposition = 0

while proposition != juste_prix:
    proposition = int(input("Entrez un nombre entre 1 et 100 : "))
    tentatives += 1
    if proposition < juste_prix:
        print("C'est plus !")
    elif proposition > juste_prix:
        print("C'est moins !")

print(f"C'est gagné ! Trouvé en {tentatives} tentative(s).")


"""
Exercices supplémentaires:
• 1) Réalisez un système de connexion à l'aide d'un mot de passe. L'algorithme demande à l'utilisateur de saisir son mot de
passe. Si ce dernier valide de bon mot de passe, on le salue. Par contre, si il fait une erreur trois fois de suite, un message lui
signalera que son compte est bloqué et il ne pourra pas réessayer une quatrième fois
"""
# =====================================================================
# Supplémentaire 1 - Connexion par mot de passe (3 essais)
# =====================================================================
MOT_DE_PASSE = "python123"
essais = 0
connecte = False

while essais < 3 and not connecte:
    saisie = input("Mot de passe : ")
    essais += 1
    if saisie == MOT_DE_PASSE:
        connecte = True
    else:
        print(f"Mot de passe incorrect ({essais}/3).")

if connecte:
    print("Bienvenue !")
else:
    print("Votre compte est bloqué.")
    

"""
• 2) Réalisez un algorithme qui demande un nombre à l'utilisateur et affiche autant de ligne que le nombre spécifié par
l'utilisateur.Exemple : l'utilisateur a rentré le nombre 5 et l'algorithme affiche :
*
**
***
****
*****
"""

# =====================================================================
# Supplémentaire 2 - Triangle d'étoiles
# =====================================================================
nombre = int(input("Entrez un nombre : "))

for i in range(1, nombre + 1):
    print("*" * i)

# Variante avec deux boucles (plus "algorithmique") :
# for i in range(1, nombre + 1):
#     ligne = ""
#     for j in range(i):
#         ligne += "*"
#     print(ligne)


"""
• 3) Ecrire un algorithme qui demande à l’utilisateur de taper 10 entiers et qui affiche le plus petit de ces entiers.

"""
# =====================================================================
# Supplémentaire 3 - Plus petit de 10 entiers (sans min())
# =====================================================================
plus_petit = int(input("Entier 1 : "))

for i in range(2, 11):
    nombre = int(input(f"Entier {i} : "))
    if nombre < plus_petit:
        plus_petit = nombre

print(f"Le plus petit entier est : {plus_petit}")


"""
• 4) Algorithme demandant 3 nombres : nbRep, nbTiret, nbEspace. Ce dernier affiche à l'écran autant de tiret que la valeur de
nbTiret, suivi d'autant d'espace que la valeur de nbEspace. Le tout autant de fois que la valeur de nbRep.Exemple : si nbRep
= 2, nbTiret = 1 et nbEspace = 3 le résultat est le suivant :|- - |
110
Projet : juste_prix
• Améliorez encore le juste_prix : l'utilisateur a droit à 10 essais après ces 10
essais, il a perdu.
• L'ordinateur affiche le juste_prix
• Ajouter un niveau :
– facile : entre 1 et 10
– moyen : entre 1 et 100
– difficile : entre 1 et 1000
• Tant que la personne veut rejouer, redemandez le niveau et générez un
nombre.
• Vérifiez que tout caractère entré est correct, c'est-à-dire pour que le
programme ne plante jamais.
111

Indices
• Pour générer un nombre entre 0 et 10, il faut 2
choses :
– import random
– juste_prix = random.randrange(0, 11, 1)
• Pour effacer l'écran, il faut 2 choses :
– import os
– os.system('cls')

Indices
• Pour vérifier qu'une chaine de caractères est
un nombre :
– chaine = "4"
– if chaine.isdigit() :
print("C'est un nombre")
else :
print("Ce n'est pas un nombre")
"""

# =====================================================================
# Supplémentaire 4 - Tirets et espaces répétés
# =====================================================================
nb_rep = int(input("Nombre de répétitions : "))
nb_tiret = int(input("Nombre de tirets : "))
nb_espace = int(input("Nombre d'espaces : "))

motif = ""
for i in range(nb_rep):
    motif += "-" * nb_tiret + " " * nb_espace

print(f"|{motif}|")



# =====================================================================
# PROJET - Juste prix complet
# (10 essais, niveaux, rejouer, saisie sécurisée)
# =====================================================================
import os
import random

rejouer = "o"

while rejouer == "o":
    os.system("cls")
    print("=== JUSTE PRIX ===")
    print("1. Facile    (1 - 10)")
    print("2. Moyen     (1 - 100)")
    print("3. Difficile (1 - 1000)")

    # Choix du niveau sécurisé
    niveau = input("Choisissez un niveau (1, 2 ou 3) : ")
    while niveau not in ("1", "2", "3"):
        niveau = input("Choix invalide. Entrez 1, 2 ou 3 : ")

    if niveau == "1":
        borne_max = 10
    elif niveau == "2":
        borne_max = 100
    else:
        borne_max = 1000

    juste_prix = random.randrange(1, borne_max + 1, 1)
    max_essais = 10
    essais = 0
    trouve = False

    while essais < max_essais and not trouve:
        saisie = input(f"Essai {essais + 1}/{max_essais} - Votre proposition (1-{borne_max}) : ")

        # Saisie non numérique : on redemande sans consommer d'essai
        if not saisie.isdigit():
            print("Veuillez entrer un nombre entier positif.")
            continue

        proposition = int(saisie)

        # Hors bornes : on redemande sans consommer d'essai
        if proposition < 1 or proposition > borne_max:
            print(f"Le nombre doit être compris entre 1 et {borne_max}.")
            continue

        essais += 1

        if proposition < juste_prix:
            print("C'est plus !")
        elif proposition > juste_prix:
            print("C'est moins !")
        else:
            trouve = True
            print(f"C'est gagné ! Trouvé en {essais} essai(s).")

    if not trouve:
        print(f"Perdu ! Le juste prix était {juste_prix}.")

    # Demande pour rejouer, sécurisée
    rejouer = input("Voulez-vous rejouer ? (o/n) : ").lower()
    while rejouer not in ("o", "n"):
        rejouer = input("Répondez par 'o' ou 'n' : ").lower()

print("Merci d'avoir joué !")