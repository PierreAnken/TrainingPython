from pprint import pprint
from string import ascii_lowercase as alphabet

liste = list(range(1, 11))
print(liste)

liste = liste[1::2] + liste[::2]
print(liste)

for index in range(0, len(liste)):
    liste[index] **= 2
print(liste)

index = 0
while index < len(liste):
    if liste[index] % 4 != 0:
        liste.remove(liste[index])
    else:
        index += 1
print(liste)

for index in range(0, len(liste)):
    liste[index] = int(str(liste[index])[::-1])
print(liste)

for index in range(0, len(liste) // 2):
    # liste[0], liste[4] = [5]*2
    liste[index], liste[-1 - index] = [liste[index] + liste[-1 - index]] * 2
print(liste)

for index in range(0, len(liste)):
    liste[index] *= "*"
pprint(liste)

for index_liste in range(0, len(liste)):
    for index_texte in range(0, len(liste[index_liste])):
        liste[index_liste] = liste[index_liste][:index_texte] + alphabet[index_texte % 26] + liste[index_liste][index_texte + 1:]
pprint(liste)

texte = 'bonjour, comment tu vas brutus?'
for index_texte in range(0, len(texte)):
    if texte[index_texte] in alphabet:
        texte = texte[:index_texte] + alphabet[(alphabet.find(texte[index_texte])+5) % 26] + texte[index_texte + 1:]
    else:
        texte = texte[:index_texte] + texte[index_texte] + texte[index_texte + 1:]
print(texte)

