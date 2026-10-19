# Python — Récapitulatif Théorique Complet

## Table des matières

1. [Nature du langage](#1-nature-du-langage)
2. [Modèle d'exécution](#2-modèle-dexécution)
3. [Système de typage](#3-système-de-typage)
4. [Modèle mémoire et gestion des objets](#4-modèle-mémoire-et-gestion-des-objets)
5. [Structures de données natives](#5-structures-de-données-natives)
6. [Fonctions et portée des variables](#6-fonctions-et-portée-des-variables)
7. [Programmation orientée objet](#7-programmation-orientée-objet)
8. [Protocole itérateur et générateurs](#8-protocole-itérateur-et-générateurs)
9. [Décorateurs et métaprogrammation](#9-décorateurs-et-métaprogrammation)
10. [Gestion des exceptions](#10-gestion-des-exceptions)
11. [Modules, packages et imports](#11-modules-packages-et-imports)
12. [Concurrence et parallélisme](#12-concurrence-et-parallélisme)
13. [Gestion de la mémoire et garbage collection](#13-gestion-de-la-mémoire-et-garbage-collection)
14. [Compréhensions et expressions génératrices](#14-compréhensions-et-expressions-génératrices)
15. [Context managers](#15-context-managers)
16. [Type hints et annotations](#16-type-hints-et-annotations)
17. [Le protocole descripteur](#17-le-protocole-descripteur)
18. [Bonnes pratiques et philosophie](#18-bonnes-pratiques-et-philosophie)

---

## 1. Nature du langage

Python est un langage **interprété**, **multi-paradigme** et à **typage dynamique fort**.

### Interprété vs compilé

Python n'est pas directement exécuté par le processeur. Le code source (`.py`) est d'abord compilé en **bytecode** (`.pyc`), un code intermédiaire indépendant de la plateforme, qui est ensuite exécuté par la **Python Virtual Machine (PVM)**. Ce processus est transparent pour le développeur.

```
Code source (.py)  →  Bytecode (.pyc)  →  Exécution par la PVM
```

L'implémentation de référence est **CPython** (écrite en C). D'autres implémentations existent : **PyPy** (avec JIT), **Jython** (JVM), **IronPython** (.NET), **MicroPython** (microcontrôleurs).

### Multi-paradigme

Python supporte simultanément :

- La **programmation impérative** (instructions séquentielles, boucles, conditions)
- La **programmation orientée objet** (classes, héritage, polymorphisme)
- La **programmation fonctionnelle** (fonctions de premier ordre, `lambda`, `map`, `filter`, `reduce`)

### Indentation significative

Contrairement à la plupart des langages qui utilisent des accolades `{}` ou des mots-clés `begin/end`, Python utilise l'**indentation** comme délimiteur de blocs. Ce n'est pas cosmétique, c'est **syntaxique** : une mauvaise indentation provoque une `IndentationError`. La convention standard est de 4 espaces par niveau.

```python
if condition:
    # Ce bloc est défini par l'indentation
    instruction_1()
    instruction_2()
# Retour au niveau précédent = fin du bloc
```

---

## 2. Modèle d'exécution

### Compilation en bytecode

Quand Python exécute un fichier `.py`, il le compile d'abord en bytecode (stocké dans `__pycache__/`). Ce bytecode est un jeu d'instructions de bas niveau pour la PVM. On peut l'inspecter via le module `dis` :

```python
import dis

def addition(a, b):
    return a + b

dis.dis(addition)
# Affiche les instructions bytecode : LOAD_FAST, BINARY_ADD, RETURN_VALUE...
```

### Évaluation dynamique

Python évalue le code **à l'exécution** (runtime). Les définitions de classes et de fonctions sont des instructions exécutées, pas des déclarations statiques. Cela signifie qu'une classe peut être définie conditionnellement :

```python
if use_advanced:
    class Engine:
        pass
else:
    class Engine:
        pass
```

### Espace de noms (Namespaces)

Tout en Python vit dans un dictionnaire appelé **namespace**. Il en existe plusieurs niveaux : built-in, global (module), enclosing (fonctions englobantes), local (fonction courante). On peut les inspecter avec `globals()` et `locals()`.

---

## 3. Système de typage

### Typage dynamique

Les variables ne sont pas typées : ce sont des **étiquettes** (noms) qui référencent des objets. Un même nom peut pointer vers des objets de types différents au cours de l'exécution :

```python
x = 42          # x pointe vers un int
x = "hello"     # x pointe maintenant vers un str
x = [1, 2, 3]   # x pointe maintenant vers une list
```

### Typage fort

Python est **fortement typé** : il ne fait pas de conversions implicites entre types incompatibles. `"3" + 5` lève une `TypeError`, contrairement à JavaScript qui produirait `"35"`.

```python
"3" + 5    # TypeError: can only concatenate str to str
int("3") + 5  # 8 — conversion explicite nécessaire
```

### Duck typing

Python suit le principe : *"If it walks like a duck and quacks like a duck, it's a duck."* Le type réel d'un objet importe moins que les **méthodes et attributs** qu'il expose. Cela permet un polymorphisme naturel sans héritage :

```python
class Canard:
    def parler(self):
        return "Coin coin"

class Chien:
    def parler(self):
        return "Wouf"

def faire_parler(animal):
    # Peu importe le type, tant qu'il a une méthode parler()
    print(animal.parler())
```

### Tout est objet

En Python, **absolument tout** est un objet : les entiers, les fonctions, les classes, les modules, même `None`. Chaque objet possède une **identité** (`id()`), un **type** (`type()`) et une **valeur**.

```python
type(42)          # <class 'int'>
type(print)       # <class 'builtin_function_or_method'>
type(int)         # <class 'type'>
isinstance(42, object)  # True — même les int héritent d'object
```

---

## 4. Modèle mémoire et gestion des objets

### Référence vs valeur

Les variables Python ne contiennent jamais directement une valeur. Elles stockent une **référence** (pointeur) vers un objet en mémoire. L'affectation `a = b` ne copie pas l'objet : elle fait pointer `a` vers le même objet que `b`.

```python
a = [1, 2, 3]
b = a           # b et a pointent vers la MÊME liste
b.append(4)
print(a)        # [1, 2, 3, 4] — a est aussi modifié
```

### Mutabilité vs immutabilité

C'est une distinction fondamentale en Python :

| Immuables (immutable) | Mutables (mutable) |
|---|---|
| `int`, `float`, `str`, `tuple`, `frozenset`, `bytes` | `list`, `dict`, `set`, `bytearray` |

Un objet **immuable** ne peut pas être modifié après sa création. Toute opération qui semble le modifier crée en réalité un **nouvel objet** :

```python
s = "hello"
id_avant = id(s)
s += " world"
id_apres = id(s)
# id_avant != id_apres → un nouvel objet str a été créé
```

Un objet **mutable** peut être modifié en place sans changer son identité :

```python
lst = [1, 2, 3]
id_avant = id(lst)
lst.append(4)
id_apres = id(lst)
# id_avant == id_apres → même objet, modifié en place
```

### Interning et mise en cache

CPython optimise la mémoire en réutilisant certains objets immuables fréquemment utilisés. Les entiers de **-5 à 256** et les chaînes courtes sont *internés* (un seul objet en mémoire partagé par toutes les références) :

```python
a = 256
b = 256
a is b   # True — même objet en mémoire (interné)

a = 257
b = 257
a is b   # False (potentiellement) — objets distincts
```

### `is` vs `==`

- `==` compare les **valeurs** (appelle `__eq__`)
- `is` compare les **identités** (même objet en mémoire, même `id()`)

```python
a = [1, 2]
b = [1, 2]
a == b   # True  — mêmes valeurs
a is b   # False — objets distincts en mémoire
```

---

## 5. Structures de données natives

### `list` — Liste

Tableau dynamique ordonné et mutable. Implémenté en C comme un **tableau de pointeurs** vers des objets. L'accès par index est en O(1), l'ajout en fin (`append`) est en O(1) amorti, l'insertion/suppression au milieu est en O(n).

```python
lst = [1, "deux", 3.0, [4, 5]]  # types hétérogènes autorisés
lst[0]       # 1 — accès O(1)
lst[-1]      # [4, 5] — indexation négative
lst[1:3]     # ["deux", 3.0] — slicing (crée une copie superficielle)
```

### `tuple` — Tuple

Séquence ordonnée et **immuable**. Plus léger en mémoire qu'une liste. Utilisé comme clé de dictionnaire (car hashable si tous ses éléments le sont).

```python
t = (1, 2, 3)
t[0] = 10     # TypeError — immuable
# Unpacking
a, b, c = t   # a=1, b=2, c=3
```

Les **named tuples** ajoutent des noms aux positions :

```python
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(3, 4)
p.x  # 3
```

### `dict` — Dictionnaire

Table de hachage (hash map) ordonnée (depuis Python 3.7+, l'ordre d'insertion est garanti). Les clés doivent être **hashables** (immuables). Accès, insertion et suppression en O(1) en moyenne.

```python
d = {"nom": "Alice", "age": 30}
d["nom"]           # "Alice" — O(1)
d.get("ville", "?")  # "?" — valeur par défaut si clé absente
d["ville"] = "Paris"  # insertion
```

Implémentation interne : chaque clé est hachée via `hash()`. Le hash détermine la position dans un tableau interne. Les collisions sont gérées par **open addressing** (sondage linéaire).

### `set` — Ensemble

Collection non ordonnée d'éléments **uniques** et **hashables**. Basé sur une table de hachage (comme `dict` mais sans valeurs). Opérations ensemblistes en O(1) moyen :

```python
s = {1, 2, 3, 3, 3}  # {1, 2, 3} — doublons supprimés
a = {1, 2, 3}
b = {2, 3, 4}
a | b   # {1, 2, 3, 4} — union
a & b   # {2, 3} — intersection
a - b   # {1} — différence
a ^ b   # {1, 4} — différence symétrique
```

### `str` — Chaîne de caractères

Séquence immuable de caractères Unicode. Python 3 utilise Unicode nativement (UTF-8 en interne avec optimisation selon le contenu).

```python
s = "Hello 🌍"
len(s)          # 7 — compte les caractères, pas les octets
s.encode('utf-8')  # b'Hello \xf0\x9f\x8c\x8d' — 10 octets
```

Les **f-strings** (Python 3.6+) permettent l'interpolation :

```python
nom = "Alice"
f"Bonjour {nom}, 2+2 = {2+2}"  # "Bonjour Alice, 2+2 = 4"
```

---

## 6. Fonctions et portée des variables

### Fonctions comme objets de premier ordre

Les fonctions sont des objets à part entière. Elles peuvent être assignées à des variables, passées en argument, retournées par d'autres fonctions, stockées dans des structures de données :

```python
def carre(x):
    return x ** 2

f = carre          # f est maintenant une référence à la fonction
f(5)               # 25
list(map(f, [1, 2, 3]))  # [1, 4, 9]
```

### Règle LEGB

La résolution des noms suit l'ordre **LEGB** :

1. **L**ocal — variables définies dans la fonction courante
2. **E**nclosing — variables des fonctions englobantes (closures)
3. **G**lobal — variables au niveau du module
4. **B**uilt-in — noms prédéfinis (`print`, `len`, `int`…)

```python
x = "global"

def externe():
    x = "enclosing"
    def interne():
        x = "local"
        print(x)  # "local" (L)
    interne()

externe()
```

Les mots-clés `global` et `nonlocal` permettent de modifier des variables hors de la portée locale :

```python
compteur = 0
def incrementer():
    global compteur
    compteur += 1

def externe():
    x = 10
    def interne():
        nonlocal x
        x += 1
    interne()
    print(x)  # 11
```

### Arguments : mécanisme de passage

Python utilise le passage par **affectation d'objet** (*pass by object reference*). Ce n'est ni du pass-by-value ni du pass-by-reference classique :

- Pour un objet **immuable** : le comportement ressemble au passage par valeur (la fonction ne peut pas modifier l'original)
- Pour un objet **mutable** : le comportement ressemble au passage par référence (la fonction peut modifier l'objet original)

```python
def modifier(lst, nombre):
    lst.append(4)    # modifie l'objet original (mutable)
    nombre += 10     # crée un nouvel objet local (immutable)

ma_liste = [1, 2, 3]
mon_nombre = 5
modifier(ma_liste, mon_nombre)
print(ma_liste)     # [1, 2, 3, 4] — modifiée
print(mon_nombre)   # 5 — inchangé
```

### Arguments avancés

```python
# Valeurs par défaut (ATTENTION : évaluées une seule fois !)
def ajouter(element, liste=None):
    if liste is None:
        liste = []
    liste.append(element)
    return liste

# *args : tuple d'arguments positionnels variables
def somme(*args):
    return sum(args)

# **kwargs : dict d'arguments nommés variables
def config(**kwargs):
    for cle, val in kwargs.items():
        print(f"{cle} = {val}")

# Argument positionnel uniquement (/) et nommé uniquement (*)
def f(pos_only, /, normal, *, kw_only):
    pass
# f(1, 2, kw_only=3)  ✓
# f(pos_only=1, ...)   ✗ TypeError
```

### Piège classique : argument mutable par défaut

```python
# ⚠ PIÈGE : la liste par défaut est partagée entre tous les appels
def mauvais(element, liste=[]):
    liste.append(element)
    return liste

mauvais(1)  # [1]
mauvais(2)  # [1, 2] ← inattendu ! Même objet liste réutilisé
```

### Fonctions lambda

Fonctions anonymes limitées à une seule expression :

```python
carre = lambda x: x ** 2
tri = sorted(mots, key=lambda m: len(m))
```

---

## 7. Programmation orientée objet

### Modèle objet de Python

En Python, la POO repose sur quelques principes :

- **Tout est objet**, y compris les classes elles-mêmes (qui sont des instances de `type`)
- Les attributs sont résolus dynamiquement à l'exécution
- Il n'y a pas de vrai encapsulation privée (convention `_` et name mangling `__`)

### Classes et instances

```python
class Animal:
    # Attribut de classe (partagé par toutes les instances)
    espece_count = 0

    def __init__(self, nom, age):
        # Attributs d'instance
        self.nom = nom
        self.age = age
        Animal.espece_count += 1

    def parler(self):
        raise NotImplementedError

    def __repr__(self):
        return f"Animal(nom={self.nom!r}, age={self.age})"

    def __str__(self):
        return f"{self.nom} ({self.age} ans)"
```

### `self` explicite

Contrairement à Java ou C++ où `this` est implicite, Python exige que le premier paramètre de chaque méthode d'instance soit **explicitement** `self`. Ce n'est pas un mot-clé mais une **convention** forte :

```python
class Exemple:
    def methode(self):
        # self est la référence à l'instance courante
        print(self.attribut)
```

### Héritage et MRO

Python supporte l'**héritage multiple**. L'ordre de résolution des méthodes suit l'algorithme **C3 Linearization** (MRO — Method Resolution Order) :

```python
class A:
    def qui(self):
        return "A"

class B(A):
    def qui(self):
        return "B"

class C(A):
    def qui(self):
        return "C"

class D(B, C):
    pass

D().qui()    # "B" — suit le MRO
D.__mro__    # (D, B, C, A, object)
```

`super()` parcourt le MRO, pas seulement la classe parente directe :

```python
class B(A):
    def qui(self):
        return "B puis " + super().qui()  # Suit le MRO
```

### Méthodes spéciales (dunder methods)

Les méthodes `__xxx__` permettent de définir le comportement des opérateurs et des fonctions built-in :

| Méthode | Déclenchée par | Usage |
|---|---|---|
| `__init__` | `Classe()` | Initialisation |
| `__repr__` | `repr(obj)` | Représentation développeur |
| `__str__` | `str(obj)`, `print(obj)` | Représentation utilisateur |
| `__len__` | `len(obj)` | Longueur |
| `__getitem__` | `obj[key]` | Accès par index/clé |
| `__setitem__` | `obj[key] = val` | Affectation par index/clé |
| `__contains__` | `x in obj` | Test d'appartenance |
| `__eq__` | `obj == other` | Égalité |
| `__lt__` | `obj < other` | Comparaison |
| `__add__` | `obj + other` | Addition |
| `__iter__` | `for x in obj` | Itération |
| `__call__` | `obj()` | Appel comme fonction |
| `__enter__`/`__exit__` | `with obj` | Context manager |
| `__hash__` | `hash(obj)` | Hashage (clé de dict/set) |

### Encapsulation par convention

Python n'a pas de `private` ou `protected`. La convention est :

- `_attribut` : « protégé » (usage interne, ne pas accéder depuis l'extérieur)
- `__attribut` : **name mangling** — renommé en `_Classe__attribut` pour éviter les collisions dans l'héritage

```python
class Compte:
    def __init__(self):
        self._solde = 0       # convention "protégé"
        self.__secret = 42    # name mangling

c = Compte()
c._solde          # accessible (pas de vrai blocage)
c.__secret        # AttributeError
c._Compte__secret # 42 — accessible via le nom décoré
```

### `@property` — Propriétés

Permet de transformer un attribut en accesseur avec getter/setter sans changer l'interface :

```python
class Cercle:
    def __init__(self, rayon):
        self._rayon = rayon

    @property
    def rayon(self):
        return self._rayon

    @rayon.setter
    def rayon(self, valeur):
        if valeur < 0:
            raise ValueError("Le rayon doit être positif")
        self._rayon = valeur

    @property
    def aire(self):
        import math
        return math.pi * self._rayon ** 2

c = Cercle(5)
c.rayon       # 5 (appelle le getter)
c.rayon = 10  # appelle le setter
c.aire        # 314.15... (propriété calculée, read-only)
```

### Classes abstraites

Le module `abc` fournit le mécanisme de classes abstraites :

```python
from abc import ABC, abstractmethod

class Forme(ABC):
    @abstractmethod
    def aire(self):
        pass

    @abstractmethod
    def perimetre(self):
        pass

# Forme() → TypeError: Can't instantiate abstract class
```

### `@staticmethod` et `@classmethod`

```python
class MaClasse:
    compteur = 0

    @staticmethod
    def utilitaire():
        # Pas d'accès à self ni cls
        return "fonction indépendante rangée dans la classe"

    @classmethod
    def creer(cls):
        # cls est la classe elle-même (pas l'instance)
        cls.compteur += 1
        return cls()
```

### Dataclasses (Python 3.7+)

Simplifient la création de classes de données en générant automatiquement `__init__`, `__repr__`, `__eq__` :

```python
from dataclasses import dataclass, field

@dataclass
class Point:
    x: float
    y: float
    label: str = "origin"

@dataclass(frozen=True)  # rend les instances immuables
class PointImmuable:
    x: float
    y: float
```

---

## 8. Protocole itérateur et générateurs

### Protocole itérateur

Un objet est **itérable** s'il implémente `__iter__()` (retourne un itérateur). Un **itérateur** implémente `__next__()` (retourne l'élément suivant ou lève `StopIteration`) :

```python
class Compteur:
    def __init__(self, maximum):
        self.maximum = maximum
        self.courant = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.courant >= self.maximum:
            raise StopIteration
        self.courant += 1
        return self.courant

for n in Compteur(3):
    print(n)  # 1, 2, 3
```

### Générateurs

Les générateurs sont des fonctions qui produisent des valeurs **paresseusement** (lazy evaluation) via `yield`. Ils implémentent automatiquement le protocole itérateur et sont beaucoup plus économes en mémoire :

```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a        # suspend l'exécution et retourne la valeur
        a, b = b, a + b

# Consomme à la demande, pas de liste infinie en mémoire
gen = fibonacci()
next(gen)  # 0
next(gen)  # 1
next(gen)  # 1
next(gen)  # 2
```

### `yield from`

Délègue à un sous-générateur :

```python
def chain(*iterables):
    for it in iterables:
        yield from it

list(chain([1, 2], [3, 4], [5]))  # [1, 2, 3, 4, 5]
```

### Coroutines basées sur les générateurs

Les générateurs peuvent aussi **recevoir** des valeurs via `send()` :

```python
def accumulateur():
    total = 0
    while True:
        valeur = yield total
        total += valeur

acc = accumulateur()
next(acc)         # 0 (initialisation)
acc.send(10)      # 10
acc.send(20)      # 30
```

---

## 9. Décorateurs et métaprogrammation

### Décorateurs

Un décorateur est une **fonction qui prend une fonction en argument et retourne une nouvelle fonction**. Syntaxe `@` :

```python
def journaliser(func):
    def wrapper(*args, **kwargs):
        print(f"Appel de {func.__name__} avec {args}, {kwargs}")
        resultat = func(*args, **kwargs)
        print(f"Résultat : {resultat}")
        return resultat
    return wrapper

@journaliser
def additionner(a, b):
    return a + b

# Équivalent à : additionner = journaliser(additionner)
additionner(3, 4)
# Appel de additionner avec (3, 4), {}
# Résultat : 7
```

### Préserver les métadonnées avec `functools.wraps`

```python
from functools import wraps

def decorateur(func):
    @wraps(func)  # Copie __name__, __doc__, etc.
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

### Décorateurs avec arguments

```python
def repeter(n):
    def decorateur(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                resultat = func(*args, **kwargs)
            return resultat
        return wrapper
    return decorateur

@repeter(3)
def saluer(nom):
    print(f"Bonjour {nom}")
```

### Décorateurs de classe

Les décorateurs peuvent aussi être appliqués aux classes, ou être implémentés comme classes :

```python
class Singleton:
    def __init__(self, cls):
        self._cls = cls
        self._instance = None

    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = self._cls(*args, **kwargs)
        return self._instance

@Singleton
class Database:
    pass
```

### Métaclasses

Les classes sont des instances de leur **métaclasse** (par défaut `type`). On peut personnaliser la création de classes :

```python
class MetaValidation(type):
    def __new__(mcs, name, bases, namespace):
        # Vérifie que toutes les méthodes ont une docstring
        for key, val in namespace.items():
            if callable(val) and not key.startswith('_'):
                if not val.__doc__:
                    raise TypeError(f"{key} doit avoir une docstring")
        return super().__new__(mcs, name, bases, namespace)

class MonAPI(metaclass=MetaValidation):
    def methode(self):
        """Documentation obligatoire."""
        pass
```

---

## 10. Gestion des exceptions

### Hiérarchie des exceptions

```
BaseException
├── SystemExit
├── KeyboardInterrupt
├── GeneratorExit
└── Exception
    ├── ValueError
    ├── TypeError
    ├── KeyError
    ├── IndexError
    ├── AttributeError
    ├── FileNotFoundError (OSError)
    ├── RuntimeError
    └── ...
```

Toujours attraper `Exception` ou ses sous-classes, jamais `BaseException` (qui inclut `SystemExit` et `KeyboardInterrupt`).

### Syntaxe complète

```python
try:
    resultat = risque()
except ValueError as e:
    # Gère une erreur de valeur
    print(f"Valeur invalide : {e}")
except (TypeError, KeyError):
    # Gère plusieurs types
    pass
except Exception as e:
    # Attrape tout le reste (sauf BaseException)
    raise  # Re-lève l'exception
else:
    # Exécuté UNIQUEMENT si aucune exception n'a été levée
    print("Succès :", resultat)
finally:
    # Exécuté TOUJOURS (nettoyage)
    fermer_ressources()
```

### Exceptions personnalisées

```python
class ErreurMetier(Exception):
    """Exception de base pour l'application."""
    pass

class SoldeInsuffisant(ErreurMetier):
    def __init__(self, solde, montant):
        self.solde = solde
        self.montant = montant
        super().__init__(
            f"Solde insuffisant : {solde}€ disponible, {montant}€ demandé"
        )
```

### EAFP vs LBYL

Python favorise le style **EAFP** (Easier to Ask Forgiveness than Permission) :

```python
# LBYL (Look Before You Leap) — style non-pythonique
if "cle" in dictionnaire:
    valeur = dictionnaire["cle"]

# EAFP — style pythonique
try:
    valeur = dictionnaire["cle"]
except KeyError:
    valeur = default
```

---

## 11. Modules, packages et imports

### Structure d'un package

```
mon_package/
├── __init__.py       # Fait du dossier un package (peut être vide)
├── module_a.py
├── module_b.py
└── sous_package/
    ├── __init__.py
    └── module_c.py
```

### Mécanisme d'import

Quand Python exécute `import mon_module` :

1. Vérifie `sys.modules` (cache des modules déjà importés)
2. Cherche le module dans les chemins de `sys.path`
3. Compile le fichier en bytecode si nécessaire
4. Exécute le code du module (une seule fois)
5. Crée un objet module dans `sys.modules`

### Types d'imports

```python
import math                     # Module entier
from math import sqrt, pi       # Noms spécifiques
from math import sqrt as racine # Alias
from math import *              # TOUT importer (déconseillé)

# Import relatif (dans un package)
from . import module_a          # Module frère
from ..sous_package import module_c  # Package parent
```

### `if __name__ == "__main__"`

Quand un fichier est exécuté directement, `__name__` vaut `"__main__"`. Quand il est importé, `__name__` vaut le nom du module. Ce pattern permet d'avoir du code exécutable uniquement en mode script :

```python
def ma_fonction():
    pass

if __name__ == "__main__":
    # Exécuté seulement si le fichier est lancé directement
    ma_fonction()
```

---

## 12. Concurrence et parallélisme

### Le GIL (Global Interpreter Lock)

Le **GIL** est un verrou global dans CPython qui empêche l'exécution simultanée de bytecode Python par plusieurs threads. C'est la spécificité la plus importante et la plus controversée de CPython :

- Un seul thread exécute du bytecode Python à la fois
- Le GIL est relâché pendant les opérations I/O (lecture fichier, requête réseau)
- Le GIL est relâché par les extensions C (NumPy, etc.)
- Conséquence : le **multithreading** n'accélère **pas** les tâches CPU-bound en Python

### Threading

Utile pour les tâches **I/O-bound** (réseau, fichiers, bases de données) grâce au relâchement du GIL :

```python
import threading

def telecharger(url):
    # Le GIL est relâché pendant l'I/O réseau
    pass

threads = [threading.Thread(target=telecharger, args=(url,)) for url in urls]
for t in threads:
    t.start()
for t in threads:
    t.join()
```

### Multiprocessing

Contourne le GIL en utilisant des **processus séparés** (chacun avec son propre interpréteur et GIL). Adapté aux tâches **CPU-bound** :

```python
from multiprocessing import Pool

def calcul_lourd(n):
    return sum(i * i for i in range(n))

with Pool(4) as pool:
    resultats = pool.map(calcul_lourd, [10**6, 10**6, 10**6, 10**6])
```

### Asyncio

Modèle de concurrence **mono-thread** basé sur une boucle événementielle. Idéal pour gérer des milliers de connexions I/O concurrentes :

```python
import asyncio

async def fetch(url):
    # Simule une requête réseau asynchrone
    await asyncio.sleep(1)
    return f"Résultat de {url}"

async def main():
    # Lance 3 requêtes en parallèle (concurrence, pas parallélisme)
    resultats = await asyncio.gather(
        fetch("url1"),
        fetch("url2"),
        fetch("url3"),
    )
    # Prend ~1 seconde au lieu de ~3

asyncio.run(main())
```

Les mots-clés `async` et `await` (Python 3.5+) définissent et consomment des **coroutines** :

- `async def` déclare une fonction coroutine
- `await` suspend l'exécution jusqu'à ce que le résultat soit prêt
- La boucle événementielle orchestre l'exécution de toutes les coroutines

---

## 13. Gestion de la mémoire et garbage collection

### Comptage de références

Le mécanisme principal de CPython est le **reference counting**. Chaque objet maintient un compteur du nombre de références pointant vers lui. Quand ce compteur atteint 0, l'objet est immédiatement détruit :

```python
import sys

a = [1, 2, 3]
sys.getrefcount(a)  # 2 (a + l'argument de getrefcount)

b = a
sys.getrefcount(a)  # 3

del b
sys.getrefcount(a)  # 2
```

### Garbage collector cyclique

Le comptage de références ne détecte pas les **cycles** (A référence B qui référence A). Python dispose d'un **garbage collector cyclique** (module `gc`) qui détecte et collecte ces cycles :

```python
import gc

a = []
b = []
a.append(b)  # a → b
b.append(a)  # b → a (cycle !)
del a, b      # refcount ne tombe pas à 0
# Le GC cyclique détectera et nettoiera ce cycle
```

### `__del__` et finalisation

Le destructeur `__del__` est appelé quand l'objet est collecté. Son usage est **déconseillé** car le moment de l'appel n'est pas garanti. Préférer les context managers (`with`) :

```python
# Déconseillé
class Fichier:
    def __del__(self):
        self.handle.close()

# Recommandé
class Fichier:
    def __enter__(self):
        return self
    def __exit__(self, *args):
        self.handle.close()
```

### `__slots__`

Par défaut, chaque instance stocke ses attributs dans un `__dict__` (dictionnaire). `__slots__` remplace ce dict par une structure fixe, économisant de la mémoire :

```python
class PointSlots:
    __slots__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y

# ~40% moins de mémoire par instance qu'avec __dict__
# Mais impossible d'ajouter des attributs dynamiquement
```

---

## 14. Compréhensions et expressions génératrices

### Compréhensions de listes

Syntaxe concise et performante pour créer des listes (plus rapide qu'une boucle `for` équivalente car optimisée en bytecode) :

```python
# Forme générale : [expression for item in iterable if condition]
carres = [x**2 for x in range(10)]
pairs = [x for x in range(20) if x % 2 == 0]

# Compréhension imbriquée
matrice = [[1, 2, 3], [4, 5, 6]]
aplati = [elem for ligne in matrice for elem in ligne]  # [1, 2, 3, 4, 5, 6]
```

### Compréhensions de dictionnaires et ensembles

```python
# Dict comprehension
inverse = {v: k for k, v in original.items()}
compteur = {mot: texte.count(mot) for mot in set(texte.split())}

# Set comprehension
uniques = {mot.lower() for mot in phrase.split()}
```

### Expressions génératrices

Même syntaxe que les compréhensions de listes, mais avec des parenthèses. Produit les valeurs **paresseusement** (une à la fois), sans tout stocker en mémoire :

```python
# Compréhension de liste : crée toute la liste en mémoire
somme = sum([x**2 for x in range(10_000_000)])  # ~80 Mo

# Expression génératrice : calcule à la demande
somme = sum(x**2 for x in range(10_000_000))    # ~0 Mo supplémentaire
```

---

## 15. Context managers

### Protocole `with`

Le mot-clé `with` garantit l'exécution du code de nettoyage, même en cas d'exception. Un context manager implémente `__enter__` et `__exit__` :

```python
class GestionFichier:
    def __init__(self, chemin, mode):
        self.chemin = chemin
        self.mode = mode

    def __enter__(self):
        self.fichier = open(self.chemin, self.mode)
        return self.fichier

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.fichier.close()
        return False  # Ne supprime pas les exceptions

with GestionFichier("data.txt", "r") as f:
    contenu = f.read()
# f.close() est garanti, même si une exception est levée
```

### `contextlib`

Le module `contextlib` simplifie la création de context managers via `@contextmanager` :

```python
from contextlib import contextmanager

@contextmanager
def timer(label):
    import time
    debut = time.perf_counter()
    yield  # Point de suspension — le bloc `with` s'exécute ici
    duree = time.perf_counter() - debut
    print(f"{label} : {duree:.3f}s")

with timer("Calcul"):
    sum(range(10_000_000))
```

---

## 16. Type hints et annotations

### Annotations de type (Python 3.5+)

Python reste dynamiquement typé, mais les **type hints** permettent de documenter les types attendus. Ils ne sont **pas vérifiés** à l'exécution, mais des outils externes (mypy, pyright) peuvent les analyser statiquement :

```python
def saluer(nom: str, fois: int = 1) -> str:
    return (f"Bonjour {nom}!\n") * fois

# Types composés
from typing import List, Dict, Optional, Tuple, Union

def traiter(donnees: list[int]) -> dict[str, float]:  # Python 3.9+
    pass

def trouver(cle: str) -> Optional[int]:  # Équivalent à int | None
    pass

# Python 3.10+ : syntaxe union avec |
def convertir(valeur: int | str) -> float:
    pass
```

### Generics et Protocol

```python
from typing import TypeVar, Generic, Protocol

T = TypeVar('T')

class Pile(Generic[T]):
    def __init__(self) -> None:
        self._items: list[T] = []

    def empiler(self, item: T) -> None:
        self._items.append(item)

    def depiler(self) -> T:
        return self._items.pop()

# Protocol : duck typing structurel
class Dessinable(Protocol):
    def dessiner(self) -> None: ...

def afficher(obj: Dessinable) -> None:
    obj.dessiner()  # Tout objet avec dessiner() est accepté
```

---

## 17. Le protocole descripteur

### Mécanisme fondamental

Les descripteurs sont le mécanisme sous-jacent de `property`, `staticmethod`, `classmethod` et du binding de méthodes. Un descripteur est un objet qui implémente `__get__`, `__set__` et/ou `__delete__` :

```python
class Validateur:
    def __init__(self, minimum, maximum):
        self.minimum = minimum
        self.maximum = maximum

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, f'_{self.name}')

    def __set__(self, obj, value):
        if not self.minimum <= value <= self.maximum:
            raise ValueError(f"{self.name} doit être entre {self.minimum} et {self.maximum}")
        setattr(obj, f'_{self.name}', value)

class Produit:
    prix = Validateur(0, 10000)
    quantite = Validateur(0, 1000)

    def __init__(self, prix, quantite):
        self.prix = prix          # Appelle Validateur.__set__
        self.quantite = quantite
```

### Ordre de résolution des attributs

Quand on accède à `obj.attr`, Python suit cet ordre :

1. **Data descriptor** de la classe (descripteur avec `__set__` ou `__delete__`)
2. Attribut d'**instance** (`obj.__dict__`)
3. **Non-data descriptor** de la classe (descripteur avec seulement `__get__`)
4. Attribut de **classe** (`type(obj).__dict__` et ses parents via le MRO)
5. `__getattr__` s'il est défini (dernier recours)

---

## 18. Bonnes pratiques et philosophie

### Le Zen de Python

```python
import this
```

Les principes les plus importants :

- **Explicit is better than implicit** — pas de magie cachée
- **Readability counts** — le code est lu plus souvent qu'il n'est écrit
- **There should be one obvious way to do it** — une façon claire de faire
- **Errors should never pass silently** — ne jamais ignorer les exceptions
- **Simple is better than complex** — préférer la simplicité

### PEP 8 — Style guide

- Nommage : `snake_case` pour fonctions/variables, `PascalCase` pour classes, `UPPER_CASE` pour constantes
- Longueur de ligne : 79 caractères (code), 72 (docstrings)
- Imports : un par ligne, groupés (stdlib, tiers, locaux), séparés par une ligne vide
- Espaces : autour des opérateurs, après les virgules, pas à l'intérieur des parenthèses

### Principes Pythoniques

```python
# Unpacking plutôt qu'indexation
x, y, z = point

# Enumerate plutôt qu'un compteur manuel
for i, elem in enumerate(liste):
    pass

# Zip pour itérer en parallèle
for nom, age in zip(noms, ages):
    pass

# Any/all pour les vérifications
if any(x > 0 for x in nombres):
    pass

# Dictionnaire avec .get() plutôt que vérifier la clé
valeur = d.get("cle", "défaut")

# Walrus operator := (Python 3.8+)
if (n := len(data)) > 10:
    print(f"{n} éléments trouvés")
```

---

> *Ce document couvre les fondements théoriques de Python 3.x (CPython). Pour approfondir, consulter la documentation officielle sur [docs.python.org](https://docs.python.org/3/) et les PEP (Python Enhancement Proposals).*
