# Exercice : Système de gestion de bibliothèque

---

## Consigne générale

Crée un programme de gestion de bibliothèque en Python.
Le programme doit tourner en boucle avec un menu principal et gérer toutes les erreurs possibles.

---

## Structure des données

```python
livres = [
    {
        "id": 1,
        "titre": "Le Petit Prince",
        "auteur": "Antoine de Saint-Exupéry",
        "genre": "conte",
    }
]
```

---

## Menu principal

```
=== BIBLIOTHÈQUE ===
1. Ajouter un livre
2. Afficher tous les livres
3. Chercher un livre
4. Supprimer un livre
5. Quitter
```

---

## Détail de chaque fonctionnalité

### 1. Ajouter un livre
- Demander : titre, auteur, genre
- Le genre doit être parmi : roman, conte, science-fiction, policier, histoire, science, autre
- L'ID est généré automatiquement (le plus grand ID existant + 1)
- Titre et auteur ne peuvent pas être vides
- Par défaut : disponible = True, emprunteur = None, date_emprunt = None

### 2. Afficher tous les livres
- Afficher chaque livre avec son ID, titre, auteur, genre et statut (disponible ou emprunté par qui)
- Si la bibliothèque est vide, afficher un message

### 3. Chercher un livre
- Proposer la recherche par : titre, auteur ou genre
- La recherche doit être insensible à la casse (majuscules/minuscules)
- La recherche partielle doit fonctionner ("petit" doit trouver "Le Petit Prince")
- Afficher tous les résultats trouvés ou un message si rien trouvé

### 4. Supprimer un livre
- Demander l'ID du livre
- Vérifier que le livre existe
- Interdire la suppression si le livre est emprunté
- Demander confirmation avant de supprimer

---

## Fonctions à créer

- `get_nombre(message)` → demande un entier valide en boucle
- `get_texte(message)` → demande un texte non vide en boucle
- `trouver_livre(livres, livre_id)` → retourne le livre correspondant à l'ID ou None
- `generer_id(livres)` → retourne le prochain ID disponible
- `ajouter_livre(livres)` → ajoute un nouveau livre
- `afficher_livres(livres)` → affiche tous les livres
- `chercher_livre(livres)` → cherche par titre, auteur ou genre
- `supprimer_livre(livres)` → supprime un livre après vérification
- `main()` → menu principal en boucle

---

## Erreurs à gérer

- ID invalide (pas un nombre) → redemander
- ID inexistant → message clair
- Texte vide pour titre/auteur → redemander
- Genre invalide → redemander
- Bibliothèque vide → message adapté
- Choix de menu invalide → message d'erreur

--- 
# Correction

