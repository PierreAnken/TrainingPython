mot = input('Entrez un mot: ')

for index in range(len(mot)//2):
    if mot[index] != mot[-1-index]:
        print(mot, 'n\'est pas un palindrome')
        break
else:
   print(mot, 'est un palindrome')
