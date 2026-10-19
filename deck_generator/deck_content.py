# -*- coding: utf-8 -*-
"""Python - Base (enrichi) — génération du deck au style bstorm Training."""
from pathlib import Path

from pptx.enum.text import PP_ALIGN
from pptx.util import Pt

import deck_lib as L
from deck_lib import (ASSETS, GREEN, PURPLE, TEXT, add_bonus_tag, add_code,
                      add_footer, add_paragraphs, add_slide_title, add_table,
                      add_textbox, blank_slide, new_presentation, no_bullet,
                      rich_runs, set_bullet, style_run)

OUT = Path(__file__).parent.parent / "Python - Base (enrichi).pptx"


# ================================================================ types de slides
def slide_titre(prs):
    s = blank_slide(prs)
    box, tf = add_textbox(s, 0, 128, 720, 70)
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    style_run(p.add_run(), "Python", font=L.TITLE_FONT, size=52, color=GREEN, bold=True)
    box, tf = add_textbox(s, 0, 200, 720, 40)
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    style_run(p.add_run(), "Base", font=L.TITLE_FONT, size=27, color=PURPLE, bold=True)
    s.shapes.add_picture(str(ASSETS / "logo_training.png"), Pt(14), Pt(322), height=Pt(72))


def slide_marque(prs):
    s = blank_slide(prs)
    s.shapes.add_picture(str(ASSETS / "qui_sommes_nous.png"), 0, 0,
                         width=L.SLIDE_W, height=L.SLIDE_H)


def slide_section(prs, num, titre):
    s = blank_slide(prs)
    box, tf = add_textbox(s, 0, 178, 720, 50)
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    style_run(p.add_run(), titre, font=L.TITLE_FONT, size=28, color=PURPLE, bold=False)
    add_footer(s, num)


def slide_toc(prs, num, titre, col_gauche, col_droite):
    s = blank_slide(prs)
    add_slide_title(s, titre)
    for items, x in ((col_gauche, 42), (col_droite, 375)):
        box, tf = add_textbox(s, x, 92, 320, 280)
        for i, (lvl, text) in enumerate(items):
            p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
            p.line_spacing = 1.0
            if lvl == 0:
                set_bullet(p, "➔", 0, size_pct=85)
                p.space_before = Pt(9)
                p.space_after = Pt(3)
                rich_runs(p, text, size=14.5)
            else:
                set_bullet(p, "◆", 1, size_pct=70)
                p.space_after = Pt(2.5)
                rich_runs(p, text, size=13)
    add_footer(s, num)


def slide_contenu(prs, num, titre, blocks, bonus=False, body_size=15):
    s = blank_slide(prs)
    add_slide_title(s, titre)
    if bonus:
        add_bonus_tag(s)
    y = 86.0
    for block in blocks:
        kind = block[0]
        if kind == "txt":
            h = add_paragraphs(s, block[1], 30, y, 660, size=body_size)
            y += h + 8
        elif kind == "code":
            code = block[1]
            opts = block[2] if len(block) > 2 else {}
            x = opts.get("x", 60)
            w = opts.get("w", 600)
            h = add_code(s, code, x, y, w, size=opts.get("size", 12))
            y += h + 10
        elif kind == "table":
            headers, rows, widths = block[1], block[2], block[3]
            opts = block[4] if len(block) > 4 else {}
            h = add_table(s, headers, rows, widths, opts.get("x", 30), y,
                          size=opts.get("size", 12), row_h=opts.get("row_h", 21),
                          mono_cols=opts.get("mono_cols", ()))
            y += h + 10
        elif kind == "gap":
            y += block[1]
        elif kind == "note":
            box, tf = add_textbox(s, 30, y, 660, 20)
            p = tf.paragraphs[0]
            rich_runs(p, block[1], size=12.5, color=L.GRAY)
            y += 20
    add_footer(s, num)
    return y


def slide_merci(prs, num):
    s = blank_slide(prs)
    box, tf = add_textbox(s, 0, 178, 720, 50)
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    style_run(p.add_run(), "Merci pour votre attention.", font=L.TITLE_FONT,
              size=28, color=PURPLE)
    add_footer(s, num)


