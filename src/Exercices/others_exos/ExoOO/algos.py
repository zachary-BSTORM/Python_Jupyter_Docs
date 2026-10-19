from itertools import product


# --- Bookseller ---
# On parcourt le stock, on récupère la première lettre de chaque code (= catégorie)
# et on additionne les quantités par catégorie dans un dictionnaire.
# Ensuite on formate le résultat pour chaque catégorie demandée.
# Ex: ["ABART 20", "BKWRK 25"] + ["A", "B"] → "(A : 20) - (B : 25)"

def stock_list(stock, categories):
    if not stock or not categories:
        return ""
    totals = {}
    for entry in stock:
        code, qty = entry.split()
        cat = code[0]  # La catégorie est la première lettre du code
        totals[cat] = totals.get(cat, 0) + int(qty)
    return " - ".join(f"({cat} : {totals.get(cat, 0)})" for cat in categories)


# --- Deadfish ---
# Mini langage avec 4 commandes sur une seule valeur entière (départ 0) :
#   i → +1, d → -1, s → valeur au carré, o → afficher la valeur
# On lit le programme caractère par caractère et on met à jour la valeur.
# Ex: "iiisdoso" → i=1, i=2, i=3, s=9, d=8, o→[8], s=64, o→[8,64]

def parse(code):
    val = 0
    result = []
    for ch in code:
        if ch == "i":
            val += 1
        elif ch == "d":
            val -= 1
        elif ch == "s":
            val *= val
        elif ch == "o":
            result.append(val)
    return result


# --- Missing term in AP ---
# Une suite arithmétique a un pas constant entre chaque terme.
# On calcule le pas attendu à partir du premier et dernier élément.
# Ensuite on cherche l'endroit où l'écart est différent du pas : c'est là qu'il manque un nombre.
# Ex: [1, 3, 5, 9, 11] → pas = 2, écart entre 5 et 9 = 4 → manque 7

def find_missing(seq):
    # len(seq) termes présents, donc len(seq)+1 termes au total → len(seq) intervalles
    step = (seq[-1] - seq[0]) // len(seq)
    for i in range(len(seq) - 1):
        if seq[i + 1] - seq[i] != step:
            return seq[i] + step
    return None


# --- Sum of pairs ---
# On cherche la première paire (a, b) telle que a + b = s,
# avec b ayant le plus petit index possible.
# Astuce : on mémorise les nombres déjà vus dans un set.
# Pour chaque nombre n, on vérifie si (s - n) a déjà été vu → paire trouvée.
# C'est O(n) au lieu de O(n²) avec une double boucle.
# Ex: [11, 3, 7, 5], s=10 → pour 7 : 10-7=3, 3 est dans seen → [3, 7]

def sum_of_pairs(ints, s):
    seen = set()
    for n in ints:
        complement = s - n
        if complement in seen:
            return [complement, n]
        seen.add(n)
    return None


# --- Sum of parts ---
# Pour chaque "partie" de la liste (en retirant les éléments depuis le début), on veut la somme.
# Au lieu de recalculer chaque somme depuis zéro, on part de la fin :
# result[i] = result[i+1] + ls[i]  (on ajoute juste l'élément courant à la somme du reste)
# Ex: [0, 1, 3, 6, 10] → [20, 20, 19, 16, 10, 0]

def parts_sums(ls):
    result = [0] * (len(ls) + 1)  # Le dernier élément est toujours 0 (liste vide)
    for i in range(len(ls) - 1, -1, -1):
        result[i] = result[i + 1] + ls[i]
    return result


# --- Bracket Matcher ---
# On parcourt la chaîne et on maintient un compteur :
#   ( → +1, ) → -1
# Si le compteur passe sous 0, une parenthèse fermante arrive trop tôt → invalide.
# À la fin, si le compteur vaut 0 toutes les parenthèses sont bien fermées → valide.
# Ex: "(hello (world))" → count finit à 0 → 1

def bracket_matcher(s):
    count = 0
    for ch in s:
        if ch == "(":
            count += 1
        elif ch == ")":
            count -= 1
        if count < 0:  # Fermeture sans ouverture correspondante
            return 0
    return 1 if count == 0 else 0


# --- Pick Peaks ---
# Un pic est un élément strictement supérieur à ses deux voisins.
# Cas plateau : si plusieurs éléments consécutifs ont la même valeur,
# on regarde ce qui suit le plateau. Si ça descend → c'est un pic (au début du plateau).
# Ex: [1, 2, 2, 2, 1] → pic à l'index 1 (début du plateau de 2)
# Ex: [1, 2, 2, 2, 3] → pas de pic (le plateau monte)

