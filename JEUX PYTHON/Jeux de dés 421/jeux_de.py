from random import randrange

# Résultat des dés a comparer apres la fin de tous les lancés:

gain_1 = [4,2,1] # Autant de jetons qu'il y a dans le pot -1
gain_2 = [[1,1,6],[1,1,5],[1,1,4],[1,1,3],[1,1,2]] # Autant de jetons que le dernier nombre
gain_3 = [[6,5,4],[5,4,3],[4,3,2],[3,2,1]] # 2 jetons
# sinon un jetons
tirage_des = []
des_garder = []
# ------------- Lancer de dés -------------------------
def lancerDes():
    de = randrange(1,7)
    return de

# ------------- Tirage dés -------------------------
def tirage(nbDes):
    tirage_des[:] = []
    i = 0
    while i < nbDes:
        nbre = lancerDes()
        tirage_des.append(nbre)
        i += 1

# ------------- Dés à gardés après tirage -------------------------
def desGarder():
    global des_garder

    # garde tous
    choix = eval(input('Tu garde quoi?: '))
    if choix == 1:
        des_garder = tirage_des
        #print(f'Dés gardés{des_garder}')
        tirage(0)
        afficherTirage(0)
        return des_garder

    # En garde deux
    elif choix == 2:
        des_garder.append(tirage_des[0])
        des_garder.append(tirage_des[1])
        #print(f'Dés gardés{des_garder}')
        tirage(1)
        afficherTirage(1)
        return des_garder
    elif choix == 3:
        des_garder.append(tirage_des[0])
        des_garder.append(tirage_des[2])
        #print(f'Dés gardés{des_garder}')
        tirage(1)
        afficherTirage(1)
        return des_garder
    elif choix == 4:
        des_garder.append(tirage_des[1])
        des_garder.append(tirage_des[2])
        #print(f'Dés gardés{des_garder}')
        tirage(1)
        afficherTirage(1)
        return des_garder

    # En garde un
    elif choix == 5:
        des_garder.append(tirage_des[0])
        #print(f'Dés gardés{des_garder}')
        tirage(2)
        afficherTirage(2)
        return des_garder
    elif choix == 6:
        des_garder.append(tirage_des[1])
        #print(f'Dés gardés{des_garder}')
        tirage(2)
        afficherTirage(2)
        return des_garder
    elif choix == 7:
        des_garder.append(tirage_des[2])
        #print(f'Dés gardés{des_garder}')
        tirage(2)
        afficherTirage(2)
        return des_garder
    elif choix == 30:
        tirage(3)
        afficherTirage(3)
        return des_garder
    elif choix == 20:
        tirage(2)
        afficherTirage(2)
        return des_garder
    elif choix == 10:
        tirage(1)
        afficherTirage(1)
        return des_garder
    else:
        print("Je n'ai pas compris ton choix!")

# ------------- Affiche le lancé de dés -------------------------
def afficherTirage(des=3):
    if len(tirage_des) == 0:
        tirage(3)

    if des == 3:
        print('---------------------')
        print(f'Dés gardés{des_garder}')
        print(f'Tirage: {tirage_des}')
        print('---------------------')
        print(f'(1)-> [{tirage_des[0]}], [{tirage_des[1]}], [{tirage_des[2]}]')
        print(f'(2)-> [{tirage_des[0]}], [{tirage_des[1]}]')
        print(f'(3)-> [{tirage_des[0]}], [{tirage_des[2]}]')
        print(f'(4)-> [{tirage_des[1]}], [{tirage_des[2]}]')
        print(f'(5)-> [{tirage_des[0]}]')
        print(f'(6)-> [{tirage_des[1]}]')
        print(f'(7)-> [{tirage_des[2]}]')
        print(('(30)-> Aucun'))
        print('---------------------')
        desGarder()
    elif des == 2:
        print('---------------------')
        print(f'Dés gardés{des_garder}')
        print(f'Tirage: {tirage_des}')
        print('---------------------')
        print(f'(1)-> [{tirage_des[0]}], [{tirage_des[1]}]')
        print(f'(2)-> [{tirage_des[0]}]')
        print(f'(3)-> [{tirage_des[1]}]')
        print(('(20)-> Aucun'))
        print('---------------------')
        desGarder()
    elif des == 1:
        print('---------------------')
        print(f'Dés gardés{des_garder}')
        print(f'Tirage: {tirage_des}')
        print('---------------------')
        print(f'(1)-> [{tirage_des[0]}]')
        print(('(10)-> Aucun'))
        print('---------------------')
        desGarder()



# --- menu ---
print("\n---- JEUX DU 421 ----\n")
afficherTirage()
print(f'***{des_garder}')

