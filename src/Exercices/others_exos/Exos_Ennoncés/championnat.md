# Exercice : Le championnat

## Le contexte

Vous écrivez le logiciel de gestion d'un championnat de football : calendrier,
résultats, classement, et phase finale. Tout se passe en console, les données
vivent dans des listes et des dictionnaires, et le championnat est sauvegardé
dans un fichier JSON pour pouvoir être repris plus tard.

## Données fournies (à copier telles quelles)

```python
equipes = ["Anderlecht", "Bruges", "Standard", "Genk", "Gand", "Charleroi"]
```

## Étapes

### Étape 1 — Le calendrier

- Générer la liste de tous les matchs : chaque équipe rencontre chaque autre
  équipe exactement une fois (pas de match d'une équipe contre elle-même, et
  si Anderlecht-Bruges existe, Bruges-Anderlecht ne doit pas exister).
- Conseil : une double boucle sur les indices, en ne gardant que les paires
  où le deuxième indice est plus grand que le premier.
- Représenter chaque match par un dictionnaire :

```python
{"domicile": "Anderlecht", "exterieur": "Bruges", "buts_dom": None, "buts_ext": None}
```

- Un match dont les buts valent None n'a pas encore été joué.
- Afficher le calendrier numéroté avec, pour chaque match, son état
  (à jouer, ou le score s'il est joué). Avec 6 équipes, vous devez obtenir
  15 matchs.

### Étape 2 — Jouer les matchs

- Proposer un menu : jouer le prochain match, jouer tous les matchs restants,
  afficher le calendrier, afficher le classement, quitter.
- Jouer un match : au choix de l'utilisateur, soit saisir les deux scores
  (validation : des entiers, refuser le reste), soit laisser l'ordinateur
  simuler (buts tirés au hasard entre 0 et 4).
- Un match déjà joué ne peut pas être rejoué.

### Étape 3 — Le classement

- Calculer pour chaque équipe : matchs joués, gagnés, nuls, perdus, buts
  pour, buts contre, différence, points (victoire 3, nul 1, défaite 0).
- Conseil : un dictionnaire par équipe, construit en parcourant les matchs
  joués.
- Trier le classement : points décroissants, puis différence de buts
  décroissante, puis buts pour décroissants (une seule clé de tri qui
  renvoie un tuple).
- Afficher un tableau aligné : position, nom, joués, gagnés, nuls, perdus,
  buts pour, buts contre, différence, points.

### Étape 4 — La sauvegarde

- À chaque match joué, écraser un fichier championnat.json contenant la
  liste des matchs.
- Au lancement du programme : si le fichier existe, reprendre le championnat
  où il en était ; sinon, générer un calendrier neuf et créer le fichier.

### Étape 5 — La phase finale

- Quand les 15 matchs sont joués, proposer la phase finale : le premier du
  classement affronte le quatrième, le deuxième affronte le troisième.
- Les vainqueurs se retrouvent en finale, les perdants jouent la petite
  finale.
- En cas d'égalité dans un match à élimination : séance de tirs au but
  simulée (5 tirs chacun réussis au hasard, puis mort subite tant qu'il y a
  égalité).
- Afficher le podium final.

## Exemple d'affichage du classement

```
Pos  Equipe        J   G   N   P   BP  BC  Diff  Pts
 1   Bruges        5   4   1   0   12   3   +9    13
 2   Genk          5   3   1   1    9   6   +3    10
 3   Anderlecht    5   2   2   1    8   7   +1     8
 4   Standard      5   2   1   2    7   8   -1     7
 5   Gand          5   1   0   4    4  10   -6     3
 6   Charleroi     5   0   1   4    3   9   -6     1
```

## Bonus

1. Les matchs aller-retour (chaque paire se joue deux fois, une fois chez
   chaque équipe) : 30 matchs.
2. Les statistiques : meilleure attaque, meilleure défense, plus grand
   nombre de buts dans un match.
3. L'historique : afficher tous les résultats d'une équipe choisie.
4. La journée de championnat : organiser le calendrier pour que chaque
   équipe joue exactement une fois par journée (3 matchs par journée avec
   6 équipes).