def pick_peaks(arr):
    pos, peaks = [], []
    i = 1
    while i < len(arr) - 1:
        if arr[i] > arr[i - 1]:
            plateau_start = i
            # On avance tant qu'on est sur un plateau (valeurs égales)
            while i < len(arr) - 1 and arr[i] == arr[plateau_start]:
                i += 1
            # Si après le plateau ça descend, c'est un vrai pic
            if arr[i] < arr[plateau_start]:
                pos.append(plateau_start)
                peaks.append(arr[plateau_start])
        else:
            i += 1
    return {"pos": pos, "peaks": peaks}


# --- Range Extraction ---
# On regroupe les entiers consécutifs en plages.
# Pour chaque position i, on avance j tant que les nombres se suivent (+1).
# Si la plage fait au moins 3 éléments → notation "début-fin", sinon on liste chaque nombre.
# Ex: [-10,-9,-8,-6] → "-10--8,-6"

def solution(arr):
    parts = []
    i = 0
    while i < len(arr):
        j = i
        # On cherche jusqu'où va la séquence consécutive
        while j + 1 < len(arr) and arr[j + 1] == arr[j] + 1:
            j += 1
        if j - i >= 2:  # Au moins 3 nombres consécutifs → plage
            parts.append(f"{arr[i]}-{arr[j]}")
        else:  # 1 ou 2 nombres → on les écrit séparément
            parts.extend(str(arr[k]) for k in range(i, j + 1))
        i = j + 1
    return ",".join(parts)


# --- PIN Variations ---
# Pour chaque chiffre du PIN observé, on liste les chiffres adjacents sur le clavier
# (voisins horizontaux/verticaux + le chiffre lui-même).
# Ensuite on génère toutes les combinaisons possibles avec itertools.product.
# Ex: "11" → chaque "1" peut être 1,2,4 → 3×3 = 9 combinaisons

ADJACENT = {
    "0": ["0", "8"],
    "1": ["1", "2", "4"],
    "2": ["2", "1", "3", "5"],
    "3": ["3", "2", "6"],
    "4": ["4", "1", "5", "7"],
    "5": ["5", "2", "4", "6", "8"],
    "6": ["6", "3", "5", "9"],
    "7": ["7", "4", "8"],
    "8": ["8", "7", "9", "5", "0"],
    "9": ["9", "6", "8"],
}


def get_pins(observed):
    # product(*listes) génère toutes les combinaisons possibles (produit cartésien)
    return ["".join(combo) for combo in product(*[ADJACENT[d] for d in observed])]


# --- Strip Comments ---
# Pour chaque ligne, on cherche le premier marqueur de commentaire (ex: #, //, !)
# et on coupe la ligne à cet endroit.
# On supprime aussi les espaces en fin de ligne.
# Ex: "hello # world" avec marker "#" → "hello"

def strip_comments(text, markers):
    lines = []
    for line in text.split("\n"):
        for m in markers:
            idx = line.find(m)
            if idx != -1:
                line = line[:idx]  # On garde seulement ce qui est avant le marqueur
        lines.append(line.rstrip())
    return "\n".join(lines)


# --- Snail Sort ---
# On lit la matrice en spirale dans le sens horaire :
#   1. On prend la première ligne (haut)
#   2. On fait pivoter la matrice restante de 90° dans le sens antihoraire
#      (zip(*matrix) transpose, [::-1] inverse → équivalent à une rotation)
#   3. On répète jusqu'à ce que la matrice soit vide
# Ex: [[1,2,3],[4,5,6],[7,8,9]] → [1,2,3,6,9,8,7,4,5]

def snail(matrix):
    result = []
    while matrix:
        result += matrix.pop(0)      # On prend la première ligne
        matrix = list(zip(*matrix))[::-1]  # Rotation 90° antihoraire du reste
    return result


# --- Roman Numerals ---
# Table triée du plus grand au plus petit (avec les cas soustractifs comme CM, IX...).
# to_roman : on soustrait la plus grande valeur possible en boucle et on ajoute le symbole.
# from_roman : on lit 2 caractères d'abord (cas soustractifs), sinon 1 seul.
# Ex: 1990 → M(1000) CM(900) XC(90) → "MCMXC"

ROMAN_TABLE = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
    (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
]


def to_roman(n):
    result = ""
    for value, symbol in ROMAN_TABLE:
        while n >= value:
            result += symbol
            n -= value
    return result


