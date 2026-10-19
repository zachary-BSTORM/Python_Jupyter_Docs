# Formation Python : Gestion des Erreurs
## Programme complet — Journée complète

---

# PARTIE 1 — MATIN : Les bases (9h00 - 9h30)

---

## Module 1 : Comprendre les erreurs (9h00 - 9h45)

### 1.1 — Qu'est-ce qu'une erreur ?

Quand Python exécute ton code ligne par ligne, il peut rencontrer des situations imprévues. Sans gestion d'erreurs, le programme **plante immédiatement** et affiche un *traceback*.

```python
# Ce code plante :
nombre = int("abc")
print("Cette ligne ne s'exécute jamais")
```

Résultat :
```
Traceback (most recent call last):
  File "main.py", line 1, in <module>
    nombre = int("abc")
ValueError: invalid literal for int() with base 10: 'abc'
```

### 1.2 — Lire un traceback

Un traceback se lit **de bas en haut** :

```
Traceback (most recent call last):
  File "main.py", line 5, in <module>      ← 3. Le fichier et la ligne
    resultat = calcul(10, 0)               ← 2. Le code qui a échoué
  File "main.py", line 2, in calcul
    return a / b
ZeroDivisionError: division by zero        ← 1. LIRE ICI EN PREMIER
```

- **Ligne du bas** : le type d'erreur et son message
- **Lignes au-dessus** : la pile d'appels (quel fichier, quelle ligne, quelle fonction)

### 1.3 — Les deux familles d'erreurs

**Erreurs de syntaxe (SyntaxError)** — Python ne peut même pas démarrer :
```python
# Il manque les deux-points
if True:
    print("hello")
# SyntaxError: expected ':'
```

**Erreurs d'exécution (Exceptions)** — Python démarre mais plante en cours de route :
```python
# Le code est correct syntaxiquement mais échoue à l'exécution
liste = [1, 2, 3]
print(liste[10])
# IndexError: list index out of range
```

> **Important** : On ne peut PAS attraper les `SyntaxError` avec try/except car le programme ne démarre même pas.

### 1.4 — Tableau des exceptions courantes

| Exception | Description |
|---|---|
| `ValueError` | Valeur incorrecte (ex : `int("abc")`) |
| `TypeError` | Type incompatible (ex : `"a" + 1`) |
| `ZeroDivisionError` | Division par zéro |
| `IndexError` | Index hors limites |
| `KeyError` | Clé inexistante dans un dictionnaire |
| `FileNotFoundError` | Fichier introuvable |
| `AttributeError` | Attribut ou méthode inexistant (ex : `"abc".append(1)`) |
| `NameError` | Variable non définie (ex : utiliser `x` sans déclaration) |
| `ImportError` | Module introuvable lors d'un `import` |
| `ModuleNotFoundError` | Sous-classe de `ImportError`, module inexistant |
| `IOError` | Erreur générale d'entrée/sortie |
| `PermissionError` | Droits insuffisants sur un fichier |
| `IsADirectoryError` | Opération fichier tentée sur un dossier |
| `RuntimeError` | Erreur générique à l'exécution |
| `RecursionError` | Profondeur de récursion maximale dépassée |
| `StopIteration` | Plus d'éléments dans un itérateur (`next()`) |
| `OverflowError` | Résultat numérique trop grand |
| `NotImplementedError` | Méthode non implémentée (classes abstraites) |
| `UnicodeDecodeError` | Décodage de texte impossible |
| `UnicodeEncodeError` | Encodage de texte impossible |
| `ConnectionError` | Problème de connexion réseau |
| `TimeoutError` | Délai d'attente dépassé |
| `OSError` | Erreur liée au système d'exploitation |

---

### DÉMO 1 : Provoquer des erreurs volontairement

```python
# Copie ce code et exécute-le ligne par ligne en décommentant

# ValueError
# int("abc")

# TypeError
# "hello" + 5

# ZeroDivisionError
# 10 / 0

# IndexError
# liste = [1, 2, 3]
# print(liste[10])

# KeyError
# dico = {"nom": "Alice"}
# print(dico["age"])

# NameError
# print(variable_inexistante)

# AttributeError
# x = 5
# x.append(10)

# FileNotFoundError
# open("fichier_qui_nexiste_pas.txt")
```

---

### EXERCICE 1 : Identifier les erreurs (15 min)

**Consigne** : Pour chaque code ci-dessous, **sans l'exécuter**, trouve :
1. Le type d'exception levée
2. La raison de l'erreur

```python
# Code A
resultat = 10 + "5"

# Code B
notes = [15, 12, 18]
print(notes[3])

# Code C
age = int(input("Ton âge : "))  # L'utilisateur tape "vingt"

# Code D
personne = {"nom": "Bob"}
print(personne["prenom"])

# Code E
texte = "Bonjour"
texte.append(" monde")

# Code F
x = 10
y = 0
z = x % y

# Code G
import mathh

# Code H
liste = [1, 2, 3]
print(liste[1.5])
```

### CORRECTION EXERCICE 1

```
Code A → TypeError        → On ne peut pas additionner int et str
Code B → IndexError       → L'index 3 n'existe pas (indices 0, 1, 2)
Code C → ValueError       → "vingt" ne peut pas être converti en int
Code D → KeyError          → La clé "prenom" n'existe pas dans le dictionnaire
Code E → AttributeError   → Les strings n'ont pas de méthode append()
Code F → ZeroDivisionError → Le modulo par zéro est une division par zéro
Code G → ModuleNotFoundError → Le module "mathhh" n'existe pas
Code H → TypeError         → Les indices de liste doivent être des entiers, pas des floats
```

