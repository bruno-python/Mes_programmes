import sqlite3

# Sauvegarde de tous les parametres en cours de jeux

chemin = 'P:\\PROGRAMMATION\\PYTHON\\JEUX\\Jeux_livre_heros\\livre_hero.db'
def backup(page=1):
    def backupVie():
        db_loc = sqlite3.connect(chemin)
        cursor = db_loc.cursor()
        parametresVie = cursor.execute("SELECT * FROM vie")
        for line in parametresVie:
            return line
        db_loc.commit()
        db_loc.close()

    def backupProvisionsPotions():
        db_loc = sqlite3.connect(chemin)
        cursor = db_loc.cursor()
        parametresProvitionsPotions = cursor.execute("SELECT * FROM provisions_potions")
        for line in parametresProvitionsPotions:
            listeProvisionsPotions.append(line)
        db_loc.commit()
        db_loc.close()

    def backupObjets():
        db_loc = sqlite3.connect(chemin)
        cursor = db_loc.cursor()
        parametresObjets = cursor.execute("SELECT * FROM objets")
        for line in parametresObjets:
            listeObjets.append(line)
        db_loc.commit()
        db_loc.close()

    def backupPieces():
        db_loc = sqlite3.connect(chemin)
        cursor = db_loc.cursor()
        parametresPieces = cursor.execute("SELECT * FROM pieces")
        for line in parametresPieces:
            return line
        db_loc.commit()
        db_loc.close()

    def backupBijoux():
        db_loc = sqlite3.connect(chemin)
        cursor = db_loc.cursor()
        parametresBijoux = cursor.execute("SELECT * FROM bijoux")
        for line in parametresBijoux:
            listeBijoux.append(line)
        db_loc.commit()
        db_loc.close()

    def backupArmes():
        db_loc = sqlite3.connect(chemin)
        cursor = db_loc.cursor()
        parametresArmes = cursor.execute("SELECT * FROM armes_protection")
        for line in parametresArmes:
            listeArmes.append(line)
        db_loc.commit()
        db_loc.close()

    def backupCreatures():
        db_loc = sqlite3.connect(chemin)
        cursor = db_loc.cursor()
        parametresCreatures = cursor.execute("SELECT * FROM creatures")
        for line in parametresCreatures:
            listeCreatures.append(line)
        db_loc.commit()
        db_loc.close()

    def backupPageEnCours():
        pageEnCours = page
        print('page',pageEnCours)



    # SAUVEGADRE DANS UN FICHIER TEXTE
    listeVie = backupVie()
    with open('txt/backup_vie.bak', 'w', encoding='utf-8') as file:
        print("# Sauvegadre parametres de vie (h, e, c)")
        for line in listeVie:
            file.write(str(line) + ',')

    listeProvisionsPotions = []
    backupProvisionsPotions()
    with open('txt/backup_provisions_potions.bak', 'w', encoding='utf-8') as file:
        print("# Sauvegarde parametres provisions et potions")
        for line in listeProvisionsPotions:
            for i in line:
                file.write(str(i) + ',')
            file.write('\n')

    listeObjets = []
    backupObjets()
    with open('txt/backup_objets.bak', 'w', encoding='utf-8') as file:
        print("# Sauvegarde parametres d'objets")
        for line in listeObjets:
            for i in line:
                file.write(str(i) + ',')
            file.write('\n')

    listePieces = backupPieces()
    with open('txt/backup_or.bak', 'w', encoding='utf-8') as file:
        print("# Sauvegarde parametres de pièces d'or")
        file.write(str(listePieces) + ',')

    listeBijoux = []
    backupBijoux()
    with open('txt/backup_bijoux.bak', 'w', encoding='utf-8') as file:
        print("# Sauvegarde parametres des bijoux")
        for line in listeBijoux:
            for i in line:
                file.write(str(i) + ',')
            file.write('\n')

    listeArmes = []
    backupArmes()
    with open('txt/backup_armes.bak', 'w', encoding='utf-8') as file:
        print("# Sauvegarde parametres des armes")
        for line in listeArmes:
            for i in line:
                file.write(str(i) + ',')
            file.write('\n')

    listeCreatures = []
    backupCreatures()
    with open('txt/backup_creatures.bak', 'w', encoding='utf-8') as file:
        print("# Sauvegarde parametres des creatures")
        for line in listeCreatures:
            for i in line:
                file.write(str(i) + ',')
            file.write('\n')
        print('#------------------------------------#')


if __name__ == '__main__':
    backup()
