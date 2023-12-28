#Importation des bibliothèques nécessaires
import pygame
from pygame.locals import *
#import os


#Initialisation de la bibliothèque Pygame
pygame.init()

#Création de la fenêtre
fenetre = pygame.display.set_mode((640, 480))
# fenetre = pygame.display.set_mode((640, 480), RESIZABLE) # agrandir ou rétrecir la fenêtre
# fenetre = pygame.display.set_mode((640, 480), FULLSREEN) # plein écran

# Chargement et collage du fond
fond = pygame.image.load("background.jpg").convert() # converti les images au format pygame plus rapide
fenetre.blit(fond, (0,0)) # 1 parametre l'image
						  # 2 parametre le point de collage (coin en haut à gauche de l'image)

#Chargement et collage du personnage
perso = pygame.image.load("perso.png").convert_alpha()
positionPerso = perso.get_rect()
fenetre.blit(perso, positionPerso)

# image.set_colorkey((255,255,255)) #Rend le blanc (valeur RGB : 255,255,255) de l'image transparent


# Raffraîchissement de l'écran
pygame.display.flip()

#Boucle infinie
continuer = 1
while continuer:
	for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
		if event.type == QUIT:     	   #Si un de ces événements est de type QUIT
			continuer = 0      		   #On arrête la boucle
		#if event.type == KEYDOWN and event.key == K_SPACE:
		#	print('Espace')
		if event.type == KEYDOWN:
			if event.key == K_DOWN: # Si flêche bas
				positionPerso = positionPerso.move(0,3)
			elif event.key == K_UP: # Si flêche haut
				positionPerso = positionPerso.move(0,-3)
			elif event.key == K_RIGHT: # Si flêche droite
				positionPerso = positionPerso.move(3,0)
			elif event.key == K_LEFT: # Si flêche gauche
				positionPerso = positionPerso.move(-3,0)

	# recollage
	fenetre.blit(fond,(0,0))
	fenetre.blit(perso, positionPerso)
	# Rafraichissement
	pygame.display.flip()
"""
Le type d'événement créé lorsque l'on appuie sur une touche est KEYDOWN, (ou KEYUP au relâchement de la touche). Vous penserez donc à créer une condition semblable à la précédente :
if event.type == KEYDOWN:
Pour définir une seule touche, utilisez en plus event.key, qui détermine la touche pressée
Lettres:
K_a ... K_z

Nombres:
K_0 ... K_9

Controles:
K_TAB
K_RETURN
K_ESCAPE
K_SCROLLOCK
K_SYSREQ
K_BREAK
K_DELETE
K_BACKSPACE
K_CAPSLOCK
K_CLEAR
K_NUMLOCK

Ponctuation:
K_SPACE

Touches F:
K_F1 ... K_F15

Clavier numérique:
K_KP0 ... K_KP9
K_KP_DIVIDE
K_KP_ENTER
K_KP_EQUALS
K_KP_MINUS
K_KP_MULTIPLY
K_KP_PERIOD
K_KP_PLUS

CTL,ALT,SHIFT:
K_LALT, K_RALT
K_LCTRL, K_RCTRL
K_LSHIFT, K_RSHIFT


Flèches:
K_LEFT
K_UP
K_RIGHT
K_DOWN


"""