---

## Module 2 : try / except (9h30 - 10h45)

### 2.1 — La syntaxe de base

```python
try:
    # Code qui pourrait échouer
    nombre = int(input("Entre un nombre : "))
    print(f"Tu as entré : {nombre}")
except ValueError:
    # Ce bloc s'exécute SEULEMENT si ValueError survient
    print("Ce n'est pas un nombre valide !")
```

**Comment ça marche :**
1. Python exécute le bloc `try`
2. Si une erreur survient, il **saute** au bloc `except` correspondant
3. Le reste du `try` après l'erreur est **ignoré**
4. Si aucune erreur, le `except` est **ignoré**

### 2.2 — Attraper plusieurs exceptions

```python
try:
    nombre = int(input("Entre un nombre : "))
    resultat = 100 / nombre
    print(f"100 / {nombre} = {resultat}")
except ValueError:
    print("Ce n'est pas un nombre !")
except ZeroDivisionError:
    print("On ne peut pas diviser par zéro !")
```

### 2.3 — Grouper des exceptions

```python
# Même traitement pour plusieurs types d'erreurs
try:
    # ...code...
    pass
except (ValueError, TypeError):
    print("Erreur de valeur ou de type")
```

### 2.4 — Récupérer le message avec `as`

```python
try:
    nombre = int("abc")
except ValueError as e:
    print(f"Erreur attrapée : {e}")
    # Affiche : Erreur attrapée : invalid literal for int() with base 10: 'abc'
```

### 2.5 — Le piège du except trop général

```python
# ❌ MAUVAIS — cache tous les bugs
try:
    resultat = ma_fonction()
except:
    pass  # On ignore TOUT, même les vrais bugs

# ❌ ENCORE MAUVAIS — trop large
try:
    resultat = ma_fonction()
except Exception:
    print("Une erreur")  # On ne sait pas laquelle

# ✅ BON — spécifique
try:
    resultat = int(valeur)
except ValueError:
    print("La valeur n'est pas un nombre")
```

---

### DÉMO 2 : Calculatrice sécurisée

```python
# Calculatrice sécurisée

# empecher le programme de se bloquer 

# methodes : 

# getNumber()
# getOperator()
# calculAgain()
# addition - soustraction - division - multiplication
# calculatrice sera la methode principale 
# le tout sera dans une boucle pour proposer à l'utilisateur de faire un autre calcul


# récupération des valeurs
def get_number():
    while True:
        try:
            return float(input("Entre un nombre : "))
        except ValueError:
            print("Erreur : ce n'est pas un nombre valide. Réessaie.")


def get_operator():
    operateurs_valides = ["+", "-", "*", "/"]
    while True:
        operateur = input("Opérateur (+, -, *, /) : ").strip()
        if operateur in operateurs_valides:
            return operateur
        print(f"Erreur : '{operateur}' n'est pas valide. Réessaie.")


# execution du calcul
def addition(a, b):
    return a + b


def soustraction(a, b):
    return a - b


def division(a, b):
    if b == 0:
        raise ZeroDivisionError("Division par zéro impossible")
    return a / b


def multiplication(a, b):
    return a * b


# demande à l'utilisateur si il veut recommencer
def calcul_again():
    while True:
        reponse = input("\nAutre calcul ? (o/n) : ").strip().lower()
        if reponse == "o":
            return True
        elif reponse == "n":
            return False
        print("Erreur : tape 'o' pour oui ou 'n' pour non.")


# methode principale
def calculatrice():
    print("=== Calculatrice ===\n")
    again = True
    while again:
        a = get_number()
        operateur = get_operator()
        b = get_number()

        try:
            if operateur == "+":
                resultat = addition(a, b)
            elif operateur == "-":
                resultat = soustraction(a, b)
            elif operateur == "*":
                resultat = multiplication(a, b)
            elif operateur == "/":
                resultat = division(a, b)

            print(f"\n  {a} {operateur} {b} = {resultat}")

        except ZeroDivisionError as e:
            print(f"\n  Erreur : {e}")

        if not calcul_again():
            print("Au revoir !")
            again = False


calculatrice()
```

---

### EXERCICE 2 : Sécuriser un programme (20 min)

**Consigne** : Le code suivant plante dans plusieurs situations. Ajoute des `try/except` pour gérer **chaque** erreur possible et afficher un message clair à l'utilisateur.

```python
# Programme à sécuriser
def programme():
    # Étape 1 : Demander l'âge
    age = int(input("Entre ton âge : "))
    
    # Étape 2 : Accéder à une catégorie
    categories = {
        "enfant": "0-12 ans",
        "ado": "13-17 ans",
        "adulte": "18+ ans"
    }
    
    if age < 0:
        print("L'âge ne peut pas être négatif !")
        return
    elif age <= 12:
        cat = "enfant"
    elif age <= 17:
        cat = "ado"
    else:
        cat = "adulte"
    
    print(f"Tu es dans la catégorie : {categories[cat]} ({cat})")
    
    # Étape 3 : Lire un fichier de bienvenue
    fichier = open(f"bienvenue_{cat}.txt", "r")
    contenu = fichier.read()
    print(contenu)
    fichier.close()

programme()
```

### CORRECTION EXERCICE 2

