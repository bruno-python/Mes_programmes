import sqlite3
import os
from creation_des_tables import *


chemin = 'P:\\PROGRAMMATION\\PYTHON\\JEUX\\Jeux_livre_heros\\livre_hero.db'

def ajoutBackupVie():
    db_loc = sqlite3.connect(chemin)
    cursor = db_loc.cursor()
    # Prépare le fichier "backup_vie.bak" a insérer dans la table "vie"
    with open('txt/backup_vie.bak', encoding='utf-8') as file:
        for line in file:
            cell = line.split(',')
            cursor.execute('''INSERT INTO vie(habilete, endurance, chance) VALUES (?,?,?);''' , (cell[0], cell[1], cell[2]))
    db_loc.commit()
    db_loc.close()
#-----------------------------------------------------------------
def ajoutBackupProvisionsPotions():
    db_loc = sqlite3.connect(chemin)
    cursor = db_loc.cursor()
    # Prépare le fichier "backup_provisions_potions.bak" a insérer dans la table "provisions_potions"
    with open('txt/backup_provisions_potions.bak', encoding='utf-8') as file:
        for line in file:
            cell = line.split(',')
            cursor.execute('''INSERT INTO provisions_potions(idObjet, objet, nombre, habilete, endurance, chance) VALUES (?,?,?,?,?,?);''' , (cell[0], cell[1], cell[2], cell[3], cell[4], cell[5]))
    db_loc.commit()
    db_loc.close()

#-----------------------------------------------------------------
def ajoutBackupArmes():
    db_loc = sqlite3.connect(chemin)
    cursor = db_loc.cursor()
    # Prépare le fichier "backup_armes.bak" a insérer dans la table "armes_protection"
    with open('txt/backup_armes.bak', encoding='utf-8') as file:
        for line in file:
            cell = line.split(',')
            cursor.execute('''INSERT INTO armes_protection(idObjet, objet, nombre, habilete, endurance, chance) VALUES (?,?,?,?,?,?);''' , (cell[0], cell[1], cell[2], cell[3], cell[4], cell[5]))
    db_loc.commit()
    db_loc.close()

#-----------------------------------------------------------------
def ajoutBackupCreatures():
    db_loc = sqlite3.connect(chemin)
    cursor = db_loc.cursor()
    # Prépare le fichier "backup_creatures.bak" a insérer dans la table "creatures"
    with open('txt/backup_creatures.bak', encoding='utf-8') as file:
        for line in file:
            cell = line.split(',')
            cursor.execute('''INSERT INTO creatures(pageId, nom, habilete, endurance, vivant) VALUES (?,?,?,?,?);''' , (cell[0], cell[1], cell[2], cell[3], cell[4]))
    db_loc.commit()
    db_loc.close()

#-----------------------------------------------------------------
def ajoutBackupObjets():
    db_loc = sqlite3.connect(chemin)
    cursor = db_loc.cursor()
    # Prépare le fichier "backup_objets.bak" a insérer dans la table "objets"
    with open('txt/backup_objets.bak', encoding='utf-8') as file:
        for line in file:
            cell = line.split(',')
            cursor.execute('''INSERT INTO objets(idObjet, objet, nombre, habilete, endurance, chance) VALUES (?,?,?,?,?,?);''' , (cell[0], cell[1], cell[2], cell[3], cell[4], cell[5]))
    db_loc.commit()
    db_loc.close()

#-----------------------------------------------------------------
def ajoutBackupOr():
    db_loc = sqlite3.connect(chemin)
    cursor = db_loc.cursor()
    # Prépare le fichier "backup_or.bak" a insérer dans la table "pieces"
    with open('txt/backup_or.bak', encoding='utf-8') as file:
        for line in file:
            cell = line.split(',')
            cursor.execute('''INSERT INTO pieces(idObjet, objet, nombre) VALUES (?,?,?);''' , (cell[0], cell[1], cell[2]))
    db_loc.commit()
    db_loc.close()

#-----------------------------------------------------------------
def ajoutBackupBijoux():
    db_loc = sqlite3.connect(chemin)
    cursor = db_loc.cursor()
    # Prépare le fichier "backup_bijoux.bak" a insérer dans la table "bijoux"
    with open('txt/backup_bijoux.bak', encoding='utf-8') as file:
        for line in file:
            cell = line.split(',')
            cursor.execute('''INSERT INTO bijoux(idObjet, objet, nombre, habilete, endurance, chance) VALUES (?,?,?,?,?,?);''' , (cell[0], cell[1], cell[2], cell[3], cell[4], cell[5]))
    db_loc.commit()
    db_loc.close()



if __name__ == '__main__':
    deleteTable()
    creationBase()
    ajoutBackupArmes():
    ajoutBackupObjets():
    ajoutBackupCreatures():
    ajoutBackupOr():
    ajoutBackupBijoux():
    ajoutBackupProvisionsPotions():
    ajoutBackupVie():