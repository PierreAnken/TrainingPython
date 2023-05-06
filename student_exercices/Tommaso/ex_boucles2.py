import math

dictionnaire = {}
for chiffre in range(1,6):
    dictionnaire[chiffre] = chiffre ** 3
print(dictionnaire)

liste = []
for chiffre in range(1,6):
    liste.append((chiffre, chiffre ** 3))
print(liste)

for x in range(5):
    liste[x] = liste[x][0] * liste[x][1]
print(liste)

for x in range(5):
    liste[x] = int(math.sqrt(liste[x]))
print(liste)

for x in range(5):
    if liste[x]% 2 == 0:
        liste[x] -= 1
print(liste)

liste = liste[1:-1]
print(liste)