```python
# Système de gestion de bibliothèque


# ============================================================
#  FONCTIONS UTILITAIRES
# ============================================================

def get_nombre(message):
    """Demande un entier valide en boucle."""
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Erreur : entre un nombre entier valide.")

def get_texte(message):
    """Demande un texte non vide en boucle."""
    while True:
        texte = input(message).strip()
        if texte == "":
            print("Erreur : ce champ ne peut pas être vide.")
            continue
        return texte

def trouver_livre(livres, livre_id):
    """Parcourt la liste et retourne le livre avec cet ID, ou None."""
    for livre in livres:
        if livre["id"] == livre_id:
            return livre
    return None

def generer_id(livres):
    """Retourne le prochain ID disponible."""
    if len(livres) == 0:
        return 1

    max_id = 0
    for livre in livres:
        if livre["id"] > max_id:
            max_id = livre["id"]
    return max_id + 1


# ============================================================
#  FONCTIONNALITÉS
# ============================================================

def ajouter_livre(livres):
    """Ajoute un nouveau livre à la bibliothèque."""
    print("\n--- Ajouter un livre ---")

    titre = get_texte("Titre : ")
    auteur = get_texte("Auteur : ")

    # Liste des genres autorisés
    genres_valides = ["roman", "conte", "science-fiction", "policier", "histoire", "science", "autre"]
    print(f"Genres disponibles : {', '.join(genres_valides)}")

    while True:
        genre = input("Genre : ").strip().lower()
        if genre == "":
            print("Erreur : le genre ne peut pas être vide.")
            continue
        if genre not in genres_valides:
            print(f"Erreur : '{genre}' n'est pas un genre valide.")
            continue
        break

    livre = {
        "id": generer_id(livres),
        "titre": titre,
        "auteur": auteur,
        "genre": genre
    }

    livres.append(livre)
    print(f"Livre '{titre}' ajouté avec l'ID {livre['id']}.")

def afficher_livres(livres):
    """Affiche tous les livres de la bibliothèque."""
    if len(livres) == 0:
        print("La bibliothèque est vide.")
        return

    print(f"\n--- Bibliothèque ({len(livres)} livre(s)) ---")
    for livre in livres:
        print(f"  [{livre['id']}] {livre['titre']} - {livre['auteur']} ({livre['genre']})")
    print()

def chercher_livre(livres):
    """Cherche un livre par titre, auteur ou genre."""
    if len(livres) == 0:
        print("La bibliothèque est vide.")
        return

    print("\n--- Chercher un livre ---")
    print("Chercher par :")
    print("  1. Titre")
    print("  2. Auteur")
    print("  3. Genre")

    choix = input("Choix : ").strip()

    if choix == "1":
        champ = "titre"
    elif choix == "2":
        champ = "auteur"
    elif choix == "3":
        champ = "genre"
    else:
        print("Choix invalide.")
        return

    recherche = get_texte("Recherche : ").lower()

    # On parcourt les livres pour trouver les correspondances
    resultats = []
    for livre in livres:
        if recherche in livre[champ].lower():
            resultats.append(livre)

    if len(resultats) == 0:
        print(f"Aucun livre trouvé pour '{recherche}'.")
    else:
        print(f"\n{len(resultats)} résultat(s) trouvé(s) :")
        for livre in resultats:
            print(f"  [{livre['id']}] {livre['titre']} - {livre['auteur']} ({livre['genre']})")

def supprimer_livre(livres):
    """Supprime un livre après vérification et confirmation."""
    if len(livres) == 0:
        print("La bibliothèque est vide.")
        return

    print("\n--- Supprimer un livre ---")

    livre_id = get_nombre("ID du livre : ")

    livre = trouver_livre(livres, livre_id)

    if livre is None:
        print(f"Erreur : aucun livre avec l'ID {livre_id}.")
        return

    print(f"Livre trouvé : '{livre['titre']}' de {livre['auteur']}")
    confirmer = input("Confirmer la suppression ? (o/n) : ").strip().lower()

    if confirmer == "o":
        livres.remove(livre)
        print(f"Livre '{livre['titre']}' supprimé.")
    else:
        print("Suppression annulée.")


# ============================================================
#  PROGRAMME PRINCIPAL
# ============================================================

def main():
    livres = [
        {"id": 1, "titre": "Le Petit Prince", "auteur": "Antoine de Saint-Exupéry", "genre": "conte"},
        {"id": 2, "titre": "1984", "auteur": "George Orwell", "genre": "science-fiction"},
        {"id": 3, "titre": "Sherlock Holmes", "auteur": "Arthur Conan Doyle", "genre": "policier"}
    ]

    print("=== SYSTÈME DE GESTION DE BIBLIOTHÈQUE ===\n")
    again = True
    while again == True:
        print("=== BIBLIOTHÈQUE ===")
        print("1. Ajouter un livre")
        print("2. Afficher tous les livres")
        print("3. Chercher un livre")
        print("4. Supprimer un livre")
        print("5. Quitter")

        choix = input("\nChoix : ").strip()

        if choix == "1":
            ajouter_livre(livres)
        elif choix == "2":
            afficher_livres(livres)
        elif choix == "3":
            chercher_livre(livres)
        elif choix == "4":
            supprimer_livre(livres)
        elif choix == "5":
            print("Merci et à bientôt !")
            again = False
        else:
            print("Erreur : choisis un numéro entre 1 et 5.")



main()
```