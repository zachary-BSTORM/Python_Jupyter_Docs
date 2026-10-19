# Exercice : L'escape game

## Le jeu

Vous êtes enfermé dans une pièce représentée par une grille de 10 lignes sur
10 colonnes. Des énigmes sont cachées dans la pièce. Pour sortir, il faut
toutes les résoudre, puis atteindre la porte — avant d'avoir épuisé votre
réserve de déplacements.

## Règles générales

- Le joueur se déplace avec les touches Z (haut), Q (gauche), S (bas),
  D (droite), suivies de Entrée. X pour abandonner.
- Chaque déplacement coûte 1 point de la réserve (départ : 60 points).
- Les positions des énigmes sont invisibles : elles se déclenchent quand le
  joueur marche dessus.
- Une énigme résolue reste résolue. La porte ne s'ouvre que si toutes les
  énigmes sont résolues.
- Le programme ne plante jamais, quelles que soient les saisies.

## Données fournies (à copier telles quelles)

```python
devinettes = [
    {"question": "Je commence la nuit et je finis le matin. Qui suis-je ?",
     "reponses": ["n", "la lettre n"],
     "indice": "C'est une lettre."},
    {"question": "Plus j'ai de gardiens, moins je suis gardé. Qui suis-je ?",
     "reponses": ["un secret", "secret", "le secret"],
     "indice": "Chut..."},
    {"question": "Je suis plein de trous mais je retiens l'eau. Qui suis-je ?",
     "reponses": ["une eponge", "eponge", "l'eponge"],
     "indice": "On me trouve près de l'évier."},
    {"question": "Quel mot s'écrit toujours mal dans le dictionnaire ?",
     "reponses": ["mal", "le mot mal"],
     "indice": "Relisez la question, tout simplement."},
    {"question": "Je grandis quand on m'enlève quelque chose. Qui suis-je ?",
     "reponses": ["un trou", "trou", "le trou"],
     "indice": "On me creuse."},
    {"question": "Combien font 3 puissance 4 ?",
     "reponses": ["81"],
     "indice": "3 x 3 x 3 x 3"},
]
```

Remarque : les réponses attendues sont volontairement écrites sans accents,
pour simplifier la comparaison avec la saisie des joueurs.

## Étapes

### Étape 1 — La pièce et le déplacement

- Représenter la pièce par une grille 10 x 10 (liste de listes).
- Afficher la grille à chaque tour : un point pour une case ordinaire,
  J pour le joueur, P pour la porte (placée dans le coin opposé au départ).
- Lire la commande, déplacer le joueur en restant dans la grille (un
  déplacement refusé ne coûte rien), décompter la réserve, afficher la
  réserve restante.
- Réserve à zéro : message de défaite et fin du programme.

### Étape 2 — Les énigmes cachées

- Tirer au hasard 4 positions d'énigmes, toutes différentes, différentes de
  la case de départ et de la porte. Associer à chaque position une devinette
  différente (tirage sans remise dans la liste fournie).
- Conseil de structure : un dictionnaire dont les clés sont des tuples
  (ligne, colonne) et les valeurs les devinettes, plus un ensemble (set) des
  positions déjà résolues.
- Quand le joueur arrive sur une case à énigme non résolue : poser la
  question, lire la réponse. La comparaison ignore les majuscules et les
  espaces autour, et accepte toutes les formulations de la liste "reponses".
- Bonne réponse : l'énigme est résolue, la case devient visible (affichée R).
- Mauvaise réponse : le joueur reste sur la case, l'énigme reste cachée, et
  la tentative coûte 2 points de réserve.

### Étape 3 — L'indice

- Pendant une énigme, la saisie I affiche l'indice de la devinette, puis
  repose la question. L'indice coûte 5 points de réserve. Un indice déjà
  affiché pour une énigme ne coûte plus rien les fois suivantes.

### Étape 4 — La sortie

- Afficher en permanence le nombre d'énigmes résolues (exemple : 2 / 4).
- Quand le joueur atteint la porte : s'il reste des énigmes non résolues,
  afficher combien, et le joueur reste bloqué dans la pièce. Sinon :
  victoire, avec le nombre de points de réserve restants comme score.

### Étape 5 — La partie complète

- Proposer de rejouer à la fin (victoire ou défaite). À chaque partie, les
  positions et les devinettes sont retirées au sort.

## Exemple d'affichage

```
Reserve : 54    Enigmes : 1 / 4

. . . . . . . . . P
. . . . . . . . . .
. . . . R . . . . .
. . . . . . . . . .
. . J . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .

Deplacement (Z/Q/S/D, X pour abandonner) :
```

## Bonus

1. Le brouillard : n'afficher que les cases situées à une distance d'au plus
   2 cases du joueur, le reste masqué.
2. Les pièges : 3 positions cachées supplémentaires qui coûtent 5 points de
   réserve quand on marche dessus (une seule fois chacune).
3. Les meilleurs scores : sauvegarder dans un fichier JSON le nom du joueur
   et son score en cas de victoire, afficher le top 5 au lancement.
4. Les niveaux : facile (80 points, 3 énigmes), normal (60, 4), difficile
   (45, 5).
