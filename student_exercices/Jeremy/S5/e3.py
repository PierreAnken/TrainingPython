# liste_entiers = list(map(int, input("saisissez une liste d'entier (3 5 54)").split()))
liste_entiers = [2, 58, 6, 99, 84]
print(liste_entiers)

for index, value in enumerate(liste_entiers):
    print(index, value)

somme = sum(liste_entiers)
print(somme)

list_triple = []
for value in liste_entiers:
    list_triple.append(value*3)

print(list_triple)

print(max(liste_entiers))
print(min(liste_entiers))

compteur = 0
for chiffre in liste_entiers:
    if chiffre % 2 == 0:
        compteur+=1
print(compteur)

somme=0
for chiffre in liste_entiers:
    if chiffre % 2 == 1:
        somme+=chiffre
print(somme)

