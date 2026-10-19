# Exercices d'algorithmique


## Règles de la session


- Chaque exercice est découpé en **paliers**. Valide un palier (tous ses tests passent) avant de passer au suivant.
- Si tu bloques plus de 10 minutes sur un palier, passe à l'exercice suivant : tu pourras revenir plus tard.
- Les fonctions intégrées comme `sorted()`, `str.lower()` ou `str.isalnum()` sont autorisées, sauf mention contraire dans un palier.
- Les **indices** sont cachés : ne les ouvre que si tu es bloqué.

| # | Exercice | Difficulté | Temps indicatif |
|---|---|---|---|
| 1 | Valid Palindrome | ★☆☆ Facile | 20 min |
| 2 | Roman to Integer | ★☆☆ Facile | 20 min |
| 3 | Valid Anagram → Group Anagrams | ★★☆ Moyen | 30 min |
| 4 | Merge Intervals | ★★☆ Moyen | 35 min |

---

## 1. Valid Palindrome

**Difficulté :** ★☆☆ Facile — **Temps indicatif :** 20 min
**Notions :** chaînes de caractères, double pointeur

### Énoncé

Une phrase est un **palindrome** si, après avoir converti toutes les lettres majuscules en minuscules et retiré tous les caractères non alphanumériques, elle se lit de la même façon de gauche à droite et de droite à gauche. Les caractères alphanumériques sont les lettres et les chiffres.

Étant donné une chaîne `s`, renvoie `True` si c'est un palindrome, `False` sinon.

```python
def is_palindrome(s: str) -> bool:
    ...
```

### Exemples

**Exemple 1**
```
Entrée : s = "A man, a plan, a canal: Panama"
Sortie : True
Explication : "amanaplanacanalpanama" est un palindrome.
```

**Exemple 2**
```
Entrée : s = "race a car"
Sortie : False
Explication : "raceacar" n'est pas un palindrome.
```

**Exemple 3**
```
Entrée : s = " "
Sortie : True
Explication : après nettoyage, s est une chaîne vide "".
              Une chaîne vide se lit pareil dans les deux sens.
```

### Contraintes

- `1 <= len(s) <= 2 * 10^5`
- `s` ne contient que des caractères ASCII imprimables.

### Paliers

**Palier 1 — Version fonctionnelle.** N'importe quelle méthode est acceptée.

**Palier 2 — Sans nouvelle chaîne.** Réécris la fonction **sans construire de chaîne nettoyée ni de copie inversée**. Pas de `[::-1]`, pas de `"".join(...)`. La mémoire supplémentaire doit être en O(1).

**Palier 3 — Bonus : Valid Palindrome II.** Écris `is_almost_palindrome(s)` qui renvoie `True` si `s` (minuscules uniquement, sans espaces) est un palindrome **après suppression d'au plus un caractère**.

```python
def is_almost_palindrome(s: str) -> bool:
    ...
```

```
"aba"  → True   (déjà un palindrome)
"abca" → True   (on supprime 'c' ou 'b')
"abc"  → False
```

### Tests

```python
assert is_palindrome("A man, a plan, a canal: Panama") is True
assert is_palindrome("race a car") is False
assert is_palindrome(" ") is True
assert is_palindrome("0P") is False
assert is_palindrome("No 'x' in Nixon") is True
assert is_palindrome("ab_a") is True

# Bonus
assert is_almost_palindrome("aba") is True
assert is_almost_palindrome("abca") is True
assert is_almost_palindrome("abc") is False
assert is_almost_palindrome("deeee") is True
print("Valid Palindrome : tous les tests passent ✅")
```

<details>
<summary>💡 Indice palier 2</summary>

Place un index `gauche` au début et un index `droite` à la fin. Fais-les avancer l'un vers l'autre en sautant les caractères qui ne sont pas alphanumériques, et compare les caractères en minuscules.

</details>

<details>
<summary>💡 Indice palier 3</summary>

Au premier caractère différent, il n'y a que deux possibilités : supprimer celui de gauche ou celui de droite. Il suffit de vérifier si l'une des deux sous-chaînes restantes est un palindrome.

