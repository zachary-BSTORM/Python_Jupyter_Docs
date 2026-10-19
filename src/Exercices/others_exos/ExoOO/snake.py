import random
import keyboard
import time

# --- Snake (version terminal, librairie keyboard) ---
# Architecture orientée objet :
#   - Position     : simple conteneur (x, y) utilisé pour les coordonnées et la direction
#   - Snake        : corps du serpent (liste de Position) + direction courante
#   - Apple        : une pomme à une position aléatoire
#   - Plates       : plateau de jeu ; orchestre Snake et Apple, construit la grille d'affichage
#
# Gestion des entrées (librairie `keyboard`) :
#   keyboard.on_press() enregistre un callback appelé dans un thread séparé → non-bloquant.
#   Cela permet au jeu de continuer à avancer pendant que le joueur appuie sur une touche.
#
# Rendu terminal sans scintillement :
#   On utilise l'escape ANSI "\033[1;1H" pour repositionner le curseur en haut à gauche
#   au lieu d'effacer l'écran ("\033[2J"), ce qui évite le scintillement.
#
# Mécanique de déplacement (Snake.move) :
#   On insère la nouvelle tête en début de liste.
#   Si le serpent grandit (il vient de manger), on ne supprime pas la queue.
#   Le modulo (% w, % h) assure le wrap-around (le serpent sort d'un côté et réapparaît de l'autre).


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Snake:
    def __init__(self):
        # Serpent initial de 2 segments, orienté vers la droite (direction x=+1)
        self.positions = [Position(5, 5), Position(4, 5)]
        self.direction = Position(1, 0)

    def move(self, w, h, grow=False):
        tete = self.positions[0]
        # Calcul de la nouvelle tête avec wrap-around
        nx = (tete.x + self.direction.x) % w
        ny = (tete.y + self.direction.y) % h
        self.positions.insert(0, Position(nx, ny))
        if not grow:
            self.positions.pop()  # On retire la queue sauf si le serpent vient de manger


class Apple:
    def __init__(self, w, h):
        self.position = Position(random.randint(0, w - 1), random.randint(0, h - 1))


class Plates:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.snake = Snake()
        self.apple = Apple(w, h)

    def update(self):
        # Reconstruit la grille d'affichage à partir des positions actuelles
        self.map = [[" " for _ in range(self.w)] for _ in range(self.h)]

        for k, pos in enumerate(self.snake.positions):
            if k == 0:
                self.map[pos.y][pos.x] = "O"  # Tête du serpent
            else:
                self.map[pos.y][pos.x] = "="  # Corps du serpent

        self.map[self.apple.position.y][self.apple.position.x] = "*"  # Pomme

    def afficher(self):
        # Revenir en haut à gauche SANS effacer → pas de scintillement
        print("\033[1;1H", end="")
        for ligne in self.map:
            print(" ".join(ligne))

    def tick(self):
        # Un tick = un pas du jeu : on calcule si le serpent mange, on le déplace, on met à jour
        tete = self.snake.positions[0]
        nx = (tete.x + self.snake.direction.x) % self.w
        ny = (tete.y + self.snake.direction.y) % self.h

        mange = (nx == self.apple.position.x and ny == self.apple.position.y)
        self.snake.move(self.w, self.h, grow=mange)

        if mange:
            self.apple = Apple(self.w, self.h)  # Nouvelle pomme aléatoire

        self.update()
        return mange


def snake_game():
    print("\033[2J", end="")    # Effacer l'écran une fois au départ
    print("\033[?25l", end="")  # Masquer le curseur pendant le jeu

    plates = Plates(10, 10)
    points = 0
    speed = 0.8  # Délai entre chaque tick en secondes (diminue à chaque pomme mangée)

    # --- Callback clavier (thread séparé, non-bloquant) ---
    # Les noms de touches varient selon l'OS/clavier ; ici "haut", "bas", etc. sont pour
    # certains claviers français. Si ça ne répond pas, vérifier avec keyboard.read_key().
    # La condition (ex: direction.y != 1) empêche le demi-tour immédiat (marche arrière interdite).
    def on_key(event):
        if event.name == "haut" and plates.snake.direction.y != 1:
            plates.snake.direction = Position(0, -1)
        elif event.name == "bas" and plates.snake.direction.y != -1:
            plates.snake.direction = Position(0, 1)
        elif event.name == "gauche" and plates.snake.direction.x != 1:
            plates.snake.direction = Position(-1, 0)
        elif event.name == "droite" and plates.snake.direction.x != -1:
            plates.snake.direction = Position(1, 0)

    keyboard.on_press(on_key)

    try:
        while True:
            if plates.tick():
                points += 1
                if speed > 0.01:
                    speed -= 0.01  # On accélère légèrement à chaque pomme mangée
            plates.afficher()
            print(f"\nScore : {points} pommes")
            time.sleep(speed)

    except KeyboardInterrupt:
        print("\033[?25h", end="")  # Réafficher le curseur avant de quitter
        print("\nGame Over!")
    finally:
        keyboard.unhook_all()  # Nettoyage : on détache tous les listeners clavier


if __name__ == "__main__":
    # Guard : évite que le jeu se lance automatiquement à l'import du module
    snake_game()
