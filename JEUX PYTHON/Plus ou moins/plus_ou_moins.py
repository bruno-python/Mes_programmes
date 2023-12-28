#Programme du jeu "plus ou moins"

import random

VALEUR_MAX = 1000

print("************** JEU DU PLUS OU MOINS V1.0 ***************\n\
Je viens de penser à un nombre entre 1 et "+ str(VALEUR_MAX) +"\nDevines lequel ?")

nbreAleatoire = random.randint(1, VALEUR_MAX) # Ou random.randrange(1, 100)

while(True):
      nbreUser = int(input("Votre valeur ? "))

      if(nbreUser > nbreAleatoire):
            print("Votre nombre est trop grand")
      elif(nbreUser < nbreAleatoire):
            print("Votre nombre est trop petit")
      else:
            print("Bingo !!!")
            break
            
