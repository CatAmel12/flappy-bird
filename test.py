import pygame
import sys
import os

# Initialiser Pygame
pygame.init()

# Constantes
LARGEUR, HAUTEUR = 800, 600
FPS = 60

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)

# Créer l'écran
ecran = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Zelda 2D")

# Charger les images
dossier_images = "images"
image_personnage = pygame.image.load(os.path.join(dossier_images, "personnage.png"))
image_fond = pygame.image.load(os.path.join(dossier_images, "fond.png"))

# Obtenir la taille du personnage
largeur_personnage, hauteur_personnage = image_personnage.get_size()

# Position initiale du personnage
x_personnage, y_personnage = LARGEUR // 2 - largeur_personnage // 2, HAUTEUR // 2 - hauteur_personnage // 2

# Définir la vitesse du personnage
vitesse_personnage = 5

# Main loop
horloge = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Gérer les mouvements du personnage
    touches = pygame.key.get_pressed()
    if touches[pygame.K_LEFT] and x_personnage > 0:
        x_personnage -= vitesse_personnage
    if touches[pygame.K_RIGHT] and x_personnage < LARGEUR - largeur_personnage:
        x_personnage += vitesse_personnage
    if touches[pygame.K_UP] and y_personnage > 0:
        y_personnage -= vitesse_personnage
    if touches[pygame.K_DOWN] and y_personnage < HAUTEUR - hauteur_personnage:
        y_personnage += vitesse_personnage

    # Dessiner le fond et le personnage
    ecran.fill(BLANC)
    ecran.blit(image_fond, (0, 0))
    ecran.blit(image_personnage, (x_personnage, y_personnage))

    # Mettre à jour l'affichage
    pygame.display.flip()

    # Limiter le nombre d'images par seconde
    horloge.tick(FPS)