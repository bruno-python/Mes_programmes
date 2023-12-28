def move(source, cible):
    print(f'Deplace le disque de {source} vers {cible}')

def hanoi(nbre, source, libre, cible):
    """
    nbre  : nombre de disque
    source: position de départ
    cible : position arrivé
    libre : position libre
    """
    if nbre == 0:
        pass
    else:
        hanoi(nbre-1, source, cible, libre)
        move(source, cible)
        hanoi(nbre-1, libre, source, cible)


hanoi(4, 'A', 'B', 'C')
