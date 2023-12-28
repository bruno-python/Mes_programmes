# Le jeu du juste prix
"""
--L'ordinateur choisit le prix de l'objet entre 30€ et 100€
--Vous devez trouver le prix en un minimum d'essais
--A chaque propositions l'ordinateur vous répondra: c'est plus, c'est moins, c'est gagné

Optimiser le programme:
--Afficher le nombre de tentatives
--On ne peux faire que 10 essais, ensuite l'ordinateur donne la réponse
--A pres 5 essais l'ordinateur previent "Attention plus que 5 tentatives"
--Qu'on puisse mettre code triche pour connaître le résultat
--A la fin de la partie , propose de rejouer
--A la fin de la partie s'affiche:
--le nombre de coups moyens pour trouver le prix
--Le pourcentage de réussite au jeu
"""
import random
moyenne = []
listeCoups = []
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
		
	# Affiche le nombre de coups
	print("Vous avez trouver en {}:".format(cpt))
	listeCoups.append(cpt)
	print("Liste: ",listeCoups)	
	
	# Affiche la moyenne des parties
	j = 0
	total = 0
	while j < len(listeCoups): 
		total = total + listeCoups[j]
		j += 1
		
	cpt = 0
	
	continuePartie = input("Continuer la partie? o/n ")
	if continuePartie == 'n':
		# Moyenne des nombres de coups réussi
		moyenne = total / len(listeCoups)
		print("moyenne des {} parties: {} ".format(len(listeCoups),moyenne))
		# Pourcentage de réusite sur les parties joué 
		pourcentage = (total / (nbreCoupsPartie * 10)) * 100
		print("Le pourcentage de réussite est de {}% sur {} parties".format(pourcentage, nbreCoupsPartie))

