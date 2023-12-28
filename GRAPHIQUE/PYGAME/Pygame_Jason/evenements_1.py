import pygame

window_resolution = (640, 480)
white_color = (255, 255, 255)
black_color = (0, 0, 0)

pygame.init()
pygame.display.set_caption("Evenements")
window_surface = pygame.display.set_mode(window_resolution, pygame.RESIZABLE)

arial_font = pygame.font.SysFont("arial", 30)
dimensions_text = arial_font.render(f'{window_resolution}', True, white_color)
window_surface.blit(dimensions_text, [10, 10])

pygame.display.flip()

launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
        elif event.type == pygame.VIDEORESIZE:
            window_surface.fill(black_color)
            dimensions_text = arial_font.render(f'{event.w}x{event.h}', True, white_color)
            window_surface.blit(dimensions_text, [10, 10])
            pygame.display.flip()
