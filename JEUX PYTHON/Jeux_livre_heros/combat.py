import sqlite3
from fonctions import *
#from random import randint

chemin = 'P:\\PROGRAMMATION\\PYTHON\\JEUX\\Jeux_livre_heros\\livre_hero.db'
listePage = [19, 20, 116, 140, 199, 236, 282, 309, 350, 365, 372] # liste des pages avec creatures

listeHero = ['Hero']

# --------------------- [POINTS EXPERIENCE HERO] -------------------------------------
def pointsXpHero():
    db_loc = sqlite3.connect(chemin)
    cursor = db_loc.cursor()
    habilete = cursor.execute("SELECT habilete FROM vie")
    habilete = cursor.fetchone()
    listeHero.append(habilete[0])
    endurance = cursor.execute("SELECT endurance FROM vie")
    endurance = cursor.fetchone()
    listeHero.append(endurance[0])
    chance = cursor.execute("SELECT chance FROM vie")
    chance = cursor.fetchone()
    listeHero.append(chance[0])
    return listeHero
    db_loc.commit()
    db_loc.close()

# --------------------- [POINTS EXPERIENCE UNE CREATURE] -------------------------------------
listeCreature = []
listeCreature1 = []
listeCreature2 = []
listeCreature3 = []
listeCreature4 = []
listeCreature5 = []

def pointsXpCreatures(page, nbCreature):
    pageCreature = 'P' + str(page)
    db_loc = sqlite3.connect(chemin)
    cursor = db_loc.cursor()
    cursor.execute("SELECT nom, habilete, endurance FROM creatures WHERE pageId=?", (pageCreature,))
    creatures = cursor.fetchall()
    for line in creatures:
        listeCreature.append(line[0])
        listeCreature.append(line[1])
        listeCreature.append(line[2])

    listeCreature1.append(listeCreature[0:3])
    listeCreature2.append(listeCreature[3:6])
    listeCreature3 = listeCreature[6:9]
    listeCreature4 = listeCreature[9:12]
    listeCreature5 = listeCreature[12:15]

    if nbCreature == 1:
        print(listeCreature1)
    elif nbCreature == 2:
        print('CREATURE A COMBATTRE')
        print(listeCreature1)
        print(listeCreature2)
        print('------------------------')

    elif nbCreature == 3:
        print(listeCreature1)
        print(listeCreature2)
        print(listeCreature3)
    elif nbCreature == 4:
        print(listeCreature1)
        print(listeCreature2)
        print(listeCreature3)
        print(listeCreature4)
    elif nbCreature == 5:
        print(listeCreature1)
        print(listeCreature2)
        print(listeCreature3)
        print(listeCreature4)
        print(listeCreature5)
    #return listeCreature
    db_loc.commit()
    db_loc.close()


# --------------------- [BATAILLE] -------------------------------------
def bataille(creature):
    forceAttaqueCreature = 0
    forceAttaqueHero = 0

    print('---------------------------------')
    forceAttaqueCreature = lancerDes(2) + creature[0][1]
    print('Force creature:', forceAttaqueCreature)
    forceAttaqueHero = lancerDes(2) + listeHero[1]
    print('Force hero:', forceAttaqueHero)

    if forceAttaqueHero > forceAttaqueCreature: # héro l'attaque
        creature[0][2] = creature[0][2] - 2
        print('Attaque réussi !!!')
        if creature[0][2] == 0:
            print('Vous avez tué la créature')
            creatureMort(creature)
            xpHeroActualiser()
            #break
        else:
            tenterChance('augmenterBlessures')
            fuite()
            print('Hero', listeHero)
            print('Creature', creature)
            print('---------------------------------')

    elif forceAttaqueHero < forceAttaqueCreature: # héro perd l'attaque
        listeHero[2] = listeHero[2] - 2
        print('Reçu une blessure.')
        if listeHero[2] == 0:
            print('Vous êtes mort !!!')
            xpHeroActualiser()
            #break
        else:
            tenterChance('reduireBlessures')
            fuite()
            print('Hero', listeHero)
            print('Creature', creature)
            print('---------------------------------')

    else:
        print('Egalité, le combat continue...')
        print('---------------------------------')


