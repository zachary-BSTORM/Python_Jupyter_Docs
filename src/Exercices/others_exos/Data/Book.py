# --- Modèle de données : Book ---
# Classe simple (data class manuelle) représentant un livre.
# Utilisée par library_manager.py pour manipuler les livres en mémoire.
# Les annotations de type (str, list[str]) servent de documentation et permettent
# aux outils d'analyse statique (mypy, Pylance) de détecter les erreurs de type.

class Book:
    def __init__(self, isbn: str, title: str, categories: list[str]):
        self.isbn = isbn            # Identifiant unique (format ISBN-13)
        self.title = title
        self.categories = categories  # Liste de genres/catégories (ex: ["Fantasy", "Aventure"])