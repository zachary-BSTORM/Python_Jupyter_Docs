# Gros exercice 2/3 : La médiathèque — dict de dicts et liste de tuples

## Contexte

Vous gérez les emprunts d'une médiathèque : un catalogue de livres avec un stock
d'exemplaires, un registre des abonnés, et la liste des emprunts en cours.
Le programme tourne en boucle avec un menu, comme le CRUD contacts.

## Contrainte

⚠ **Sans classes, sans fonctions (`def`), sans compréhensions** — boucle
`while` + `match/case`, et les méthodes natives des collections.

## Les données (à copier telles quelles)

```python
catalogue = {                                    # dict de DICTS, clé = titre
    "1984": {"auteur": "George Orwell", "exemplaires": 2},
    "Le Petit Prince": {"auteur": "Antoine de Saint-Exupéry", "exemplaires": 1},
    "Dune": {"auteur": "Frank Herbert", "exemplaires": 3},
    "Fondation": {"auteur": "Isaac Asimov", "exemplaires": 0},
}

abonnes = {"Alice", "Bob", "Chloé"}              # set des abonnés en règle

emprunts = []                                    # liste de TUPLES (abonné, titre)
```

## Le menu

```
=== Médiathèque ===
1. Afficher le catalogue
2. Emprunter un livre
3. Rendre un livre
4. Emprunts en cours
5. Statistiques
0. Quitter
```

## Comportements attendus

1. **Catalogue** : une ligne par livre —
   `1984 — George Orwell (2 exemplaire(s) disponible(s))` — et `ÉPUISÉ` à la
   place du nombre quand il n'y a plus d'exemplaire.
2. **Emprunter** : demander le nom puis le titre. Trois vérifications, dans
   l'ordre, avec un message chacune :
   - le nom est dans le **set** `abonnes` (sinon : pas abonné) ;
   - le titre est une clé du catalogue (sinon : inconnu) ;
   - il reste au moins 1 exemplaire.
   Si tout est bon : décrémenter les exemplaires et ajouter le **tuple**
   `(nom, titre)` à la liste `emprunts`.
3. **Rendre** : demander le nom et le titre, vérifier que le tuple
   `(nom, titre)` est bien **dans** la liste `emprunts` (opérateur `in` — il
   compare des tuples entiers !). Si oui : le retirer (`remove`) et
   ré-incrémenter les exemplaires.
4. **Emprunts en cours** : `Alice a emprunté « 1984 »` — une ligne par tuple,
   avec unpacking dans le `for`. Liste vide → message.
5. **Statistiques** :
   - les titres épuisés (parcours du catalogue, exemplaires = 0) ;
   - le **set** des emprunteurs actifs (construit en bouclant sur `emprunts`) ;
   - les abonnés qui n'ont **rien** emprunté (différence de sets `-`) ;
   - le nombre total d'emprunts en cours (`len`).

Le programme ne plante jamais : toute saisie inattendue → message et retour au
menu.

## Bonus

1. À l'emprunt, refuser un 2ᵉ emprunt du **même titre** par la **même
   personne** (le tuple est déjà dans la liste).
2. Option `6. Ajouter un livre` au catalogue (titre, auteur, exemplaires).
3. Dans les statistiques : le livre le plus emprunté **en ce moment**
   (dictionnaire compteur construit depuis `emprunts`).
