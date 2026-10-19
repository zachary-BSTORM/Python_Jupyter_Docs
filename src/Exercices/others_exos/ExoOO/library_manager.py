from src.Exercices.others_exos.Data.Book import Book
from src.Exercices.others_exos.Data.library import library

# --- Library Manager ---
# Gestionnaire de bibliothèque en mémoire.
# Les données initiales viennent du dictionnaire `library` (isbn → (titre, catégories)).
# On les convertit en une liste d'objets Book au démarrage.
# Les opérations CRUD (Create, Read, Update, Delete) agissent directement sur cette liste.
# Note : les modifications ne sont PAS persistées sur disque (contrairement à todo_app).

# Initialisation : conversion du dict de données brutes en objets Book
books = [
    Book(isbn, title, categories)
    for isbn, (title, categories) in library.items()
]


def get_book(isbn: str):
    # Recherche linéaire dans la liste ; retourne None si non trouvé
    # Pour une bibliothèque très grande, un dict {isbn: Book} serait O(1) au lieu de O(n)
    for book in books:
        if book.isbn == isbn:
            return book
    return None


def input_isbn(prompt="Enter ISBN: "):
    # Factorisation de la saisie ISBN pour éviter la duplication dans chaque fonction
    return input(prompt).strip()


def input_categories():
    # Saisie d'une liste de catégories séparées par des virgules, avec nettoyage des espaces
    raw = input("Enter categories (comma separated): ")
    return [c.strip() for c in raw.split(",") if c.strip()]


def show_books():
    print("\n--- Library ---")
    for book in books:
        print(f"{book.isbn} | {book.title} | {book.categories}")


def search_book():
    isbn = input_isbn()
    book = get_book(isbn)

    if book:
        print(f"\nFound: {book.isbn} | {book.title} | {book.categories}")
    else:
        print("Book not found")


def add_book():
    isbn = input_isbn()

    # On vérifie l'unicité de l'ISBN avant d'ajouter
    if get_book(isbn):
        print("Book already exists")
        return

    title = input("Enter title: ")
    categories = input_categories()

    books.append(Book(isbn, title, categories))
    print("Book added successfully")


def update_book():
    isbn = input_isbn()
    book = get_book(isbn)

    if not book:
        print("Book not found")
        return

    print("Leave empty to keep current value")

    # Mise à jour partielle : on ne modifie que les champs où l'utilisateur a saisi quelque chose
    new_title = input(f"New title ({book.title}): ")
    if new_title:
        book.title = new_title

    new_categories = input("New categories (comma separated): ")
    if new_categories:
        book.categories = [c.strip() for c in new_categories.split(",")]

    print("Book updated")


def delete_book():
    isbn = input_isbn()
    book = get_book(isbn)

    if not book:
        print("Book not found")
        return

    books.remove(book)  # Supprime l'objet Book de la liste en mémoire
    print("Book deleted")


def menu():
    while True:
        print("\nWelcome to Library Manager!\n")
        print("1. Show all books")
        print("2. Search for a book")
        print("3. Add a book to the library")
        print("4. Update a book")
        print("5. Delete a book")
        print("6. Exit")

        choice = input("Choose an option: ").strip()

        match choice:
            case "1":
                show_books()
            case "2":
                search_book()
            case "3":
                add_book()
            case "4":
                update_book()
            case "5":
                delete_book()
            case "6":
                print("Goodbye!")
                break
            case _:
                print("Invalid choice")


