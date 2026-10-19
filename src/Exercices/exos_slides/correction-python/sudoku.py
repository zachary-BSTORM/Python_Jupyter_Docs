import copy

CHIFFRES = set(range(1, 10))


# ---------- Exercice 1 : vérifier une grille complète ----------

def est_valide(grille):
    # Lignes et colonnes
    for i in range(9):
        ligne = set(grille[i])
        colonne = {grille[l][i] for l in range(9)}
        if ligne != CHIFFRES or colonne != CHIFFRES:
            return False

    # Blocs 3x3 (coin haut-gauche : 0, 3, 6)
    for bl in range(0, 9, 3):
        for bc in range(0, 9, 3):
            bloc = {grille[l][c] for l in range(bl, bl + 3) for c in range(bc, bc + 3)}
            if bloc != CHIFFRES:
                return False

    return True


# ---------- Exercice 2 : compléter une grille (backtracking) ----------

def peut_placer(grille, l, c, n):
    """Vrai si n peut aller en (l, c) sans conflit."""
    if n in grille[l]:
        return False
    if any(grille[i][c] == n for i in range(9)):
        return False
    bl, bc = 3 * (l // 3), 3 * (c // 3)
    for i in range(bl, bl + 3):
        for j in range(bc, bc + 3):
            if grille[i][j] == n:
                return False
    return True


def resoudre(grille):
    """Complète la grille sur place. Renvoie True si une solution existe."""
    for l in range(9):
        for c in range(9):
            if grille[l][c] == 0:
                for n in range(1, 10):
                    if peut_placer(grille, l, c, n):
                        grille[l][c] = n
                        if resoudre(grille):
                            return True
                        grille[l][c] = 0      # retour arrière
                return False                  # aucun chiffre ne convient
    return True                               # plus de case vide : terminé


def afficher(grille):
    for l, ligne in enumerate(grille):
        if l % 3 == 0 and l:
            print("------+-------+------")
        print(" ".join(
            ("| " if c in (3, 6) else "") + (str(v) if v else ".")
            for c, v in enumerate(ligne)
        ))


# ---------- Tests ----------

if __name__ == "__main__":
    grille_valide = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9],
    ]
    grille_invalide = copy.deepcopy(grille_valide)
    grille_invalide[0][0] = 3

    grille_1 = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]
    grille_2 = [
        [0, 0, 4, 5, 3, 0, 2, 7, 1],
        [2, 0, 1, 8, 0, 4, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 6, 0],
        [3, 0, 0, 7, 0, 0, 0, 0, 5],
        [6, 4, 0, 0, 9, 2, 0, 0, 0],
        [0, 1, 0, 0, 0, 5, 0, 9, 2],
        [0, 8, 6, 0, 5, 3, 9, 0, 7],
        [0, 2, 0, 1, 8, 6, 0, 5, 0],
        [4, 0, 0, 9, 0, 0, 0, 0, 0],
    ]
    grille_3 = [
        [0, 6, 0, 5, 0, 9, 0, 0, 1],
        [2, 0, 0, 0, 0, 0, 0, 3, 0],
        [5, 0, 0, 0, 0, 1, 0, 0, 0],
        [3, 9, 2, 0, 0, 0, 6, 0, 5],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 5, 3, 9, 0],
        [0, 8, 6, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 1, 8, 6, 0, 5, 0],
        [0, 5, 0, 9, 2, 0, 1, 8, 0],
    ]
    solution_2_3 = [
        [8, 6, 4, 5, 3, 9, 2, 7, 1],
        [2, 7, 1, 8, 6, 4, 5, 3, 9],
        [5, 3, 9, 2, 7, 1, 8, 6, 4],
        [3, 9, 2, 7, 1, 8, 6, 4, 5],
        [6, 4, 5, 3, 9, 2, 7, 1, 8],
        [7, 1, 8, 6, 4, 5, 3, 9, 2],
        [1, 8, 6, 4, 5, 3, 9, 2, 7],
        [9, 2, 7, 1, 8, 6, 4, 5, 3],
        [4, 5, 3, 9, 2, 7, 1, 8, 6],
    ]

    print("Exercice 1")
    print("  grille_valide   :", est_valide(grille_valide))
    print("  grille_invalide :", est_valide(grille_invalide))

    print("\nExercice 2")
    for nom, g, attendu in [("grille_1", grille_1, grille_valide),
                            ("grille_2", grille_2, solution_2_3),
                            ("grille_3", grille_3, solution_2_3)]:
        resoudre(g)
        print(f"  {nom} : résolue={est_valide(g)}, conforme={g == attendu}")

    print()
    afficher(grille_3)