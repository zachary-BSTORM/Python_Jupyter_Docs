# Concessionnaire automobile — explications de la correction

Notes qui accompagnent `crud_concessionnaire.py` : les choix de conception, point
par point, et les pièges à montrer en salle.

## 1. L'architecture en une image

```
démarrage ──► charger_voitures() ──► voitures (dict en mémoire)
                                          │
              ┌──── boucle de menu ◄──────┘
              │
              │  option 1, 2 : lecture seule       → pas de sauvegarde
              │  option 3, 4, 5 : le dict CHANGE   → sauvegarder_voitures()
              │                                      (le fichier est écrasé)
              └──── 0 : quitter (rien à faire, le fichier est déjà à jour)
```

Le principe : **la mémoire est la source de vérité pendant l'exécution**, le
fichier n'est qu'une photographie, re-prise après chaque changement. C'est le
modèle de la plupart des petites applications (et c'est exactement ce que fera
la base de données au jour web — en mieux).

## 2. Pourquoi un dictionnaire DE dictionnaires ?

| Avec une liste de dicts | Avec un dict de dicts (notre choix) |
|---|---|
| retrouver une voiture = **boucler** en comparant les plaques | `voitures["1-ABC-123"]` → **accès direct** |
| doublons de plaque possibles, à vérifier soi-même | les clés d'un dict sont **uniques par nature** |
| supprimer = retrouver l'index puis `pop(i)` | `del voitures[plaque]` |

La plaque est ce qu'on appelle une **clé métier** : une donnée du monde réel,
unique par nature, qui sert d'identifiant. Le test d'existence s'écrit
simplement `plaque in voitures` — utilisé par les options 2, 3, 4 et 5.

## 3. La persistance JSON

### `dump` / `load` vs `dumps` / `loads` (le « stringify » de Python)

| Python | JavaScript | Travaille avec |
|---|---|---|
| `json.dumps(obj)` | `JSON.stringify(obj)` | une **chaîne** |
| `json.loads(texte)` | `JSON.parse(texte)` | une **chaîne** |
| `json.dump(obj, f)` | — | directement un **fichier** |
| `json.load(f)` | — | directement un **fichier** |

Le « s » signifie *string*. Ici on utilise les versions fichier : une étape de
moins. (`json.dump(obj, f)` ⇔ `f.write(json.dumps(obj))`.)

### Les trois paramètres qui changent tout

```python
with open(FICHIER, "w", encoding="utf-8") as f:
    json.dump(voitures, f, ensure_ascii=False, indent=4)
```

- `"w"` : oure en écriture **en écrasant** tout l'ancien contenu — c'est voulu :
  on ré-écrit la photographie complète du stock à chaque fois.
- `encoding="utf-8"` : sans lui, Windows utilise cp1252 → les accents se
  corrompent entre machines. **Toujours** le préciser, en lecture ET en écriture.
- `ensure_ascii=False` : sinon « Citroën » devient `"Citroën"` dans le
  fichier (valide mais illisible pour un humain).
- `indent=4` : un objet par bloc indenté au lieu d'une seule ligne compacte —
  le fichier devient lisible et modifiable à la main dans VS Code.

### Pourquoi sauvegarder à CHAQUE changement (et pas à la sortie) ?

Si on ne sauvegardait qu'au moment de quitter : un crash, un Ctrl+C, une coupure
→ tout le travail de la session est perdu. En écrasant le fichier après chaque
mutation, le fichier est toujours synchronisé avec la mémoire. Coût : ré-écrire
quelques kilo-octets — invisible à cette échelle.

### Un détail élégant de `charger_voitures()`

```python
if not os.path.exists(FICHIER):
    sauvegarder_voitures(STOCK_DEPART)   # premier lancement : on crée le fichier...
with open(FICHIER, "r", encoding="utf-8") as f:
    return json.load(f)                  # ...puis UN SEUL chemin de lecture
```

Au lieu de « si le fichier existe je le lis, sinon je renvoie le stock de
départ », on **crée d'abord le fichier manquant puis on lit dans tous les cas** :
un seul chemin de sortie, et subtilité bonus — on ne renvoie jamais
`STOCK_DEPART` lui-même (modifier la constante partagée serait un piège de
référence, cf. la copie superficielle du cours collections).

