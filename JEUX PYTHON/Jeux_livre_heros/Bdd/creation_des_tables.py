import sqlite3

# Création de la base et des tables

chemin = 'P:\\PROGRAMMATION\\PYTHON\\JEUX\\Jeux_livre_heros\\livre_hero.db'

def deleteTable():
      """ SUPPRESSION DES TABLE """
      db_loc = sqlite3.connect(chemin)
      cursor = db_loc.cursor()
      cursor.execute('''DELETE FROM creatures''')
      cursor.execute('''DELETE FROM armes_protection''')
      cursor.execute('''DELETE FROM objets''')
      cursor.execute('''DELETE FROM pieces''')
      cursor.execute('''DELETE FROM inventaire''')
      cursor.execute('''DELETE FROM bijoux''')
      cursor.execute('''DELETE FROM vie''')
      db_loc.commit()
      db_loc.close()

def creationBase():
      """ CREATION DE LA BASE "livre_hero.db" """
      db_loc = sqlite3.connect(chemin)
      cursor = db_loc.cursor()

      # CREATION DE LA TABLE "quete"
      cursor.execute('''CREATE TABLE IF NOT EXISTS quete(
                  pageId INTEGER,
                  texte TEXT);''')

      # CREATION DE LA TABLE "creatures"
      cursor.execute('''CREATE TABLE IF NOT EXISTS creatures(
                  pageId TEXT,
                  nom TEXT,
                  habilete INTEGER,
                  endurance INTEGER
                  vivant INTEGER);''')

      # CREATION DE LA TABLE "armes_protection"
      cursor.execute('''CREATE TABLE IF NOT EXISTS armes_protection(
                  idObjet INTEGER,
                  objet TEXT,
                  nombre INTEGER,
                  habilete INTEGER,
                  endurance INTEGER,
                  chance INTEGER);''')

      # CREATION DE LA TABLE "objets"
      cursor.execute('''CREATE TABLE IF NOT EXISTS objets(
                  idObjet INTEGER,
                  objet TEXT,
                  nombre INTEGER,
                  habilete INTEGER,
                  endurance INTEGER,
                  chance INTEGER);''')

      # CREATION DE LA TABLE "pieces"
      cursor.execute('''CREATE TABLE IF NOT EXISTS pieces(
                  idObjet INTEGER,
                  objet TEXT,
                  nombre INTEGER);''')

      # CREATION DE LA TABLE "inventaire"
      cursor.execute('''CREATE TABLE IF NOT EXISTS inventaire(
                  idObjet INTEGER,
                  objet TEXT,
                  nombre INTEGER,
                  habilete INTEGER,
                  endurance INTEGER,
                  chance INTEGER);''')

      # CREATION DE LA TABLE "bijoux"
      cursor.execute('''CREATE TABLE IF NOT EXISTS bijoux(
                  idObjet INTEGER,
                  objet TEXT,
                  nombre INTEGER,
                  habilete INTEGER,
                  endurance INTEGER,
                  chance INTEGER);''')

      # CREATION DE LA TABLE "vie"
      cursor.execute('''CREATE TABLE IF NOT EXISTS vie(
                  habilete INTEGER,
                  endurance INTEGER,
                  chance INTEGER);''')
