from collections import Counter

dict_mots = ['camion', 'bateau', 'ete', 'tee']
# Print the array containing all defintions of "Fromage"

mot_entre = 'incamo'

for mot in dict_mots:

    if Counter(mot) == Counter(mot_entre):
        print('avec les lettres', mot_entre, 'on peut former le mot', mot)
