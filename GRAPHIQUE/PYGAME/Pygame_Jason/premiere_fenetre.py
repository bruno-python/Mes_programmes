import pygame

"""
    pygame.FULLSCREEM
    pygame.RESIZABLE
    pygame.NOFRAME

    pygame.OPENGL
    pygame.HWSURFACE
    pygame.DOUBLEBUF
"""

res = (640, 480)

pygame.init()
pygame.display.set_caption('Mon programme PYGAME')
window_surface = pygame.display.set_mode(res, pygame.RESIZABLE)

#print(pygame.display.Info())
print(pygame.get_sdl_version())

launched = True

while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
