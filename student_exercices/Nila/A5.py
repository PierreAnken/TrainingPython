def get_maxima():
    # liste_str = input('Geben Sie ein liste von nummer ein: Bsp: 2,5,4,3,')
    liste_str = '2,5,4,3,3,7,6,1' # nur fur schnell testen
    liste_str = liste_str.split(',')

    maxima_liste = []
    for index in range(1, len(liste_str) - 1):

        number_before = int(liste_str[index - 1])
        number = int(liste_str[index])
        number_after = int(liste_str[index + 1])

        if number_before < number > number_after:
            maxima_liste.append(number)

    print(maxima_liste)


get_maxima()