### JSON garde les types

`annee`, `prix`, `kilometrage` sont stockés comme **nombres** JSON : au
rechargement, ce sont déjà des `int` — aucune reconversion. (Comparer avec un
fichier texte « maison » ou CSV, où tout revient en `str` : c'est un argument
clé en faveur de JSON.)

## 4. Deux stratégies de saisie numérique — et pourquoi

| Contexte | Outil | Raison |
|---|---|---|
| Ajout (option 3) | `demander_entier()` : `while True` + `try/except` | la valeur est **obligatoire** → on insiste jusqu'à l'obtenir |
| Modification (option 4) | `input()` + `.isdigit()` | une saisie **vide est légitime** (= conserver) → impossible d'« insister », on teste soi-même |

`demander_entier` est le pattern « saisie robuste » du cours exceptions,
réutilisé tel quel. Faire remarquer qu'un même problème (valider un nombre) a
deux bonnes réponses selon le contexte — c'est ça, concevoir.

## 5. La modification travaille « par référence »

```python
voiture = voitures[plaque]      # PAS une copie : une référence au dict interne
voiture["marque"] = marque      # ... donc voitures est modifié aussi
```

C'est le partage de référence vu au chapitre collections — ici il **joue pour
nous** : on modifie `voiture` et le grand dictionnaire est à jour, sans rien
recopier. Bon moment pour refaire le lien avec `alias = original`.

## 6. Petites finitions qui font les bons programmes

- `.strip().upper()` sur les plaques : `" 1-abc-123 "` et `"1-ABC-123"`
  désignent la même voiture — on **normalise** la clé à l'entrée.
- Confirmation `o/n` avant suppression, en rappelant marque et modèle : une
  suppression est irréversible, on ne supprime jamais « en aveugle ».
- Le choix de menu reste une **chaîne** (`case "3"`) : aucun plantage possible
  sur le menu, pas besoin de conversion.
- `afficher_liste()` est appelée par les options 1, 4 et 5 — le copier-coller
  du CRUD contacts a disparu : c'est la promesse des fonctions, tenue.

## 7. Pièges classiques à montrer en salle

1. **Oublier `encoding="utf-8"`** : marche chez soi, casse les accents chez le
   voisin (cp1252). Le démontrer en ouvrant le JSON produit sans l'option.
2. **Ouvrir en `"w"` trop tôt** : `open(FICHIER, "w")` vide le fichier
   immédiatement, même si on ne `dump` jamais — à ne faire qu'au moment précis
   d'écrire.
3. **Oublier une `sauvegarder_voitures()`** après une mutation : tout semble
   marcher… jusqu'au redémarrage. Le test « quitter puis relancer » de l'énoncé
   attrape exactement ça.
4. **Chemin relatif** : `concessionnaire.json` est créé dans le dossier **d'où
   on lance** le programme (le répertoire courant), pas forcément à côté du
   script. En salle : lancer depuis le bon dossier, ou montrer le problème.

## 8. Pistes pour les bonus

```python
# Bonus 1 — recherche par marque (insensible à la casse)
recherche = input("Marque : ").strip().lower()
for plaque, voiture in voitures.items():
    if voiture["marque"].lower() == recherche:
        print(f"  {plaque} — {voiture['marque']} {voiture['modele']}")

# Bonus 2 — budget maximum
budget = demander_entier("Budget maximum (€) : ")
for plaque, voiture in voitures.items():
    if voiture["prix"] <= budget:
        print(f"  {plaque} — {voiture['modele']} : {voiture['prix']} €")

# Bonus 3 — statistiques au démarrage
total = 0
for voiture in voitures.values():
    total += voiture["prix"]
print(f"{len(voitures)} voitures — prix moyen : {total / len(voitures):.0f} €")

# Bonus 4 — fichier corrompu : blinder charger_voitures()
try:
    with open(FICHIER, "r", encoding="utf-8") as f:
        return json.load(f)
except json.JSONDecodeError:
    print("⚠ Fichier illisible : on repart du stock de départ")
    sauvegarder_voitures(STOCK_DEPART)
    return dict(STOCK_DEPART)
```
