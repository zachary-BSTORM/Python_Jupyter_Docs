import random
import time

# --- Démineur (Minesweeper) ---
# Architecture :
#   - hidden  : grille interne avec les mines ("*") et les chiffres (nombre de mines voisines)
#   - visible : ce que le joueur voit ("?" = caché, chiffre ou "*" si révélé)
#   - flags   : set de coordonnées (r, c) marquées par le joueur
#
# Mécanique clé — "safe first click" :
#   Les mines sont générées APRÈS le premier clic, en excluant la case cliquée.
#   Ainsi le joueur ne peut jamais exploser dès son premier coup.
#
# Propagation (reveal) :
#   Si une case révélée vaut 0 (aucune mine voisine), on propage récursivement à tous ses voisins.
#   C'est un DFS (depth-first search) implicite via la récursion.
#
# Commandes de jeu :
#   "row-col"   → ouvrir une case  (ex: 2-3)
#   "f row-col" → poser/retirer un drapeau (ex: f 2-3)


def create_grid(rows, cols, value):
    # Crée une grille rows x cols remplie d'une valeur initiale
    return [[value for _ in range(cols)] for _ in range(rows)]


def get_neighbors(rows, cols, r, c):
    # Retourne les coordonnées des cases adjacentes (8 directions) dans les limites de la grille
    neighbors = []
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                neighbors.append((nr, nc))
    return neighbors


def generate_mines(rows, cols, nb_mines, forbidden_cell):
    # Place les mines aléatoirement, en excluant la première case cliquée
    mines = set()
    while len(mines) < nb_mines:
        r = random.randint(0, rows - 1)
        c = random.randint(0, cols - 1)
        if (r, c) != forbidden_cell:
            mines.add((r, c))
    return mines


def create_hidden_grid(rows, cols, mines):
    # Construit la grille interne : "*" pour les mines, sinon le nombre de mines adjacentes
    grid = create_grid(rows, cols, 0)
    for r, c in mines:
        grid[r][c] = "*"
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "*":
                continue
            count = sum(1 for nr, nc in get_neighbors(rows, cols, r, c) if (nr, nc) in mines)
            grid[r][c] = count
    return grid


def reveal(hidden, visible, r, c):
    # Révèle une case ; si elle vaut 0, propage récursivement aux voisins non encore révélés
    rows = len(hidden)
    cols = len(hidden[0])
    if visible[r][c] != "?":
        return
    visible[r][c] = hidden[r][c]
    if hidden[r][c] == 0:
        for nr, nc in get_neighbors(rows, cols, r, c):
            if visible[nr][nc] == "?":
                reveal(hidden, visible, nr, nc)


def print_grid(grid):
    # Affiche la grille avec les numéros de lignes et colonnes en en-tête
    rows = len(grid)
    cols = len(grid[0])
    col_header = "    " + "  ".join(str(c) for c in range(cols))
    print(col_header)
    print("   " + "-" * (cols * 3))
    for r in range(rows):
        row_str = f"{r:2} | "
        for c in range(cols):
            cell = grid[r][c]
            # Les cases à 0 sont affichées avec un point pour plus de lisibilité
            if cell == 0:
                row_str += ".  "
            else:
                row_str += f"{cell}  "
        print(row_str)


def has_won(hidden, visible):
    # Vérifie si toutes les cases sans mine ont été révélées
    for r in range(len(hidden)):
        for c in range(len(hidden[0])):
            if hidden[r][c] != "*" and visible[r][c] == "?":
                return False
    return True


def minesweeper(rows=9, cols=9, nb_mines=10):
    # Grille visible initialement entièrement cachée ("?")
    visible = create_grid(rows, cols, "?")
    # La grille interne et les mines sont générées au premier clic
    hidden = None
    mines = None
    flags = set()
    first_click = True
    moves = 0
    start_time = time.time()

    print(f"\nMinesweeper {rows}x{cols} — {nb_mines} mines")
    print("Open a cell: row-col  (ex: 2-3)")
    print("Flag a cell: f row-col  (ex: f 2-3)\n")

    while True:
        # Construit la grille d'affichage en superposant les drapeaux sur la grille visible
        display = create_grid(rows, cols, "?")
        for r in range(rows):
            for c in range(cols):
                if (r, c) in flags:
                    display[r][c] = "F"
                else:
                    v = visible[r][c]
                    display[r][c] = v if v != "?" else "?"

        print_grid(display)

        raw = input("\n> ").strip().lower().split()

        # Format accepté : "row-col" pour ouvrir, "f row-col" pour un drapeau
        if len(raw) == 1:
            cmd = "o"
            coords_str = raw[0]
        elif len(raw) == 2 and raw[0] == "f":
            cmd = "f"
            coords_str = raw[1]
        else:
            print("Invalid input. Use: row-col  or  f row-col  (ex: 2-3 or f 2-3)")
            continue

        try:
            r, c = map(int, coords_str.split("-"))
        except ValueError:
            print("Invalid coordinates. Use format: row-col  (ex: 2-3)")
            continue

        if not (0 <= r < rows and 0 <= c < cols):
            print(f"Coordinates out of range (0-{rows-1}, 0-{cols-1})")
            continue

        if cmd == "f":
            if visible[r][c] != "?":
                print("Cannot flag a revealed cell")
                continue
            # Bascule le drapeau : pose ou retire
            if (r, c) in flags:
                flags.discard((r, c))
                print("Flag removed")
            else:
                flags.add((r, c))
                print("Flag placed")

        elif cmd == "o":
            if (r, c) in flags:
                print("Remove the flag first")
                continue
            if visible[r][c] != "?":
                print("Cell already revealed")
                continue

            # Premier clic : on génère les mines maintenant pour garantir que la case est sûre
            if first_click:
                mines = generate_mines(rows, cols, nb_mines, (r, c))
                hidden = create_hidden_grid(rows, cols, mines)
                first_click = False

            moves += 1

            if hidden[r][c] == "*":
                # Mine touchée : on révèle toute la grille et on affiche game over
                for mr, mc in mines:
                    visible[mr][mc] = "*"
                print_grid(visible)
                elapsed = round(time.time() - start_time, 1)
                print(f"\n BOOM! Game over after {moves} moves and {elapsed}s")
                return

            reveal(hidden, visible, r, c)

            if has_won(hidden, visible):
                elapsed = round(time.time() - start_time, 1)
                print_grid(visible)
                print(f"\n You win! {moves} moves in {elapsed}s")
                return

        else:
            print("Unknown command. Use 'o' or 'f'")