```python
def programme():
    # Étape 1 : Demander l'âge (peut lever ValueError)
    try:
        age = int(input("Entre ton âge : "))
    except ValueError:
        print("Erreur : tu dois entrer un nombre entier.")
        return
    
    # Étape 2 : Accéder à une catégorie
    categories = {
        "enfant": "0-12 ans",
        "ado": "13-17 ans",
        "adulte": "18+ ans"
    }
    
    if age < 0:
        print("L'âge ne peut pas être négatif !")
        return
    elif age <= 12:
        cat = "enfant"
    elif age <= 17:
        cat = "ado"
    else:
        cat = "adulte"
    
    print(f"Tu es dans la catégorie : {categories[cat]} ({cat})")
    
    # Étape 3 : Lire un fichier de bienvenue (peut lever FileNotFoundError)
    try:
        fichier = open(f"bienvenue_{cat}.txt", "r")
        contenu = fichier.read()
        print(contenu)
        fichier.close()
    except FileNotFoundError:
        print(f"Le fichier bienvenue_{cat}.txt est introuvable.")
    except PermissionError:
        print(f"Pas la permission de lire le fichier bienvenue_{cat}.txt.")

programme()
```

---

### EXERCICE 3 : La boucle de saisie (15 min)

**Consigne** : Écris une fonction `demander_nombre(message)` qui :
- Affiche le message passé en paramètre
- Demande un nombre entier à l'utilisateur
- Si l'utilisateur entre autre chose qu'un nombre, redemande en boucle
- Retourne le nombre une fois valide

Ensuite utilise cette fonction pour demander 2 nombres et afficher leur division.

```python
# Résultat attendu :
# Entre un nombre : abc
# Erreur ! Ce n'est pas un nombre. Réessaie.
# Entre un nombre : xyz
# Erreur ! Ce n'est pas un nombre. Réessaie.
# Entre un nombre : 42
# Tu as entré : 42
```

### CORRECTION EXERCICE 3

```python
def demander_nombre(message):
    while True:
        try:
            nombre = int(input(message))
            return nombre
        except ValueError:
            print("Erreur ! Ce n'est pas un nombre entier. Réessaie.")

# Utilisation
a = demander_nombre("Entre le premier nombre : ")
b = demander_nombre("Entre le deuxième nombre : ")

try:
    resultat = a / b
    print(f"{a} / {b} = {resultat}")
except ZeroDivisionError:
    print("Impossible de diviser par zéro !")
```

---

## ☕ Pause (10h30 - 10h45)

---

## Module 3 : else, finally et les bonnes pratiques (11h00 - 12h00)

### 3.1 — Le bloc `else`

Le bloc `else` s'exécute **seulement si aucune erreur** n'est survenue dans le `try` :

```python
try:
    nombre = int(input("Entre un nombre : "))
except ValueError:
    print("Ce n'est pas un nombre !")
else:
    # Ici on est sûr que 'nombre' est un entier valide
    print(f"Le double de {nombre} est {nombre * 2}")
```

**Pourquoi ne pas simplement mettre le code dans le `try` ?**
Parce que le `else` protège le code qui **ne devrait pas** lever d'exception. Si une erreur survient dans le `else`, elle n'est pas attrapée — et c'est voulu, car ça signifie qu'il y a un vrai bug.

### 3.2 — Le bloc `finally`

Le bloc `finally` s'exécute **toujours**, qu'il y ait eu une erreur ou non :

```python
try:
    fichier = open("data.txt", "r")
    contenu = fichier.read()
except FileNotFoundError:
    print("Fichier introuvable.")
else:
    print(f"Lu : {len(contenu)} caractères")
finally:
    print("Opération terminée.")  # Toujours affiché
```

**Cas d'utilisation principal** : fermer des ressources (fichiers, connexions).

### 3.3 — Récapitulatif du flux

```
PAS D'ERREUR :     try → else → finally
ERREUR ATTRAPÉE :  try (jusqu'à l'erreur) → except → finally
ERREUR NON ATTRAPÉE : try (jusqu'à l'erreur) → finally → CRASH
```

### 3.4 — Bonne pratique : mettre le minimum dans le try

```python
# ❌ MAUVAIS — trop de code dans le try
try:
    fichier = open("config.txt")
    contenu = fichier.read()
    lignes = contenu.split("\n")
    for ligne in lignes:
        cle, valeur = ligne.split("=")
        print(f"{cle} → {valeur}")
    fichier.close()
except FileNotFoundError:
    print("Fichier introuvable")
# Problème : si le split("=") échoue, on ne le sait pas !

# ✅ BON — try ciblé
try:
    fichier = open("config.txt")
except FileNotFoundError:
    print("Fichier introuvable")
else:
    contenu = fichier.read()
    lignes = contenu.split("\n")
    for ligne in lignes:
        try:
            cle, valeur = ligne.split("=")
            print(f"{cle} → {valeur}")
        except ValueError:
            print(f"Ligne mal formatée ignorée : {ligne}")
    fichier.close()
```

---

# PARTIE 2 — APRÈS-MIDI : Approfondissement (13h30 - 17h00)

---

## Module 4 : raise — Lever ses propres erreurs (13h30 - 14h15)

### 4.1 — Pourquoi lever des erreurs ?

Parfois c'est **ton** code qui doit signaler un problème. Par exemple, si une fonction reçoit une valeur absurde :

```python
def retirer_argent(solde, montant):
    if montant < 0:
        raise ValueError("Le montant ne peut pas être négatif")
    if montant > solde:
        raise ValueError("Solde insuffisant")
    return solde - montant


```

