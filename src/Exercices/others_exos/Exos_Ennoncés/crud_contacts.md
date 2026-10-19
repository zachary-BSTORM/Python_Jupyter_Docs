# Exercice : Répertoire de contacts — un CRUD avec menu interactif

## Description

CRUD est l'acronyme des 4 opérations de base de toute application de gestion :

| Lettre | Opération | Dans cet exercice |
|---|---|---|
| **C**reate | créer | ajouter un contact |
| **R**ead | lire | afficher les contacts |
| **U**pdate | modifier | changer le numéro d'un contact |
| **D**elete | supprimer | retirer un contact |

Vous allez écrire un répertoire téléphonique en console : le programme affiche un menu,
exécute l'opération choisie, puis réaffiche le menu — jusqu'à ce que l'utilisateur quitte.

## Contrainte principale

⚠ **Sans classes (POO) ni fonctions (`def`)** : tout le code dans un seul script.
Vous disposez uniquement de ce qui a déjà été vu : variables, conditions, boucles
(`while`, `for`, `break`), collections, `match/case`, `input()`.
Les méthodes fournies par Python sur les listes et les chaînes
(`append`, `pop`, `strip`, `lower`, `isdigit`…) sont évidemment permises.

## Les données

Une **liste de dictionnaires**, pré-remplie pour pouvoir tester immédiatement :

```python
contacts = [
    {"nom": "Alice Dupont", "telephone": "0470 11 22 33"},
    {"nom": "Bob Martin", "telephone": "0485 44 55 66"},
]
```

## Le menu

```
=== Répertoire de contacts ===
1. Afficher les contacts
2. Ajouter un contact
3. Modifier un numéro
4. Supprimer un contact
0. Quitter
```

## Comportements attendus

1. **Afficher** : la liste numérotée à partir de 1 (`enumerate`), au format
   `1. Alice Dupont — 0470 11 22 33`. Si le répertoire est vide, afficher
   `Le répertoire est vide`.
2. **Ajouter** : demander le nom puis le numéro. Un nom vide (ou composé
   uniquement d'espaces) est refusé avec un message.
3. **Modifier** : afficher la liste numérotée, demander le numéro de ligne du
   contact, puis le nouveau numéro de téléphone.
4. **Supprimer** : afficher la liste numérotée, demander le numéro de ligne du
   contact, le retirer (`pop`) et confirmer avec son nom.
5. **Quitter** : sortir de la boucle et saluer.

**Le programme ne doit jamais planter** :

- un choix de menu inconnu → `Choix invalide` et retour au menu ;
- pour modifier/supprimer : la saisie doit être un nombre (`.isdigit()`) **et**
  correspondre à une ligne existante, sinon message et retour au menu ;
- modifier/supprimer dans un répertoire vide → message et retour au menu.

## Exemple de session

```
=== Répertoire de contacts ===
1. Afficher les contacts
...
Votre choix : 2
Nom du contact : Chloé Petit
Numéro de téléphone : 0493 77 88 99
Chloé Petit a été ajouté(e) au répertoire

Votre choix : 1
1. Alice Dupont — 0470 11 22 33
2. Bob Martin — 0485 44 55 66
3. Chloé Petit — 0493 77 88 99

Votre choix : 4
Numéro du contact à supprimer : 9
Il n'y a pas de contact n°9

Votre choix : 0
Au revoir !
```

## Bonus (si vous avez fini)

1. À l'ajout, **refuser un nom déjà présent** dans le répertoire (sans tenir
   compte des majuscules/minuscules → `lower()`).
2. À la modification, une saisie **vide** conserve l'ancien numéro.
3. Une option `5. Rechercher` : demander un morceau de nom et afficher tous les
   contacts dont le nom le contient (opérateur `in`).

## À méditer une fois terminé

Vous avez copié-collé trois fois le bloc « afficher la liste numérotée » ?
C'est exactement le problème que les **fonctions** (chapitre suivant) résolvent :
écrire ce bloc une seule fois, et l'appeler partout.
