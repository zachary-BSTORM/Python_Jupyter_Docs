# --- Correction de Exos_Ennoncés/collections_festival.md ---
# Le festival : liste de tuples + set + dict compteur + opérations d'ensembles.
# Contrainte : sans classes, sans fonctions (def), sans compréhensions.

programme = [                                   # liste de TUPLES (groupe, scène, heure)
    ("Les Pythons", "Grande Scène", 18),
    ("Snake Charmers", "Club", 19),
    ("Boa Constrictor", "Plein Air", 18),
    ("Indentation", "Grande Scène", 20),
    ("Les Tuples", "Club", 21),
    ("Mamba Noir", "Grande Scène", 22),
]

capacites = {"Grande Scène": 5000, "Club": 800, "Plein Air": 2500}

pass_vendredi = {"Alice", "Bob", "Chloé", "David", "Emma"}
pass_samedi = {"Bob", "Emma", "Farid", "Gilles"}


# ══ Étape 1 — L'affiche ══
# L'unpacking déballe chaque tuple directement dans le for
print("=== Programme du festival ===")
for groupe, scene, heure in programme:
    print(f"{heure}h — {groupe} ({scene})")

# ══ Étape 2 — Les scènes utilisées ══
# Un set : les ajouts en double sont ignorés automatiquement
scenes_utilisees = set()
for groupe, scene, heure in programme:
    scenes_utilisees.add(scene)

print(f"\n{len(scenes_utilisees)} scènes utilisées : {scenes_utilisees}")

# ══ Étape 3 — Concerts par scène ══
# LE pattern compteur : initialiser la clé à 0 si absente, puis += 1
concerts_par_scene = {}
for groupe, scene, heure in programme:
    if scene not in concerts_par_scene:
        concerts_par_scene[scene] = 0
    concerts_par_scene[scene] += 1

print(f"Concerts par scène : {concerts_par_scene}")

# ══ Étape 4 — À quelle heure ? ══
saisie = input("\nQuelle heure ? ")
if not saisie.isdigit():
    print("Ce n'est pas une heure valide")
else:
    heure_demandee = int(saisie)
    trouve = False
    for groupe, scene, heure in programme:
        if heure == heure_demandee:
            print(f"À {heure}h : {groupe} sur {scene}")
            trouve = True
    if not trouve:
        print(f"Aucun concert à {heure_demandee}h")

# ══ Étape 5 — Les pass ══
print("\n=== Les pass ===")
print(f"Présents les deux jours : {pass_vendredi & pass_samedi}")
print(f"Seulement vendredi      : {pass_vendredi - pass_samedi}")
print(f"Festivaliers distincts  : {len(pass_vendredi | pass_samedi)}")
print(f"Un seul jour            : {pass_vendredi ^ pass_samedi}")

# ══ Étape 6 — La tête d'affiche ══
# Maximum provisoire : on garde le TUPLE complet du concert le plus tardif
plus_tardif = programme[0]
for concert in programme:
    if concert[2] > plus_tardif[2]:         # l'heure est en position 2
        plus_tardif = concert

groupe, scene, heure = plus_tardif          # unpacking du gagnant
print(f"\nLa soirée se termine avec {groupe} à {heure}h sur la {scene}")

# ══ Bonus 1 — La scène la plus chargée ══
scene_max = ""
nb_max = 0
for scene, nb in concerts_par_scene.items():
    if nb > nb_max:
        scene_max = scene
        nb_max = nb
print(f"Scène la plus chargée : {scene_max} ({nb_max} concerts)")

# ══ Bonus 2 — Programme trié par heure, SANS key= ══
# Les tuples se comparent élément par élément : (18, "Boa...") < (19, "Snake...")
# En mettant l'heure EN PREMIER dans le tuple, sort() trie d'abord par heure
# (et départage par nom de groupe en cas d'égalité).
horaire = []
for groupe, scene, heure in programme:
    horaire.append((heure, groupe))

horaire.sort()
print("\n=== Programme trié ===")
for heure, groupe in horaire:
    print(f"{heure}h — {groupe}")
