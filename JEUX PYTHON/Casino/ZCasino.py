import os
from math import ceil
from random import randrange

print("----------- ZCasino----------")
print("Regle du jeu")
print("Miser sur un numero compris entre 0 et 49")
print("Si le numero sortie est le meme que le votre: votre mise + 3 fois la mise")
print("si les deux numeros sont pair ou les deux impair: votre mise + 50% de la mise\n")

print("Debut du jeux")
print("Votre gains de depart: 100 euros\n")
argent = 100
continuer_partie = True

while continuer_partie:
	# Demande du numero a l'utilisateur
	numero = -1
	while numero < 0 or numero > 49:
		numero = input("Entre un numero(entre 0 et 49): ")
		# Conversion du numero choisi 
		try:
			numero = int(numero)	
		except ValueError:
			print("Tu n'as pas saisi de nombre")
			numero = -1
			continue
		if numero < 0:
			print("Ce nombre est negatif")
		if numero > 49:
			print("Ce nombre est superieur a 49")
	
	# Demande de la somme a miser
	mise = 0
	while mise <= 0 or mise > argent:
		mise = input("Entre une mise maxi: ")
		# Conversion de la mise
		try:
			mise = int(mise)
		except ValueError:
			print("Tu n'as pas saisi de nombre")
			mise = -1
			continue
		if mise <= 0:
			print("Cette mise est negative ou nulle")
		if mise > argent:
			print("Tu ne peux pas miser autant, vous n'avez que", argent, "euros")
	
	# Lancement de la roulette	
	croupier = randrange(50)
	print("La roulette s'arrete sur le numero", croupier)

	if numero == croupier:
		argent += (3*mise)
	elif numero % 2 == croupier % 2:
		argent += ceil(mise / 2)
	else:
		argent -= mise
	
	# Fin de partie si le joueur est ruine
	if argent <= 0:
		print("Tu n'as plus d'argent, c'est la fin de la partie")
		continuer_partie =False
	else:
		print("Vos gain: ", argent, "euros")
		quitter = input("Veux tu quitter le casino (o/n) ?")
		if quitter == "o" or quitter == "O":
			print("A bientot dans notre casino")
			continuer_partie = False
	print('-------------')

os.system("pause")