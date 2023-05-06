chiffres = [1, 2, 3]
print(len(chiffres))
chiffres.insert(2, 'a')
print(chiffres)

chiffres.pop(-2)
print(chiffres)

lettres = ['a', 'b', 'c', 'a']
chiffres.insert(1, lettres)
print(chiffres)

chiffres.extend(lettres)
print(chiffres)

print(chiffres[1][2])

for lettre in lettres:
    print(lettre)

for index in range(len(lettres)):
    if lettres[index] == 'a':
        lettres.pop(index)
        lettres.insert(index, 'b')
print(lettres)

lettres2 = []
for lettre in lettres:
    if lettre == 'a':
        lettres2.append('b')
    else:
        lettres2.append(lettre)
print(lettres)

list2 = list(range(10))
print(list2)

print('========')
# pair => x2 / impair => -1
for index in range(len(list2)):
    if list2[index] % 2 == 0:
        list2[index] = list2[index]*2
    else:
        list2[index] = list2[index]-1

print(list2)
