# --- Correction de Exos_Ennoncés/collections_meteo.md ---
# La station météo : tuples + unpacking + dict accumulateur + set + slicing.
# Contrainte : sans classes, sans fonctions (def), sans compréhensions.

releves = [                       # 14 TUPLES (jour, température °C, pluie mm)
    ("lundi", 12, 5.2), ("mardi", 15, 0.0), ("mercredi", 9, 12.5),
    ("jeudi", 11, 3.0), ("vendredi", 18, 0.0), ("samedi", 21, 0.0),
    ("dimanche", 17, 1.2),
    ("lundi", 14, 0.0), ("mardi", 10, 8.4), ("mercredi", 13, 0.0),
    ("jeudi", 16, 0.5), ("vendredi", 19, 0.0), ("samedi", 23, 0.0),
    ("dimanche", 20, 2.8),
]


# ══ Étape 1 — Le thermomètre (un seul parcours) ══
premier_jour, premiere_temp, premiere_pluie = releves[0]
temp_min = premiere_temp
temp_max = premiere_temp
total_temp = 0

for jour, temperature, pluie in releves:        # unpacking dans le for
    if temperature < temp_min:
        temp_min = temperature
    if temperature > temp_max:
        temp_max = temperature
    total_temp += temperature

moyenne = total_temp / len(releves)
print("=== Le thermomètre ===")
print(f"Minimum : {temp_min} °C | Maximum : {temp_max} °C | Moyenne : {moyenne:.1f} °C")

# ══ Étape 2 — Les jours de pluie ══
releves_pluvieux = []           # les relevés complets (liste)
noms_jours_pluie = set()        # les NOMS de jours, dédoublonnés (set)

for jour, temperature, pluie in releves:
    if pluie > 0:
        releves_pluvieux.append((jour, temperature, pluie))
        noms_jours_pluie.add(jour)

print("\n=== Les jours de pluie ===")
print(f"Il a plu sur {len(releves_pluvieux)} relevés sur {len(releves)}")
print(f"Jours de la semaine touchés ({len(noms_jours_pluie)}) : {noms_jours_pluie}")

# ══ Étape 3 — Cumul de pluie par jour de la semaine ══
# Le pattern ACCUMULATEUR : comme le compteur, mais on ajoute la valeur
cumul_pluie = {}
for jour, temperature, pluie in releves:
    if jour not in cumul_pluie:
        cumul_pluie[jour] = 0
    cumul_pluie[jour] += pluie

print(f"\nCumul de pluie : {cumul_pluie}")

# ══ Étape 4 — Le jour le plus chaud ══
# Maximum provisoire : il faut retenir le nom ET la température
jour_record = ""
temp_record = temp_min                  # on part du minimum connu
for jour, temperature, pluie in releves:
    if temperature > temp_record:
        jour_record = jour
        temp_record = temperature

print(f"\nRecord : {jour_record}, {temp_record} °C")

# ══ Étape 5 — Semaine 1 vs semaine 2 (slicing) ══
semaine_1 = releves[:7]                 # les 7 premiers relevés
semaine_2 = releves[7:]                 # les 7 suivants

total_1 = 0
for jour, temperature, pluie in semaine_1:
    total_1 += temperature
moyenne_1 = total_1 / len(semaine_1)

total_2 = 0
for jour, temperature, pluie in semaine_2:
    total_2 += temperature
moyenne_2 = total_2 / len(semaine_2)

print("\n=== Semaine 1 vs semaine 2 ===")
print(f"Semaine 1 : {moyenne_1:.1f} °C | Semaine 2 : {moyenne_2:.1f} °C")
if moyenne_2 > moyenne_1:
    print("La semaine 2 a été la plus chaude")
elif moyenne_1 > moyenne_2:
    print("La semaine 1 a été la plus chaude")
else:
    print("Les deux semaines sont à égalité")

# ══ Étape 6 — Interrogation ══
demande = input("\nQuel jour voulez-vous consulter ? ").strip().lower()

if cumul_pluie.get(demande) is None:    # .get() : pas de KeyError sur un nom inconnu
    print(f"« {demande} » n'est pas un jour connu de la station")
else:
    for jour, temperature, pluie in releves:
        if jour == demande:
            print(f"{jour} : {temperature} °C, {pluie} mm de pluie")
    print(f"Cumul de pluie des {demande}s : {cumul_pluie[demande]} mm")

# ══ Bonus 1 — La plus longue série de jours secs ══
serie_actuelle = 0
serie_record = 0
for jour, temperature, pluie in releves:
    if pluie == 0:
        serie_actuelle += 1
        if serie_actuelle > serie_record:
            serie_record = serie_actuelle
    else:
        serie_actuelle = 0              # la pluie casse la série

print(f"\nPlus longue série de jours secs : {serie_record}")

# ══ Bonus 2 — L'écart de température le plus brutal ══
# Comparer chaque relevé au PRÉCÉDENT → boucle sur les indices à partir de 1
ecart_max = 0
ou = ""
for i in range(1, len(releves)):
    ecart = releves[i][1] - releves[i - 1][1]   # position 1 du tuple = température
    if ecart < 0:
        ecart = -ecart                          # valeur absolue « à la main »
    if ecart > ecart_max:
        ecart_max = ecart
        ou = f"entre {releves[i - 1][0]} ({releves[i - 1][1]} °C) et {releves[i][0]} ({releves[i][1]} °C)"

print(f"Écart le plus brutal : {ecart_max} °C, {ou}")
