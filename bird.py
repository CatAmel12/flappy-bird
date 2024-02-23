import pygame
import random

# Initialisation de Pygame
pygame.init()

# Définition des variables globales
WIDTH, HEIGHT = 400, 600
GRAVITY = 0.25
BIRD_JUMP = 4
PIPE_WIDTH = 50
PIPE_GAP = 200
FPS = 60
clock = pygame.time.Clock()

# Création de la fenêtre du jeu
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flappy Bird')

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Charge des images
bird_img = pygame.image.load('bird.png').convert_alpha()
bird_img = pygame.transform.scale(bird_img, (50, 50))
pipe_img = pygame.image.load('pipe.png').convert_alpha()

# Classe Bird
class Bird:
    def __init__(self):
        self.x = 100
        self.y = HEIGHT // 2
        self.velocity = 0
        self.lift = -BIRD_JUMP
        self.image = bird_img
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def flap(self):
        self.velocity += self.lift

    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity
        self.rect.centery = self.y

# Classe Pipe
class Pipe:
    def __init__(self):
        self.x = WIDTH
        self.pipe_gap = PIPE_GAP
        self.top = random.randint(0, HEIGHT - self.pipe_gap)
        self.bottom = self.top + self.pipe_gap
        self.image = pipe_img
        self.pipe_top = pygame.transform.rotate(self.image, 180)
        self.rect_top = self.pipe_top.get_rect(midbottom=(self.x, self.top))
        self.rect_bottom = self.image.get_rect(midtop=(self.x, self.bottom))

    def update(self):
        self.x -= 2
        self.rect_top = self.pipe_top.get_rect(midbottom=(self.x, self.top))
        self.rect_bottom = self.image.get_rect(midtop=(self.x, self.bottom))

# Fonction principale
def main():
    bird = Bird()
    pipes = []
    score = 0
    running = True

    # Boucle de jeu
    while running:
        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.flap()

        # Mise à jour des éléments
        bird.update()
        if pipes:
            if pipes[0].x < -PIPE_WIDTH:
                pipes.pop(0)
            else:
                if bird.rect.colliderect(pipes[0].rect_top) or bird.rect.colliderect(pipes[0].rect_bottom):
                    running = False
                elif bird.rect.top <= 0 or bird.rect.bottom >= HEIGHT:
                    running = False

        if pipes and pipes[-1].x < WIDTH - PIPE_GAP:
            pipes.append(Pipe())
        elif not pipes:
            pipes.append(Pipe())

        for pipe in pipes:
            pipe.update()

        # Vérification des collisions
        if pipes and bird.rect.centerx > pipes[0].rect.centerx and pipes[0].x + PIPE_WIDTH < bird.rect.centerx:
            score += 1
            print(f"Score: {score}")

        # Affichage
        screen.fill(BLACK)
        screen.blit(bird.image, bird.rect)
        for pipe in pipes:
            screen.blit(pipe.pipe_top, pipe.rect_top)
            screen.blit(pipe.image, pipe.rect_bottom)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
