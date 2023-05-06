hauteur_pyramide = 9
pyramide = []

for index_etage_pyramide in range(hauteur_pyramide):
    etage_pyramide = []
    centre = index_etage_pyramide + 1

    for valeur in range(1, centre + 1):
        etage_pyramide.append(valeur)

    for valeur in range(centre - 1, 0, -1):
        etage_pyramide.append(valeur)

    pyramide.append(etage_pyramide)

largueur_pyramide = hauteur_pyramide * 4 - 1
largueur_etage = 1
for index_etage in range(hauteur_pyramide):
    espace_gauche = (largueur_pyramide - largueur_etage) // 2
    etage_str = espace_gauche * ' '
    for valeur in pyramide[index_etage]:
        etage_str += str(valeur) + ' '
    print(etage_str[:-1])
    largueur_etage += 4