# ================================================================ le contenu
def build():
    prs = new_presentation()
    n = 0

    def C(titre, *blocks, bonus=False, body_size=15):
        nonlocal n
        n += 1
        slide_contenu(prs, n, titre, list(blocks), bonus=bonus, body_size=body_size)

    def SEC(titre):
        nonlocal n
        n += 1
        slide_section(prs, n, titre)

    # ---- 1. titre + marque -------------------------------------------------
    n += 1
    slide_titre(prs)
    n += 1
    slide_marque(prs)

    # ---- table des matières ------------------------------------------------
    n += 1
    slide_toc(prs, n, "Table des matières",
              [(0, "Les variables"),
               (1, "nommage et mots réservés"),
               (1, "types de base et typage dynamique"),
               (1, "affectation et conversion"),
               (0, "Interaction avec la console"),
               (1, "print"),
               (1, "les f-strings"),
               (1, "input"),
               (0, "Les opérateurs"),
               (1, "arithmétique"),
               (1, "comparaison, in, is"),
               (1, "logique")],
              [(0, "La structure conditionnelle"),
               (1, "if / elif / else"),
               (1, "l'indentation"),
               (1, "le ternaire"),
               (0, "Les structures itératives"),
               (1, "while"),
               (1, "for, range, enumerate"),
               (1, "break / continue")])
    n += 1
    slide_toc(prs, n, "Table des matières",
              [(0, "Les collections"),
               (1, "list et le slicing"),
               (1, "tuple"),
               (1, "dictionaries"),
               (1, "set"),
               (1, "les compréhensions 🎓")],
              [(0, "Les fonctions"),
               (1, "définition, paramètres, return"),
               (1, "portée et docstring"),
               (1, "*args, lambda 🎓"),
               (0, "Gestion des erreurs"),
               (1, "try / except / else / finally"),
               (1, "raise"),
               (1, "exceptions personnalisées 🎓")])

    # ======================================================== LES VARIABLES
    SEC("Les variables")

    C("Qu'est-ce que c'est ?",
      ("txt", [("p", "Une variable permet de **stocker une information en mémoire** pour la réutiliser — une étiquette collée sur une valeur. Celle-ci se compose :"),
               ("b0", "Un **nom**"),
               ("b0", "Un **type**"),
               ("b0", "Une **valeur**"),
               ("b0", "Une **référence mémoire**")]),
      ("code", """
age = 30                 # une étiquette « age » sur la valeur 30
prenom = "Alice"

TVA = 0.21               # « constante » : convention d'écriture uniquement
"""),
      ("txt", [("p", "Le concept de variable **constante** n'existe pas en python : la convention est d'écrire le nom `EN_MAJUSCULES` pour signaler « ne pas modifier ».")]))

    C("Le nom d'une variable",
      ("txt", [("p", "En python, la convention de nommage pour les variables est le **« snake_case »**"),
               ("b0", "Peut être composé de lettres, chiffres et underscores"),
               ("b0", "Ne peut pas **commencer** par un chiffre"),
               ("b0", "En **minuscules** — les caractères spéciaux et accents sont interdits"),
               ("b0", "Sensible à la casse : `age` et `Age` sont deux variables différentes !")]),
      ("gap", 4),
      ("table", ["✅ Correct", "❌ Incorrect"],
       [["nombre_de_clients", "NombreDeClients   (style C# / Java)"],
        ["prix_total", "prix total   (espace interdit)"],
        ["message_2", "2eme_message   (commence par un chiffre)"]],
       [240, 420], {"mono_cols": (0, 1), "row_h": 22}))

    C("Les mots réservés",
      ("txt", [("p", "Attention, il y a des mots-clefs que vous ne pouvez pas utiliser comme noms !"),
               ("p", "Python en compte aujourd'hui **35** — inutile de les mémoriser : les reconnaître suffit (votre éditeur les colore).")]),
      ("table", None,
       [["False", "None", "True", "and", "as", "assert", "async"],
        ["await", "break", "class", "continue", "def", "del", "elif"],
        ["else", "except", "finally", "for", "from", "global", "if"],
        ["import", "in", "is", "lambda", "nonlocal", "not", "or"],
        ["pass", "raise", "return", "try", "while", "with", "yield"]],
       [94, 94, 94, 94, 94, 94, 94], {"mono_cols": (0, 1, 2, 3, 4, 5, 6), "row_h": 22, "x": 31}),
      ("gap", 2),
      ("code", """
import keyword
print(len(keyword.kwlist))     # 35 — la liste officielle, toujours à jour
""", {"size": 11.5}))

    C("Le type d'une variable",
      ("txt", [("p", "Le python est un langage à **typage dynamique**."),
               ("b0", "Le type adapté est automatiquement utilisé lors de l'affectation — il est porté par la **valeur**, pas par la variable"),
               ("b0", "Il est conseillé de **ne pas changer** le type d'une variable en cours de programme !"),
               ("p", "La fonction `type(...)` permet de récupérer le type de la variable.")]),
      ("code", """
x = 5
print(type(x))       # <class 'int'>

x = "cinq"           # autorisé... mais à éviter : le code devient confus
print(type(x))       # <class 'str'>
"""))

    C("Dynamique… mais fortement typé",
      ("txt", [("b0", "Python ne mélange **pas** les types tout seul : additionner un texte et un nombre est une erreur"),
               ("b0", "C'est une protection : Python préfère **s'arrêter** plutôt que deviner (contrairement à JavaScript)")]),
      ("code", """
# ❌ Mélanger texte et nombre → erreur claire
# print("J'ai " + 30 + " ans")     # TypeError: can only concatenate str...

# ✅ Solution 1 : convertir explicitement
print("J'ai " + str(30) + " ans")

# ✅ Solution 2 (la bonne pratique) : la f-string — voir plus loin
age = 30
print(f"J'ai {age} ans")
"""))

    C("Les types de base",
      ("table", ["Type", "Nom complet", "Exemple", "Utilité"],
       [["int", "entier", "42", "compter, indexer"],
        ["float", "nombre à virgule", "3.14", "mesures, prix"],
        ["str", "chaîne de caractères", "\"bonjour\"", "texte"],
        ["bool", "booléen", "True / False", "vrai ou faux — ⚠ majuscule !"],
        ["NoneType", "valeur vide", "None", "l'équivalent du « null » de C#, Java…"]],
       [90, 170, 130, 270], {"mono_cols": (0, 2), "row_h": 23}),
      ("gap", 4),
      ("txt", [("b0", "Une valeur de type texte s'écrit en simples ou doubles quotes ; pour du texte multiligne, il faut **tripler** les quotes"),
               ("b0", "En Python 3, `str` gère déjà l'Unicode — le type « unicode » de Python 2 a disparu")]))

    C("Affectation",
      ("txt", [("p", "Contrairement aux langages classiques… il n'est **pas nécessaire de déclarer** les variables. L'affectation se réalise avec l'opérateur `=`.")]),
      ("code", """
entier = 42
texte = "Hello World"

# Python autorise également l'affectation multiple
nb1, nb2 = 13, 42

# ... qui permet d'échanger deux valeurs sans variable temporaire !
nb1, nb2 = nb2, nb1
print(nb1, nb2)          # 42 13
"""))

    C("Conversion",
      ("txt", [("p", "Il existe des fonctions permettant de convertir une valeur vers un type donné :"),
               ("b0", "`int(...)` — conversion vers un entier"),
               ("b0", "`float(...)` — conversion vers un nombre à virgule"),
               ("b0", "`str(...)` — transformation vers du texte")]),
      ("code", """
print(int("42"))         # 42
print(float("3.14"))     # 3.14
print(str(42))           # "42"

print(int(3.99))         # 3 → tronqué, PAS arrondi !
print(round(3.99))       # 4 → pour arrondir : round()

# int("abc")             # ❌ ValueError : conversion impossible
"""))

    # ======================================================== LA CONSOLE
    SEC("Interaction avec la console")

    C("Écrire dans la console",
      ("txt", [("p", "La fonction à utiliser pour afficher du texte dans la console est `print(...)`."),
               ("b0", "Plusieurs valeurs → un **séparateur** est ajouté (espace par défaut)"),
               ("b0", "En fin de ligne, un **saut de ligne** est ajouté"),
               ("b0", "Les paramètres `sep` et `end` permettent de modifier ce comportement")]),
      ("code", """
print("Bonjour")
print("A", "B", "C")                  # A B C
print("A", "B", "C", sep=" - ")       # A - B - C

print("Sans saut de ligne", end="")
print(" → la suite, sur la même ligne")
"""))

    C("Les f-strings — la façon moderne d'afficher",
      ("txt", [("b0", "Un `f` devant les guillemets, et des accolades `{ }` pour insérer n'importe quelle variable ou calcul"),
               ("b0", "À utiliser systématiquement : plus lisible que les concaténations avec `+`")]),
      ("code", """
prenom = "Alice"
age = 30
taille = 1.6842

print(f"{prenom} a {age} ans")            # insérer des variables
print(f"Dans 10 ans : {age + 10} ans")    # insérer un calcul
print(f"Taille : {taille:.2f} m")         # .2f → 2 chiffres après la virgule
"""))

    C("Lire dans la console",
      ("txt", [("p", "Pour interagir avec l'utilisateur, `input(\"message\")` affiche la question, attend la saisie, et la renvoie."),
               ("p", "⚠ La valeur récupérée sera **toujours de type texte** (`str`) — une conversion est nécessaire pour la transformer en entier, réel…")]),
      ("code", """
reponse = input("Quel âge avez-vous ? ")
print(type(reponse))       # <class 'str'> — TOUJOURS, même si on a tapé 30

age = int(reponse)         # conversion nécessaire pour calculer
print(f"L'année prochaine : {age + 1} ans")
"""))

    # ======================================================== LES OPÉRATEURS
    SEC("Les opérateurs")

    C("Arithmétique",
      ("txt", [("p", "Les opérateurs arithmétiques sont :")]),
      ("table", ["Opérateur", "Rôle", "Exemple", "Résultat"],
       [["+   -   *", "addition, soustraction, multiplication", "7 * 3", "21"],
        ["/", "division réelle — donne **toujours** un float", "7 / 2", "3.5"],
        ["//", "division entière (quotient)", "7 // 2", "3"],
        ["%", "modulo — le reste de la division entière", "7 % 2", "1"],
        ["**", "puissance", "2 ** 10", "1024"]],
       [110, 330, 110, 110], {"mono_cols": (0, 2, 3), "row_h": 23}),
      ("gap", 4),
      ("txt", [("p", "Le classique du `%` : un nombre est **pair** si `nombre % 2 == 0`.")]))

    C("Comparaison",
      ("txt", [("p", "Une comparaison renvoie toujours un booléen : `True` ou `False`.")]),
      ("table", ["Opérateur", "Signification"],
       [["==", "est égal à — ⚠ deux « = », à ne pas confondre avec l'affectation"],
        ["!=", "est différent de"],
        ["<    <=", "strictement inférieur / inférieur ou égal"],
        [">    >=", "strictement supérieur / supérieur ou égal"]],
       [110, 550], {"mono_cols": (0,), "row_h": 22}),
      ("code", """
age = 20
print(age >= 18)             # True
print("albert" < "bernard")  # True — le texte se compare (ordre alphabétique)
print(0 <= age <= 25)        # True — spécialité Python : le chaînage !
""", {"size": 11.5}))

    C("« in » et « is » — appartenance et identité",
      ("txt", [("b0", "`in` — test d'**appartenance** : « a » est-il contenu dans « b » ?"),
               ("b0", "`is` — test d'**identité** : « a » et « b » sont-ils le **même objet** en mémoire ? (⚠ pas le même contenu : ça, c'est le rôle de `==`)")]),
      ("code", """
email = "alice@entreprise.be"
print("@" in email)                     # True

jour = "samedi"
print(jour in ("samedi", "dimanche"))   # in remplace une série de « or »

a = [1, 2]
b = [1, 2]
print(a == b)    # True  → même CONTENU
print(a is b)    # False → deux objets différents en mémoire
"""),
      ("txt", [("p", "Usage quotidien de `is` : le test `if valeur is None` (cf. les fonctions).")]))

    C("Logique",
      ("txt", [("p", "Python utilise des **mots**, pas des symboles — `&&` et `||` n'existent pas !")]),
      ("table", ["Mot-clé", "Vrai quand…", "Exemple"],
       [["and", "**les deux** valeurs sont vraies", "age >= 18 and a_un_ticket"],
        ["or", "**au moins une** des deux est vraie", "est_admin or est_moderateur"],
        ["not", "la valeur est **fausse** (l'inverse)", "not est_bloque"]],
       [90, 260, 310], {"mono_cols": (0, 2), "row_h": 23}),
      ("gap", 4),
      ("txt", [("p", "Évaluation « paresseuse » : Python s'arrête dès que le résultat est connu — dans `a and b`, si `a` est faux, `b` n'est même pas évalué.")]))

    C("Affectation et opération",
      ("txt", [("p", "Il existe une écriture raccourcie qui combine une opération arithmétique avec une affectation :")]),
      ("table", None,
       [["a += b", "⇔", "a = a + b"],
        ["a -= b", "⇔", "a = a - b"],
        ["a *= b", "⇔", "a = a * b"],
        ["a /= b", "⇔", "a = a / b"]],
       [140, 60, 140], {"mono_cols": (0, 2), "row_h": 22, "x": 190}),
      ("gap", 2),
      ("code", """
compteur = 0
compteur += 5      # 5
compteur *= 2      # 10
print(compteur)
""", {"size": 11.5}))

    # ======================================================== CONDITIONNELLE
    SEC("La structure conditionnelle")

    C("Le « if, elif, else »",
      ("txt", [("p", "La structure `if` permet d'exécuter des opérations en fonction de conditions :"),
               ("b0", "`if` — condition à tester (obligatoire)"),
               ("b0", "`elif` — testée si la précédente est fausse (optionnel et répétable)"),
               ("b0", "`else` — traitement si aucune condition validée (optionnel)")]),
      ("code", """
note = 14

if note >= 16:
    print("Très bien")
elif note >= 12:
    print("Bien")          # ← 14 >= 12 : c'est ce bloc qui s'exécute
else:
    print("Peut mieux faire")

# Python teste DANS L'ORDRE et s'arrête à la PREMIÈRE condition vraie
"""))

    C("L'indentation EST la syntaxe",
      ("txt", [("b0", "Pas d'accolades en Python : le bloc est défini par le `:` et l'**indentation** — 4 espaces, la convention"),
               ("b0", "Tout ce qui est indenté sous le `if` appartient au `if` ; on « sort » du bloc en revenant à gauche"),
               ("b0", "Une indentation incohérente → `IndentationError`")]),
      ("code", """
age = 20

if age >= 18:
    print("Majeur")            # dans le if
    print("Accès autorisé")    # dans le if aussi

print("Fin du programme")      # HORS du if : toujours exécuté
"""))

    C("Conditions imbriquées… et comment les aplatir",
      ("txt", [("b0", "Un `if` dans un `if` fonctionne — mais au-delà de 2 niveaux, le code devient dur à lire"),
               ("b0", "Souvent, un `and` bien placé aplatit tout")]),
      ("code", """
age = 25
a_un_ticket = True

# ❌ Version imbriquée : chaque niveau ajoute de la complexité
if age >= 18:
    if a_un_ticket:
        print("Accès autorisé")

# ✅ Version aplatie : même logique, plus lisible
if age >= 18 and a_un_ticket:
    print("Accès autorisé")
"""))

    C("Bonus : la condition en une ligne (ternaire)",
      ("txt", [("b0", "Pour affecter une valeur selon une condition : `valeur_si_vrai if condition else valeur_si_faux`"),
               ("b0", "À réserver aux cas **simples** — dès que c'est long, revenir au `if` classique")]),
      ("code", """
age = 20

# Version classique en 4 lignes...
if age >= 18:
    statut = "majeur"
else:
    statut = "mineur"

# ... et la même chose en 1 ligne
statut = "majeur" if age >= 18 else "mineur"
print(statut)
"""))

    # ======================================================== ITÉRATIVES
    SEC("Les structures itératives")

    C("Deux boucles, deux usages",
      ("txt", [("p", "Répéter une action sans recopier le code : traiter 1000 lignes d'un fichier, réessayer une connexion, afficher chaque produit d'un catalogue…")]),
      ("gap", 4),
      ("table", ["Boucle", "Idée", "Quand l'utiliser"],
       [["while", "« **tant que** la condition est vraie, répète »", "on ne sait pas à l'avance combien de fois"],
        ["for", "« **pour chaque** élément de la collection, répète »", "on parcourt quelque chose — le cas de loin le plus courant"]],
       [80, 300, 280], {"mono_cols": (0,), "row_h": 30}))

    C("La structure « while »",
      ("txt", [("p", "La boucle `while` répète un ensemble d'opérations **tant que** la condition vérifiée est vraie — testée **avant** chaque tour."),
               ("p", "⚠ Attention, vous devez toujours **maîtriser la condition** : quelque chose doit changer dans le bloc, sinon la boucle est infinie !")]),
      ("code", """
compteur = 5

while compteur > 0:
    print(compteur)
    compteur -= 1        # ← SANS cette ligne : boucle infinie !

print("Décollage 🚀")
"""),
      ("txt", [("p", "Le cas d'usage typique : **redemander** une saisie tant qu'elle est invalide (on ne sait pas combien d'essais il faudra).")]))

    C("La structure « for »",
      ("txt", [("p", "La boucle `for` parcourt une collection : à chaque tour, la variable prend la valeur suivante."),
               ("b0", "Fonctionne sur tout ce qui se parcourt : une liste, un texte, un fichier…"),
               ("b0", "Le réflexe Python : on boucle **directement sur les éléments**, pas sur des indices !")]),
      ("code", """
courses = ["pain", "lait", "œufs"]

for article in courses:
    print(f"À acheter : {article}")

for lettre in "abc":        # un texte se parcourt aussi
    print(lettre)
"""))

    C("La fonction « range(start, stop, step) »",
      ("txt", [("p", "`range(...)` génère une suite de nombres — utilisable de 3 manières :"),
               ("b0", "`range(stop)` — de 0 à stop-1"),
               ("b0", "`range(start, stop)` — le pas par défaut est 1"),
               ("b0", "`range(start, stop, step)` — tous les paramètres · la fin est **toujours exclue** !")]),
      ("code", """
for i in range(5):            # 0 1 2 3 4  (la fin est exclue)
    print(i, end=" ")

for i in range(1, 11):        # 1 2 3 ... 10
    print(i, end=" ")

for i in range(0, 20, 2):     # 0 2 4 ... 18 (de 2 en 2)
    print(i, end=" ")
"""))

    C("« enumerate(...) » — l'élément ET sa position",
      ("txt", [("p", "Besoin du numéro de chaque élément ? Pas de compteur à gérer à la main : `enumerate` fournit des paires `(position, element)` — et `start=1` fait commencer à 1.")]),
      ("code", """
podium = ["Alice", "Bob", "Chloé"]

# ❌ Le réflexe venu d'autres langages : un compteur manuel
i = 0
for nom in podium:
    i += 1
    print(f"{i}. {nom}")

# ✅ La façon Python : enumerate s'occupe du compteur
for position, nom in enumerate(podium, start=1):
    print(f"{position}. {nom}")
"""))

    C("« break » et « continue » — piloter la boucle",
      ("table", ["Mot-clé", "Effet"],
       [["break", "**sort** de la boucle immédiatement et définitivement"],
        ["continue", "**saute** au tour suivant (ignore la fin du bloc pour ce tour)"]],
       [110, 550], {"mono_cols": (0,), "row_h": 22}),
      ("code", """
for produit in ["clavier", "souris", "écran", "casque"]:
    if produit == "écran":
        break              # trouvé → inutile de continuer
    print(produit)

for nombre in range(1, 11):
    if nombre % 2 != 0:
        continue           # impair → on passe au suivant
    print(f"{nombre} est pair")
"""))

    # ======================================================== COLLECTIONS
    SEC("Les collections")

    C("Les différentes collections du python",
      ("txt", [("p", "Les collections permettent de regrouper dans une seule variable un **ensemble d'informations**. En python, il en existe 4 :")]),
      ("table", ["Nom", "Syntaxe", "Ordonnée", "Modifiable", "Doublons", "Spécialité"],
       [["List", "[1, 2, 3]", "Oui", "Oui", "Oui", "LA collection à tout faire"],
        ["Tuple", "(1, 2, 3)", "Oui", "Non", "Oui", "données figées"],
        ["Dictionaries", "{\"clé\": val}", "Oui *", "Oui", "clés uniques", "fiches clé → valeur"],
        ["Set", "{1, 2, 3}", "Non", "Oui", "Non", "unicité, recherche rapide"]],
       [100, 105, 70, 82, 88, 215], {"mono_cols": (1,), "row_h": 24}),
      ("gap", 3),
      ("txt", [("p", "*  depuis Python 3.7, le dictionnaire **conserve l'ordre d'insertion**"),
               ("p", "Au quotidien : **la liste et le dictionnaire font 90 % du travail**.")]))

    C("La collection « list »",
      ("txt", [("p", "En python, une liste s'écrit entre crochets `[ ]` — une suite **ordonnée** de valeurs, modifiable à volonté. Chaque élément a une **position** (un index) qui commence à **0**.")]),
      ("code", """
courses = ["pain", "lait", "œufs", "beurre"]

print(courses[0])         # pain   → premier élément (index 0 !)
print(courses[1])         # lait
print(courses[-1])        # beurre → -1 = le dernier (astuce très utilisée)

print(len(courses))       # 4      → la taille
print("lait" in courses)  # True   → test de présence
"""))

    C("La collection « list » — modifier",
      ("code", """
courses = ["pain", "lait", "œufs"]

courses.append("fromage")      # ajouter à la fin (LA méthode n°1 de Python)
courses.insert(0, "café")      # insérer à une position précise
courses.remove("lait")         # supprimer par valeur
dernier = courses.pop()        # retirer ET renvoyer le dernier élément
courses[0] = "café moulu"      # modifier un élément existant
print(courses)

notes = [12, 8, 17, 14]
notes.sort()                   # trier la liste sur place
print(notes)                   # [8, 12, 14, 17]
"""))

    C("Le kit complet des méthodes de liste", bonus=True, *[
      ("table", ["Méthode", "Ce qu'elle fait", "Renvoie"],
       [["append(x)", "ajoute **un** élément à la fin", "rien"],
        ["extend(coll)", "ajoute les éléments de la collection **un par un**", "rien"],
        ["insert(pos, x)", "insère à cette position et décale le reste", "rien"],
        ["remove(x)", "supprime la **première** occurrence (erreur si absente)", "rien"],
        ["pop(pos)", "supprime **et renvoie** (le dernier si pos omise)", "l'élément"],
        ["index(x)  /  count(x)", "position de la 1ʳᵉ occurrence / nombre d'occurrences", "un entier"],
        ["sort(key=, reverse=)", "trie **la liste elle-même** — `sorted(l)` renvoie une copie triée", "rien"],
        ["clear()", "vide entièrement la liste", "rien"]],
       [155, 400, 105], {"mono_cols": (0,), "row_h": 23})])

    C("Les deux pièges : append/extend et sort/sorted", bonus=True, *[
      ("code", """
nombres = [1, 2, 3]
nombres.append([4, 5])     # append ajoute LA LISTE ENTIÈRE comme 1 élément
print(nombres)             # [1, 2, 3, [4, 5]]   ← le piège !

nombres = [1, 2, 3]
nombres.extend([4, 5])     # extend ajoute les éléments UN PAR UN
print(nombres)             # [1, 2, 3, 4, 5]

mots = ["kiwi", "banane", "pomme"]
print(sorted(mots))        # NOUVELLE liste triée — l'originale intacte
mots.sort()                # trie la liste ELLE-MÊME... et renvoie None !
print(mots)
""")])

    C("Le découpage (slicing)",
      ("txt", [("p", "Le langage python permet de récupérer un **ensemble d'éléments** : `liste[début:fin]` — la fin est **exclue**, comme pour `range()`.")]),
      ("code", """
nombres = [10, 20, 30, 40, 50]

print(nombres[1:3])     # [20, 30]      → de l'index 1 à 2 (3 exclu)
print(nombres[:2])      # [10, 20]      → du début à l'index 1
print(nombres[2:])      # [30, 40, 50]  → de l'index 2 à la fin
print(nombres[-2:])     # [40, 50]      → les 2 derniers

email = "alice@entreprise.be"
print(email[:5])        # alice — le slicing marche aussi sur le texte !
"""))

    C("Slicing avancé — le pas, et les copies", bonus=True, *[
      ("txt", [("b0", "Le slicing complet a **trois** nombres : `liste[début : fin : pas]` — et `[::-1]` inverse la liste"),
               ("b0", "**Copier ≠ renommer** : `alias = original` ne copie rien ! Pour une vraie copie : `.copy()` ou `[:]`")]),
      ("code", """
nombres = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nombres[3:8:2])    # [3, 5, 7]         → de 3 à 7, de 2 en 2
print(nombres[::2])      # [0, 2, 4, 6, 8, 10] → un élément sur deux
print(nombres[::-1])     # [10, 9, ... 0]    → la liste À L'ENVERS

original = [1, 2, 3]
alias = original         # PAS une copie : 2 noms pour LA MÊME liste !
alias[0] = 77
print(original)          # [77, 2, 3] → « l'originale » a changé aussi

copie = original.copy()  # vraie copie (ou original[:])
""")])

    C("Le piège de la copie superficielle", bonus=True, *[
      ("txt", [("p", "`.copy()` ne copie que le **premier niveau** — les sous-listes restent **partagées**. Analogie : photocopier le classeur… mais pas les feuilles à l'intérieur. La solution : `copy.deepcopy()`.")]),
      ("code", """
grille = [[1, 2, 3], [4, 5, 6]]         # une liste DE listes
grille_copie = grille.copy()

grille_copie[0][0] = 99                 # on modifie... la copie ?
print(grille)            # [[99, 2, 3], [4, 5, 6]] → l'originale AUSSI ?!

# ✅ La copie PROFONDE recopie tous les niveaux
import copy
grille = [[1, 2, 3], [4, 5, 6]]
grille_copie = copy.deepcopy(grille)
grille_copie[0][0] = 99
print(grille)            # [[1, 2, 3], [4, 5, 6]] → intacte ✔
""")])

    C("La collection « tuple »",
      ("txt", [("p", "En python, un tuple s'écrit entre parenthèses `( )` — comme une liste, mais **non modifiable** après création (immuable)."),
               ("p", "Utilité : signaler « ces valeurs vont **ensemble** et ne changeront pas » — un point GPS, une paire jour/mois…")]),
      ("code", """
position = (50.85, 4.35)       # latitude, longitude de Bruxelles

print(position[0])             # accès par index, comme une liste
# position[0] = 51.0           # ❌ TypeError : non modifiable !

# Le « déballage » (unpacking) : chaque valeur dans sa variable
latitude, longitude = position
print(f"lat={latitude}, lon={longitude}")
"""))

    C("Tuples — unpacking avancé et « zip »", bonus=True, *[
      ("table", ["Écriture", "Effet"],
       [["(42,)", "tuple d'**un** élément — la virgule est obligatoire !"],
        ["premier, *reste = t", "`*reste` **ramasse tout le reste** (dans une liste)"],
        ["a, b = b, a", "échange de deux variables sans variable temporaire"],
        ["zip(c1, c2)", "appaire deux collections **par position**, pour les parcourir côte à côte"]],
       [190, 470], {"mono_cols": (0,), "row_h": 22}),
      ("code", """
resultats = (18, 15, 12, 9, 7)
premier, *reste = resultats
print(premier, reste)          # 18  [15, 12, 9, 7]

noms = ("Alice", "Bob", "Chloé")
ages = (25, 30, 35)
for nom, age in zip(noms, ages):
    print(f"{nom} a {age} ans")
""", {"size": 11.5})])

    C("La collection « Dictionaries »",
      ("txt", [("p", "Un dictionnaire s'écrit entre accolades avec des combinaisons **« clef / valeur »** : on retrouve une valeur par son **étiquette**, pas par sa position. C'est la « fiche » : un client, un produit…")]),
      ("code", """
client = {"nom": "Dupont", "prenom": "Alice", "age": 30}

print(client["nom"])             # lire une valeur par sa clé
client["email"] = "a@bstorm.be"  # nouvelle clé      → ajout
client["age"] = 31               # clé existante     → modification

# print(client["tel"])           # ❌ clé absente → KeyError !
print(client.get("tel"))                   # None — sans planter
print(client.get("tel", "non renseigné"))  # ou une valeur par défaut
"""))

    C("Parcourir un dictionnaire",
      ("code", """
client = {"nom": "Dupont", "prenom": "Alice", "age": 31}

# Parcourir les clés (comportement par défaut du for)
for cle in client:
    print(cle)

# Parcourir clés ET valeurs ensemble : .items()
for cle, valeur in client.items():
    print(f"{cle} : {valeur}")
"""),
      ("txt", [("p", "L'ordre d'insertion est **conservé** (Python ≥ 3.7) — mais on reste sur l'idée : un dict se consulte **par clé**, pas par position.")]))

    C("Dictionnaires — fusion et imbrication", bonus=True, *[
      ("txt", [("b0", "`d1.update(d2)` verse d2 **dans** d1 (clés communes écrasées) ; `d1 | d2` crée un **nouveau** dict fusionné"),
               ("b0", "Le dict **imbriqué** : un crochet **par niveau** — pendant un `for` : modifier les valeurs ✅, ajouter/supprimer des clés ❌ (`RuntimeError`)")]),
      ("code", """
profil = {"nom": "Alice", "age": 30}
profil.update({"age": 31, "ville": "Bruxelles"})
print(profil)         # age écrasé, ville ajoutée

catalogue = {
    "vjx45": {"nom": "chaussures", "commande": False},
    "ab812": {"nom": "veste", "commande": False},
}
print(catalogue["vjx45"]["nom"])         # un crochet PAR NIVEAU
catalogue["vjx45"]["commande"] = True    # modification imbriquée
""")])

    C("Le combo gagnant : une liste de dictionnaires",
      ("txt", [("p", "**LA** structure de données du monde professionnel : chaque dict est une **fiche**, la liste est le **fichier** — c'est exactement la forme du JSON.")]),
      ("code", """
produits = [
    {"nom": "Clavier", "prix": 49.99, "stock": 12},
    {"nom": "Souris", "prix": 19.99, "stock": 0},
    {"nom": "Écran", "prix": 219.00, "stock": 5},
]

# Tout ce qu'on a appris se combine : boucle + dict + condition + f-string
for produit in produits:
    if produit["stock"] > 0:
        print(f"{produit['nom']} : {produit['prix']} €")
    else:
        print(f"{produit['nom']} : RUPTURE DE STOCK")
"""))

    C("La collection « set »",
      ("txt", [("p", "En python, un set s'écrit entre accolades `{ }` — pas d'ordre, **pas de doublons**. Ses deux super-pouvoirs :"),
               ("b0", "**Dédoublonner** une liste en une ligne"),
               ("b0", "Tester une appartenance **très rapidement**, même sur des millions d'éléments")]),
      ("code", """
votes = ["oui", "non", "oui", "oui", "non"]
print(set(votes))             # {'oui', 'non'} — doublons éliminés
print(len(set(votes)))        # 2 réponses différentes

ids_autorises = {101, 205, 318, 442}
print(205 in ids_autorises)   # True — quasi instantané
"""))

    C("Sets — les opérations d'ensembles", bonus=True, *[
      ("table", ["Opérateur", "Nom", "Se lit"],
       [["A | B", "union", "« dans A **ou** B »"],
        ["A & B", "intersection", "« dans A **et** B »"],
        ["A - B", "différence", "« dans A **mais pas** B »"],
        ["A ^ B", "différence symétrique", "« dans un seul des deux »"]],
       [90, 180, 250], {"mono_cols": (0,), "row_h": 21, "x": 30}),
      ("code", """
invites = {"Alice", "Bob", "Chloé", "David"}
presents = {"Bob", "Chloé", "Emma"}

print(invites & presents)   # {'Bob', 'Chloé'}     → les venus
print(invites - presents)   # {'Alice', 'David'}   → les absents
print(presents - invites)   # {'Emma'}             → venue sans invitation !
""", {"size": 11.5})])

    C("Les compréhensions de liste", bonus=True, *[
      ("txt", [("p", "Construire une liste en une ligne : `[expression for element in collection if condition]` — l'idiome Python qui remplace `map` et `filter`.")]),
      ("code", """
nombres = [1, 2, 3, 4, 5, 6]

doubles = [n * 2 for n in nombres]            # TRANSFORMER chacun
print(doubles)              # [2, 4, 6, 8, 10, 12]

pairs = [n for n in nombres if n % 2 == 0]    # FILTRER
print(pairs)                # [2, 4, 6]

carres = [n ** 2 for n in nombres if n % 2 == 0]   # les deux à la fois
print(carres)               # [4, 16, 36]
""")])

    # ======================================================== FONCTIONS
    SEC("Les fonctions")

    C("Définition d'une fonction",
      ("txt", [("p", "Une fonction est un **bloc de code réutilisable** avec un nom — pour éviter la répétition de code. Déclarée avec le mot clef `def`, nommée en « snake_case ». Il en existe 2 types :"),
               ("b0", "**Procédure** → ne retourne aucune valeur"),
               ("b0", "**Fonction** → retourne une valeur"),
               ("p", "⚠ Définir une fonction ne l'exécute **pas** — il faut l'**appeler** avec ses parenthèses.")]),
      ("code", """
def afficher_bienvenue():          # définition : Python mémorise la recette
    print("Bienvenue !")

afficher_bienvenue()               # appel : c'est ICI que le code s'exécute
afficher_bienvenue()               # ... réutilisable à volonté
"""))

    C("Fonction vs méthode — le bon vocabulaire",
      ("txt", [("b0", "Une **fonction** s'appelle seule : `len(courses)`, `print(...)`, `type(x)`"),
               ("b0", "Une **méthode** est une fonction attachée à un objet — appelée avec un point : `objet.methode(...)`"),
               ("p", "Les deux termes reviennent sans cesse : autant les employer correctement dès maintenant.")]),
      ("code", """
courses = ["pain", "lait"]

print(len(courses))         # fonction :  len(...)
courses.append("œufs")      # méthode  :  la liste AGIT sur elle-même

texte = "bonjour"
print(texte.upper())        # méthode des str → BONJOUR
"""))

    C("Les paramètres",
      ("txt", [("b0", "Les **paramètres** sont les variables déclarées entre les parenthèses du `def` — les valeurs reçues sont **copiées** dans des variables locales à la fonction"),
               ("b0", "Les **arguments** sont les valeurs réelles envoyées à l'appel — dans l'ordre (positionnels), ou **nommés** (ordre libre, plus lisible)")]),
      ("code", """
def saluer(prenom, langue):
    if langue == "fr":
        print(f"Bonjour {prenom} !")
    else:
        print(f"Hello {prenom}!")

saluer("Alice", "fr")                  # arguments positionnels
saluer(langue="en", prenom="Bob")      # arguments nommés : ordre libre
"""))

    C("« return » — renvoyer un résultat",
      ("txt", [("b0", "`print` **affiche** (pour les humains) ; `return` **renvoie** une valeur au programme — stockable, comparable, réutilisable"),
               ("b0", "`return` termine immédiatement la fonction · sans `return`, la fonction renvoie `None`")]),
      ("code", """
def prix_ttc(prix_ht, taux_tva):
    return prix_ht * (1 + taux_tva)

prix = prix_ttc(100, 0.21)                  # le résultat se stocke...
print(f"Pour 3 articles : {prix * 3} €")    # ... et se réutilise !

def diviser(a, b):
    if b == 0:
        return None       # return = sortie immédiate (cas particulier)
    return a / b
"""))

    C("Les valeurs par défaut",
      ("txt", [("p", "Un paramètre peut avoir une **valeur par défaut** : l'argument devient facultatif à l'appel.")]),
      ("code", """
def creer_utilisateur(nom, role="lecteur", actif=True):
    return {"nom": nom, "role": role, "actif": actif}

print(creer_utilisateur("Alice"))                  # défauts utilisés
print(creer_utilisateur("Bob", role="admin"))      # défaut remplacé
"""),
      ("txt", [("p", "⚠ **Jamais de liste en valeur par défaut** : elle est créée **une seule fois** et partagée entre tous les appels — le remède : `None` par défaut, et créer la liste dans la fonction (`if liste is None:`).")]))

    C("Variable locale VS globale",
      ("txt", [("b0", "Les variables créées au sein d'une fonction n'existent **que dans celle-ci**"),
               ("b0", "Le mot clef `global` permet d'utiliser une variable du dehors — ⚠ **ceci n'est pas conseillé !**"),
               ("b0", "Le bon modèle mental : les données **entrent par les paramètres**, **sortent par le return**")]),
      ("code", """
def calculer():
    resultat_local = 42        # variable LOCALE
    return resultat_local

print(calculer())              # 42
# print(resultat_local)        # ❌ NameError : n'existe pas ici !
"""))

    C("Documenter une fonction : la docstring",
      ("txt", [("p", "Le texte `\"\"\" ... \"\"\"` juste sous le `def` décrit ce que fait la fonction — affiché par `help(...)` et au survol dans VS Code. Vos collègues (et vous dans 6 mois) vous remercieront !")]),
      ("code", '''
def prix_ttc(prix_ht, taux_tva=0.21):
    """Calcule le prix TTC à partir du prix hors taxe.

    taux_tva : taux de TVA (0.21 = 21 %, le taux belge par défaut)
    """
    return prix_ht * (1 + taux_tva)

help(prix_ttc)        # affiche la docstring
'''))

    C("Le kit complet des fonctions", bonus=True, *[
      ("txt", [("b0", "`return a, b` renvoie un **tuple** → à déballer : `mini, maxi = ...`"),
               ("b0", "`*args` : positionnels en vrac (tuple) · `**kwargs` : nommés en vrac (dict) · `f(*liste)` déballe à l'appel"),
               ("b0", "`lambda p: expression` — mini-fonction jetable, surtout pour `key=` de `sorted` / `max` / `min`")]),
      ("code", """
def statistiques(notes):
    return min(notes), max(notes)          # un tuple !
mini, maxi = statistiques([12, 15, 9, 17])

def addition(*nombres):                    # print() fonctionne ainsi !
    return sum(nombres)
print(addition(1, 2, 3, 4))                # 10

produits = [{"nom": "Écran", "prix": 219.0},
            {"nom": "Souris", "prix": 19.99}]
tri = sorted(produits, key=lambda p: p["prix"])    # trier PAR le prix
""", {"size": 11.5})])

    # ======================================================== ERREURS
    SEC("Gestion des erreurs")

    C("Qu'est-ce qu'une exception ?",
      ("txt", [("b0", "Dans la vraie vie, tout peut mal se passer : saisie invalide, fichier absent, réseau coupé…"),
               ("b0", "Une **exception** est le signal d'erreur levé par Python — non interceptée, le programme **plante**"),
               ("b0", "Le message se lit **de bas en haut** : le type d'exception + la ligne fautive — savoir le lire, c'est 50 % du débogage !")]),
      ("code", """
int("abc")

# Traceback (most recent call last):
#   File "app.py", line 1, in <module>
# ValueError: invalid literal for int() with base 10: 'abc'
# ^^^^^^^^^^
# le TYPE d'erreur — et juste au-dessus, la ligne exacte du plantage
"""))

    C("Les exceptions les plus courantes",
      ("table", ["Exception", "Se produit quand…", "Exemple déclencheur"],
       [["ValueError", "la valeur n'a pas le bon format", "int(\"abc\")"],
        ["TypeError", "les types sont incompatibles", "\"texte\" + 5"],
        ["ZeroDivisionError", "division par zéro", "10 / 0"],
        ["KeyError", "clé absente d'un dictionnaire", "client[\"tel\"]"],
        ["IndexError", "position hors de la liste", "liste[99]"],
        ["FileNotFoundError", "fichier introuvable", "open(\"absent.txt\")"]],
       [175, 290, 195], {"mono_cols": (0, 2), "row_h": 24}))

    C("Try… Except",
      ("txt", [("p", "La gestion des erreurs permet d'**intercepter** les exceptions pour les traiter — le programme **continue** au lieu de planter."),
               ("p", "En python, quatre types de blocs sont prévus pour cela : `try`, `except`, `else` et `finally`.")]),
      ("code", """
saisie = "abc"                # imaginez que ça vient d'un input()

try:
    nombre = int(saisie)
    print(f"Le double : {nombre * 2}")
except ValueError:
    print(f"'{saisie}' n'est pas un nombre valide")

print("→ Le programme continue de tourner !")
"""))

    C("Multiples « Except » — attraper précisément",
      ("txt", [("b0", "Toujours indiquer **quelle** exception on attend — un `except:` tout nu attrape tout, y compris les bugs qu'on voulait voir ❌"),
               ("b0", "`as e` récupère l'objet exception (son message) · l'exception passe d'`except` en `except`, à la recherche du premier bloc compatible")]),
      ("code", """
def convertir_et_diviser(texte, diviseur):
    try:
        return int(texte) / diviseur
    except ValueError as e:               # « as e » : les détails
        print(f"Saisie invalide → {e}")
    except ZeroDivisionError:
        print("Division par zéro impossible")

convertir_et_diviser("abc", 2)     # intercepté par ValueError
convertir_et_diviser("20", 0)      # intercepté par ZeroDivisionError
"""))

    C("Le quatuor : try / except / else / finally",
      ("table", ["Bloc", "S'exécute…"],
       [["try", "toujours — c'est le code surveillé"],
        ["except", "seulement si une exception a eu lieu"],
        ["else", "seulement si tout s'est **bien** passé"],
        ["finally", "**toujours**, quoi qu'il arrive — nettoyage, fermeture…"]],
       [100, 560], {"mono_cols": (0,), "row_h": 21}),
      ("code", """
try:
    nombre = int("42")
except ValueError:
    print("❌ échec de la conversion")
else:
    print(f"✅ conversion réussie : {nombre}")
finally:
    print("🧹 nettoyage — s'exécute TOUJOURS")
""", {"size": 11.5}))

    C("« raise » — lever soi-même une exception",
      ("txt", [("b0", "Nos propres fonctions peuvent **refuser** des données invalides : `raise ValueError(\"message clair\")`"),
               ("b0", "C'est mieux que renvoyer `None` en silence : l'erreur est **impossible à ignorer**, et le message explique le problème")]),
      ("code", """
def creer_tache(titre):
    if not titre.strip():          # titre vide (ou que des espaces) ?
        raise ValueError("Le titre ne peut pas être vide")
    return {"titre": titre.strip(), "faite": False}

try:
    creer_tache("   ")
except ValueError as e:
    print(f"Refusé : {e}")
"""))

    C("Le pattern à connaître : la saisie robuste",
      ("txt", [("p", "Combiner `while True` + `try/except` : redemander **jusqu'à** obtenir une saisie valide — impossible à faire planter.")]),
      ("code", """
def demander_entier(question):
    \"\"\"Repose la question jusqu'à obtenir un entier valide.\"\"\"
    while True:
        try:
            return int(input(question))   # ça marche → return sort
        except ValueError:
            print("⚠ Veuillez entrer un nombre entier")

age = demander_entier("Votre âge : ")
print(f"Âge enregistré : {age}")
"""))

    C("Pour aller plus loin avec les exceptions", bonus=True, *[
      ("table", ["Technique", "Syntaxe", "Quand"],
       [["plusieurs types d'un coup", "except (ValueError, TypeError):", "même traitement pour plusieurs erreurs"],
        ["re-lever l'exception", "raise   (tout nu, dans un except)", "observer sans avaler l'erreur"],
        ["sa propre exception", "class MonErreur(Exception):", "un **nom métier** pour vos erreurs"]],
       [150, 250, 260], {"mono_cols": (1,), "row_h": 22, "size": 11.5}),
      ("gap", 6),
      ("code", """
class SoldeInsuffisantError(Exception):
    \"\"\"Levée quand un retrait dépasse le solde disponible.\"\"\"

def retirer(solde, montant):
    if montant > solde:
        raise SoldeInsuffisantError(f"Refusé : solde {solde} €")
    return solde - montant

try:
    retirer(50, 200)
except SoldeInsuffisantError as e:     # un except sur MESURE
    print(e)
""", {"size": 10.5})])

    # ======================================================== FIN
    C("Pour aller plus loin",
      ("txt", [("p", "Ce module couvre le **socle** du langage. La suite logique :"),
               ("b0", "**La programmation orientée objet** — classes, héritage, encapsulation (support « Python - Orienté objet »)"),
               ("b0", "**Fichiers et modules** — lire/écrire des fichiers, le JSON, organiser son code en plusieurs fichiers"),
               ("b0", "**Le web** — un premier site avec Flask : formulaires GET/POST, templates, base de données SQLite"),
               ("b0", "**Sous le capot** — références mémoire, hachage, ce que Python fait vraiment de vos variables"),
               ("b0", "**La performance** — mesurer avec `timeit`, choisir la bonne collection, écrire du Python rapide")]),
      body_size=15.5)

    n += 1
    slide_merci(prs, n)

    prs.save(OUT)
    print(f"OK — {n} slides → {OUT}")


if __name__ == "__main__":
    build()