</details>

---

## 2. Roman to Integer

**Difficulté :** ★☆☆ Facile — **Temps indicatif :** 20 min
**Notions :** dictionnaires, parcours de chaîne

### Énoncé

Les chiffres romains utilisent sept symboles :

| Symbole | Valeur |
|---|---|
| `I` | 1 |
| `V` | 5 |
| `X` | 10 |
| `L` | 50 |
| `C` | 100 |
| `D` | 500 |
| `M` | 1000 |

Les symboles s'écrivent en général du plus grand au plus petit, de gauche à droite, et leurs valeurs s'additionnent : `XII` = 10 + 1 + 1 = 12.

Il existe cependant six cas **soustractifs**, où un symbole plus petit placé avant un plus grand se soustrait :

- `I` avant `V` (5) ou `X` (10) donne 4 et 9.
- `X` avant `L` (50) ou `C` (100) donne 40 et 90.
- `C` avant `D` (500) ou `M` (1000) donne 400 et 900.

Étant donné une chaîne `s` représentant un chiffre romain, convertis-la en entier.

```python
def roman_to_int(s: str) -> int:
    ...
```

### Exemples

**Exemple 1**
```
Entrée : s = "III"
Sortie : 3
Explication : III = 1 + 1 + 1 = 3.
```

**Exemple 2**
```
Entrée : s = "LVIII"
Sortie : 58
Explication : L = 50, V = 5, III = 3.
```

**Exemple 3**
```
Entrée : s = "MCMXCIV"
Sortie : 1994
Explication : M = 1000, CM = 900, XC = 90, IV = 4.
```

### Contraintes

- `1 <= len(s) <= 15`
- `s` ne contient que les caractères `I`, `V`, `X`, `L`, `C`, `D`, `M`.
- `s` est un chiffre romain **valide**, compris entre 1 et 3999.

### Paliers

**Palier 1 — Addition simple.** Gère les nombres qui ne contiennent **aucun** cas soustractif (`"III"`, `"LVIII"`, `"MDCLXVI"`).

**Palier 2 — Cas soustractifs.** Gère tous les nombres valides, y compris `IV`, `IX`, `XL`, `XC`, `CD`, `CM`.

**Palier 3 — Bonus : Integer to Roman.** Écris la conversion inverse.

```python
def int_to_roman(num: int) -> str:
    ...
```

```
3749 → "MMMDCCXLIX"   (3000 = MMM, 700 = DCC, 40 = XL, 9 = IX)
58   → "LVIII"
1994 → "MCMXCIV"
```

### Tests

```python
# Palier 1
assert roman_to_int("III") == 3
assert roman_to_int("LVIII") == 58
assert roman_to_int("MDCLXVI") == 1666

# Palier 2
assert roman_to_int("IV") == 4
assert roman_to_int("IX") == 9
assert roman_to_int("XLII") == 42
assert roman_to_int("MCMXCIV") == 1994
assert roman_to_int("MMMCMXCIX") == 3999

# Bonus
assert int_to_roman(3749) == "MMMDCCXLIX"
assert int_to_roman(58) == "LVIII"
assert int_to_roman(1994) == "MCMXCIV"
assert int_to_roman(4) == "IV"
assert int_to_roman(3999) == "MMMCMXCIX"
print("Roman to Integer : tous les tests passent ✅")
```

<details>
<summary>💡 Indice palier 2</summary>

Compare chaque symbole avec **le suivant**. S'il est plus petit, il faut le soustraire ; sinon, l'ajouter. Une autre approche consiste à parcourir la chaîne **à l'envers**.

</details>

<details>
<summary>💡 Indice palier 3</summary>

Prépare une liste de paires `(valeur, symbole)` triée de la plus grande à la plus petite, **en incluant les six cas soustractifs** (`900 → "CM"`, `400 → "CD"`…). Ensuite, tant qu'il reste quelque chose à convertir, prends le plus grand symbole possible.

</details>

---

## 3. Valid Anagram → Group Anagrams

**Difficulté :** ★★☆ Moyen — **Temps indicatif :** 30 min
**Notions :** dictionnaires, `sorted`, clés de dictionnaire immuables

