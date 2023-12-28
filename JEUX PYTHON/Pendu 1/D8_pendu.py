# Le jeu du pendu:
import random
import os
os.chdir('p:/programmation/python/jeux/pendu 1')

def tirage():
	""" Tirage du mot aléatoire """
	#tirageMot = choice(listeMot)
	fichier = open("motPendu.txt", "r")
	num = random.randint(1, 29)
	i = 0
	while i < num:
		tirageMot = fichier.readline().replace('\n', '')
		i += 1
	fichier.close()	
	return tirageMot
	
def recupererLettre():
	""" Récuperer et vérifier la lettre du joueur """
	lettreJoueur = input("\nDonner un lettre: ").upper()
	if lettreJoueur in lettreTrouvees:
		print("*** Lettre déja tirée ***")
		return recupererLettre()
	else:
		lettreTrouvees.append(lettreJoueur)	
	return lettreTrouvees
	
def afficheMotMasque(word, letter): 
	""" Vérifie la lettre avec le joueur 
	m = motATrouver, l = lettreTrouvees """
	motMasque = ''
	for c in word:
		if c in letter:
			motMasque += c.upper()
		else:
			motMasque += "_ "
	return motMasque

# ------------- Menu principale ----------------
continuePartie = 'o'
while continuePartie != 'n':
	motATrouver = tirage()	
	lettreTrouvees = []
	motTrouve = ''
	#print(motATrouver)# temporaire contrôle jeu
	coups = 0
	chance = 7
	while chance >= 0 and motTrouve != motATrouver: 
		recupererLettre()
		coups += 1
		motTrouve = afficheMotMasque(motATrouver, lettreTrouvees)
		if motTrouve == motATrouver:
			print("*******************************************")
			print("Bravo, pas de pendu aujourd'hui !!!")
			print("Tu as trouve le mot qui est: {} en {} coups".format(motATrouver, coups))
			print("*******************************************")
		elif chance == 0:
			print("*******************************************")
			print("*** Désolé, tu vas être pendu !!! ***")
			print("Le mot à trouve était: ", motATrouver)
			print("*******************************************")
		else:
			print(motTrouve)
		chance -= 1
	
	continuePartie = input("Veux tu rejoué: o/n ")
	


	
	
	
