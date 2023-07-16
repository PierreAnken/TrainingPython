l1 = ['a', 'b', 'c']
s1 = 'abc'

print(l1[1], s1[1])

l1 += l1
print(l1)

liste = []
liste.extend(range(1, 10, 2))
print(liste)

del liste[-1]
print(liste)

liste.append(5)
print(liste)

print(liste.count(5))

liste[0] = 2
print(liste)

s1 = 'Sabrina Smith'
print(s1[8:13])

print(s1[::2])

# vérification d'age
age = 18
if age > 18:
    print('Majeur')
elif age < 18:
    print('Mineur')
else:
    print('Exactement 18')

# Nombre pairs entre 1 et 10
for x in range(11):
    if x % 2 == 0:
        print(x)

# Tant que x < 5 on continue
x = 0
while 5 > x:
    x += 1
    print(x)

# Test si deux mots sont inverses
mot1 = 'test'
mot2 = 'tset'

if mot1 == mot2[::-1]:
    print('Inverses')
else:
    print('Pas inverses')


