# Les Opérateurs en Python — Guide Simple

## C'est quoi un opérateur ?

Un opérateur, c'est un **symbole** qui dit à Python de faire quelque chose avec des valeurs.
Par exemple, le `+` dit à Python d'additionner deux nombres. Simple !

---

## 1. Opérateurs arithmétiques (faire des maths)

Ce sont les opérateurs pour **calculer**, comme sur une calculatrice :

```python
5 + 3     # 8       → Addition
10 - 4    # 6       → Soustraction
3 * 4     # 12      → Multiplication
10 / 3    # 3.333   → Division (donne toujours un nombre à virgule)
10 // 3   # 3       → Division entière (coupe la virgule, garde le nombre entier)
10 % 3    # 1       → Modulo (le reste de la division : 10 ÷ 3 = 3 reste 1)
2 ** 5    # 32      → Puissance (2 × 2 × 2 × 2 × 2)
```

### Petites astuces

```python
# Le modulo % est super utile pour savoir si un nombre est pair ou impair
7 % 2    # 1 → impair (il reste 1)
8 % 2    # 0 → pair (il reste 0)

# La division / donne TOUJOURS un nombre à virgule, même quand ça tombe juste
10 / 2   # 5.0  (pas 5, mais 5.0)

# La division entière // coupe tout ce qui est après la virgule
7 // 2   # 3  (pas 3.5, juste 3)
```

---

## 2. Opérateurs de comparaison (comparer des choses)

Ces opérateurs **comparent** deux valeurs et répondent `True` (vrai) ou `False` (faux) :

```python
5 == 5    # True    → Est-ce que c'est égal ?
5 != 3    # True    → Est-ce que c'est différent ?
5 > 3     # True    → Est-ce que c'est plus grand ?
5 < 3     # False   → Est-ce que c'est plus petit ?
5 >= 5    # True    → Plus grand OU égal ?
5 <= 3    # False   → Plus petit OU égal ?
```

### Attention : `=` et `==` c'est pas pareil !

```python
x = 5     # Un seul = → on DONNE une valeur à x
x == 5    # Deux == → on DEMANDE "est-ce que x vaut 5 ?"
```

C'est l'erreur la plus fréquente chez les débutants !

### On peut chaîner les comparaisons

```python
x = 15
1 < x < 20      # True → "est-ce que x est entre 1 et 20 ?"
10 <= x <= 20    # True → "est-ce que x est entre 10 et 20 (inclus) ?"
```

---

## 3. Opérateurs logiques (combiner des conditions)

Quand on veut vérifier **plusieurs conditions** en même temps :

```python
# and → les DEUX conditions doivent être vraies
age = 25
a_permis = True
age >= 18 and a_permis    # True → il a 18+ ET le permis

# or → AU MOINS UNE condition doit être vraie
jour = "samedi"
jour == "samedi" or jour == "dimanche"    # True → c'est le weekend !

# not → inverse le résultat (vrai devient faux, faux devient vrai)
est_connecte = False
not est_connecte    # True → il n'est PAS connecté
```

### Exemples concrets

```python
# Vérifier qu'un utilisateur peut s'inscrire
age = 20
email = "alice@mail.com"

if age >= 13 and email != "":
    print("Inscription OK !")

# Vérifier si c'est un weekend
jour = "lundi"
if jour == "samedi" or jour == "dimanche":
    print("C'est le weekend !")
else:
    print("C'est un jour de semaine")

# Vérifier qu'une liste n'est PAS vide
ma_liste = [1, 2, 3]
if not len(ma_liste) == 0:
    print("La liste contient des éléments")
```

---

## 4. Opérateurs d'affectation (donner une valeur)

Le plus basique c'est `=`, mais il existe des **raccourcis** super pratiques :

```python
x = 10       # x vaut 10

x += 5       # x = x + 5       → x vaut maintenant 15
x -= 3       # x = x - 3       → x vaut maintenant 12
x *= 2       # x = x * 2       → x vaut maintenant 24
x /= 4       # x = x / 4       → x vaut maintenant 6.0
x //= 2      # x = x // 2      → x vaut maintenant 3.0
x %= 2       # x = x % 2       → x vaut maintenant 1.0
x **= 3      # x = x ** 3      → x vaut maintenant 1.0
```

En gros, `x += 5` c'est juste un raccourci pour écrire `x = x + 5`. C'est plus court et plus lisible.

---

## 5. Opérateurs d'appartenance (chercher dedans)

Pour vérifier si quelque chose **se trouve dans** une collection :

```python
# in → "est-ce que c'est dedans ?"
"a" in "abcdef"           # True → "a" est dans la chaîne
3 in [1, 2, 3, 4]         # True → 3 est dans la liste
"chat" in ["chien", "chat", "poisson"]  # True

# not in → "est-ce que c'est PAS dedans ?"
5 not in [1, 2, 3]        # True → 5 n'est pas dans la liste
"z" not in "bonjour"      # True → pas de "z" dans "bonjour"
```

### Exemples pratiques

```python
# Vérifier un mot de passe interdit
mot_de_passe = "1234"
interdits = ["1234", "password", "azerty"]

if mot_de_passe in interdits:
    print("Ce mot de passe est trop simple !")

# Chercher un mot dans une phrase
phrase = "Le chat dort sur le canapé"
if "chat" in phrase:
    print("On parle d'un chat !")
```

