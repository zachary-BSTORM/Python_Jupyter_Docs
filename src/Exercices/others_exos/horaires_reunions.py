# --- Correction de Exos_Ennoncés/horaires_reunions.md ---
# Les 5 exercices progressifs : plages libres, fusion, bornage, pipeline final.
# Version pseudo-code : correction-pseudo-code/horaires-reunions.algo


# ══ Exercice 1 — Trouver les plages libres ══
# Pré-condition : réunions triées et sans chevauchement.
def free_slots(start_work, end_work, meetings):
    """Les trous entre les réunions, bornes de la journée comprises."""
    libres = []
    curseur = start_work                    # fin de la dernière occupation connue

    for debut, fin in meetings:
        if debut > curseur:                 # un trou avant cette réunion
            libres.append([curseur, debut])
        curseur = fin

    if curseur < end_work:                  # le trou final, jusqu'à la fin de journée
        libres.append([curseur, end_work])
    return libres


# ══ Exercice 2 — Fusionner les réunions qui se chevauchent ══
def merge_meetings(meetings):
    """Trie, puis parcourt : chaque réunion prolonge la dernière plage ou en ouvre une."""
    fusionnees = []

    for debut, fin in sorted(meetings):     # tri par heure de début
        if fusionnees and debut <= fusionnees[-1][1]:
            # chevauche (ou touche : exigé à l'exercice 4) → on prolonge la dernière
            fusionnees[-1][1] = max(fusionnees[-1][1], fin)
        else:
            fusionnees.append([debut, fin])     # nouvelle plage indépendante
    return fusionnees


# ══ Exercice 3 — Réunions à l'intérieur des heures de travail ══
def clip_meetings(start_work, end_work, meetings):
    """Tronque chaque réunion à la journée ; écarte celles qui deviennent vides."""
    bornees = []

    for debut, fin in meetings:
        nouveau_debut = max(debut, start_work)
        nouvelle_fin = min(fin, end_work)
        if nouveau_debut < nouvelle_fin:    # il reste quelque chose dans la journée
            bornees.append([nouveau_debut, nouvelle_fin])
    return bornees


# ══ Exercices 4 et 5 — Le planning complet ══
def get_free_time(start_work, end_work, meetings):
    """Le pipeline : borner (ex. 3) → fusionner (ex. 2) → trous (ex. 1)."""
    occupees = clip_meetings(start_work, end_work, meetings)    # étape 1
    occupees = merge_meetings(occupees)                         # étapes 2 et 3
    return free_slots(start_work, end_work, occupees)           # étapes 4 et 5


# ══ Difficulté supplémentaire — tout à la main (style examen) ══
# Sans sorted() ni fonction toute faite : tri par insertion (cf. exo 26),
# fusion et trous dans la même fonction.
def get_free_time_manuel(start_work, end_work, meetings):
    # 1. borner à la journée
    occupees = []
    for debut, fin in meetings:
        if debut < start_work:
            debut = start_work
        if fin > end_work:
            fin = end_work
        if debut < fin:
            occupees.append([debut, fin])

    # 2. tri manuel : insertion de chaque réunion à sa position
    triees = []
    for reunion in occupees:
        position = 0
        while position < len(triees) and triees[position][0] < reunion[0]:
            position += 1
        triees.insert(position, reunion)

    # 3. fusion des plages qui se chevauchent ou se touchent
    fusionnees = []
    for debut, fin in triees:
        if len(fusionnees) > 0 and debut <= fusionnees[-1][1]:
            if fin > fusionnees[-1][1]:
                fusionnees[-1][1] = fin
        else:
            fusionnees.append([debut, fin])

    # 4. les trous entre les plages, bornes comprises
    libres = []
    curseur = start_work
    for debut, fin in fusionnees:
        if debut > curseur:
            libres.append([curseur, debut])
        curseur = fin
    if curseur < end_work:
        libres.append([curseur, end_work])
    return libres


# ═══════════════ Les 11 exemples de l'énoncé ═══════════════
tests = [
    ("exo 1, exemple", free_slots(8, 17, [[9, 10], [11, 13], [15, 16]]),
     [[8, 9], [10, 11], [13, 15], [16, 17]]),
    ("exo 1, cas supplémentaire", free_slots(8, 17, [[8, 10], [12, 14], [15, 17]]),
     [[10, 12], [14, 15]]),
    ("exo 2, exemple 1", merge_meetings([[9, 11], [10, 13], [14, 16], [15, 17]]),
     [[9, 13], [14, 17]]),
    ("exo 2, exemple 2", merge_meetings([[11, 13], [5, 8], [7, 10], [15, 16]]),
     [[5, 10], [11, 13], [15, 16]]),
    ("exo 3, exemple 1", clip_meetings(8, 17, [[5, 9], [11, 13], [15, 20]]),
     [[8, 9], [11, 13], [15, 17]]),
    ("exo 3, exemple 2", clip_meetings(9, 18, [[6, 10], [8, 12], [16, 20]]),
     [[9, 10], [9, 12], [16, 18]]),
    ("exo 4, occupées", merge_meetings(clip_meetings(8, 17,
        [[5, 8], [7, 10], [9, 12], [13, 14], [13, 16], [16, 18]])),
     [[8, 12], [13, 17]]),
    ("exo 4, libres", get_free_time(8, 17,
        [[5, 8], [7, 10], [9, 12], [13, 14], [13, 16], [16, 18]]),
     [[12, 13]]),
    ("exo 5, exemple 1", get_free_time(8, 17, [[5, 8], [9, 11], [10, 13], [14, 15], [15, 16]]),
     [[8, 9], [13, 14], [16, 17]]),
    ("exo 5, exemple 2", get_free_time(8, 17, [[5, 10], [8, 12], [11, 14], [16, 20]]),
     [[14, 16]]),
    ("exo 5, exemple 3", get_free_time(9, 18, [[12, 13], [9, 10], [15, 17], [10, 12], [16, 18]]),
     [[13, 15]]),
]

for nom, obtenu, attendu in tests:
    statut = "OK" if obtenu == attendu else f"ÉCHEC (attendu {attendu})"
    print(f"{nom:28s} {statut:6s} → {obtenu}")

# La version manuelle doit donner les mêmes résultats que le pipeline
for sw, ew, m in [(8, 17, [[5, 8], [9, 11], [10, 13], [14, 15], [15, 16]]),
                  (8, 17, [[5, 10], [8, 12], [11, 14], [16, 20]]),
                  (9, 18, [[12, 13], [9, 10], [15, 17], [10, 12], [16, 18]])]:
    identique = get_free_time_manuel(sw, ew, m) == get_free_time(sw, ew, m)
    print(f"version manuelle = pipeline : {identique}")