### 4.2 — La syntaxe de raise

```python
# Lever une exception avec un message
raise ValueError("Message d'erreur explicite")

# Lever sans message (déconseillé)
raise ValueError

# Relever l'exception en cours (dans un except)
try:
    risque()
except ValueError:
    print("Log : une erreur est survenue")
    raise  # On relance l'erreur vers le code appelant
```

### 4.3 — Valider les entrées d'une fonction

```python
def creer_utilisateur(nom, age, email):
    # Validation du nom
    if not isinstance(nom, str):
        raise TypeError("Le nom doit être une chaîne de caractères")
    if len(nom.strip()) == 0:
        raise ValueError("Le nom ne peut pas être vide")
    if len(nom) > 50:
        raise ValueError("Le nom ne peut pas dépasser 50 caractères")
    
    # Validation de l'âge
    if not isinstance(age, int):
        raise TypeError("L'âge doit être un entier")
    if age < 0 or age > 150:
        raise ValueError("L'âge doit être entre 0 et 150")
    
    # Validation de l'email
    if "@" not in email or "." not in email:
        raise ValueError("L'email n'est pas valide")
    
    return {"nom": nom, "age": age, "email": email}


# Utilisation
try:
    user = creer_utilisateur("Alice", 25, "alice@mail.com")
    print(f"Utilisateur créé : {user}")
except (TypeError, ValueError) as e:
    print(f"Erreur de création : {e}")
```

### 4.4 — Relever une exception (re-raise)

Parfois tu veux **logger** une erreur mais la laisser remonter :

```python
def traiter_commande(commande):
    try:
        valider_commande(commande)
        envoyer_commande(commande)
    except ValueError as e:
        print(f"[LOG] Commande invalide : {e}")
        raise  # L'erreur remonte au code appelant
```

---

### DÉMO 4 : Système de notes

```python
def ajouter_note(bulletin, matiere, note):
    """Ajoute une note au bulletin après validation."""
    
    if not isinstance(matiere, str):
        raise TypeError("La matière doit être une chaîne de caractères")
    
    if matiere.strip() == "":
        raise ValueError("La matière ne peut pas être vide")
    
    if not isinstance(note, (int, float)):
        raise TypeError(f"La note doit être un nombre, pas {type(note).__name__}")
    
    if note < 0 or note > 20:
        raise ValueError(f"La note {note} doit être entre 0 et 20")
    
    matiere = matiere.strip().capitalize()
    
    if matiere not in bulletin:
        bulletin[matiere] = []
    
    bulletin[matiere].append(note)
    print(f"Note {note}/20 ajoutée en {matiere}")


def afficher_bulletin(bulletin):
    """Affiche le bulletin avec les moyennes."""
    if len(bulletin) == 0:
        print("Bulletin vide.")
        return
    
    print("\n=== BULLETIN ===")
    total = 0
    nb_matieres = 0
    
    for matiere, notes in bulletin.items():
        moyenne = sum(notes) / len(notes)
        total += moyenne
        nb_matieres += 1
        notes_str = ", ".join(str(n) for n in notes)
        print(f"  {matiere} : {notes_str} → Moyenne : {moyenne:.1f}/20")
    
    moyenne_generale = total / nb_matieres
    print(f"  Moyenne générale : {moyenne_generale:.1f}/20")
    print("================\n")


# --- Programme principal ---
bulletin = {}

# Tests avec des données valides
try:
    ajouter_note(bulletin, "maths", 15)
    ajouter_note(bulletin, "maths", 12)
    ajouter_note(bulletin, "français", 14)
    ajouter_note(bulletin, "python", 18)
    ajouter_note(bulletin, "python", 16)
except (TypeError, ValueError) as e:
    print(f"Erreur : {e}")

afficher_bulletin(bulletin)

# Tests avec des données invalides
print("--- Tests d'erreurs ---")

tests_invalides = [
    ("", 15),            # Matière vide
    ("maths", -5),       # Note négative
    ("maths", 25),       # Note > 20
    ("maths", "quinze"), # Note pas un nombre
    (123, 15),           # Matière pas une string
]

for matiere, note in tests_invalides:
    try:
        ajouter_note(bulletin, matiere, note)
    except (TypeError, ValueError) as e:
        print(f"  Rejeté ({matiere}, {note}) → {e}")
```

---

### EXERCICE 6 : Le distributeur automatique (25 min)

**Consigne** : Crée un distributeur automatique qui gère stock, argent et erreurs.

```python
# Règles :
# - Le distributeur a un stock de produits avec des prix
# - L'utilisateur insère de l'argent, choisit un produit
# - Utilise raise pour lever des erreurs quand :
#   → Le produit n'existe pas
#   → Le produit est en rupture de stock
#   → L'argent inséré est insuffisant
#   → Le montant inséré est négatif ou nul

# Stock initial :
# "café" : {"prix": 1.50, "stock": 5}
# "thé" : {"prix": 1.20, "stock": 3}
# "chocolat" : {"prix": 2.00, "stock": 0}
# "eau" : {"prix": 0.80, "stock": 10}
```

### CORRECTION EXERCICE 6

