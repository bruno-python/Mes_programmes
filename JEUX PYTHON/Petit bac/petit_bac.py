from pathlib import Path

"""
Jeux du petit bac
"""

chemin = Path(__file__).parent
chemin_1 = chemin /"Listes"

liste_mots = ["Anatomie",
              "Animaux",
              "Capitales",
              "Couleurs",
              "Fruits",
              "Legumes",
              "Metiers",
              "Outils",
              "Pays",
              "Prenoms feminin",
              "Prenoms masculin",
              "Transports",
              "Verbes"]

# choix = input("Choissir une lettre: ")

for i in liste_mots:
    dossier = i + ".txt"
    #print(chemin_1 / dossier)
    print(f'***{i}***')
    with open(chemin_1 /dossier, encoding='utf-8') as file:
        #lecture = file.readlines()
        for mot in file:
            if mot[0] == "A" or mot[0] == "a":
                print(mot)