def from_roman(s):
    roman_map = {sym: val for val, sym in ROMAN_TABLE}
    result = 0
    i = 0
    while i < len(s):
        # On essaie d'abord de lire 2 caractères (ex: CM, IX) avant 1 seul
        if i + 1 < len(s) and s[i:i+2] in roman_map:
            result += roman_map[s[i:i+2]]
            i += 2
        else:
            result += roman_map[s[i]]
            i += 1
    return result


# --- Daily Temperatures ---
# Pour chaque jour, on veut savoir combien de jours attendre pour avoir une température plus haute.
# On utilise une pile (stack) qui stocke les indices des jours "en attente".
# Quand on trouve une température plus haute, on dépile tous les jours plus froids
# et on calcule la différence d'indices.
# Ex: [73,74,75,71,69,72,76,73]
#   jour 0 (73) attend jour 1 (74) → 1 jour
#   jour 3 (71) et jour 4 (69) attendent jour 5 (72) → 2 et 1 jour

def daily_temperatures(temperatures):
    answer = [0] * len(temperatures)
    stack = []  # Pile d'indices de jours dont on n'a pas encore trouvé de jour plus chaud
    for i, temp in enumerate(temperatures):
        # Tant que la température actuelle est plus haute que celle du jour en haut de la pile
        while stack and temperatures[stack[-1]] < temp:
            j = stack.pop()
            answer[j] = i - j  # Nombre de jours d'attente
        stack.append(i)
    return answer


# --- Backspace String Compare ---
# On simule la frappe dans un éditeur de texte : '#' efface le dernier caractère.
# On utilise une liste comme pile : on empile les lettres, on dépile sur '#'.
# On compare ensuite les deux résultats finaux.
# Ex: "ab#c" → a,b,(#→efface b),c → "ac"
#     "ad#c" → a,d,(#→efface d),c → "ac"  → égaux → True

def backspace_compare(s, t):
    def process(string):
        result = []
        for ch in string:
            if ch == "#":
                if result:
                    result.pop()
            else:
                result.append(ch)
        return result
    return process(s) == process(t)


# --- Simplify Path ---
# On découpe le chemin par "/" et on traite chaque segment :
#   ".."  → on remonte d'un niveau (on dépile)
#   "."   → on reste sur place (on ignore)
#   ""    → slash multiple, on ignore
#   autre → dossier valide, on l'ajoute à la pile
# On reconstruit le chemin final à partir de la pile.
# Ex: "/a/./b/../../c/" → segments: a, ., b, .., .., c → pile finale: [c] → "/c"

def simplify_path(path):
    parts = []
    for segment in path.split("/"):
        if segment == "..":
            if parts:
                parts.pop()  # Remonter d'un niveau
        elif segment and segment != ".":
            parts.append(segment)  # Dossier valide
    return "/" + "/".join(parts)


# --- Longest Substring Without Repeating Characters ---
# On utilise une fenêtre glissante [left, right].
# On avance 'right' caractère par caractère et on mémorise la dernière position vue.
# Si on revoit un caractère déjà dans la fenêtre, on déplace 'left' juste après sa dernière occurrence.
# On garde la taille maximale atteinte.
# Ex: "abcabcbb" → fenêtre "abc" (taille 3), puis on glisse → max = 3

def length_of_longest_substring(s):
    seen = {}   # Mémorise la dernière position de chaque caractère
    left = 0    # Début de la fenêtre courante
    best = 0
    for right, ch in enumerate(s):
        # Si le caractère est déjà dans la fenêtre, on avance 'left'
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1
        seen[ch] = right
        best = max(best, right - left + 1)
    return best


# --- CheckDOM ---
# On vérifie que les balises HTML sont correctement imbriquées (comme des parenthèses).
# is_valid utilise une pile : ouvrante → on empile, fermante → on vérifie que le sommet correspond.
# check_dom essaie d'abord si c'est déjà valide.
# Sinon, on teste chaque balise ouvrante/fermante en la remplaçant par une autre balise valide.
# Si un seul changement suffit → on retourne le nom de la balise à changer.
# Si aucun changement unique ne suffit → False.
# Ex: "<div><i>hello</i>world</b>" → si on change <div> en <b> → valide → retourne "div"

VALID_TAGS = {"b", "i", "em", "div", "p"}


def parse_tags(s):
    # Extrait toutes les balises du HTML sous forme de liste de strings
    # Ex: "<div><b>hi</b></div>" → ["div", "b", "/b", "/div"]
    tags = []
    i = 0
    while i < len(s):
        if s[i] == "<":
            j = s.index(">", i)
            tag = s[i+1:j]
            tags.append(tag)
            i = j + 1
        else:
            while i < len(s) and s[i] != "<":
                i += 1
    return tags


