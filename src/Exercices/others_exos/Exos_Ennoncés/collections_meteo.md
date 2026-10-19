# Gros exercice 3/3 : La station météo — analyse d'une quinzaine

## Contexte

Une station météo a enregistré 14 jours de relevés (2 semaines complètes).
Chaque relevé est un tuple `(jour, température, pluie_en_mm)`. Vous écrivez le
rapport d'analyse complet — c'est un travail de **données**, sans menu.

## Contrainte

⚠ **Sans classes, sans fonctions (`def`), sans compréhensions** — boucles,
conditions, unpacking, slicing, et les méthodes natives des collections.

## Les données (à copier telles quelles)

```python
releves = [                       # 14 TUPLES (jour, température °C, pluie mm)
    ("lundi", 12, 5.2), ("mardi", 15, 0.0), ("mercredi", 9, 12.5),
    ("jeudi", 11, 3.0), ("vendredi", 18, 0.0), ("samedi", 21, 0.0),
    ("dimanche", 17, 1.2),
    ("lundi", 14, 0.0), ("mardi", 10, 8.4), ("mercredi", 13, 0.0),
    ("jeudi", 16, 0.5), ("vendredi", 19, 0.0), ("samedi", 23, 0.0),
    ("dimanche", 20, 2.8),
]
```

## Les étapes

1. **Le thermomètre** — en un seul parcours (unpacking dans le `for`) : la
   température minimale, la maximale et la moyenne de la quinzaine
   (`Moyenne : 15.6 °C` — une décimale, `:.1f`).
2. **Les jours de pluie** — construire :
   - la **liste** des relevés pluvieux (pluie > 0) et son nombre → `7` ;
   - le **set** des *noms* de jours où il a plu au moins une fois → 5 noms
     (sur 14 relevés, les noms se répètent : le set dédoublonne).
3. **Cumul de pluie par jour de la semaine** — le **dictionnaire accumulateur**
   `nom du jour → total des mm sur les 2 semaines` (même pattern que le
   compteur : initialiser la clé à 0 si absente, puis `+=`) :
   ```
   {'lundi': 5.2, 'mardi': 8.4, 'mercredi': 12.5, 'jeudi': 3.5,
    'vendredi': 0.0, 'samedi': 0.0, 'dimanche': 4.0}
   ```
4. **Le jour le plus chaud** — parcours avec maximum provisoire (sans `sort`) :
   `Record : samedi, 23 °C` — attention, il faut retenir le **nom** ET la
   température.
5. **Semaine 1 vs semaine 2** — découper `releves` en deux avec le **slicing**
   (`[:7]` et `[7:]`), calculer la température moyenne de chaque semaine, et
   afficher laquelle a été la plus chaude.
6. **Interrogation** — demander un nom de jour à l'utilisateur et afficher ses
   relevés des deux semaines (`lundi : 12 °C, 5.2 mm de pluie` …), puis son
   cumul de pluie en réutilisant le dictionnaire de l'étape 3 (`.get()` pour
   un nom inconnu → message).

## Bonus

1. Le nombre de jours « secs » consécutifs le plus long de la quinzaine
   (compteur remis à zéro à chaque jour de pluie, maximum provisoire).
2. L'écart de température entre deux relevés consécutifs le plus brutal
   (boucle sur les **indices** avec `range(1, len(releves))`).
