import sqlite3
#from combat import *
#from random import randint
import re


chemin = 'P:\\PROGRAMMATION\\PYTHON\\JEUX\\Jeux_livre_heros\\livre_hero.db'

############################# FONCTIONS DIVERS #############################
#--------------------- [PAGE ENCOURS] -------------------------------------
def afficherPage(page= 1):
    """ Affiche tous le contenu de la page """
    db_loc = sqlite3.connect(chemin)
    cursor = db_loc.cursor()
    # Affiche le texte en sélèctionnant pageId
    cursor.execute("SELECT * FROM contenu WHERE pageId=?", (page,))
    texte = cursor.fetchone()
    print('---------------------------[Page N°'+ str(page) +']---------------------------------------------')
    print(texte[1])

    db_loc.commit()
    db_loc.close()

#--------------------- [PAGES SUIVANTES] -------------------------------------
def cheminPossible(p):
    chemin = 'P:\\PROGRAMMATION\\PYTHON\\JEUX\\Jeux_livre_heros\\pages\\'

    pattern = r"(rendez-vous(.)* au [0-9]{1,3})"

    with open(chemin + str(p) + ".txt", 'r') as file:
        texte = file.read()
        rechercher = re.finditer(pattern, texte, re.MULTILINE)

        for recherche in rechercher:
            print (f"{recherche.group()}")