def is_valid(tags):
    # Vérifie que les balises sont correctement imbriquées (principe de pile)
    stack = []
    for tag in tags:
        if not tag.startswith("/"):
            stack.append(tag)  # Balise ouvrante → on empile
        else:
            name = tag[1:]
            if not stack or stack[-1] != name:
                return False   # Fermante sans ouvrante correspondante
            stack.pop()
    return len(stack) == 0  # Toutes les ouvrantes ont été fermées


def check_dom(s):
    tags = parse_tags(s)
    if is_valid(tags):
        return True

    # On essaie de changer chaque balise ouvrante par une autre balise valide
    for i, tag in enumerate(tags):
        if tag.startswith("/"):
            continue
        for candidate in VALID_TAGS:
            if candidate == tag:
                continue
            new_tags = tags[:i] + [candidate] + tags[i+1:]
            if is_valid(new_tags):
                return tag  # On retourne le nom de la balise à changer

    # On essaie de changer chaque balise fermante par une autre balise valide
    for i, tag in enumerate(tags):
        if not tag.startswith("/"):
            continue
        name = tag[1:]
        for candidate in VALID_TAGS:
            if candidate == name:
                continue
            new_tags = tags[:i] + ["/" + candidate] + tags[i+1:]
            if is_valid(new_tags):
                return name

    return False  # Aucun changement unique ne suffit


# --- Menu interactif algos ---

def algos_menu():
    while True:
        print("\n--- Algorithmes ---")
        print("1.  Bookseller")
        print("2.  Deadfish")
        print("3.  Missing term in AP")
        print("4.  Sum of pairs")
        print("5.  Sum of parts")
        print("6.  Bracket Matcher")
        print("7.  Pick Peaks")
        print("8.  Range Extraction")
        print("9.  PIN Variations")
        print("10. Strip Comments")
        print("11. Snail Sort")
        print("12. Roman Numerals")
        print("13. Daily Temperatures")
        print("14. Backspace String Compare")
        print("15. Simplify Path")
        print("16. Longest Substring")
        print("17. CheckDOM")
        print("0.  Back")

        choice = input("Choice: ").strip()

        match choice:
            case "1":
                stock = ["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"]
                cats = ["A", "B", "C", "W"]
                print(stock_list(stock, cats))
            case "2":
                code = input("Deadfish program: ")
                print(parse(code))
            case "3":
                raw = input("Sequence (space separated): ")
                seq = list(map(int, raw.split()))
                print(find_missing(seq))
            case "4":
                raw = input("List (space separated): ")
                nums = list(map(int, raw.split()))
                s = int(input("Target sum: "))
                print(sum_of_pairs(nums, s))
            case "5":
                raw = input("List (space separated): ")
                ls = list(map(int, raw.split()))
                print(parts_sums(ls))
            case "6":
                s = input("String: ")
                print(bracket_matcher(s))
            case "7":
                raw = input("Array (space separated): ")
                arr = list(map(int, raw.split()))
                print(pick_peaks(arr))
            case "8":
                raw = input("Array (space separated): ")
                arr = list(map(int, raw.split()))
                print(solution(arr))
            case "9":
                observed = input("Observed PIN: ")
                pins = get_pins(observed)
                print(f"{len(pins)} variations: {pins}")
            case "10":
                text = input("Text (use \\n for newlines): ").replace("\\n", "\n")
                markers_raw = input("Markers (space separated): ")
                markers = markers_raw.split()
                print(strip_comments(text, markers))
            case "11":
                rows_input = input("Number of rows/cols: ")
                n = int(rows_input)
                matrix = []
                for i in range(n):
                    row = list(map(int, input(f"Row {i}: ").split()))
                    matrix.append(row)
                print(snail(matrix))
            case "12":
                sub = input("1. to Roman  2. from Roman: ").strip()
                if sub == "1":
                    n = int(input("Number: "))
                    print(to_roman(n))
                else:
                    r = input("Roman: ")
                    print(from_roman(r))
            case "13":
                raw = input("Temperatures (space separated): ")
                temps = list(map(int, raw.split()))
                print(daily_temperatures(temps))
            case "14":
                s = input("s: ")
                t = input("t: ")
                print(backspace_compare(s, t))
            case "15":
                path = input("Path: ")
                print(simplify_path(path))
            case "16":
                s = input("String: ")
                print(length_of_longest_substring(s))
            case "17":
                s = input("HTML string: ")
                print(check_dom(s))
            case "0":
                break
            case _:
                print("Invalid choice")
