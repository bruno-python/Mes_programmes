"""
Stoker au fur et a mesure les résultats et pour afficher ainsi les statistiques
"""
#import math
import random
import os

os.chdir('p:/programmation/python/Apprendre par le jeu')

fichier = open("resultat.txt", "a")
#moyenne = []
#listeCoups = []
nbreCoupsPartie = 0
continuePartie = ' '

while continuePartie != 'n':
	
	nbreCoupsPartie += 1

	# Tirage du prix par l'ordinateur
	ordinateur = random.randint(30,100)
	print("----------------------------------------------------")
	print("Trouver le prix de l'objet qui est entre 30€ et 100€")
	print("----------------------------------------------------")
	
	# Recherche du prix par le joueur
	cpt = 0
	i = 0 
	
	while i != 10:
		code = 'triche' # code pour tricher !!!
		joueur = input("Entrer le prix de l'objet: ")
		if joueur == code:
			print("ordinateur prix: ", ordinateur)
		else:
			if int(joueur) == ordinateur:
				print("C'est gagné")
				cpt += 1
				break
			elif int(joueur) > ordinateur:
				print("C'est moins")
				cpt += 1
			elif int(joueur) < ordinateur:
				print("C'est plus")
				cpt += 1
			i += 1
			if i == 5:
				print("ATTENTION plus que 5 tentatives")
		
	# Enregistrement du nombres de coups dans un fichier
	fichier.write(str(cpt) + '\n')
	
	# Affiche le nombre de coups
	print("Vous avez trouver en {} coups:".format(cpt))
	continuePartie = input("Continuer la partie? o/n ")
	
	if continuePartie == 'n':
		fichier.close()
		# Moyenne des nombres de coups réussi
		fichier = open("resultat.txt", "r")
		total = 0
		moyenne = 0
		ligne = 0
		for coups in fichier:
			ligne += 1
			total = total + int(coups)
		moyenne = total / ligne
		fichier.close()
		# Pourcentage de réusite sur les parties joué 
		pourcentage = (total / (total * 10)) * 100
		print("-----------------------------")
		print("moyenne des {} parties: {} ".format(ligne, round(moyenne, 2)))
		print("Le pourcentage de réussite est de {}% sur {} parties".format(round(pourcentage,2), ligne))	
	
	