# --------------------- [COMBAT AVEC UNE OU CREATURES] -------------------------------------
def combatCreature():
    pointsXpHero()
    page = eval(input('Entrer le numero de page avec la créature: '))

    if page in listePage:
        # 1 pour une creature
        # 2, 3, 4, 5 creatures
        # 1 pour (vous affronter toutes les créatures comme une seul)

        nbreCreatures = eval(input('Nombre de creatures, (1) si affronter comme une seule: '))
        if nbreCreatures == 1:
            pointsXpCreatures(page, 1)
            print('Hero =>', listeHero)
            print('Creature 1 =>', listeCreature1)
            bataille(listeCreature1)

        elif nbreCreatures == 2:
            pointsXpCreatures(page, 2)
            while nbreCreatures > 0:
                print('Hero =>', listeHero)
                print('Creature 1 =>', listeCreature1)
                bataille(listeCreature1)
                nbreCreatures -= 1
                print('Creature 2 =>', listeCreature2)
                bataille(listeCreature2)
                nbreCreatures -= 1

        elif nbreCreatures == 3:
            pointsXpCreatures(page, 3)
            while nbreCreatures > 3:
                print('Hero =>', listeHero)
                print('Creature 1 =>', listeCreature1)
                bataille(listeCreature1)
                nbreCreatures -= 1
                print('Creature 2 =>', listeCreature2)
                bataille(listeCreature2)
                nbreCreatures -= 1
                print('Creature 3 =>', listeCreature3)
                bataille(listeCreature3)
                nbreCreatures -= 1

        elif nbreCreatures == 4:
            pointsXpCreatures(page, 4)
            while nbreCreatures > 3:
                print('Hero =>', listeHero)
                print('Creature 1 =>', listeCreature1)
                bataille(listeCreature1)
                nbreCreatures -= 1
                print('Creature 2 =>', listeCreature2)
                bataille(listeCreature2)
                nbreCreatures -= 1
                print('Creature 3 =>', listeCreature3)
                bataille(listeCreature3)
                nbreCreatures -= 1
                print('Creature 4 =>', listeCreature4)
                bataille(listeCreature4)
                nbreCreatures -= 1

        elif nbreCreatures == 5:
            pointsXpCreatures(page, 5)
            while nbreCreatures > 3:
                print('Hero =>', listeHero)
                print('Creature 1 =>', listeCreature1)
                bataille(listeCreature1)
                nbreCreatures -= 1
                print('Creature 2 =>', listeCreature2)
                bataille(listeCreature2)
                nbreCreatures -= 1
                print('Creature 3 =>', listeCreature3)
                bataille(listeCreature3)
                nbreCreatures -= 1
                print('Creature 4 =>', listeCreature4)
                bataille(listeCreature4)
                nbreCreatures -= 1
                print('Creature 5 =>', listeCreature5)
                bataille(listeCreature5)
                nbreCreatures -= 1


# --------------------- [ACTUALISE LA TABLE APRES LE COMBAT] ---------------------------
def xpHeroActualiser():
    db_loc = sqlite3.connect(chemin)
    cursor = db_loc.cursor()
    habilete = listeHero[1]
    endurance = listeHero[2]
    chance = listeHero[3]
    cursor.execute('''UPDATE vie SET habilete=?, endurance=?, chance=?;''' , (habilete, endurance, chance))
    db_loc.commit()
    db_loc.close()

#--------------------- [PRENDRE LA FUITE] -------------------------------------
def fuite():
    ''' Le héro prends la fuite, quel lâche '''
    print("Si vous prenez la fuite, vous perdrez 2 points d'endurance")
    choix = input('Prendre la fuite ? (o/n)')
    if choix == 'o':
        listeHero[2] = listeHero[2] - 2

#--------------------- [CREATURE TUER ACTALISATION DE LA TABLE] ----------------
def creatureMort(creature):
    ''' Met 0 a la place de 1 quand la créature meurt '''
    db_loc = sqlite3.connect(chemin)
    cursor = db_loc.cursor()

    cursor.execute('''UPDATE creatures SET vivant=? WHERE nom=?;''' , (0, creature[1]))

    db_loc.commit()
    db_loc.close()