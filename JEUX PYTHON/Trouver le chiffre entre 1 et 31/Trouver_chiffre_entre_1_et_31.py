import os

# Trouver le chiffre entre 1 et 31 (chiffre binaire)

# Grille binaire '1'
g_1 = [
        [3, 7, 23, 19],
        [17, 9, 11, 31],
        [5, 27, 21, 13],
        [1, 25, 29, 15]
      ]

# Grille binaire '2'
g_2 = [
        [14, 16, 10, 27],
        [3, 30, 15, 18],
        [31, 6, 19, 23],
        [2, 7, 11, 22]
      ]

# Grille binaire '4'
g_3 = [
        [6, 5, 20, 14],
        [28, 23, 15, 13],
        [31, 29, 21, 22],
        [4, 30, 7, 12]
      ]

# Grille binaire '8'
g_4 = [
        [14, 10, 15, 31],
        [11, 27, 29, 13],
        [26, 28, 9, 12],
        [8, 30, 25, 24]
      ]

# Grille binaire '16'
g_5 = [
        [17, 23, 19, 25],
        [27, 30, 29, 18],
        [22, 21, 26, 24],
        [16, 28, 31, 20]
      ]

grille = [g_1, g_2, g_3, g_4, g_5]


def affiche_grille(grille):
    print("|- - |- - |- - |- - |")
    for i in grille:
        print(end="| ")
        for j in i:
            if j < 10:
                print(str(j).zfill(2), end=' | ')
            else:
                print(j, end=' | ')
        print("\n|- - |- - |- - |- - |")


def cherche_nombre(grille):
    choix = input("\nEst-ce que le nombre est dans la grille (o/n):")
    if choix == 'o':
        if grille == g_1:
            return 1
        if grille == g_2:
            return 2
        if grille == g_3:
            return 4
        if grille == g_4:
            return 8
        if grille == g_5:
            return 16
    else:
        return 0

#----------------------------------------------
if __name__ == '__main__':
    os.system('cls')
    nombre = 0
    for k in grille:
        print("Choissir un nombre en (1 et 31):\n")
        affiche_grille(k)
        nombre = nombre + cherche_nombre(k)
        os.system('cls')
    print('-------------------')
    print(f'| Ton nombre est: {nombre} |')
    print('-------------------\n')

