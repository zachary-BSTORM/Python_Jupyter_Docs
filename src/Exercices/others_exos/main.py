# --- Point d'entrée principal ---
# Lance le menu principal et dispatch vers chaque mini-application selon le choix de l'utilisateur.
# Note d'import : library_manager.py expose aussi une fonction appelée `menu`.
# On l'importe avec un alias explicite (library_menu) pour éviter le conflit de noms
# avec le module menu.py du dossier parent.

from src.Exercices.others_exos.ExoOO.Calculatrice import calculator
from src.Exercices.others_exos.ExoOO.algos import algos_menu
from src.Exercices.others_exos.ExoOO.minesweeper import minesweeper
from src.Exercices.others_exos.ExoOO.mystery_number import mystery_number_start
from src.Exercices.others_exos.ExoOO.library_manager import menu as library_menu
from src.Exercices.others_exos.ExoOO.todo_app import todo_menu
from src.Exercices.others_exos.menu import show_menu


def main():
    quit_game = False

    while not quit_game:
        choice = show_menu()  # Retourne toujours un entier valide entre 0 et 6

        match choice:
            case 0:
                quit_game = True
            case 1:
                calculator()
            case 2:
                mystery_number_start()
            case 3:
                library_menu()
            case 4:
                todo_menu()
            case 5:
                minesweeper()
            case 6:
                algos_menu()


if __name__ == '__main__':
    main()