### Énoncé — Partie A : Valid Anagram

Un **anagramme** est un mot formé en réarrangeant **toutes** les lettres d'un autre mot, chacune utilisée exactement une fois.

Étant donné deux chaînes `s` et `t`, renvoie `True` si `t` est un anagramme de `s`, `False` sinon.

```python
def is_anagram(s: str, t: str) -> bool:
    ...
```

**Exemple 1**
```
Entrée : s = "anagram", t = "nagaram"
Sortie : True
```

**Exemple 2**
```
Entrée : s = "rat", t = "car"
Sortie : False
```

### Énoncé — Partie B : Group Anagrams

Étant donné une liste de chaînes `strs`, **regroupe les anagrammes ensemble**. La réponse peut être renvoyée **dans n'importe quel ordre**, aussi bien pour les groupes que pour les mots à l'intérieur d'un groupe.

```python
def group_anagrams(strs: list[str]) -> list[list[str]]:
    ...
```

**Exemple 1**
```
Entrée : strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
Sortie : [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
Explication :
  - Aucun autre mot n'utilise les lettres de "bat".
  - "nat" et "tan" sont des anagrammes.
  - "ate", "eat" et "tea" sont des anagrammes.
```

**Exemple 2**
```
Entrée : strs = [""]
Sortie : [[""]]
```

**Exemple 3**
```
Entrée : strs = ["a"]
Sortie : [["a"]]
```

### Contraintes

- `1 <= len(s), len(t) <= 5 * 10^4`
- `1 <= len(strs) <= 10^4`
- `0 <= len(strs[i]) <= 100`
- Toutes les chaînes ne contiennent que des **lettres minuscules** de `a` à `z`.

### Paliers

**Palier 1 — Valid Anagram.** Implémente `is_anagram`.

**Palier 2 — Group Anagrams.** Implémente `group_anagrams`. Une solution qui compare chaque mot avec tous les autres (O(n²)) est acceptée pour valider ce palier.

**Palier 3 — Optimisation.** Fais une solution en **un seul passage** sur la liste, avec un dictionnaire. Ensuite, **sans utiliser `sorted()`**, trouve une clé qui identifie un groupe d'anagrammes en O(k), où k est la longueur du mot.

### Tests

```python
# Partie A
assert is_anagram("anagram", "nagaram") is True
assert is_anagram("rat", "car") is False
assert is_anagram("a", "ab") is False
assert is_anagram("aacc", "ccac") is False

# Partie B — on normalise l'ordre pour pouvoir comparer
def normaliser(groupes):
    return sorted(sorted(g) for g in groupes)

assert normaliser(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])) == \
       normaliser([["bat"], ["nat", "tan"], ["ate", "eat", "tea"]])
assert normaliser(group_anagrams([""])) == [[""]]
assert normaliser(group_anagrams(["a"])) == [["a"]]
assert normaliser(group_anagrams(["ab", "ba", "abc", "cab", "x"])) == \
       normaliser([["ab", "ba"], ["abc", "cab"], ["x"]])
print("Group Anagrams : tous les tests passent ✅")
```

<details>
<summary>💡 Indice palier 3 (un seul passage)</summary>

Deux anagrammes deviennent identiques une fois leurs lettres triées : `"eat"` et `"tea"` donnent tous les deux `"aet"`. Utilise ce résultat comme **clé** d'un dictionnaire dont les valeurs sont des listes de mots.

</details>

<details>
<summary>💡 Indice palier 3 (sans sorted)</summary>

Compte les occurrences de chaque lettre dans un tableau de 26 cases. Attention : une liste ne peut pas servir de clé de dictionnaire. Quel type immuable peut la remplacer ?

</details>

---

## 4. Merge Intervals

**Difficulté :** ★★☆ Moyen — **Temps indicatif :** 35 min
**Notions :** tri avec `key`, logique de chevauchement

### Énoncé

Étant donné une liste d'intervalles `intervals` où `intervals[i] = [debut_i, fin_i]`, **fusionne tous les intervalles qui se chevauchent** et renvoie la liste des intervalles qui ne se chevauchent pas et qui couvrent tous les intervalles d'entrée.

