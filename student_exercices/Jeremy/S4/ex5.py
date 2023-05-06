for lettre in "Ab cd":
    print(lettre)

texte = "Homme libre, toujours tu chériras la mer !"
compteur = 0
for lettre in texte:
    if lettre == "e":
        compteur += 1

print(compteur)

print('\n\n')

k = 0
while k < 6:
    print(k)
    k += 2

k = 0
while k < 6:
    k += 2
    print(k)

# 0 / 3 / 6 / 9 / 12
n = 0
while n <= 12:
    print(n)
    n += 3

# la plus petite valeur de n telle que n²+3n dépasse 1000
n = 0
while (n ** 2) + (3 * n) <= 1000:
    n += 1
print(n)

# affiche la plus petite valeur de n telle que 2*1+ 2*2 + 2*3 + ... + 2*n dépasse 10000 ?
n = 0
somme = 0
while somme < 10000:
    n += 1
    somme += n*2
print(n)

