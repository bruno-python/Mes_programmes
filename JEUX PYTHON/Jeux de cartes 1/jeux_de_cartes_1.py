from random import shuffle,randint
class Carte():

    def __init__(self, f, c):
        self.figure = f
        self.couleur = c

    def affiche (self):
        s = self.figure + " de " + self.couleur
        return (s)

class JeuDeCartes():
    def __init__(self):
        couleur = ["Pique","Coeur","Carreau","Trèfle"]
        valeur = ["As","2","3","4","5","6","7","8","9","10","Valet","Dame","Roi"]

        # Construction de la liste des 52 cartes
        self.cartes = []
        for coul in couleur:
            for val in valeur:
                self.cartes.append(Carte(val,coul))
        return

    #~ Mélange des cartes
    def battre(self):
        shuffle (self.cartes)

    # Tirage la première carte de la pile
    def tirer(self):
        if (len(self.cartes) == 0):
            print("Plus aucune carte")
            return
        else:
            t = randint (0, len(self.cartes)-1)
            carte = self.cartes[t]
            del (self.cartes[t])
            return (carte)

    # Affichage du jeu de carte
    def afficher(self):
        for carte in (self.cartes):
            print (carte.affiche())


if __name__ == '__main__':
    jeu = JeuDeCartes()
    jeu.afficher()

    print('Nous allons mélanger le jeu de cartes\n')

    jeu.battre()
    jeu.afficher()

    print('Nous allons tirer les cartes une à une\n')

    for i in range(52):
        c = jeu.tirer()
        print(f"je viens de tirer la carte: {c.affiche()}")
