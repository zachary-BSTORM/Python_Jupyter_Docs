# Gros exercice 1/3 : Le festival — listes de tuples et ensembles

## Contexte

Vous organisez un festival de musique. Le programme, les capacités des scènes et
les détenteurs de pass sont déjà encodés — à vous d'en tirer toutes les
informations utiles.

## Contrainte

**Sans classes, sans fonctions** : uniquement
variables, conditions, boucles, `input()` et les méthodes natives des
collections (`append`, `add`, `sort`…).

## Les données (à copier telles quelles)

```python
programme = [                                   # liste de TUPLES (groupe, scène, heure)
    ("Les Pythons", "Grande Scène", 18),
    ("Snake Charmers", "Club", 19),
    ("Boa Constrictor", "Plein Air", 18),
    ("Indentation", "Grande Scène", 20),
    ("Les Tuples", "Club", 21),
    ("Mamba Noir", "Grande Scène", 22),
]

capacites = {"Grande Scène": 5000, "Club": 800, "Plein Air": 2500}   # dict

pass_vendredi = {"Alice", "Bob", "Chloé", "David", "Emma"}           # sets
pass_samedi = {"Bob", "Emma", "Farid", "Gilles"}
```

## Les étapes

1. **L'affiche** — afficher le programme, une ligne par concert, en déballant
   chaque tuple directement dans le `for` (unpacking) :
   ```
   18h — Les Pythons (Grande Scène)
   19h — Snake Charmers (Club)
   ...
   ```
2. **Les scènes utilisées** — construire le **set** des scènes qui apparaissent
   dans le programme (boucle + `add` : les doublons disparaissent tout seuls),
   puis l'afficher avec son nombre : `3 scènes utilisées : {...}`.
3. **Concerts par scène** — construire le **dictionnaire compteur**
   `scène → nombre de concerts` :
   ```
   {'Grande Scène': 3, 'Club': 2, 'Plein Air': 1}
   ```
4. **À quelle heure ?** — demander une heure à l'utilisateur (vérifier avec
   `.isdigit()` que c'est un nombre) et afficher les concerts qui jouent à
   cette heure-là — ou un message s'il n'y en a aucun.
5. **Les pass** — à l'aide des opérations d'ensembles, afficher :
   - qui vient **les deux jours** (`&`) → `{'Bob', 'Emma'}`
   - qui ne vient **que vendredi** (`-`) → `{'Alice', 'Chloé', 'David'}`
   - le nombre de festivaliers **distincts** (`|` + `len`) → `7`
   - qui ne vient **qu'un seul jour** (`^`)
6. **La tête d'affiche** — trouver le concert le plus tardif **sans `sort`**
   (parcours avec un maximum provisoire) :
   `La soirée se termine avec Mamba Noir à 22h sur la Grande Scène`.

## Bonus

1. La scène la plus chargée (le maximum du dictionnaire de l'étape 3).
2. Trier le programme par heure **sans `key=`** : construire une liste de
   tuples `(heure, groupe)` puis appeler `.sort()` — expliquez en commentaire
   pourquoi ça marche. *(indice : comment deux tuples se comparent-ils ?)*
