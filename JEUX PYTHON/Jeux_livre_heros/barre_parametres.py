import sqlite3
#from combat import *
#from random import randint
#import re


chemin = 'P:\\PROGRAMMATION\\PYTHON\\JEUX\\Jeux_livre_heros\\livre_hero.db'

#--------------------- [BARRE PERSONNAGE] -------------------------------------
def personnage(a='Aucune', h=0, e=0, c=0, o=0, b=0):
    print("Arme: " + a + "\n" + "Habileté: " + str(h) + " |" + " Endurance: " + str(e) + " |" + " Chance: " + str(c) + "\n" + "Pièce or: " + str(o) + " |" + " Bijou: " + str(b) + " |")

    # def estVivant():
    #     if endurance() >= 0:
    #         endurance() = 'Mort'

#--------------------- [BARRE PARAMETRES] -------------------------------------
def parametres():
    db_loc = sqlite3.connect(chemin)
    cursor = db_loc.cursor()
    print("Calcule de l'habileté")
    habilete = lancerDes(1) + 6
    print("Calcule de l'endurance")
    endurance = lancerDes(2) + 12
    print('Calcule de la chance')
    chance = lancerDes(1) + 6
    cursor.execute('''UPDATE vie SET habilete=?, endurance=?, chance=?;''' ,(habilete, endurance, chance))
    db_loc.commit()
    db_loc.close()

#--------------------- [BARRE ARME] ---------------------------------------------
def arme(nb):
    db_loc = sqlite3.connect(chemin)
    cursor = db_loc.cursor()
    arme = cursor.execute("SELECT objet FROM armes_protection WHERE idObjet= ?",(nb,))
    arme = cursor.fetchone()
    return arme[0]
    db_loc.commit()
    db_loc.close()

#--------------------- [CHOISIR UNE DES POTIONS AU DEPART] ----------------------
def choisirPotion():
    print(pointsXpHero())

    print("(1)- Potion d'adresse (2 doses) = Rend points d'habilité du début")
    print("(2)- Potion de vigueur (2 doses) = Rend points d'endurance du début")
    print("(3)- Potion de bonne fortune (2 doses) = Rend points de chance du début + 1")
    choix = eval(input("choisir parmis l'une des 3 boiteilles de potion: "))

    db_loc = sqlite3.connect(chemin)
    cursor = db_loc.cursor()
    nombre = 2
    if choix == 1:
        habilete = listeHero[1]
        cursor.execute('''UPDATE provisions_potions SET nombre=?, habilete=? WHERE idObjet= 4;''' , (nombre, habilete))
    elif choix == 2:
        endurance = listeHero[2]
        cursor.execute('''UPDATE provisions_potions SET nombre=?, endurance=? WHERE idObjet= 5;''' , (nombre, endurance))
    else:
        chance = listeHero[3] + 1
        cursor.execute('''UPDATE provisions_potions SET nombre=?, chance=? WHERE idObjet= 6;''' , (nombre, chance))
    db_loc.commit()
    db_loc.close()

#--------------------- [BARRE HABILETE] ------------------------------------------
def habilete():
    db_loc = sqlite3.connect(chemin)
    cursor = db_loc.cursor()
    habilete = cursor.execute("SELECT habilete FROM vie")
    habilete = cursor.fetchone()
    return habilete[0]
    db_loc.commit()
    db_loc.close()

#--------------------- [BARRE ENDURANCE] ------------------------------------------
def endurance():
    db_loc = sqlite3.connect(chemin)
    cursor = db_loc.cursor()
    endurance = cursor.execute("SELECT endurance FROM vie")
    endurance = cursor.fetchone()
    return endurance[0]
    db_loc.commit()
    db_loc.close()

#--------------------- [BARRE CHANCE] --------------------------------------------
def chance():
    db_loc = sqlite3.connect(chemin)
    cursor = db_loc.cursor()
    chance = cursor.execute("SELECT chance FROM vie")
    chance = cursor.fetchone()
    return chance[0]
    db_loc.commit()
    db_loc.close()