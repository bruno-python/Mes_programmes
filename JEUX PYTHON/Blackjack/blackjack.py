# Blackjack
# règles : http://fr.wikipedia.org/wiki/Blackjack_(jeu)

from random import randrange
from tkinter import *
from time import sleep
from winsound import PlaySound

couleur = ('pique', 'trefle', 'carreau', 'coeur')
valeur = ('as', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'valet', 'dame', 'roi')

   
def calculer_main(cartes):
    # Les cartes sont des numéros allant de 1 (as) à 13 (roi)
    val = 0
    for carte in cartes:
        if 1 < carte <= 10:
            val += carte
        elif carte > 10:     # buche
            val += 10      
    # valeur de l'as ou des as
    nb_as = cartes.count(1) # Attention s'il y a plusieurs as dans la main
    while nb_as>1:
        val += 1    # un seul as peut valoir 11 pts. Les autres valent 1.
        nb_as -= 1
    if nb_as == 1 and val + 11 <= 21:
        return val + 11
    elif 1 in cartes:
        return val + 1
    else:
        return val    


class Carte(object):
    """Carte a jouer"""
    
    def __init__(self,val='as',coul='carreau'):
        self.valeur = val
        self.couleur = coul

    def dessin_carte(self):
        "Renvoi du nom du fichier image de la carte c"
        # les cartes sont dans le répertoire "cartes", au même niveau que ce programme
        nom = "cartes/"+self.valeur+"_"+self.couleur+".gif"
        return PhotoImage(file=nom)


class Joueur(object):
    """Main du joueur"""
    
    def __init__(self):
        "Construction de la liste des 52 cartes"
        self.main = []

    def ajouter(self, c):
        "Ajoute la carte c"
        # 1:as, 2...10, 11:valet, 12:dame, 13:roi
        self.main.append(valeur.index(c.valeur)+1)

    def total(self):
        "Calcule le total des points de la main"
        return calculer_main(self.main)

    def nb_cartes(self):
        return len(self.main)

    def reinit(self):
        self.main = []


class Paquet_de_cartes(object):
    """Paquet de cartes"""
    
    def __init__(self):
        "Construction de la liste des 52 cartes"
        self.cartes = []
        for coul in range(4):
            for val in range(13):
                nouvelle_carte = Carte(valeur[val], couleur[coul])
                self.cartes.append(nouvelle_carte) 

    def battre(self):
        "Mélanger les cartes"
        PlaySound("sons/distrib.wav",2)
        t = len(self.cartes)
        for i in range(t):
            h1, h2 = randrange(t), randrange(t)
            self.cartes[h1], self.cartes[h2] = self.cartes[h2], self.cartes[h1]

    def tirer(self):
        "Tirer la première carte de la pile"
        PlaySound("sons/ramass.wav",1)
        t = len(self.cartes)
        if t>0:
            carte = self.cartes[0]   # choisir la première carte du jeu
            del(self.cartes[0])      # et la supprimer du jeu
            return carte
        else:
            return None


def reinit():
    global mes_cartes, ses_cartes, mon_score, son_score, moi, coupier
    global jeu, can

    can.delete(ALL)
    can.create_text(60,30,text="Croupier",fill='black',font='Arial 18')
    can.create_text(60,470,text="Joueur",fill='black',font='Arial 18')
    can.update()
    croupier.reinit()
    ses_cartes = []
    jeu = Paquet_de_cartes()
    jeu.battre()    # mélange des cartes
    sleep(1)        # pause d'une seconde
    c = jeu.tirer()
    ses_cartes.append(c.dessin_carte())
    can.create_image(100, 150, image=ses_cartes[0])
    croupier.ajouter(c)
    son_score = can.create_text(150,30,text=str(croupier.total()),fill='black',font='Arial 18')
    can.update()
    sleep(1)

    moi.reinit()    # joueur humain
    mes_cartes = []    
    c = jeu.tirer()
    mes_cartes.append(c.dessin_carte())
    can.create_image(100, 350, image=mes_cartes[0])
    can.update()
    sleep(1)
    moi.ajouter(c)
    c = jeu.tirer()
    mes_cartes.append(c.dessin_carte())
    can.create_image(150, 350, image=mes_cartes[1])
    can.update()
    moi.ajouter(c)
    mon_score = can.create_text(150,470,text=str(moi.total()),fill='black',font='Arial 18')
    can.update()
    if moi.total()==21 :
        can.create_text(250,470,text="Blackjack",fill='red',font='Arial 18')
        can.update()
        sleep(3)
        reinit()


def hit(): # le joueur tire une carte
    global mes_cartes, moi, mon_score, son_score
    c = jeu.tirer()
    mes_cartes.append(c.dessin_carte())
    moi.ajouter(c)
    n = moi.nb_cartes()
    can.create_image(150+50*(n-2), 350, image=mes_cartes[n-1])
    can.delete(mon_score)
    mon_score = can.create_text(150,470,text=str(moi.total()),fill='black',font='Arial 18') 
    can.update()
    if moi.total()>21:
        can.create_text(250,30,text="Gagné",fill='red',font='Arial 18')
        can.update()
        sleep(3)
        reinit()


def stay(): # le joueur s'arrête et le croupier joue
    global ses_cartes, croupier, moi, son_score, mon_score
    c = jeu.tirer()
    ses_cartes.append(c.dessin_carte())
    croupier.ajouter(c)
    n = croupier.nb_cartes()
    can.create_image(100+50*(n-1), 150, image=ses_cartes[n-1])
    can.delete(son_score)
    son_score = can.create_text(150,30,text=str(croupier.total()),fill='black',font='Arial 18') 
    can.update()
    if croupier.total()>21:
        can.create_text(250,470,text="Gagné",fill='red',font='Arial 18')
        can.update()
        sleep(3)
        reinit()
    elif croupier.total()==21 and n==2:
        can.create_text(250,30,text="Blackjack",fill='red',font='Arial 18')
        can.update()
        sleep(3)
        reinit()
    elif croupier.total()<17:
        sleep(2)
        stay()
    else:
        if croupier.total()>moi.total():
            can.create_text(250,30,text="Gagné",fill='red',font='Arial 18')
        elif croupier.total()<moi.total():
            can.create_text(250,470,text="Gagné",fill='red',font='Arial 18')
        can.update()
        sleep(3)
        reinit()


# fenetre graphique
moi = Joueur()
mes_cartes = []
croupier = Joueur()
ses_cartes = []
jeu = Paquet_de_cartes()
fenetre = Tk()
fenetre.title("Blackjack")
can = Canvas(fenetre, width=600, height=500, bg ='white')
can.pack(side=TOP, padx=5, pady=5)
b2 = Button(fenetre, text ='Quitter', width=15, command=fenetre.quit)
b2.pack(side=RIGHT)
b1 = Button(fenetre, text ='Carte !', width=15, command=hit)
b1.pack(side=LEFT)
b1 = Button(fenetre, text ='Je reste', width=15, command=stay)
b1.pack(side=LEFT)
reinit()

# demarrage :
fenetre.mainloop()  
fenetre.destroy()
