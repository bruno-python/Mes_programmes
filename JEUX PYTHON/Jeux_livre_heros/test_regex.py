import re

def cheminPossible(p):
    chemin = 'P:\\PROGRAMMATION\\PYTHON\\JEUX\\Jeux_livre_heros\\pages\\'

    # pattern = r"(rendez-vous(.)* au [0-9]{1,3})"
    pattern = r"(COMBATTANT : [A-Z]*.\d{1})"


    with open(chemin + str(p) + ".txt", 'r') as file:
        texte = file.read()
        rechercher = re.finditer(pattern, texte, re.MULTILINE)

        for recherche in rechercher:
            print (f"{recherche.group()}")


cheminPossible(19)
