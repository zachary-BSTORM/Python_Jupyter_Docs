import pygame
import random

# --- Snake (version graphique Pygame) ---
# Même logique que snake.py (terminal), mais rendu via Pygame.
#
# Boucle de jeu classique Pygame — 4 phases par frame :
#   1. Événements  : lecture de la file d'événements (fermeture fenêtre, touches)
#   2. Logique     : déplacement du serpent, détection collision avec la pomme
#   3. Dessin      : effacement + dessin de tous les éléments + flip (double buffering)
#   4. Vitesse     : clock.tick(FPS) limite les FPS et évite que le jeu tourne trop vite
#
# Constantes de configuration regroupées en haut → facile à modifier (taille, couleurs, grille).
# La grille est en cases logiques (colonnes × lignes) ; chaque case fait TAILLE_CASE pixels.
#
# Mécanique de déplacement identique à snake.py :
#   - Nouvelle tête = tête + direction (avec wrap-around modulo)
#   - grow=True → on ne retire pas la queue (le corps s'allonge)
#   - La condition (direction.y != 1 etc.) empêche le demi-tour immédiat

pygame.init()

# --- Constantes de configuration ---
TAILLE_CASE = 40        # Taille d'une case en pixels
COLONNES = 10
LIGNES = 10
LARGEUR = COLONNES * TAILLE_CASE
HAUTEUR = LIGNES * TAILLE_CASE

# Palette de couleurs (R, G, B)
NOIR = (0, 0, 0)
VERT = (0, 200, 0)          # Tête du serpent
VERT_FONCE = (0, 150, 0)    # Corps du serpent
ROUGE = (200, 0, 0)         # Pomme
BLANC = (255, 255, 255)

fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Snake:
    def __init__(self):
        # Serpent initial de 2 segments, orienté vers la droite
        self.positions = [Position(5, 5), Position(4, 5)]
        self.direction = Position(1, 0)

    def move(self, w, h, grow=False):
        tete = self.positions[0]
        nx = (tete.x + self.direction.x) % w
        ny = (tete.y + self.direction.y) % h
        self.positions.insert(0, Position(nx, ny))
        if not grow:
            self.positions.pop()

    def dessiner(self):
        # La tête est en vert clair, le corps en vert foncé pour les distinguer visuellement
        for k, pos in enumerate(self.positions):
            couleur = VERT if k == 0 else VERT_FONCE
            rect = pygame.Rect(pos.x * TAILLE_CASE, pos.y * TAILLE_CASE,
                               TAILLE_CASE, TAILLE_CASE)
            pygame.draw.rect(fenetre, couleur, rect)


class Apple:
    def __init__(self, w, h):
        self.position = Position(random.randint(0, w - 1), random.randint(0, h - 1))

    def dessiner(self):
        rect = pygame.Rect(self.position.x * TAILLE_CASE,
                           self.position.y * TAILLE_CASE,
                           TAILLE_CASE, TAILLE_CASE)
        pygame.draw.rect(fenetre, ROUGE, rect)


def snake_game():
    snake = Snake()
    apple = Apple(COLONNES, LIGNES)
    points = 0
    running = True

    while running:
        # --- 1. Événements ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                # La condition (ex: direction.y != 1) bloque le demi-tour immédiat
                if event.key == pygame.K_UP and snake.direction.y != 1:
                    snake.direction = Position(0, -1)
                elif event.key == pygame.K_DOWN and snake.direction.y != -1:
                    snake.direction = Position(0, 1)
                elif event.key == pygame.K_LEFT and snake.direction.x != 1:
                    snake.direction = Position(-1, 0)
                elif event.key == pygame.K_RIGHT and snake.direction.x != -1:
                    snake.direction = Position(1, 0)

        # --- 2. Logique ---
        tete = snake.positions[0]
        nx = (tete.x + snake.direction.x) % COLONNES
        ny = (tete.y + snake.direction.y) % LIGNES

        mange = (nx == apple.position.x and ny == apple.position.y)
        snake.move(COLONNES, LIGNES, grow=mange)

        if mange:
            points += 1
            apple = Apple(COLONNES, LIGNES)  # Nouvelle pomme aléatoire

        # --- 3. Dessin ---
        fenetre.fill(NOIR)       # Effacement complet (fond noir)
        snake.dessiner()
        apple.dessiner()
        pygame.display.flip()    # Double buffering : on affiche le frame rendu

        # --- 4. Vitesse ---
        clock.tick(10)           # 10 FPS → 1 déplacement du serpent toutes les 100ms

    pygame.quit()


if __name__ == "__main__":
    # Guard : évite que le jeu se lance automatiquement à l'import du module
    snake_game()