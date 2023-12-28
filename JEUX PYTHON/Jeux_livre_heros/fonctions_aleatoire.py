import sqlite3
#from combat import *
from random import randint
#import re


chemin = 'P:\\PROGRAMMATION\\PYTHON\\JEUX\\Jeux_livre_heros\\livre_hero.db'

#--------------------- [LANCER DE DES] ------------------------------------------------
def lancerDes(nbreDes):
    totalTirage = 0
    for i in range(nbreDes):
        tirage = randint(1,6)
        totalTirage += tirage
    return totalTirage

#--------------------- [TENTER LA CHANCE] -------------------------------------
def tenterChance(texte):
    print('A chaque fois que vous tenter votre chance, vous perdrez 1 point de chance.')
    choix = input('Tentez votre chance ? (o/n)')
    if choix == 'o':
        if 'augmenterBlessures':
            listeHero[3] = listeHero[3] - 1 # enleve 1 à la chance
            if lancerDes(2) <= listeHero[3]:
                listeCreature[2] = listeCreature[2] - 2
            else:
                listeCreature[2] = listeCreature[2] + 1
        elif 'reduireBlessures':
            listeHero[3] = listeHero[3] - 1 # enleve 1 à la chance
            if lancerDes(2) <= listeHero[3]:
                listeHero[2] = listehero[2] + 1
            else:
                listeHero[2] = listeHero[2] - 2
        elif 'tenter':
            db_loc = sqlite3.connect(chemin)
            cursor = db_loc.cursor()
            cursor.execute('''UPDATE vie SET chance=?;''' , (chance,))
            db_loc.commit()
            db_loc.close()
            if lancerDes(2) <= chance():
                chance = chance() - 1
                print('Vous avez de la chance !!!')
            else:
                chance = chance() - 1
                print("La chance n'est pas avec vous")



