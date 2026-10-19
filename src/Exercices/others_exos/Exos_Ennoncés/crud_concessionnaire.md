# Gros exercice : Concessionnaire automobile — CRUD avec persistance JSON

## Description

Vous gérez le parc d'un concessionnaire automobile. Le programme est un CRUD complet
en console (comme le répertoire de contacts)… mais cette fois **les données survivent
à la fermeture du programme** : elles sont stockées dans un fichier JSON.

Cet exercice est une **synthèse** de tout ce qui a été vu : collections, boucles,
fonctions, exceptions, fichiers et JSON.

## La structure de données

Chaque voiture est un **dictionnaire**. Toutes les voitures sont rangées **dans un
dictionnaire** dont la clé est la plaque d'immatriculation (unique par nature) :

```python
voitures = {
    "1-ABC-123": {
        "marque": "Renault",
        "modele": "Clio",
        "annee": 2019,
        "prix": 11500,
        "kilometrage": 68000,
    },
    "1-DEF-456": {
        "marque": "Peugeot",
        "modele": "208",
        "annee": 2021,
        "prix": 15900,
        "kilometrage": 32000,
    },
}
```

> Pourquoi un dictionnaire plutôt qu'une liste ? Parce qu'on accède à une voiture
> **directement par sa plaque** — `voitures["1-ABC-123"]` — sans parcourir de liste,
> et l'unicité des plaques est garantie gratuitement.

## La persistance (le cœur de l'exercice)

Le stock vit dans un fichier **`concessionnaire.json`**, à côté du script.

1. **Au démarrage du programme** (avant le premier menu) : charger le fichier avec
   `json.load(...)`. Si le fichier n'existe pas encore (tout premier lancement),
   démarrer avec un stock de départ de 3 voitures **et créer le fichier
   immédiatement**.
2. **Après chaque changement** (ajout, modification, suppression) : ré-écrire le
   fichier **en entier** avec `json.dump(...)` — on ouvre en mode `"w"`, qui
   **écrase** l'ancien contenu.
3. Toujours ouvrir avec `encoding="utf-8"`, et écrire avec `ensure_ascii=False`
   (accents lisibles) et `indent=4` (fichier lisible par un humain).

> Pour ceux qui viennent du JavaScript : `json.dumps()` / `json.loads()` sont les
> équivalents de `JSON.stringify()` / `JSON.parse()` — ils travaillent avec des
> **chaînes**. Les variantes sans « s », `json.dump()` / `json.load()`, écrivent et
> lisent **directement dans un fichier** : ce sont elles qu'on utilise ici.

## Le menu

```
=== Concessionnaire AutoStorm ===
1. Afficher les voitures
2. Afficher le détail d'une voiture
3. Ajouter une voiture
4. Modifier une voiture
5. Supprimer une voiture
0. Quitter
```

## Comportements attendus

1. **Afficher** : une ligne résumée par voiture — `1-ABC-123 — Renault Clio (2019)` —
   précédée du nombre de voitures en stock. Parc vide → message.
2. **Détail** : demander la plaque, afficher **tous** les champs joliment alignés.
   Plaque inconnue → message.
3. **Ajouter** : demander la plaque, puis chaque champ.
   - plaque vide → refus ; plaque **déjà existante** → refus ;
   - `annee`, `prix` et `kilometrage` sont des **entiers** : tant que la saisie
     n'est pas un nombre valide, **reposer la question** (le programme ne plante
     jamais) ;
   - sauvegarder, puis confirmer l'ajout.
4. **Modifier** : demander la plaque (inconnue → message). Pour chaque champ
   modifiable, afficher la valeur actuelle entre crochets ; **une saisie vide
   conserve la valeur actuelle**. L'année d'une voiture ne change jamais : elle
   n'est **pas** modifiable. Sauvegarder, puis confirmer.
5. **Supprimer** : demander la plaque (inconnue → message), **demander une
   confirmation** `o/n` en rappelant la marque et le modèle, supprimer uniquement
   si `o`, sauvegarder, confirmer.
6. **Quitter** : sortir de la boucle. (Rien à sauvegarder : le fichier est déjà à
   jour après chaque changement.)

**Le programme ne doit jamais planter**, quelles que soient les saisies.

## Structure imposée

Écrivez au minimum ces quatre fonctions (avec docstrings) :

| Fonction | Rôle |
|---|---|
| `charger_voitures()` | lit le JSON (ou crée le fichier avec le stock de départ) et **renvoie** le dictionnaire |
| `sauvegarder_voitures(voitures)` | écrase le fichier avec l'état actuel |
| `demander_entier(question)` | repose la question jusqu'à obtenir un entier (le pattern « saisie robuste » du cours) |
| `afficher_liste(voitures)` | la liste résumée — réutilisée par les options 1, 4 et 5 |

> Dans le CRUD contacts, vous aviez copié-collé trois fois le bloc d'affichage…
> Cette fois, vous avez les fonctions : **plus aucune excuse**. 😉

## Exemple de session

```
3 voiture(s) chargée(s) depuis concessionnaire.json

=== Concessionnaire AutoStorm ===
...
Votre choix : 3
Plaque (ex: 1-ABC-123) : 1-JKL-001
Marque : Kia
Modèle : Ceed
Année : abcd
⚠ Veuillez entrer un nombre entier
Année : 2020
Prix (€) : 14500
Kilométrage : 41000
Kia Ceed ajoutée au parc (1-JKL-001)

Votre choix : 5
...
Plaque de la voiture à supprimer : 1-ABC-123
Supprimer Renault Clio (1-ABC-123) ? o/n : o
La voiture 1-ABC-123 a été retirée du parc

Votre choix : 0
À bientôt !
```

**Vérification clé** : quittez le programme, relancez-le → vos changements sont
toujours là. Ouvrez `concessionnaire.json` dans VS Code : vous devez pouvoir le
lire (indentation, accents corrects). Modifiez un prix à la main dans le fichier,
relancez : le programme voit la nouvelle valeur.

## Bonus (si vous avez fini)

1. Option `6. Rechercher` : saisir une marque et afficher toutes ses voitures
   (comparaison insensible à la casse → `lower()`).
2. Option `7. Budget` : saisir un prix maximum et afficher les voitures à ce
   budget.
3. Au démarrage, afficher une mini-statistique : nombre de voitures et prix moyen
   du parc.
4. Blindage : si `concessionnaire.json` est corrompu (modifié à la main avec une
   erreur de syntaxe), le programme repart du stock de départ au lieu de planter
   → `except json.JSONDecodeError`.
