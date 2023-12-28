import sqlite3
#from combat import *
#from random import randint
#import re

chemin = 'P:\\PROGRAMMATION\\PYTHON\\JEUX\\Jeux_livre_heros\\livre_hero.db'

######################## FONCTIONS INVENTAIRE ###########################################
#--------------------- [BARRE PIECE] -----------------------------------------
def pieceOr():
    db_loc = sqlite3.connect(chemin)
    cursor = db_loc.cursor()
    piece = cursor.execute("SELECT nombre FROM pieces WHERE idObjet= 1")
    piece = cursor.fetchone()
    piece = piece[0]
    return piece
    db_loc.commit()
    db_loc.close()

#--------------------- [BARRE BIJOU] -----------------------------------------
def bijou():
    db_loc = sqlite3.connect(chemin)
    cursor = db_loc.cursor()
    bijoux = cursor.execute("SELECT SUM(nombre) FROM bijoux")
    for i in bijoux:
        return i[0]
    db_loc.commit()
    db_loc.close()

#--------------------- [INVENTAIRE ARMES ET PROTECTIONS] ---------------------
def afficherArmesProtections():
    ''' Affiche armes '''
    db_loc = sqlite3.connect(chemin)
    cursor = db_loc.cursor()
    cursor.execute("SELECT * FROM armes_protection;")
    armes_protection = cursor.fetchall()
    for line in armes_protection:
        print(line)
    db_loc.commit()
    db_loc.close()

#--------------------- [INVENTAIRE BIJOUX] -------------------------------------
def afficherBijoux():
    ''' Affiche bijoux '''
    db_loc = sqlite3.connect(chemin)
    cursor = db_loc.cursor()
    cursor.execute("SELECT * FROM bijoux;")
    bijoux = cursor.fetchall()
    for line in bijoux:
        print(line)
    db_loc.commit()
    db_loc.close()


#--------------------- [INVENTAIRE OBJETS] -------------------------------------
def afficherObjets():
    ''' Affiche objets '''
    db_loc = sqlite3.connect(chemin)
    cursor = db_loc.cursor()
    cursor.execute("SELECT * FROM objets;")
    objets = cursor.fetchall()
    for line in objets:
        print(line)
    db_loc.commit()
    db_loc.close()

#--------------------- [INVENTAIRE PROVISIONS ET POTIONS] -------------------------------------
def afficherProvisionsPotions():
    ''' Affiche provisions et potions '''
    db_loc = sqlite3.connect(chemin)
    cursor = db_loc.cursor()
    cursor.execute("SELECT * FROM provisions_potions;")
    provisions_potions = cursor.fetchall()
    for line in provisions_potions:
        print(line)
    db_loc.commit()
    db_loc.close()

#--------------------- [INVENTAIRE AJOUTER OU SUPPRIMER] -------------------------------------
def modifierInventaire():
    ''' Ajoute ou supprime données dans inventaire '''
    db_loc = sqlite3.connect(chemin)
    cursor = db_loc.cursor()
    choixTable = eval(input("Tu veux modifier (1)Pieces d'or, (2)Bijoux, (3)Objets, (4)Provisions et potions: "))

    #-------------------PIECES-------------------------
    if choixTable == 1:
        cursor.execute("SELECT * FROM pieces;")
        pieces = cursor.fetchall()
        for line in pieces:
            print(line)
        print("Modifier les quantités de pièces")
        objet = eval(input("Numéro de l'objet: "))
        nombrePieces = eval(input('Nombre: '))
        cursor.execute('''UPDATE pieces SET nombre=? WHERE idObjet=?;''' , (nombrePieces, objet))
        db_loc.commit()
        db_loc.close()

    #-------------------BIJOUX-------------------------
    elif choixTable == 2:
        cursor.execute("SELECT * FROM bijoux;")
        bijoux = cursor.fetchall()
        for line in bijoux:
            print(line)
        print("Modifier les quantités de bijoux")
        objet = eval(input("Numéro de l'objet: "))
        nombreBijoux = eval(input('Nombre: '))
        h = eval(input('Habileté: '))
        e = eval(input('Endurance: '))
        c = eval(input('Chance: '))
        cursor.execute('''UPDATE bijoux SET nombre=?, habilete=?, endurance=?, chance=? WHERE idObjet=?;''' , (nombreBijoux, h, e, c, objet))
        db_loc.commit()
        db_loc.close()

    #-------------------OBJETS-------------------------
    elif choixTable == 3:
        cursor.execute("SELECT * FROM objets;")
        objets = cursor.fetchall()
        for line in objets:
            print(line)
        print("Modifier les quantités l'objet dans inventaire")
        objet = eval(input("Numéro de l'objet: "))
        nombreObjets = eval(input('Nombre: '))
        h = eval(input('Habileté: '))
        e = eval(input('Endurance: '))
        c = eval(input('Chance: '))
        cursor.execute('''UPDATE objets SET nombre=?, habilete=?, endurance=?, chance=? WHERE idObjet=?;''' , (nombreObjets, h, e, c, objet))
        db_loc.commit()
        db_loc.close()
    #-------------------PROVISION ET POTIONS-------------------------
    elif choixTable == 4:
        cursor.execute("SELECT * FROM provisions_potions;")
        provisions_potions = cursor.fetchall()
        for line in provisions_potions:
            print(line)
        print("Modifier les quantités l'objet dans inventaire")
        objet = eval(input("Numéro de l'objet: "))
        nombreObjets = eval(input('Nombre: '))
        h = eval(input('Habileté: '))
        e = eval(input('Endurance: '))
        c = eval(input('Chance: '))
        cursor.execute('''UPDATE provisions_potions SET nombre=?, habilete=?, endurance=?, chance=? WHERE idObjet=?;''' , (nombreObjets, h, e, c, objet))
        db_loc.commit()
        db_loc.close()

