import pygame
from os.path import join
import random

# general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) # fenetre du jeu 
pygame.display.set_caption('Shooter') # titre fenetre principal
running = True

# plain surface
surf = pygame.Surface((100, 200))
surf.fill('orange')
x = 100
direction = 1

# importing an image
player_surf = pygame.image.load(join('images', 'player.png')).convert_alpha()
star_surf = pygame.image.load(join('images', 'star.png')).convert_alpha()
    # je creer un dict compr pour calculer et stockcer des positions (20) a l'avance:
stars_positions = [ (random.randint(1,WINDOW_WIDTH),random.randint(1,WINDOW_HEIGHT)) for i in range(20)]

while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # DRAW THE GAME:
        # ordre : couches qui se chevauchent!!
    

        # direction du vaisseau automatique 
    if x > WINDOW_WIDTH or x < 0:
        direction *= -1
    x += direction

    display_surface.fill('grey')  # fond de l'cran du logiciel
    for i in stars_positions:
        display_surface.blit(star_surf, i )

    display_surface.blit(player_surf,(x,140)) # on colle la surface voulu a l'ecran du logiciel

    pygame.display.update()










# fermer tout les process 
pygame.quit()