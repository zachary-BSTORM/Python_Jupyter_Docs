# Stack & Queue — Théorie

> Fichier de théorie. Les démos pratiques sont dans [02_demos_stack_queue.ipynb](02_demos_stack_queue.ipynb).

## Table des matières

1. [Pourquoi des structures « avec règles » ?](#1-pourquoi-des-structures--avec-règles--)
2. [La pile (Stack) — LIFO](#2-la-pile-stack--lifo)
3. [La file (Queue) — FIFO](#3-la-file-queue--fifo)
4. [Les variantes : deque et file de priorité](#4-les-variantes--deque-et-file-de-priorité)
5. [Comparatif](#5-comparatif)
6. [Où les retrouve-t-on ? (y compris dans Odoo)](#6-où-les-retrouve-t-on--y-compris-dans-odoo)
7. [Algo en groupe façon LeetCode — la méthode](#7-algo-en-groupe-façon-leetcode--la-méthode)
8. [Résumé](#8-résumé)

---

## 1. Pourquoi des structures « avec règles » ?

Une `list` Python permet de tout faire : ajouter, retirer, lire **n'importe où**.
Une pile et une file sont des listes **avec une règle imposée** sur l'endroit où l'on ajoute et l'endroit où l'on retire.

Pourquoi se limiter volontairement ?
- le code dit **clairement son intention** (« ici, le dernier arrivé est traité en premier ») ;
- on évite les erreurs (impossible de retirer un élément au milieu par accident) ;
- les opérations autorisées sont **rapides : O(1)**.

> 💡 Pile et file ne sont pas des types Python à part : ce sont des **concepts** (on parle de *type abstrait de données*). En Python, on les fait simplement avec une `list` (pile) ou un `collections.deque` (file).

---

## 2. La pile (Stack) — LIFO

### 📖 Pour les nuls

Pensez à une **pile d'assiettes** :
- on pose une assiette **sur le dessus** ;
- on reprend toujours **celle du dessus** ;
- la première assiette posée est la dernière reprise.

C'est le principe **LIFO** : *Last In, First Out* — **dernier entré, premier sorti**.

```
        push(3)          pop() → 3
          ↓                 ↑
        ┌───┐            ┌───┐
        │ 3 │ ← sommet   │   │
        ├───┤            ├───┤
        │ 2 │            │ 2 │ ← nouveau sommet
        ├───┤            ├───┤
        │ 1 │            │ 1 │
        └───┘            └───┘
```

### Les opérations

| Opération | Rôle | En Python (`list`) | Complexité |
|---|---|---|---|
| `push(element)` | ajouter au sommet | `pile.append(element)` | O(1) |
| `pop()` | retirer **et renvoyer** le sommet | `pile.pop()` | O(1) |
| `peek()` / `top()` | **lire** le sommet sans le retirer | `pile[-1]` | O(1) |
| `is_empty()` | la pile est-elle vide ? | `len(pile) == 0` ou `not pile` | O(1) |
| `size()` | nombre d'éléments | `len(pile)` | O(1) |

> ✅ La `list` Python est **parfaite pour une pile** : le sommet est la **fin** de la liste, et `append()` / `pop()` sur la fin sont en O(1).

### ⚠️ Pièges

- `pop()` ou `pile[-1]` sur une pile **vide** → `IndexError`. On vérifie toujours que la pile n'est pas vide avant (`if pile:`).
- Ne jamais utiliser `pile.pop(0)` : on retirerait le **bas** de la pile (et ce serait O(n)).

### Cas d'usage typiques

- **Annuler (Ctrl+Z)** : chaque action est empilée, « annuler » dépile la dernière.
- **Bouton « Précédent » du navigateur** : historique des pages visitées.
- **Pile d'appels (call stack)** : chaque appel de fonction est empilé, il est dépilé quand la fonction se termine (c'est elle qui « déborde » lors d'une récursion infinie : `RecursionError`).
- **Vérifier des parenthèses** `( [ { } ] )` : chaque ouvrante est empilée, chaque fermante doit correspondre au sommet.
- **Parcours en profondeur (DFS)** dans un arbre ou un graphe.

---

## 3. La file (Queue) — FIFO

### 📖 Pour les nuls

Pensez à la **file d'attente à la caisse** :
- on arrive **à la fin** de la file ;
- la caissière sert **la personne en tête** ;
- le premier arrivé est le premier servi.

C'est le principe **FIFO** : *First In, First Out* — **premier entré, premier sorti**.

```
   dequeue() ← [ A | B | C | D ] ← enqueue(E)
              tête          fin
```

### Les opérations

| Opération | Rôle | Avec `collections.deque` | Complexité |
|---|---|---|---|
| `enqueue(element)` | ajouter **à la fin** | `file.append(element)` | O(1) |
| `dequeue()` | retirer **et renvoyer** la tête | `file.popleft()` | O(1) |
| `front()` / `peek()` | **lire** la tête sans la retirer | `file[0]` | O(1) |
| `is_empty()` | la file est-elle vide ? | `len(file) == 0` ou `not file` | O(1) |
| `size()` | nombre d'éléments | `len(file)` | O(1) |

### ⚠️ Le piège n°1 : `list.pop(0)`

On peut faire une file avec une `list` : `file.append(x)` puis `file.pop(0)`.
**Ça marche, mais c'est lent** : retirer le premier élément oblige Python à **décaler tous les autres** d'une case → **O(n)**.

```
pop(0) sur [A, B, C, D, E]
           ↓
        [_, B, C, D, E]   → B, C, D, E reculent tous d'une case
        [B, C, D, E]
```

> ✅ Pour une file, on utilise **`collections.deque`** (*double-ended queue*, « file à deux bouts ») : ajout et retrait sont en O(1) **aux deux extrémités**. La démo 4 du notebook chronomètre la différence.

### Cas d'usage typiques

- **File d'impression** : les documents sont imprimés dans l'ordre d'envoi.
- **Traitement de tâches / commandes** dans l'ordre d'arrivée (tickets, e-mails à envoyer…).
- **Parcours en largeur (BFS)** dans un graphe : on visite les voisins « niveau par niveau ».
- **Mémoire tampon (buffer)** : données reçues sur le réseau, traitées dans l'ordre.

---

## 4. Les variantes : deque et file de priorité

### `collections.deque` — la file à deux bouts

Un `deque` peut servir **à la fois** de pile et de file :

| Méthode | Effet |
|---|---|
| `append(x)` / `pop()` | ajouter / retirer **à droite** |
| `appendleft(x)` / `popleft()` | ajouter / retirer **à gauche** |
| `deque(maxlen=3)` | taille maximum : les plus anciens sont **éjectés automatiquement** (pratique pour « les 3 dernières actions ») |

> ⚠️ Accéder au **milieu** d'un deque (`file[500]`) est en O(n) : il est fait pour les extrémités.

### File de priorité — `heapq`

Parfois on ne veut pas « premier arrivé, premier servi », mais **« le plus urgent d'abord »** (les urgences d'un hôpital).
Le module `heapq` transforme une `list` en **tas** (*heap*) : le **plus petit** élément est toujours en tête.

| Fonction | Rôle | Complexité |
|---|---|---|
| `heapq.heappush(tas, element)` | ajouter | O(log n) |
| `heapq.heappop(tas)` | retirer le **plus petit** | O(log n) |
| `tas[0]` | lire le plus petit | O(1) |

> 💡 On stocke souvent des tuples `(priorite, valeur)` : Python compare d'abord la priorité. Plus le nombre est petit, plus c'est prioritaire (1 = urgent).

### Et `queue.Queue` ?

Le module `queue` propose `Queue`, `LifoQueue` et `PriorityQueue`. Ce sont les mêmes concepts, mais **sécurisés pour le multi-threading** (plusieurs threads qui lisent / écrivent en même temps). Pour un programme classique, `list`, `deque` et `heapq` suffisent.

---

## 5. Comparatif

| | Pile (Stack) | File (Queue) | File de priorité |
|---|---|---|---|
| Principe | LIFO — dernier entré, premier sorti | FIFO — premier entré, premier sorti | le plus prioritaire sort en premier |
| Analogie | pile d'assiettes | file d'attente | urgences d'un hôpital |
| Outil Python | `list` | `collections.deque` | `heapq` |
| Ajouter | `append()` — O(1) | `append()` — O(1) | `heappush()` — O(log n) |
| Retirer | `pop()` — O(1) | `popleft()` — O(1) | `heappop()` — O(log n) |
| Lire sans retirer | `pile[-1]` | `file[0]` | `tas[0]` |
| Exemples | Ctrl+Z, call stack, parenthèses, DFS | impression, tâches, BFS | tickets support, planification |

---

## 6. Où les retrouve-t-on ? (y compris dans Odoo)

- **Python lui-même** : la pile d'appels visible dans un *traceback* (le dernier appel est affiché en bas).
- **Odoo** :
  - le **fil d'Ariane** (*breadcrumb*) en haut de l'interface fonctionne comme une pile : chaque vue ouverte s'empile, revenir en arrière dépile ;
  - les **traitements en arrière-plan** (actions planifiées / *cron*, et le module communautaire OCA `queue_job`) reposent sur l'idée de file : des tâches mises en attente puis exécutées une par une ;
  - la **file d'envoi des e-mails** : les messages sont mis en attente puis envoyés par une action planifiée.
- **Le web** : la boucle d'événements JavaScript utilise une file de tâches.

---

## 7. Algo en groupe façon LeetCode — la méthode

### 📖 C'est quoi « style LeetCode » ?

[LeetCode](https://leetcode.com) est un site d'exercices d'algorithmique utilisés en entretien technique. Un exercice, c'est :
- un **énoncé** court ;
- des **exemples** d'entrée → sortie attendue ;
- des **contraintes** (taille des données, cas limites) ;
- un niveau : **Easy**, **Medium**, **Hard**.

Le notebook de démos propose une série d'exercices de ce type, centrés sur les piles et les files.

### La méthode en 6 étapes (à suivre à chaque exercice)

1. **Comprendre** — reformuler l'énoncé avec ses propres mots. Quelle est l'entrée ? Quelle est la sortie ?
2. **Exemples** — dérouler les exemples **à la main**, puis inventer des **cas limites** (liste vide, un seul élément, valeurs en double…).
3. **Solution naïve** — trouver d'abord une solution qui marche, même lente. Estimer sa complexité.
4. **Optimiser** — se demander : « quelle structure m'aiderait ? » Indice fréquent : *« je dois me souvenir du dernier élément ouvert / vu »* → **pile** ; *« je dois traiter dans l'ordre d'arrivée »* → **file**.
5. **Coder** — avec des noms de variables complets et des commentaires.
6. **Tester** — lancer les tests fournis, puis ses propres cas limites.

### Organisation du groupe (3 à 4 personnes)

| Rôle | Mission |
|---|---|
| **Pilote** (*driver*) | tient le clavier, écrit le code |
| **Navigateur** | guide le pilote, propose l'algorithme, repère les erreurs |
| **Testeur** | prépare les cas limites et vérifie les résultats |
| **Rapporteur** | explique la solution et sa complexité au reste de la classe |

> 🔄 On **tourne les rôles** à chaque exercice pour que chacun passe au clavier.

### Déroulé conseillé d'une séance

1. 5 min — lecture de l'énoncé en groupe, étapes 1 et 2 sur papier.
2. 15 à 20 min — étapes 3 à 6.
3. 5 min — le rapporteur présente : idée, code, complexité.
4. Comparaison entre groupes : qui a trouvé une autre approche ?

---

## 8. Résumé

- 🥞 **Pile** = LIFO → `list` avec `append()` / `pop()` / `[-1]`.
- 🚶 **File** = FIFO → `collections.deque` avec `append()` / `popleft()` / `[0]`. **Jamais `list.pop(0)`** sur de grosses files.
- 🚑 **File de priorité** → `heapq` avec des tuples `(priorite, valeur)`.
- Toutes les opérations de base de pile et de file sont en **O(1)**.
- Face à un exercice : *« dernier ouvert / vu »* → pile, *« ordre d'arrivée »* → file.
- En groupe : 6 étapes (comprendre, exemples, naïf, optimiser, coder, tester) et rôles qui tournent.

🎯 **Suite** : ouvrez [02_demos_stack_queue.ipynb](02_demos_stack_queue.ipynb) pour les démos et les exercices de groupe.
