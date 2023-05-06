import random
from string import ascii_lowercase as alphabet

# un texte, entre 20 et 50 mots, chaque mot 3 et 8 lettres aleatoires dans l'alphabet.
# première lettre majuscule, et a la fin un .

ponctuations = ',:;'
voyelles = 'aeiouy'

phrase = ""
# mots
for _ in range(random.randint(10, 20)):

    # lettres
    mot = ""
    derniere_lettre = ''
    for _ in range(random.randint(3, 8)):
        if derniere_lettre not in voyelles:
            lettre = voyelles[random.randint(0, len(voyelles)-1)]
        else:
            lettre = alphabet[random.randint(0, 25)]

        derniere_lettre = lettre
        mot += lettre
    phrase += mot + " "

compteur = 0
index_espaces = []
for caractere in phrase:
    if caractere == " ":
        index_espaces.append(compteur)
    compteur += 1

index_choisi = index_espaces[random.randint(0, len(index_espaces) - 1)]
ponctuation = ponctuations[random.randint(0, len(ponctuations) - 1)]

phrase = phrase.capitalize()[0: -1] + "."
phrase = phrase[0: index_choisi] + ponctuation + phrase[index_choisi: len(phrase)]

mots = phrase.split()
chiffre = random.randint(1,100)
mots.insert(random.randint(0,len(mots)-1), str(chiffre))
phrase = ' '.join(mots)

print(phrase)