Deux intervalles qui **se touchent** (la fin de l'un est égale au début de l'autre) se chevauchent et doivent être fusionnés.

```python
def merge(intervals: list[list[int]]) -> list[list[int]]:
    ...
```

### Exemples

**Exemple 1**
```
Entrée : intervals = [[1,3], [2,6], [8,10], [15,18]]
Sortie : [[1,6], [8,10], [15,18]]
Explication : [1,3] et [2,6] se chevauchent, on les fusionne en [1,6].
```

**Exemple 2**
```
Entrée : intervals = [[1,4], [4,5]]
Sortie : [[1,5]]
Explication : [1,4] et [4,5] se touchent, ils sont donc fusionnés.
```

**Exemple 3**
```
Entrée : intervals = [[4,7], [1,4]]
Sortie : [[1,7]]
Explication : l'entrée n'est pas forcément triée.
```

### Contraintes

- `1 <= len(intervals) <= 10^4`
- `len(intervals[i]) == 2`
- `0 <= debut_i <= fin_i <= 10^4`
- La sortie doit être **triée par début d'intervalle**.

### Paliers

**Palier 1 — Entrée triée.** Suppose que les intervalles sont déjà triés par début. Gère les exemples 1 et 2.

**Palier 2 — Cas général.** Gère une entrée **non triée** et les cas limites : un intervalle contenu dans un autre, un seul intervalle, des intervalles identiques.

**Palier 3 — Bonus : Insert Interval.** On te donne une liste d'intervalles **déjà triés et sans chevauchement**, et un nouvel intervalle. Insère-le en fusionnant si nécessaire, **sans retrier toute la liste**.

```python
def insert(intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
    ...
```

```
intervals = [[1,3], [6,9]], new_interval = [2,5]
→ [[1,5], [6,9]]

intervals = [[1,2], [3,5], [6,7], [8,10], [12,16]], new_interval = [4,8]
→ [[1,2], [3,10], [12,16]]
Explication : [4,8] chevauche [3,5], [6,7] et [8,10].
```

### Tests

```python
# Palier 1
assert merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
assert merge([[1, 4], [4, 5]]) == [[1, 5]]

# Palier 2
assert merge([[4, 7], [1, 4]]) == [[1, 7]]
assert merge([[1, 10], [2, 3], [4, 5]]) == [[1, 10]]
assert merge([[5, 5]]) == [[5, 5]]
assert merge([[2, 3], [2, 3]]) == [[2, 3]]
assert merge([[8, 10], [1, 3], [2, 6], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]

# Bonus
assert insert([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]
assert insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]) == [[1, 2], [3, 10], [12, 16]]
assert insert([], [5, 7]) == [[5, 7]]
assert insert([[1, 5]], [6, 8]) == [[1, 5], [6, 8]]
print("Merge Intervals : tous les tests passent ✅")
```

<details>
<summary>💡 Indice palier 1</summary>

Garde une liste de résultats. Pour chaque intervalle, regarde uniquement **le dernier intervalle du résultat** : s'ils se chevauchent, étends sa fin ; sinon, ajoute le nouvel intervalle.

</details>

<details>
<summary>💡 Indice palier 2</summary>

Trie d'abord avec `sorted(intervals, key=...)`. Pour l'intervalle contenu dans un autre (`[1,10]` puis `[2,3]`), quelle doit être la nouvelle fin : celle du dernier intervalle, ou la plus grande des deux ?

</details>

<details>
<summary>💡 Indice palier 3</summary>

Découpe le travail en trois phases : ajoute d'abord tels quels les intervalles qui finissent **avant** le nouveau, puis fusionne ceux qui le chevauchent, et enfin ajoute ceux qui commencent **après**.

</details>

---

## Grille de progression

Coche chaque palier validé (tous les tests passent).

| Apprenant | 1.1 | 1.2 | 1.3 | 2.1 | 2.2 | 2.3 | 3.1 | 3.2 | 3.3 | 4.1 | 4.2 | 4.3 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ |