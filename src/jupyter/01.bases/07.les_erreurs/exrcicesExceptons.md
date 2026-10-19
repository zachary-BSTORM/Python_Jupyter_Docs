# Exercice 1 : La liste de courses sécurisée
Consigne : Crée un programme qui gère une liste de courses avec un menu en boucle :

Ajouter un article (nom + quantité)
Afficher la liste
Supprimer un article
Quitter

Erreurs à gérer :

Quantité invalide (pas un nombre, négative ou nulle)
Nom d'article vide
Supprimer un article qui n'existe pas

```python
# Stocke les articles comme ça :
courses = {"pain": 2, "lait": 1, "oeufs": 6}
```
Fonctions à créer :


get_quantite() → demande une quantité valide en boucle
ajouter(courses) → ajoute un article
afficher(courses) → affiche la liste
supprimer(courses) → supprime un article


 ----

# Exercice 2 : 
# 5 Exercices Progressifs — Bases + Exceptions


# EXERCICE 1 : La liste de courses sécurisée

## Consigne


Crée un programme qui gère une liste de courses avec un menu en boucle :
1. Ajouter un article (nom + quantité)
2. Afficher la liste
3. Supprimer un article
4. Quitter

**Erreurs à gérer :**
- Quantité invalide (pas un nombre, négative ou nulle)
- Nom d'article vide
- Supprimer un article qui n'existe pas

**Structure :** `courses = {"pain": 2, "lait": 1}`

---

## Correction

```python
def get_quantite():
    """Demande une quantité valide en boucle."""
    while True:
        try:
            quantite = int(input("Quantité : "))
        except ValueError:
            # L'utilisateur a tapé autre chose qu'un nombre
            print("Erreur : entre un nombre entier.")
            continue

        # On vérifie que la quantité est positive
        if quantite <= 0:
            print("Erreur : la quantité doit être supérieure à 0.")
            continue

        return quantite


def ajouter(courses):
    """Ajoute un article à la liste."""
    nom = input("Nom de l'article : ").strip().lower()

    # On vérifie que le nom n'est pas vide
    if nom == "":
        print("Erreur : le nom ne peut pas être vide.")
        return

    quantite = get_quantite()

    # Si l'article existe déjà, on additionne les quantités
    if nom in courses:
        courses[nom] += quantite
        print(f"'{nom}' mis à jour → quantité : {courses[nom]}")
    else:
        courses[nom] = quantite
        print(f"'{nom}' ajouté (x{quantite})")


def afficher(courses):
    """Affiche la liste de courses."""
    if len(courses) == 0:
        print("La liste est vide.")
        return

    print("\n--- Liste de courses ---")
    for article, quantite in courses.items():
        print(f"  - {article} : {quantite}")
    print()


def supprimer(courses):
    """Supprime un article de la liste."""
    nom = input("Article à supprimer : ").strip().lower()

    # On essaie de supprimer, KeyError si ça n'existe pas
    try:
        del courses[nom]
        print(f"'{nom}' supprimé.")
    except KeyError:
        print(f"Erreur : '{nom}' n'est pas dans la liste.")


# --- Programme principal ---
def main():
    courses = {}

    while True:
        print("\n=== LISTE DE COURSES ===")
        print("1. Ajouter")
        print("2. Afficher")
        print("3. Supprimer")
        print("4. Quitter")

        choix = input("Choix : ").strip()

        if choix == "1":
            ajouter(courses)
        elif choix == "2":
            afficher(courses)
        elif choix == "3":
            supprimer(courses)
        elif choix == "4":
            print("Au revoir !")
            break
        else:
            print("Erreur : choisis entre 1 et 4.")

main()
```

---
---

# EXERCICE 2 : Le carnet de notes

## Consigne

Crée un programme qui gère les notes d'élèves :
1. Ajouter un élève
2. Ajouter une note à un élève (entre 0 et 20)
3. Afficher la moyenne d'un élève
4. Afficher le classement (tous les élèves triés par moyenne)
5. Quitter

**Erreurs à gérer :**
- Note invalide (pas un nombre, hors de 0-20)
- Élève inexistant quand on cherche ou ajoute une note
- Calcul de moyenne quand un élève n'a aucune note
- Nom d'élève vide

**Structure :** `eleves = {"Alice": [15, 12, 18], "Bob": [10, 8]}`

---

## Correction

```python
def get_note():
    """Demande une note valide (entre 0 et 20) en boucle."""
    while True:
        try:
            note = float(input("Note (0-20) : "))
        except ValueError:
            print("Erreur : ce n'est pas un nombre valide.")
            continue

        # On vérifie que la note est dans les limites
        if note < 0 or note > 20:
            print("Erreur : la note doit être entre 0 et 20.")
            continue

        return note


def get_nom(message):
    """Demande un nom non vide."""
    while True:
        nom = input(message).strip().capitalize()

        if nom == "":
            print("Erreur : le nom ne peut pas être vide.")
            continue

        return nom


def ajouter_eleve(eleves):
    """Ajoute un nouvel élève au carnet."""
    nom = get_nom("Nom de l'élève : ")

    # On vérifie si l'élève existe déjà
    if nom in eleves:
        print(f"Erreur : '{nom}' existe déjà.")
        return

    # On crée l'élève avec une liste de notes vide
    eleves[nom] = []
    print(f"Élève '{nom}' ajouté.")


def ajouter_note(eleves):
    """Ajoute une note à un élève existant."""
    nom = get_nom("Nom de l'élève : ")

    # On vérifie que l'élève existe
    try:
        notes = eleves[nom]
    except KeyError:
        print(f"Erreur : l'élève '{nom}' n'existe pas.")
        return

    note = get_note()

    # On ajoute la note à la liste de l'élève
    notes.append(note)
    print(f"Note {note}/20 ajoutée à {nom}.")


def afficher_moyenne(eleves):
    """Affiche la moyenne d'un élève."""
    nom = get_nom("Nom de l'élève : ")

    # On vérifie que l'élève existe
    try:
        notes = eleves[nom]
    except KeyError:
        print(f"Erreur : l'élève '{nom}' n'existe pas.")
        return

    # On vérifie qu'il a au moins une note
    if len(notes) == 0:
        print(f"{nom} n'a aucune note pour le moment.")
        return

    # On calcule et affiche la moyenne
    moyenne = sum(notes) / len(notes)
    notes_str = ", ".join(str(n) for n in notes)
    print(f"{nom} : {notes_str} → Moyenne : {moyenne:.1f}/20")


def afficher_classement(eleves):
    """Affiche tous les élèves triés par moyenne décroissante."""
    if len(eleves) == 0:
        print("Aucun élève enregistré.")
        return

    # On calcule la moyenne de chaque élève
    classement = []
    for nom, notes in eleves.items():
        if len(notes) > 0:
            moyenne = sum(notes) / len(notes)
        else:
            moyenne = 0
        classement.append((nom, moyenne, len(notes)))

    # On trie par moyenne décroissante
    classement.sort(key=lambda x: x[1], reverse=True)

    # Affichage
    print("\n--- CLASSEMENT ---")
    for i, (nom, moyenne, nb_notes) in enumerate(classement, 1):
        print(f"  {i}. {nom} : {moyenne:.1f}/20 ({nb_notes} note(s))")
    print()


# --- Programme principal ---
def main():
    eleves = {}

    while True:
        print("\n=== CARNET DE NOTES ===")
        print("1. Ajouter un élève")
        print("2. Ajouter une note")
        print("3. Moyenne d'un élève")
        print("4. Classement")
        print("5. Quitter")

        choix = input("Choix : ").strip()

        if choix == "1":
            ajouter_eleve(eleves)
        elif choix == "2":
            ajouter_note(eleves)
        elif choix == "3":
            afficher_moyenne(eleves)
        elif choix == "4":
            afficher_classement(eleves)
        elif choix == "5":
            print("Au revoir !")
            break
        else:
            print("Erreur : choisis entre 1 et 5.")

main()
```

---
---

# EXERCICE 3 : Le jeu du nombre mystère (avec raise)

## Consigne

# Jeu Du Nombre

# recuperation de la valeur utilisateur
# generation aléatoire du nombre : randint

# Verifier que l'utilisateur donne une valeur correct ( entre 1 et 100 )

#si plus grand : affiche un message 
#si plus petit : affiche un message 
#si correct : affiche un message avec le nombre de coups

# on demande à l'utilisateur en combien de coups il veut essayer

# recuperation nombre (mystere)
# recuperation nombre (nbre de coups)
# generation random
# verification
# affichage du resultat : victoire ou défaite ( et le nombre d'essai )
# utilisation d'une boucle et demander à l'utilisateur si il veut recommencer

# programme principale : mystery_number()

---

## Correction

```python
from random import randint
def get_life():
    while True:
        try:
            return int(input("Combien d'essais voulez-vous ? "))
        except Exception as e:
            print("Veuillez entrer une valeur numérique !")


def get_random():
    return randint(1, 100)


def get_user_choice():
    while True:
        try:
            user_number = int(input("Entrez un nombre entre 1 et 100 : "))
            if user_number < 101 and user_number > 0:
                return user_number
            else:
                print("La valeur doit être entre 1 et 100 !")
        except Exception as e:
            print("Veuillez entrer une valeur numérique !")


def verification(mystery, user_number):
    if mystery == user_number:
        return True
    elif mystery > user_number:
        print("Le nombre est plus grand")
    else:
        print("Le nombre est plus petit")
    return False


def show_score(score, win):
    if win == True:
        print(f"Bravo ! Vous avez réussi en {score} coup(s) !")
    else:
        print(f"Vous avez perdu avec {score} essai(s) !")


def play_again():
    while True:
        response = input("Voulez-vous recommencer ? o / n : ").strip().lower()
        if response == "o":
            return True
        elif response == "n":
            return False
        else:
            print("Veuillez entrer o pour oui et n pour non !")


def mystery_number():
    print("=== Le jeu du nombre mystère ===")
    again = True

    while again == True:

        nbTry = get_life()
        score = 0
        mystery = get_random()
        victory = False

        while nbTry > 0:
            user_choice = get_user_choice()
            victory = verification(mystery, user_choice)
            nbTry -= 1
            score += 1

            # Si le joueur a trouvé, on sort de la boucle tout de suite
            if victory:
                break

        # On affiche le score après la boucle (gagné ou perdu)
        show_score(score, victory)

        # Si perdu, on révèle le nombre
        if not victory:
            print(f"Le nombre mystère était : {mystery}")

        again = play_again()

    print("Merci d'avoir joué !")


mystery_number()
```

---
---

# EXERCICE 4 : Le mini carnet d'adresses avec fichier

## Consigne

Crée un programme qui gère un carnet d'adresses **sauvegardé dans un fichier**.

**Fonctionnalités :**
1. Au lancement, charger les contacts depuis `contacts.txt` (un contact par ligne : `nom,telephone,email`)
2. Ajouter un contact (valider le format email avec `@` et `.`)
3. Chercher un contact par nom
4. Supprimer un contact
5. Sauvegarder et quitter (écrire dans le fichier)

**Erreurs à gérer :**
- Fichier inexistant au premier lancement → créer une liste vide
- Ligne mal formatée dans le fichier → l'ignorer avec un message
- Email invalide (pas de `@` ou pas de `.`) → redemander
- Téléphone invalide (pas que des chiffres) → redemander
- Contact inexistant → message clair

**Structure :** liste de dictionnaires
```python
contacts = [
    {"nom": "Alice", "telephone": "0612345678", "email": "alice@mail.com"}
]
```

---

## Correction

```python
def charger_contacts(nom_fichier):
    """
    Charge les contacts depuis un fichier CSV.
    Retourne une liste de dictionnaires.
    Si le fichier n'existe pas, retourne une liste vide.
    """
    contacts = []

    try:
        fichier = open(nom_fichier, "r")
    except FileNotFoundError:
        # Premier lancement : le fichier n'existe pas encore
        print("Aucun fichier trouvé, carnet vide créé.")
        return contacts

    try:
        lignes = fichier.readlines()

        for i, ligne in enumerate(lignes, 1):
            ligne = ligne.strip()

            # On ignore les lignes vides
            if ligne == "":
                continue

            # On découpe la ligne par les virgules
            try:
                nom, telephone, email = ligne.split(",")
                contacts.append({
                    "nom": nom.strip(),
                    "telephone": telephone.strip(),
                    "email": email.strip()
                })
            except ValueError:
                # La ligne n'a pas le bon nombre de champs
                print(f"Ligne {i} ignorée (format invalide) : {ligne}")
    finally:
        # On ferme toujours le fichier, même en cas d'erreur
        fichier.close()

    print(f"{len(contacts)} contact(s) chargé(s).")
    return contacts


def sauvegarder_contacts(contacts, nom_fichier):
    """Sauvegarde tous les contacts dans le fichier."""
    try:
        fichier = open(nom_fichier, "w")
        for c in contacts:
            fichier.write(f"{c['nom']},{c['telephone']},{c['email']}\n")
        fichier.close()
        print(f"{len(contacts)} contact(s) sauvegardé(s).")
    except PermissionError:
        print("Erreur : impossible d'écrire dans le fichier.")


def get_email():
    """Demande un email valide en boucle."""
    while True:
        email = input("Email : ").strip()

        if email == "":
            print("Erreur : l'email ne peut pas être vide.")
            continue

        # Validation basique : il faut un @ et un .
        if "@" not in email or "." not in email:
            print("Erreur : email invalide (il faut un @ et un .)")
            continue

        return email


def get_telephone():
    """Demande un numéro de téléphone valide en boucle."""
    while True:
        telephone = input("Téléphone : ").strip()

        if telephone == "":
            print("Erreur : le téléphone ne peut pas être vide.")
            continue

        # On vérifie que ça ne contient que des chiffres
        if not telephone.isdigit():
            print("Erreur : le téléphone ne doit contenir que des chiffres.")
            continue

        return telephone


def trouver_contact(contacts, nom):
    """
    Cherche un contact par nom dans la liste.
    Retourne l'index du contact ou -1 si non trouvé.
    """
    for i, contact in enumerate(contacts):
        if contact["nom"].lower() == nom.lower():
            return i
    return -1


def ajouter_contact(contacts):
    """Ajoute un nouveau contact."""
    nom = input("Nom : ").strip().capitalize()

    if nom == "":
        print("Erreur : le nom ne peut pas être vide.")
        return

    # On vérifie que le contact n'existe pas déjà
    if trouver_contact(contacts, nom) != -1:
        print(f"Erreur : '{nom}' existe déjà.")
        return

    telephone = get_telephone()
    email = get_email()

    # On ajoute le contact à la liste
    contacts.append({"nom": nom, "telephone": telephone, "email": email})
    print(f"Contact '{nom}' ajouté !")


def chercher_contact(contacts):
    """Cherche et affiche un contact."""
    nom = input("Nom à chercher : ").strip()

    index = trouver_contact(contacts, nom)

    if index == -1:
        print(f"Erreur : aucun contact '{nom}' trouvé.")
        return

    # On affiche le contact trouvé
    c = contacts[index]
    print(f"\n  Nom       : {c['nom']}")
    print(f"  Téléphone : {c['telephone']}")
    print(f"  Email     : {c['email']}")


def supprimer_contact(contacts):
    """Supprime un contact après confirmation."""
    nom = input("Nom à supprimer : ").strip()

    index = trouver_contact(contacts, nom)

    if index == -1:
        print(f"Erreur : aucun contact '{nom}' trouvé.")
        return

    # On demande confirmation
    confirmer = input(f"Supprimer '{contacts[index]['nom']}' ? (o/n) : ").strip().lower()
    if confirmer == "o":
        supprime = contacts.pop(index)
        print(f"Contact '{supprime['nom']}' supprimé.")
    else:
        print("Annulé.")


def afficher_tous(contacts):
    """Affiche tous les contacts."""
    if len(contacts) == 0:
        print("Carnet vide.")
        return

    print(f"\n--- {len(contacts)} CONTACT(S) ---")
    for c in contacts:
        print(f"  {c['nom']} | {c['telephone']} | {c['email']}")
    print()


# --- Programme principal ---
def main():
    nom_fichier = "contacts.txt"

    # On charge les contacts au démarrage
    contacts = charger_contacts(nom_fichier)

    while True:
        print("\n=== CARNET D'ADRESSES ===")
        print("1. Ajouter un contact")
        print("2. Chercher un contact")
        print("3. Supprimer un contact")
        print("4. Afficher tous les contacts")
        print("5. Sauvegarder et quitter")

        choix = input("Choix : ").strip()

        if choix == "1":
            ajouter_contact(contacts)
        elif choix == "2":
            chercher_contact(contacts)
        elif choix == "3":
            supprimer_contact(contacts)
        elif choix == "4":
            afficher_tous(contacts)
        elif choix == "5":
            sauvegarder_contacts(contacts, nom_fichier)
            print("Au revoir !")
            break
        else:
            print("Erreur : choisis entre 1 et 5.")

main()
```

---
---

# EXERCICE 5 : La mini banque (avec exceptions personnalisées)

## Consigne

Crée un mini système bancaire avec des **exceptions personnalisées**.

**Fichier `errors.py` à créer :**
- `BanqueError` (base)
- `SoldeInsuffisantError`
- `MontantInvalideError`
- `CompteInexistantError`

**Fonctionnalités (fichier `banque.py`) :**
1. Créer un compte (nom + solde initial)
2. Déposer de l'argent
3. Retirer de l'argent
4. Virement entre deux comptes
5. Afficher le solde + historique
6. Quitter

**Erreurs à gérer :**
- Montant négatif ou nul → `MontantInvalideError`
- Retrait supérieur au solde → `SoldeInsuffisantError`
- Compte inexistant → `CompteInexistantError`
- Virement vers soi-même → `BanqueError`

**Structure :**
```python
comptes = {
    "Alice": {"solde": 500, "historique": ["Création : +500€"]}
}
```

---

## Correction

**Fichier `errors.py` :**

```python
# Chaque exception hérite de BanqueError
# Ça permet d'attraper toutes les erreurs bancaires d'un coup si besoin

class BanqueError(Exception):
    """Erreur de base pour toutes les opérations bancaires."""
    pass

class SoldeInsuffisantError(BanqueError):
    """Le solde du compte est insuffisant pour cette opération."""
    pass

class MontantInvalideError(BanqueError):
    """Le montant fourni est invalide (négatif, nul ou pas un nombre)."""
    pass

class CompteInexistantError(BanqueError):
    """Le compte demandé n'existe pas."""
    pass
```

**Fichier `banque.py` :**

```python
from errors import (
    BanqueError,
    SoldeInsuffisantError,
    MontantInvalideError,
    CompteInexistantError
)


def get_montant(message):
    """
    Demande un montant valide en boucle.
    Lève MontantInvalideError si le montant est <= 0.
    """
    while True:
        try:
            montant = float(input(message))
        except ValueError:
            print("Erreur : entre un nombre valide.")
            continue

        # On lève notre exception personnalisée si le montant est invalide
        if montant <= 0:
            raise MontantInvalideError("Le montant doit être supérieur à 0")

        return montant


def verifier_compte(comptes, nom):
    """Vérifie qu'un compte existe, sinon lève CompteInexistantError."""
    if nom not in comptes:
        raise CompteInexistantError(f"Le compte '{nom}' n'existe pas")


def creer_compte(comptes):
    """Crée un nouveau compte bancaire."""
    nom = input("Nom du titulaire : ").strip().capitalize()

    if nom == "":
        print("Erreur : le nom ne peut pas être vide.")
        return

    # On vérifie que le compte n'existe pas déjà
    if nom in comptes:
        print(f"Erreur : le compte '{nom}' existe déjà.")
        return

    # On demande le solde initial
    try:
        solde = get_montant("Solde initial : ")
    except MontantInvalideError as e:
        print(f"Erreur : {e}")
        return

    # On crée le compte avec son historique
    comptes[nom] = {
        "solde": solde,
        "historique": [f"Création du compte : +{solde:.2f}€"]
    }
    print(f"Compte '{nom}' créé avec {solde:.2f}€")


def deposer(comptes):
    """Dépose de l'argent sur un compte."""
    nom = input("Nom du titulaire : ").strip().capitalize()

    # On vérifie que le compte existe (peut lever CompteInexistantError)
    verifier_compte(comptes, nom)

    montant = get_montant("Montant à déposer : ")

    # On effectue le dépôt
    comptes[nom]["solde"] += montant
    comptes[nom]["historique"].append(f"Dépôt : +{montant:.2f}€")
    print(f"+{montant:.2f}€ → Solde : {comptes[nom]['solde']:.2f}€")


def retirer(comptes):
    """Retire de l'argent d'un compte."""
    nom = input("Nom du titulaire : ").strip().capitalize()

    verifier_compte(comptes, nom)

    montant = get_montant("Montant à retirer : ")

    # On vérifie que le solde est suffisant
    if montant > comptes[nom]["solde"]:
        raise SoldeInsuffisantError(
            f"Solde insuffisant : {comptes[nom]['solde']:.2f}€ disponible, {montant:.2f}€ demandé"
        )

    # On effectue le retrait
    comptes[nom]["solde"] -= montant
    comptes[nom]["historique"].append(f"Retrait : -{montant:.2f}€")
    print(f"-{montant:.2f}€ → Solde : {comptes[nom]['solde']:.2f}€")


def virement(comptes):
    """Effectue un virement entre deux comptes."""
    source = input("Compte source : ").strip().capitalize()
    destination = input("Compte destination : ").strip().capitalize()

    # On interdit le virement vers soi-même
    if source == destination:
        raise BanqueError("Impossible de faire un virement vers son propre compte")

    # On vérifie que les deux comptes existent
    verifier_compte(comptes, source)
    verifier_compte(comptes, destination)

    montant = get_montant("Montant du virement : ")

    # On vérifie le solde du compte source
    if montant > comptes[source]["solde"]:
        raise SoldeInsuffisantError(
            f"Solde insuffisant sur le compte de {source} ({comptes[source]['solde']:.2f}€)"
        )

    # On effectue le virement
    comptes[source]["solde"] -= montant
    comptes[destination]["solde"] += montant

    # On met à jour les deux historiques
    comptes[source]["historique"].append(f"Virement vers {destination} : -{montant:.2f}€")
    comptes[destination]["historique"].append(f"Virement de {source} : +{montant:.2f}€")

    print(f"Virement de {montant:.2f}€ : {source} → {destination}")


def consulter(comptes):
    """Affiche le solde et l'historique d'un compte."""
    nom = input("Nom du titulaire : ").strip().capitalize()

    verifier_compte(comptes, nom)

    # Affichage du solde et de l'historique
    compte = comptes[nom]
    print(f"\n--- Compte de {nom} ---")
    print(f"Solde : {compte['solde']:.2f}€")
    print("Historique :")
    for operation in compte["historique"]:
        print(f"  • {operation}")
    print()


# --- Programme principal ---
def main():
    comptes = {}

    while True:
        print("\n=== MINI BANQUE ===")
        print("1. Créer un compte")
        print("2. Déposer")
        print("3. Retirer")
        print("4. Virement")
        print("5. Consulter un compte")
        print("6. Quitter")

        choix = input("Choix : ").strip()

        # On attrape toutes les erreurs bancaires au même endroit
        try:
            if choix == "1":
                creer_compte(comptes)
            elif choix == "2":
                deposer(comptes)
            elif choix == "3":
                retirer(comptes)
            elif choix == "4":
                virement(comptes)
            elif choix == "5":
                consulter(comptes)
            elif choix == "6":
                print("Merci et à bientôt !")
                break
            else:
                print("Erreur : choisis entre 1 et 6.")

        # On attrape chaque type d'erreur séparément pour des messages clairs
        except CompteInexistantError as e:
            print(f"Erreur : {e}")
        except SoldeInsuffisantError as e:
            print(f"Erreur : {e}")
        except MontantInvalideError as e:
            print(f"Erreur : {e}")
        except BanqueError as e:
            # Filet de sécurité pour toute erreur bancaire non prévue
            print(f"Erreur bancaire : {e}")

main()
```

---
---

# Récapitulatif de la progression

| Exercice | Concepts travaillés |
|---|---|
| 1. Liste de courses | `try/except` basique, `KeyError`, dictionnaire, menu en boucle |
| 2. Carnet de notes | `try/except` multiples, listes dans un dictionnaire, `sort`, calculs |
| 3. Nombre mystère | `raise ValueError`, validation dans une fonction, `random`, meilleur score |
| 4. Carnet d'adresses | Lecture/écriture fichier, `FileNotFoundError`, `finally`, données structurées |
| 5. Mini banque | Exceptions personnalisées, `raise`, fichier `errors.py`, `import`, héritage |
```

 ----

# Exercice 3 : 
```python

```

 ----

# Exercice 4 : 
```python

```