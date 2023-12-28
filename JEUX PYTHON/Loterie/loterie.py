from random import randint

nouveau_nombre = 0
loterie = []
mes_nombres = []
cpt = 0

while len(loterie) < 5:
    nouveau_nombre = randint(1, 50)
    if nouveau_nombre not in loterie:
        loterie.append(nouveau_nombre)

print("Trouve les 5 nombres du tirage de la loterie")
print("--------------------------------------------")
while len(mes_nombres) < 5:
    nouveau_nombre = eval(input('Entrez vos nombres entre 1-50: '))
    if nouveau_nombre not in mes_nombres and nouveau_nombre <= 50 or nouveau_nombre > 0:
        mes_nombres.append(nouveau_nombre)

for nombre in loterie:
    for mom_nombre in mes_nombres:
        if nombre == mom_nombre:
            cpt += 1

print('Vous avez ' + str(cpt) + ' trouvé!')
print('Les nombres de la loterie: ')
print(loterie )