---

## 6. Opérateurs d'identité (est-ce le MÊME objet ?)

C'est un peu plus subtil. `is` vérifie si deux variables pointent vers **le même objet en mémoire**, pas juste si elles ont la même valeur :

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

a == b    # True → même valeur
a is b    # False → ce sont deux listes DIFFÉRENTES qui ont la même valeur
a is c    # True → c pointe vers la MÊME liste que a
```

### Quand utiliser `is` ?

En pratique, on l'utilise surtout pour vérifier si quelque chose est `None` :

```python
resultat = None

# La bonne façon de vérifier None :
if resultat is None:
    print("Pas de résultat")

# La mauvaise façon (ça marche mais c'est pas recommandé) :
if resultat == None:
    print("Pas de résultat")
```

---

## 7. L'opérateur ternaire (if/else en une ligne)

C'est un raccourci pour écrire un `if/else` simple sur **une seule ligne** :

```python
# Version longue
age = 20
if age >= 18:
    statut = "majeur"
else:
    statut = "mineur"

# Version courte avec l'opérateur ternaire
statut = "majeur" if age >= 18 else "mineur"
```

La forme c'est : `valeur_si_vrai if condition else valeur_si_faux`

```python
# Quelques exemples
note = 15
mention = "bien" if note >= 14 else "passable"

temperature = 35
conseil = "Bois de l'eau" if temperature > 30 else "Tout va bien"

nombre = -5
absolu = nombre if nombre >= 0 else -nombre    # valeur absolue maison
```

---

## 8. Opérateurs bit à bit (pour les curieux)

Ces opérateurs travaillent sur les **bits** (les 0 et 1) des nombres. Tu n'en auras pas besoin souvent au début, mais c'est bien de savoir qu'ils existent :

```python
a = 5      # En binaire : 0101
b = 3      # En binaire : 0011

a & b      # 1  → ET : garde les bits qui sont à 1 dans les DEUX (0001)
a | b      # 7  → OU : garde les bits qui sont à 1 dans AU MOINS UN (0111)
a ^ b      # 6  → OU EXCLUSIF : garde les bits différents (0110)
~a         # -6 → inverse tous les bits
a << 1     # 10 → décale les bits vers la gauche (multiplie par 2)
a >> 1     # 2  → décale les bits vers la droite (divise par 2)
```

---

## 9. Le `+` fait pas toujours la même chose !

Un truc sympa en Python : certains opérateurs changent de comportement selon le type de données :

```python
# Avec des nombres → addition
3 + 5          # 8

# Avec des textes → concaténation (coller ensemble)
"Bon" + "jour"    # "Bonjour"

# Avec des listes → fusion
[1, 2] + [3, 4]   # [1, 2, 3, 4]
```

```python
# Pareil pour * :
# Avec des nombres → multiplication
3 * 4          # 12

# Avec un texte et un nombre → répétition
"ha" * 3       # "hahaha"

# Avec une liste et un nombre → répétition
[0] * 5        # [0, 0, 0, 0, 0]
```

---

## 10. Ordre de priorité (qui passe en premier ?)

Comme en maths, Python suit un **ordre de priorité** :

```python
# La multiplication passe AVANT l'addition
2 + 3 * 4      # 14  (pas 20)

# Pour changer l'ordre, utilise des parenthèses
(2 + 3) * 4    # 20
```

Voici l'ordre du **plus prioritaire** au **moins prioritaire** :

```
1.  ()           Parenthèses         → toujours en premier
2.  **           Puissance
3.  -, +, ~      Négatif, positif, inversion bits
4.  *, /, //, %  Multiplication, divisions, modulo
5.  +, -         Addition, soustraction
6.  <<, >>       Décalages de bits
7.  &            ET bit à bit
8.  ^            OU exclusif
9.  |            OU bit à bit
10. ==, !=, <, >, <=, >=, is, in   Comparaisons
11. not          NON logique
12. and          ET logique
13. or           OU logique
```

**Conseil : en cas de doute, mets des parenthèses !** C'est plus clair pour tout le monde.

```python
# Difficile à lire :
result = a + b * c > d and e or f

# Beaucoup plus clair :
result = ((a + (b * c)) > d) and e) or f
```

---

## Résumé en une image mentale

| Tu veux... | Opérateur | Exemple |
|---|---|---|
| Calculer | `+  -  *  /  //  %  **` | `10 + 3` → `13` |
| Comparer | `==  !=  <  >  <=  >=` | `5 > 3` → `True` |
| Combiner des conditions | `and  or  not` | `True and False` → `False` |
| Raccourci d'affectation | `+=  -=  *=  /=` | `x += 1` (ajoute 1 à x) |
| Chercher dedans | `in  not in` | `"a" in "abc"` → `True` |
| Vérifier l'identité | `is  is not` | `x is None` |
| if/else en une ligne | `... if ... else ...` | `"oui" if ok else "non"` |

---

> 💡 **Le meilleur conseil** : ouvre un terminal Python (`python3` dans le terminal) et teste chaque opérateur toi-même. C'est en pratiquant qu'on retient !
