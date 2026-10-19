# Exercice : La bataille navale

## Le jeu

Chaque camp place une flotte sur une grille de 10 sur 10, puis les deux camps
tirent à tour de rôle sur la grille adverse. Un bateau dont toutes les cases
ont été touchées est coulé. Le premier camp qui coule toute la flotte adverse
gagne. Vous jouerez contre l'ordinateur.

## La flotte

| Bateau            | Taille |
|-------------------|--------|
| Porte-avions      | 5      |
| Croiseur          | 4      |
| Contre-torpilleur | 3      |
| Sous-marin        | 3      |
| Torpilleur        | 2      |

## Les coordonnées

Les lignes sont nommées de A à J, les colonnes de 1 à 10. Une case se note
par exemple B7. Le programme convertit cette notation en indices de grille,
et refuse toute saisie invalide (hors grille, format incorrect) sans planter.

## Étapes

### Étape 1 — Les grilles et l'affichage

- Chaque camp possède deux grilles 10 x 10 : sa flotte (où sont ses bateaux)
  et son radar (ce qu'il sait de la grille adverse : cases non tirées,
  manquées, touchées).
- Afficher une grille avec les lettres A-J devant les lignes et les numéros
  1 à 10 au-dessus. Symboles : point pour l'inconnu ou le vide, B pour une
  case de bateau (sur sa propre flotte), o pour un tir manqué, X pour un
  tir touché.
- À chaque tour du joueur : afficher son radar, puis sa flotte.

### Étape 2 — Le placement aléatoire

- Pour chaque bateau de la flotte : tirer au hasard une orientation
  (horizontale ou verticale) et une case de départ, calculer la liste des
  cases occupées, et valider que toutes sont dans la grille et qu'aucune
  n'est déjà prise par un autre bateau. Recommencer le tirage tant que le
  placement est invalide.
- Conseil de structure : un dictionnaire par camp qui associe le nom de
  chaque bateau à la liste de ses cases (des tuples ligne, colonne).
- Placer ainsi la flotte du joueur et celle de l'ordinateur.

### Étape 3 — Le tir du joueur

- Demander une case (notation B7), la convertir, et refuser une case déjà
  tirée : garder l'ensemble (set) des tirs déjà effectués sur chaque camp.
- Annoncer le résultat : manqué, touché, ou coulé avec le nom du bateau.
- Un bateau est coulé quand chacune de ses cases figure dans l'ensemble des
  tirs reçus.
- Mettre à jour le radar du joueur.

### Étape 4 — Le tour de l'ordinateur

- L'ordinateur tire sur une case au hasard qu'il n'a jamais tirée (même
  mécanisme d'ensemble des tirs), le résultat est annoncé de la même façon,
  et la flotte du joueur est mise à jour à l'affichage.
- Les deux camps tirent à tour de rôle, en commençant par le joueur.

### Étape 5 — La fin de partie

- Après chaque tir, vérifier si toute la flotte adverse est coulée :
  annoncer le vainqueur, afficher le nombre de tirs utilisés, et proposer
  de rejouer.

## Exemple d'affichage

```
Votre radar :
    1 2 3 4 5 6 7 8 9 10
A   . . . o . . . . . .
B   . . . . . X X . . .
C   . . . . . . . o . .
D   . . . . . . . . . .
...

Votre tir (exemple B7) :
```

## Bonus

1. Le placement manuel : au début, le joueur choisit pour chaque bateau la
   case de départ et l'orientation, avec les mêmes validations.
2. L'ordinateur chasseur : après un touché, il tire sur les cases voisines
   (haut, bas, gauche, droite) jusqu'à couler le bateau, puis revient au
   hasard.
3. L'interdiction de contact : deux bateaux ne peuvent pas se toucher, même
   en diagonale (à valider au placement).
4. Les statistiques de fin : précision du joueur et de l'ordinateur
   (touchés divisés par tirs).