```python
def afficher_produits(distributeur):
    print("\n--- Produits disponibles ---")
    for nom, info in distributeur.items():
        etat = f"{info['stock']} en stock" if info["stock"] > 0 else "RUPTURE"
        print(f"  {nom} : {info['prix']:.2f}€ ({etat})")
    print()


def inserer_argent():
    """Demande à l'utilisateur d'insérer de l'argent."""
    while True:
        try:
            montant = float(input("Insérez de l'argent (€) : "))
        except ValueError:
            print("Erreur : entrez un montant valide.")
            continue
        
        if montant <= 0:
            raise ValueError("Le montant doit être positif")
        
        return montant


def acheter(distributeur, produit, argent):
    """Tente d'acheter un produit."""
    # Vérifier que le produit existe
    if produit not in distributeur:
        raise KeyError(f"Le produit '{produit}' n'existe pas")
    
    info = distributeur[produit]
    
    # Vérifier le stock
    if info["stock"] <= 0:
        raise ValueError(f"'{produit}' est en rupture de stock")
    
    # Vérifier l'argent
    if argent < info["prix"]:
        manque = info["prix"] - argent
        raise ValueError(f"Argent insuffisant. Il manque {manque:.2f}€")
    
    # Tout est bon : effectuer l'achat
    info["stock"] -= 1
    monnaie = argent - info["prix"]
    return monnaie


def distributeur_automatique():
    distributeur = {
        "café": {"prix": 1.50, "stock": 5},
        "thé": {"prix": 1.20, "stock": 3},
        "chocolat": {"prix": 2.00, "stock": 0},
        "eau": {"prix": 0.80, "stock": 10}
    }
    
    while True:
        afficher_produits(distributeur)
        
        choix = input("Quel produit ? (ou 'q' pour quitter) : ").strip().lower()
        if choix == "q":
            print("Merci et à bientôt !")
            break
        
        try:
            argent = inserer_argent()
        except ValueError as e:
            print(f"Erreur : {e}")
            continue
        
        try:
            monnaie = acheter(distributeur, choix, argent)
            print(f"Voici votre {choix} ! Monnaie rendue : {monnaie:.2f}€")
        except KeyError as e:
            print(f"Erreur : {e}")
            print(f"Remboursement : {argent:.2f}€")
        except ValueError as e:
            print(f"Erreur : {e}")
            print(f"Remboursement : {argent:.2f}€")

distributeur_automatique()
```

---

## ☕ Pause (15h00 - 15h15)

---

## Module 5 : Exceptions personnalisées (15h00 - 15h45)

### 5.1 — Créer ses propres exceptions

On crée une exception en faisant une "sous-classe" de `Exception`. Pour l'instant, sans connaître la POO, retenez juste la syntaxe :

```python
class MonErreur(Exception):
    pass
```

Le mot `pass` veut dire "cette classe ne fait rien de spécial". Elle hérite du comportement de `Exception`.

### 5.2 — Pourquoi créer ses exceptions ?

Pour pouvoir **distinguer** tes erreurs métier des erreurs Python standard :

```python
# Sans exception personnalisée — impossible de distinguer
except ValueError:
    # C'est une erreur de MON code ou de Python ? On ne sait pas.

# Avec exception personnalisée — c'est clair
except SoldeInsuffisantError:
    # C'est forcément mon erreur métier
```

### 5.3 — Organisation dans des fichiers séparés

**Fichier `errors.py`** — toutes les exceptions au même endroit :

```python
class CompteError(Exception):
    """Erreur de base pour les opérations sur les comptes."""
    pass

class SoldeInsuffisantError(CompteError):
    """Levée quand le solde est insuffisant pour un retrait."""
    pass

class MontantInvalideError(CompteError):
    """Levée quand le montant est négatif ou nul."""
    pass

class CompteBloquéError(CompteError):
    """Levée quand le compte est bloqué."""
    pass
```

**Fichier `banque.py`** — utilisation :

```python
from errors import SoldeInsuffisantError, MontantInvalideError, CompteBloquéError

def retirer(solde, montant, bloque=False):
    if bloque:
        raise CompteBloquéError("Ce compte est bloqué")
    if montant <= 0:
        raise MontantInvalideError(f"Montant invalide : {montant}")
    if montant > solde:
        raise SoldeInsuffisantError(
            f"Solde insuffisant : {solde}€ disponible, {montant}€ demandé"
        )
    return solde - montant


# Utilisation
solde = 100

try:
    solde = retirer(solde, 150)
except SoldeInsuffisantError as e:
    print(f"Refusé : {e}")
except MontantInvalideError as e:
    print(f"Montant invalide : {e}")
except CompteBloquéError as e:
    print(f"Compte bloqué : {e}")
```

### 5.4 — Attraper une famille d'exceptions

Puisque `SoldeInsuffisantError`, `MontantInvalideError` et `CompteBloquéError` héritent toutes de `CompteError`, on peut attraper la famille entière :

```python
from errors import CompteError

try:
    retirer(solde, montant)
except CompteError as e:
    # Attrape TOUTES les erreurs liées aux comptes
    print(f"Erreur de compte : {e}")
```

---

### DÉMO 5 : Système de réservation

**Fichier `errors.py`** :

```python
class ReservationError(Exception):
    """Erreur de base pour les réservations."""
    pass

class SalleInexistanteError(ReservationError):
    """La salle demandée n'existe pas."""
    pass

class CreneauOccupéError(ReservationError):
    """Le créneau est déjà réservé."""
    pass

class HeureInvalideError(ReservationError):
    """L'heure de réservation est invalide."""
    pass
```

**Fichier `reservation.py`** :

