# Exercice : Le Yahtzee

## Le jeu

À chaque tour, un joueur lance 5 dés. Il peut relancer les dés de son choix
jusqu'à deux fois (donc 3 lancers au maximum), puis doit inscrire le
résultat dans une case encore libre de sa feuille de score. La partie dure
13 tours, le temps de remplir les 13 cases. Le plus grand total gagne.

## La feuille de score

Section haute — la case Dés 1 vaut la somme des dés montrant 1, la case
Dés 2 la somme des dés montrant 2, et ainsi de suite jusqu'à Dés 6.

Section figures :

| Case          | Condition                                   | Score                |
|---------------|---------------------------------------------|----------------------|
| Brelan        | au moins 3 dés identiques                   | somme des 5 dés      |
| Carré         | au moins 4 dés identiques                   | somme des 5 dés      |
| Full          | un brelan et une paire différents           | 25                   |
| Petite suite  | 4 valeurs qui se suivent                    | 30                   |
| Grande suite  | 5 valeurs qui se suivent                    | 40                   |
| Yahtzee       | 5 dés identiques                            | 50                   |
| Chance        | toujours valable                            | somme des 5 dés      |

Une case ne peut être remplie qu'une seule fois. Si aucun score n'est
possible, le joueur doit sacrifier une case libre en y inscrivant 0.

## Étapes

### Étape 1 — Le lancer

- Lancer 5 dés (valeurs de 1 à 6 au hasard) et les afficher numérotés :

```
De 1 : 3   De 2 : 5   De 3 : 3   De 4 : 6   De 5 : 2
```

### Étape 2 — Les relances

- Demander au joueur les numéros des dés qu'il garde (exemple de saisie :
  1 3, les autres sont relancés ; saisie vide : tout relancer ; le mot
  stop : s'arrêter là).
- Valider la saisie (des numéros entre 1 et 5), relancer les dés non
  gardés, afficher le nouveau jet. Deux relances au maximum, puis le jet
  est définitif.

### Étape 3 — La détection des combinaisons

- Écrire la fonction qui, pour 5 dés donnés, calcule le score de chaque
  case de la feuille.
- Conseil central : construire d'abord le compteur d'occurrences, un
  dictionnaire valeur du dé vers nombre d'exemplaires. Presque tout s'en
  déduit : le brelan et le carré se lisent dans le plus grand nombre
  d'exemplaires, le full est un 3 accompagné d'un 2, la section haute est
  valeur fois nombre d'exemplaires.
- Pour les suites : prendre les valeurs uniques, les trier, et chercher 4
  ou 5 valeurs consécutives.
- Testez cette fonction à part, avec des jets préparés à la main
  (par exemple 2 2 3 3 3 doit donner brelan 13, full 25, Dés 3 valant 9).

### Étape 4 — Le choix de la case

- Après le jet définitif, afficher toutes les cases encore libres avec le
  score que chacune rapporterait pour ce jet, et faire choisir le joueur.
- Refuser une case déjà remplie. Autoriser le sacrifice (inscrire 0 dans
  une case libre au choix).
- Mettre à jour la feuille de score et l'afficher.

### Étape 5 — La partie complète

- Enchaîner les 13 tours, afficher le total final.
- Version à plusieurs : demander les prénoms au début, faire jouer chacun
  à tour de rôle, afficher toutes les feuilles, et annoncer le classement
  final.

## Exemple d'affichage du choix

```
Jet final : 3 3 3 5 5

Cases libres :
  Des 3        -> 9
  Des 5        -> 10
  Brelan       -> 19
  Full         -> 25
  Chance       -> 19
  Petite suite -> 0

Quelle case remplir ?
```

## Bonus

1. Le bonus de la section haute : si le total des cases Dés 1 à Dés 6
   atteint 63 ou plus, ajouter 35 points.
2. Les meilleurs scores : sauvegarder les 5 meilleurs totaux dans un
   fichier JSON (prénom et score), les afficher au lancement.
3. Le conseiller : au moment du choix, marquer la case qui rapporte le plus
   de points pour ce jet.
4. Le Yahtzee multiple : un deuxième Yahtzee dans la même partie rapporte
   100 points supplémentaires.
