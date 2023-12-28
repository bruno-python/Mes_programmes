from os.path import exists
import os
import time
import sys
import subprocess

print('Verifie si pip est a jour')
subprocess.run([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])

if exists('liste_lib_pip.txt'):
    os.remove('liste_lib_pip.txt')

print('Creation du fichier des librairies a mettre a jour ...')
subprocess.run(['pip', 'list', '-o', '>>', 'liste_lib_pip.txt'], shell=True)
time.sleep(10)

liste = []
with open('liste_lib_pip.txt', encoding='utf-8') as file:
    for lines in file:
        for line in lines.split():
            if line != '':
                liste.append(line)

if len(liste) == 0:
    print('Pas de mise a jour a faire ...')
else:
    with open('liste_lib_pip.txt', 'r') as file:
        line = file.read()
        print(line)

# sys.executable (chemin de l'executable de python)
for i in range(8, len(liste), 4):
    subprocess.run([sys.executable, '-m', 'pip', 'install', liste[i], '--upgrade'])