```python
from errors import SalleInexistanteError, CreneauOccupéError, HeureInvalideError

# Base de données simple
salles = {
    "A101": {},
    "A102": {},
    "B201": {},
}

def reserver(salle, heure, personne):
    """Réserve une salle à une heure donnée."""
    if salle not in salles:
        raise SalleInexistanteError(f"La salle '{salle}' n'existe pas")
    
    if not isinstance(heure, int) or heure < 8 or heure > 18:
        raise HeureInvalideError(f"L'heure doit être entre 8h et 18h (reçu : {heure})")
    
    if heure in salles[salle]:
        occupant = salles[salle][heure]
        raise CreneauOccupéError(
            f"La salle {salle} est déjà réservée à {heure}h par {occupant}"
        )
    
    salles[salle][heure] = personne
    print(f"Réservé : {salle} à {heure}h pour {personne}")


def afficher_planning(salle):
    """Affiche le planning d'une salle."""
    if salle not in salles:
        raise SalleInexistanteError(f"La salle '{salle}' n'existe pas")
    
    print(f"\n--- Planning {salle} ---")
    reservations = salles[salle]
    if len(reservations) == 0:
        print("  Aucune réservation")
    else:
        for heure in sorted(reservations):
            print(f"  {heure}h : {reservations[heure]}")
    print()


# --- Tests ---
print("=== Réservations valides ===")
try:
    reserver("A101", 9, "Alice")
    reserver("A101", 14, "Bob")
    reserver("B201", 9, "Charlie")
except ReservationError as e:
    print(f"Erreur : {e}")

afficher_planning("A101")

print("=== Tests d'erreurs ===")

tests = [
    ("C999", 10, "David"),    # Salle inexistante
    ("A101", 9, "Eve"),       # Créneau occupé
    ("A101", 22, "Frank"),    # Heure invalide
    ("A101", -1, "Grace"),    # Heure invalide
]

for salle, heure, personne in tests:
    try:
        reserver(salle, heure, personne)
    except SalleInexistanteError as e:
        print(f"  [SalleInexistante] {e}")
    except CreneauOccupéError as e:
        print(f"  [CreneauOccupé] {e}")
    except HeureInvalideError as e:
        print(f"  [HeureInvalide] {e}")
```

---

### EXERCICE 7 : Le système de login (30 min)

**Consigne** : Crée un système de login avec des exceptions personnalisées.

Crée d'abord un fichier `errors.py` avec :
- `LoginError` (erreur de base)
- `UtilisateurInconnuError`
- `MotDePasseIncorrectError`
- `CompteBloqueError`
- `MotDePasseTropCourtError`

Puis un fichier `login.py` avec :
- Une "base de données" (dictionnaire) d'utilisateurs
- Une fonction `inscrire(pseudo, mot_de_passe)` qui valide le pseudo (pas vide, pas déjà pris) et le mot de passe (minimum 6 caractères)
- Une fonction `connecter(pseudo, mot_de_passe)` qui vérifie les identifiants et bloque le compte après 3 tentatives échouées
- Un programme principal qui propose un menu : Inscription / Connexion / Quitter

### CORRECTION EXERCICE 7

**Fichier `errors.py`** :

```python
class LoginError(Exception):
    """Erreur de base pour le système de login."""
    pass

class UtilisateurInconnuError(LoginError):
    """L'utilisateur n'existe pas."""
    pass

class MotDePasseIncorrectError(LoginError):
    """Le mot de passe est incorrect."""
    pass

class CompteBloqueError(LoginError):
    """Le compte est bloqué après trop de tentatives."""
    pass

class MotDePasseTropCourtError(LoginError):
    """Le mot de passe est trop court."""
    pass
```

**Fichier `login.py`** :

```python
from errors import (
    UtilisateurInconnuError,
    MotDePasseIncorrectError,
    CompteBloqueError,
    MotDePasseTropCourtError,
    LoginError
)

# Base de données : {pseudo: {"mdp": ..., "tentatives": ..., "bloque": ...}}
utilisateurs = {}


def inscrire(pseudo, mot_de_passe):
    """Inscrit un nouvel utilisateur."""
    if pseudo.strip() == "":
        raise ValueError("Le pseudo ne peut pas être vide")
    
    if pseudo in utilisateurs:
        raise ValueError(f"Le pseudo '{pseudo}' est déjà pris")
    
    if len(mot_de_passe) < 6:
        raise MotDePasseTropCourtError(
            f"Le mot de passe doit contenir au moins 6 caractères ({len(mot_de_passe)} fournis)"
        )
    
    utilisateurs[pseudo] = {
        "mdp": mot_de_passe,
        "tentatives": 0,
        "bloque": False
    }
    print(f"Inscription réussie ! Bienvenue {pseudo}.")


def connecter(pseudo, mot_de_passe):
    """Connecte un utilisateur existant."""
    if pseudo not in utilisateurs:
        raise UtilisateurInconnuError(f"L'utilisateur '{pseudo}' n'existe pas")
    
    user = utilisateurs[pseudo]
    
    if user["bloque"]:
        raise CompteBloqueError(
            f"Le compte '{pseudo}' est bloqué (trop de tentatives échouées)"
        )
    
    if mot_de_passe != user["mdp"]:
        user["tentatives"] += 1
        restantes = 3 - user["tentatives"]
        
        if user["tentatives"] >= 3:
            user["bloque"] = True
            raise CompteBloqueError(
                f"Le compte '{pseudo}' vient d'être bloqué après 3 tentatives"
            )
        
        raise MotDePasseIncorrectError(
            f"Mot de passe incorrect ({restantes} tentative(s) restante(s))"
        )
    
    # Connexion réussie : réinitialiser les tentatives
    user["tentatives"] = 0
    print(f"Connexion réussie ! Bonjour {pseudo}.")


# --- Programme principal ---
def menu():
    while True:
        print("\n=== Système de Login ===")
        print("1. Inscription")
        print("2. Connexion")
        print("3. Quitter")
        
        choix = input("Choix : ").strip()
        
        if choix == "1":
            pseudo = input("Pseudo : ").strip()
            mdp = input("Mot de passe : ").strip()
            try:
                inscrire(pseudo, mdp)
            except MotDePasseTropCourtError as e:
                print(f"Erreur : {e}")
            except ValueError as e:
                print(f"Erreur : {e}")
        
        elif choix == "2":
            pseudo = input("Pseudo : ").strip()
            mdp = input("Mot de passe : ").strip()
            try:
                connecter(pseudo, mdp)
            except UtilisateurInconnuError as e:
                print(f"Erreur : {e}")
            except MotDePasseIncorrectError as e:
                print(f"Erreur : {e}")
            except CompteBloqueError as e:
                print(f"Erreur : {e}")
        
        elif choix == "3":
            print("Au revoir !")
            break
        
        else:
            print("Choix invalide (1, 2 ou 3).")

menu()
```

