import pygame
import time

pygame.init()
window_resolution =(640, 480)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 75, 255)

pygame.display.set_caption('Rectangle en mouvement')
window_surface = pygame.display.set_mode(window_resolution)

myRect = pygame.Rect(10, 100, 25, 25)
myBlock = pygame.Rect(600, 50, 20, 300)
pygame.draw.rect(window_surface, red, myRect)
pygame.draw.rect(window_surface, blue, myBlock)
pygame.display.flip()

launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False

    while not myRect.colliderect(myBlock):
        time.sleep(.010)
        window_surface.fill(black)
        myRect.x += 1
        pygame.draw.rect(window_surface, red, myRect)
        pygame.draw.rect(window_surface, blue, myBlock)
        pygame.display.flip()