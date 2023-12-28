import pygame
import random

pygame.init()
screen = pygame.display.set_mode((640,640)) # creer la dimension de la fenêtre
pygame.display.set_caption('Super jeux') # titre de la fenêtre
clock = pygame.time.Clock()


# initialise la fenêtre
screen.fill((255,255,255)) # couleur de fond de la fenêtre
x1 = random.randint(0,590)
y1 = random.randint(0,590)

screen.fill((255,0,0), (x1, y1, 50, 50))
pygame.display.update() # actualise la fenêtre
x, y = 0, 0

while not pygame.key.get_pressed()[pygame.K_s]:
	clock.tick(60)
	if pygame.mouse.get_pressed() [0]:
		screen.fill((255,255,255))
		x,y = pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1]  # releve la position du pointeur
		
		if x1 < x < x1 + 50 and y1 < y < y1 + 50:
			print('gagné')
			font = pygame.font.Font(None, 36)
			text = font.render('Salut tout le monde', 1, (10, 10, 10))
			x1 = random.randint(0,590)
			y1 = random.randint(0,590)
			screen.fill((255,0,0), (x1, y1, 50, 50))
			pygame.display.update()
	
	pygame.event.pump() # permet de garder la fenêtre active
pygame.quit()# permet de quitter la fenêtre