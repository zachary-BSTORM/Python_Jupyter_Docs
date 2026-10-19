# Exercice : Le Puissance 4

## Le jeu

Deux joueurs laissent tomber tour à tour un jeton dans une grille verticale
de 6 lignes sur 7 colonnes. Le jeton glisse jusqu'à la case libre la plus
basse de la colonne choisie. Le premier joueur qui aligne 4 de ses jetons
(horizontalement, verticalement ou en diagonale) gagne. Si la grille se
remplit sans alignement, la partie est nulle.

## Étapes

### Étape 1 — La grille et l'affichage

- Représenter la grille par une liste de 6 listes de 7 cases. Une case vide
  contient un point, les jetons des joueurs sont X et O.
- Afficher la grille avec les numéros de colonnes de 1 à 7 au-dessus, et
  réafficher après chaque coup.

### Étape 2 — Le jeton qui tombe

- Demander la colonne au joueur dont c'est le tour. Valider la saisie : un
  nombre, entre 1 et 7, et la colonne ne doit pas être pleine. Toute saisie
  invalide est redemandée, sans jamais faire planter le programme.
- Faire tomber le jeton : parcourir la colonne en partant du bas et placer
  le jeton dans la première case libre rencontrée.
- Conseil : retenir la ligne où le jeton a atterri, elle servira à l'étape 4.

### Étape 3 — La partie à deux

- Faire alterner les joueurs X et O à chaque coup, en annonçant à qui est
  le tour.
- La boucle de partie continue tant qu'il n'y a ni victoire ni grille pleine.

### Étape 4 — La détection de la victoire

- Après chaque coup, vérifier si le jeton qui vient d'être posé complète un
  alignement de 4.
- La méthode conseillée, direction par direction. Il y a 4 directions à
  tester : horizontale, verticale, diagonale descendante, diagonale
  montante. Chaque direction se décrit par un pas (delta_ligne,
  delta_colonne) : par exemple (0, 1) pour l'horizontale, (1, 1) pour une
  diagonale.
- Pour une direction donnée : partir de la case jouée, compter 1, puis
  avancer pas à pas dans un sens tant que la case suivante est dans la
  grille et contient le même jeton, en comptant. Revenir à la case jouée et
  compter de la même façon dans le sens opposé (pas inversé). Si le total
  atteint 4 ou plus, c'est gagné.
- Répéter pour les 4 directions. Cette fonction est le cœur de l'exercice :
  écrivez-la proprement, testez-la à part avec une grille préparée à la main.

### Étape 5 — La fin de partie

- Victoire : annoncer le gagnant et afficher la grille finale.
- Grille pleine sans alignement (42 coups) : annoncer le match nul.
- Proposer de rejouer. Tenir le score des manches (nombre de victoires de
  X, de O, et de nuls) et l'afficher entre les parties.

## Exemple d'affichage

```
  1 2 3 4 5 6 7
  . . . . . . .
  . . . . . . .
  . . . . . . .
  . . . O . . .
  . . X X O . .
  . X O X O . .

Au tour de X. Colonne (1-7) :
```

## Bonus

1. L'ordinateur débutant : il joue dans une colonne valide tirée au hasard.
2. L'ordinateur malin : avant de jouer au hasard, il teste chaque colonne.
   S'il existe un coup qui le fait gagner immédiatement, il le joue. Sinon,
   si l'adversaire gagnerait en jouant une colonne, il la bloque.
   Conseil : simuler le coup dans la grille, tester la victoire avec la
   fonction de l'étape 4, puis retirer le jeton.
3. La grille à taille choisie (lignes, colonnes, longueur de l'alignement)
   au début de la partie.
