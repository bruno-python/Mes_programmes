import pygame

pygame.init()

window_resolution = (800, 600)
blank_color = (255, 255, 255)
black_color = (0, 0, 0)

pygame.display.set_caption('Affiche image')
window_surface = pygame.display.set_mode(window_resolution)

image_herbe = pygame.image.load('../background.jpg') # retourne une Surface
image_herbe.convert()

image_personnage = pygame.image.load('../perso.png') # retourne une Surface
image_personnage.convert()

image_herbe.set_colorkey(blank_color)# rends la couleur choisie transparente

launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False

    # Corps du programme
    window_surface.fill(blank_color)
    window_surface.blit(image_herbe, [10, 10])
    window_surface.blit(image_personnage, [650, 250])
    pygame.display.flip()
