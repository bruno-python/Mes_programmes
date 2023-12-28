import pygame

# Surface, Rect
# Rect(left, top, width, height)

pygame.init()

window_resolution = (640, 480)
blue_color = (89, 152, 255)
black_color = (0, 0, 0)

pygame.display.set_caption('Dessiner sur une surface')


window_surface = pygame.display.set_mode(window_resolution)
window_surface.fill(blue_color) # remplissage de la surface

# ligne
pygame.draw.line(window_surface, black_color, [150, 10], [250, 100])

# rectangle
rect_form = pygame.Rect(50, 120, 150, 65)
pygame.draw.rect(window_surface, black_color, rect_form, 5)

# circle
pygame.draw.circle(window_surface, black_color, [350, 100], 50, 2)

# polygone
coords = [(10, 10), (100, 10), (140, 60), (30, 50)]
pygame.draw.polygon(window_surface, black_color, coords)

pygame.display.flip()

launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
