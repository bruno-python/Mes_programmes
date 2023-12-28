import sqlite3
import os

chemin = 'P:\\PROGRAMMATION\\PYTHON\\JEUX\\Jeux_livre_heros\\livre_hero.db'

def ajoutContenuVie():
    db_loc = sqlite3.connect(chemin)
    cursor = db_loc.cursor()
    # Prépare le fichier "vie.txt" a insérer dans la table "vie"
    with open('txt/vie.txt', encoding='utf-8') as file:
        for line in file:
            cell = line.split(',')
            cursor.execute('''INSERT INTO vie(habilete, endurance, chance) VALUES (?,?,?);''' , (cell[0], cell[1], cell[2]))
    db_loc.commit()
    db_loc.close()

#-----------------------------------------------------------------
def ajoutContenuArmes():
    db_loc = sqlite3.connect(chemin)
    cursor = db_loc.cursor()
    # Prépare le fichier "arme.txt" a insérer dans la table "armes_protection"
    with open('txt/arme.txt', encoding='utf-8') as file:
        for line in file:
            cell = line.split(',')
            cursor.execute('''INSERT INTO armes_protection(idObjet, objet, nombre, habilete, endurance, chance) VALUES (?,?,?,?,?,?);''' , (cell[0], cell[1], cell[2], cell[3], cell[4], cell[5]))
    db_loc.commit()
    db_loc.close()

#-----------------------------------------------------------------
def ajoutContenuCreatures():
    db_loc = sqlite3.connect(chemin)
    cursor = db_loc.cursor()
    # Prépare le fichier "creatures.txt" a insérer dans la table "creatures"
    with open('txt/creatures.txt', encoding='utf-8') as file:
        for line in file:
            cell = line.split(',')
            cursor.execute('''INSERT INTO creatures(pageId, nom, habilete, endurance, vivant) VALUES (?,?,?,?,?);''' , (cell[0], cell[1], cell[2], cell[3], cell[4]))
    db_loc.commit()
    db_loc.close()

#-----------------------------------------------------------------
def ajoutContenuObjets():
    db_loc = sqlite3.connect(chemin)
    cursor = db_loc.cursor()
    # Prépare le fichier "objets.txt" a insérer dans la table "objets"
    with open('txt/objets.txt', encoding='utf-8') as file:
        for line in file:
            cell = line.split(',')
            cursor.execute('''INSERT INTO objets(idObjet, objet, nombre, habilete, endurance, chance) VALUES (?,?,?,?,?,?);''' , (cell[0], cell[1], cell[2], cell[3], cell[4], cell[5]))
    db_loc.commit()
    db_loc.close()

#-----------------------------------------------------------------
def ajoutContenuOr():
    db_loc = sqlite3.connect(chemin)
    cursor = db_loc.cursor()
    # Prépare le fichier "pieces.txt" a insérer dans la table "pieces"
    with open('txt/pieces.txt', encoding='utf-8') as file:
        for line in file:
            cell = line.split(',')
            cursor.execute('''INSERT INTO pieces(idObjet, objet, nombre) VALUES (?,?,?);''' , (cell[0], cell[1], cell[2]))
    db_loc.commit()
    db_loc.close()

#-----------------------------------------------------------------
def ajoutContenuBijoux():
    db_loc = sqlite3.connect(chemin)
    cursor = db_loc.cursor()
    # Prépare le fichier "bijoux.txt" a insérer dans la table "bijoux"
    with open('txt/bijoux.txt', encoding='utf-8') as file:
        for line in file:
            cell = line.split(',')
            cursor.execute('''INSERT INTO bijoux(idObjet, objet, nombre, habilete, endurance, chance) VALUES (?,?,?,?,?,?);''' , (cell[0], cell[1], cell[2], cell[3], cell[4], cell[5]))
    db_loc.commit()
    db_loc.close()

#-----------------------------------------------------------------
def ajoutContenuProvisionsPotions():
    db_loc = sqlite3.connect(chemin)
    cursor = db_loc.cursor()
    # Prépare le fichier "provision_potion.txt" a insérer dans la table "provisions_potions"
    with open('txt/provision_potion.txt', encoding='utf-8') as file:
        for line in file:
            cell = line.split(',')
            cursor.execute('''INSERT INTO provisions_potions(idObjet, objet, nombre, habilete, endurance, chance) VALUES (?,?,?,?,?,?);''' , (cell[0], cell[1], cell[2], cell[3], cell[4], cell[5]))
    db_loc.commit()
    db_loc.close()

#-----------------------------------------------------------------
def ajoutContenuPage():
    db_loc = sqlite3.connect(chemin)
    cursor = db_loc.cursor()
    # Prépare les fichiers "page.txt" a insérer dans la table "quete"
    def record(nb):
        page = 'pages/' + str(nb) + '.txt'
        with open(page, encoding='utf-8') as file:
            content = ""
            content += file.read()
            print(page)
            return content

    for i in range(0, 401):
        quete = record(i)
        numPage = i
        #print(numPage, quete)
        cursor.execute('''INSERT INTO quete(pageId, texte) VALUES (?,?);''' , (numPage, quete))
    db_loc.commit()
    db_loc.close()