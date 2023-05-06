from string import ascii_lowercase as alphabet

if __name__ == '__main__':

    my_str = 'abc'
    my_list = []

    for lettre in alphabet[:10]:
        my_list.append(lettre)

    decalage = 0
    for chiffre in range(1, 10):
        position = chiffre + decalage
        decalage += 1
        my_list.insert(position, chiffre)

    print(my_list)

    position = len(my_list) - 1
    while position >= 0:
        print(my_list[position], end=' ')
        position -= 1

    print()
    index = 0
    for element in my_list:
        if str(element) not in alphabet:
            if element % 2 == 1:
                print(my_list[index - 1], end=" ")
        index += 1

    # Exercice 3
    def somme_liste(liste):
        return sum(liste)

    print(somme_liste([1, 2, 3, 4]))

    # Exercice 4
    liste = [1, 2, 3, 4, 5]
    print(liste)
    if 4 in liste:
        print('4 est dans la liste')
    else:
        print('4 n\'est pas dans la liste')

    liste[0] = 17
    # print(liste)

    liste[2] = liste[1] + liste[3]
    # print(liste)

    liste[0], liste[-1] = liste[-1], liste[0]
    # print(liste)

    for chiffre in liste:
        print(chiffre)
