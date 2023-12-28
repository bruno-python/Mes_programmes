import pygame

window_resolution = (640, 480)

pygame.init()
pygame.display.set_caption("Evenements")
window_surface = pygame.display.set_mode(window_resolution)
pygame.display.flip()

launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
        elif event.type == pygame.MOUSEMOTION:
            print(f'{event.pos}')
