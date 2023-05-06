from string import ascii_lowercase as alphabet

if __name__ == '__main__':

    # Note Jean : on commence par créer une mise à la ligne /
    print('\nFor each')

    # on ne prend que les 3 premières lettres de l'alphabet
    # et on insère un espace entre chaque lettre trouvée.
    for letter in alphabet[:3]:  # ['a','b','c']
        print(letter, end=' ')

    print('\n\nFor each - enumerate')
    for index, letter in enumerate(alphabet[:3]):
        print(index, letter, end=' ')
    # Note Jean: on veut la position de chaque lettre (via enumerate) et la lettre elle-même

    print('\n\nFor i')
    for letter_number in range(3):  # [0, 1, 2]
        # ['a','b', ...]
        print(alphabet[letter_number], end=' ')
    # Note Jean : letter_number permet ici d'aller chercher les 3 premières lettres via range(3) dans la liste alphabet

    print('\n\nWhile')
    letter_number = 25
    while letter_number > 0:
        print(alphabet[letter_number], end=' ')
        letter_number -= 2
    # Note Jean : on print une lettre sur 2 (+= 2) sur les 26 positions de l'alphabeth.
    # Pourquoi préciser letter_number = 0... est-ce pour démarrer par la première lettre ?

    print('\n\nBreak')
    for letter in alphabet:
        print(letter, end=' ')
        if letter == 'o':
            break
    # Note Jean : on print toutes les lettres jusqu'à rencontrer la lettre "o" et le code s'arrête via break.

    print('\n\nContinue')
    for letter_number in range(26):
        if letter_number % 2 == 1:
            continue
        print(alphabet[letter_number], end=' ')
    # Note Jean : pas compris if letter_number % 2 == 1...
    # le code ne conserve la lettre que si elle est en position impaire dans la liste ?
    # trouvé explication sur internet : n % 2 == 1 signifie renvoyer Vrai si le reste de n / 2 est égal à un,
    # ce qui revient à vérifier si n est un nombre impair.

    print('\n\nLoop in loop')
    for letter1 in alphabet:
        if letter1 == 'd':
            break

        for letter2 in alphabet[::-1]:
            if letter2 == 'w':
                break
            print(letter1, letter2, sep='/', end=' ')

# Note Jean : si le code tombe su rla lettre 'd' il s'arrête et cherche la lettre suivante 'letter2' en partant depuis la fin [::-1]
# ensuite si le code renoncontre la 2e lettre 'w' il s'arrête et print letter1 (de a à c) / letter2 (de z à x depuis la fin)


# EXPLIQUER LA LOGIQUE DU CODE DE LA SUITE DE FIBONACCI
# the sum of two elements defines the next
print('\n\nFibo 1')
a, b = 0, 1  # 0 1 1 [2 3] 5 8 13
while a < 15:
    print(a, end=' ')
    a, b = b, a + b

''''
0
1
1
2
3
5
8'''

print('\n')
a, b = 0, 3
while a < 100:
    print(a, end=' ')
    a, b = b, a + b

print('\n\nZip')


mot = 'sugus'
for letter_debut, letter_fin in zip(mot, mot[::-1]):
    if letter_debut != letter_fin:
        print(mot, 'm\'est pas un palindrome')
        break
else:
    print(mot, 'est un palindrome')
