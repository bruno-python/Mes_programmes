import itertools
import random

# Création du paquet de cartes
paquetCarte = list(itertools.product(['As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi'], ['Piques', 'Carreaux', 'Trefles', 'Coeurs']))

# Mélange du paquet de cartes
random.shuffle(paquetCarte)

# Création du premier joueur
def joueur1(n):
    for i in range(n):
        print(f'Joueur 1: {paquetCarte[i][0]} {paquetCarte[i][1]}')
        paquetCarte.remove(paquetCarte[i])

# Création du second joueur
def joueur2(n):
    for i in range(n):
        print(f'Joueur 2: {paquetCarte[i][0]} {paquetCarte[i][1]}')
        paquetCarte.remove(paquetCarte[i])

while len(paquetCarte) != 0:
    joueur1(1)
    joueur2(1)
    print('-------------')