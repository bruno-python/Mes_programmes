import os
from fonctions import *
from backup_jeux import *
from creation_des_tables import *
from ajout_contenu_table import *
global ap

# Reinisalisation des tables et du contenu origines des tables
def restaurationOrigine():
    global ap
    ''' Restaure le jeux origine nouvelle partie'''
    deleteTable()
    creationBase()
    ajoutContenuArmes()
    ajoutContenuCreatures()
    ajoutContenuObjets()
    ajoutContenuOr()
    ajoutContenuBijoux()
    ajoutContenuProvisionsPotions()
    ajoutContenuVie()
    # debut des parametres
    parametres()
    print('choissir une arme ou une protection')
    afficherArmesProtections()
    ap = eval(input("Entre le numéro de l'arme: "))
    arme(ap)
    os.system('cls')
    choisirPotion()
    os.system('cls')
    afficherPage()

def restaurationBackup():
    ''' Restaure la partie sauvegarder '''
    deleteTable()
    creationBase()
    ajoutBackupArmes()
    ajoutBackupObjets()
    ajoutBackupCreatures()
    ajoutBackupOr()
    ajoutBackupBijoux()
    ajoutBackupProvisionsPotions()
    ajoutBackupVie()
    # afficherPage()

def main():
    global ap
    pageEnCours = 1
    choix = ''
    while choix != 9:
        print()
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        personnage(a=arme(ap), h=habilete(), e=endurance(), c=chance()) # pieces, bijoux
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("(0) - Lancé de dés")
        print("(1) - Poursuivre la partie")
        print("(2) - Changer armes")
        print("(3) - Afficher bijoux")
        print("(4) - Afficher objets")
        print("(5) - Afficher provisions et potions")
        print("(6) - Modifier l'inventaire")
        print("(7) - Combattre une créature")
        print("(8) - Tenter votre chance")
        print("(9) - Quitter et sauvegarder")

        choix = eval(input('Tu choissis quoi ?: '))
        os.system('cls')

        if choix == 0: #lancé de dés
            nb = int(input("Nombre de dé à lancé?: "))
            lancerDes(nb)

        elif choix == 1: # pages
            os.system('cls')
            cheminPossible(pageEnCours)
            p = eval(input('Entre le numéro où tu veux aller?: '))
            os.system('cls')
            afficherPage(p)
            pageEnCours = p


        elif choix == 2: # armes et protections
            afficherArmesProtections()
            a = eval(input("Entre le numéro de l'arme: "))

            os.system('cls')

        elif choix == 3: # bijoux
            afficherBijoux()


        elif choix == 4: # objets
            afficherObjets()


        elif choix == 5: # provisions et potions
            afficherProvisionsPotions()


        elif choix == 6: # inventaire (Ajouter ou supprimer)
            modifierInventaire()


        elif choix == 7: # combattre une créature
            combatCreature()
            print(pageEnCours)

        elif choix == 8:
            tenterChance()

        elif choix == 9:
            print('SAUVEGARDE DE LA PARTIE EN COURS')
            backup(pageEnCours)



choix = ''
while choix != 3:
    print("(1) - Nouvelle partie")
    print("(2) - Continuer la partie en cours")
    print("(3) - Quitter")

    choix = eval(input('Tu choissis quoi ?: '))
    os.system('cls')

    if choix == 1:
        restaurationOrigine()
        main()

    elif choix == 2:
        restaurationBackup()
        main()