---

## Module 6 : Projet final (15h45 - 17h00)

### EXERCICE 8 — Projet : Mini banque complète (1h15)

**Consigne** : Crée un mini système bancaire complet.

**Fichier `errors.py`** : Crée les exceptions suivantes :
- `BanqueError` (base)
- `CompteInexistantError`
- `SoldeInsuffisantError`
- `MontantInvalideError`
- `CompteDejaExistantError`
- `VirementInterditError`

**Fichier `banque.py`** : Crée les fonctions suivantes :
- `creer_compte(comptes, nom, solde_initial)` — crée un compte avec un solde initial (doit être >= 0, le nom ne doit pas déjà exister)
- `deposer(comptes, nom, montant)` — dépose de l'argent (montant doit être > 0)
- `retirer(comptes, nom, montant)` — retire de l'argent (vérifie le solde)
- `virement(comptes, source, destination, montant)` — transfère de l'argent entre deux comptes (interdit de se virer à soi-même)
- `consulter_solde(comptes, nom)` — affiche le solde
- `historique(comptes, nom)` — affiche l'historique des opérations

**Structure des comptes** :
```python
comptes = {
    "Alice": {
        "solde": 1000,
        "historique": ["Création du compte : +1000€"]
    }
}
```

**Programme principal** : menu interactif en boucle avec toutes les opérations.

### CORRECTION EXERCICE 8

**Fichier `errors.py`** :

```python
class BanqueError(Exception):
    """Erreur de base pour la banque."""
    pass

class CompteInexistantError(BanqueError):
    """Le compte demandé n'existe pas."""
    pass

class SoldeInsuffisantError(BanqueError):
    """Le solde est insuffisant."""
    pass

class MontantInvalideError(BanqueError):
    """Le montant est invalide (négatif ou nul)."""
    pass

class CompteDejaExistantError(BanqueError):
    """Un compte avec ce nom existe déjà."""
    pass

class VirementInterditError(BanqueError):
    """Le virement n'est pas autorisé."""
    pass
```

**Fichier `banque.py`** :

```python
from errors import (
    CompteInexistantError,
    SoldeInsuffisantError,
    MontantInvalideError,
    CompteDejaExistantError,
    VirementInterditError,
    BanqueError
)


def creer_compte(comptes, nom, solde_initial):
    if nom.strip() == "":
        raise ValueError("Le nom ne peut pas être vide")
    if nom in comptes:
        raise CompteDejaExistantError(f"Le compte '{nom}' existe déjà")
    if not isinstance(solde_initial, (int, float)):
        raise TypeError("Le solde initial doit être un nombre")
    if solde_initial < 0:
        raise MontantInvalideError("Le solde initial ne peut pas être négatif")
    
    comptes[nom] = {
        "solde": solde_initial,
        "historique": [f"Création du compte : +{solde_initial:.2f}€"]
    }
    print(f"Compte '{nom}' créé avec un solde de {solde_initial:.2f}€")


def verifier_compte(comptes, nom):
    """Vérifie qu'un compte existe, sinon lève une erreur."""
    if nom not in comptes:
        raise CompteInexistantError(f"Le compte '{nom}' n'existe pas")


def verifier_montant(montant):
    """Vérifie qu'un montant est valide."""
    try:
        montant = float(montant)
    except (ValueError, TypeError):
        raise MontantInvalideError(f"'{montant}' n'est pas un montant valide")
    if montant <= 0:
        raise MontantInvalideError("Le montant doit être supérieur à 0")
    return montant


def deposer(comptes, nom, montant):
    verifier_compte(comptes, nom)
    montant = verifier_montant(montant)
    
    comptes[nom]["solde"] += montant
    comptes[nom]["historique"].append(f"Dépôt : +{montant:.2f}€")
    print(f"Dépôt de {montant:.2f}€ sur le compte de {nom}")
    print(f"Nouveau solde : {comptes[nom]['solde']:.2f}€")


def retirer(comptes, nom, montant):
    verifier_compte(comptes, nom)
    montant = verifier_montant(montant)
    
    if montant > comptes[nom]["solde"]:
        raise SoldeInsuffisantError(
            f"Solde insuffisant ({comptes[nom]['solde']:.2f}€ disponible, "
            f"{montant:.2f}€ demandé)"
        )
    
    comptes[nom]["solde"] -= montant
    comptes[nom]["historique"].append(f"Retrait : -{montant:.2f}€")
    print(f"Retrait de {montant:.2f}€ du compte de {nom}")
    print(f"Nouveau solde : {comptes[nom]['solde']:.2f}€")


def virement(comptes, source, destination, montant):
    if source == destination:
        raise VirementInterditError("Impossible de faire un virement vers son propre compte")
    
    verifier_compte(comptes, source)
    verifier_compte(comptes, destination)
    montant = verifier_montant(montant)
    
    if montant > comptes[source]["solde"]:
        raise SoldeInsuffisantError(
            f"Solde insuffisant sur le compte de {source} "
            f"({comptes[source]['solde']:.2f}€ disponible)"
        )
    
    comptes[source]["solde"] -= montant
    comptes[destination]["solde"] += montant
    
    comptes[source]["historique"].append(f"Virement envoyé à {destination} : -{montant:.2f}€")
    comptes[destination]["historique"].append(f"Virement reçu de {source} : +{montant:.2f}€")
    
    print(f"Virement de {montant:.2f}€ de {source} vers {destination} effectué")


def consulter_solde(comptes, nom):
    verifier_compte(comptes, nom)
    print(f"Solde de {nom} : {comptes[nom]['solde']:.2f}€")


def afficher_historique(comptes, nom):
    verifier_compte(comptes, nom)
    print(f"\n--- Historique de {nom} ---")
    for operation in comptes[nom]["historique"]:
        print(f"  • {operation}")
    print(f"  Solde actuel : {comptes[nom]['solde']:.2f}€")
    print()


# --- Programme principal ---
def menu():
    comptes = {}
    
    while True:
        print("\n====== MINI BANQUE ======")
        print("1. Créer un compte")
        print("2. Déposer de l'argent")
        print("3. Retirer de l'argent")
        print("4. Faire un virement")
        print("5. Consulter le solde")
        print("6. Voir l'historique")
        print("7. Liste des comptes")
        print("8. Quitter")
        
        choix = input("Choix : ").strip()
        
        try:
            if choix == "1":
                nom = input("Nom du titulaire : ").strip()
                try:
                    solde = float(input("Solde initial : "))
                except ValueError:
                    print("Erreur : le solde doit être un nombre.")
                    continue
                creer_compte(comptes, nom, solde)
            
            elif choix == "2":
                nom = input("Nom du titulaire : ").strip()
                montant = input("Montant à déposer : ").strip()
                deposer(comptes, nom, montant)
            
            elif choix == "3":
                nom = input("Nom du titulaire : ").strip()
                montant = input("Montant à retirer : ").strip()
                retirer(comptes, nom, montant)
            
            elif choix == "4":
                source = input("Compte source : ").strip()
                destination = input("Compte destination : ").strip()
                montant = input("Montant : ").strip()
                virement(comptes, source, destination, montant)
            
            elif choix == "5":
                nom = input("Nom du titulaire : ").strip()
                consulter_solde(comptes, nom)
            
            elif choix == "6":
                nom = input("Nom du titulaire : ").strip()
                afficher_historique(comptes, nom)
            
            elif choix == "7":
                if len(comptes) == 0:
                    print("Aucun compte créé.")
                else:
                    print("\n--- Comptes ---")
                    for nom, info in comptes.items():
                        print(f"  {nom} : {info['solde']:.2f}€")
            
            elif choix == "8":
                print("Merci d'avoir utilisé Mini Banque !")
                break
            
            else:
                print("Choix invalide (1-8).")
        
        except BanqueError as e:
            print(f"Erreur : {e}")
        except (ValueError, TypeError) as e:
            print(f"Erreur : {e}")

menu()
```

---

# ANNEXE — Résumé de la journée

## Fiche mémo

```python
# === 1. TRY / EXCEPT de base ===
try:
    code_risqué()
except TypeError:
    traiter_erreur()

# === 2. PLUSIEURS EXCEPTIONS ===
try:
    code_risqué()
except ValueError:
    print("Valeur invalide")
except (TypeError, KeyError):
    print("Autre erreur")

# === 3. RÉCUPÉRER LE MESSAGE ===
except ValueError as e:
    print(f"Détail : {e}")

# === 4. ELSE + FINALLY ===
try:
    resultat = calcul()
except ValueError:
    print("Erreur")
else:
    print("Succès !")      # Si pas d'erreur
finally:
    print("Toujours")      # Dans tous les cas

# === 5. LEVER UNE ERREUR ===
raise ValueError("Message explicite")

# === 6. EXCEPTION PERSONNALISÉE ===
class MonErreur(Exception):
    pass

raise MonErreur("Quelque chose a mal tourné")

# === 7. BOUCLE DE SAISIE SÉCURISÉE ===
while True:
    try:
        valeur = int(input("Nombre : "))
        break
    except ValueError:
        print("Réessaie.")
```

## Les règles d'or

1. **Sois spécifique** : `except ValueError` plutôt que `except Exception`
2. **Minimum dans le try** : seulement les lignes risquées
3. **Jamais `except: pass`** : ne cache jamais les erreurs
4. **`finally` pour le nettoyage** : fermer fichiers, connexions
5. **`raise` pour signaler** : tes fonctions doivent refuser les données invalides
6. **Exceptions personnalisées** : pour séparer tes erreurs métier des erreurs Python
7. **Messages clairs** : explique POURQUOI l'erreur survient