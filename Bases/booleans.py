if __name__ == '__main__':

    print(True)
    print(3 < 5)

    if 3 > 1:
        print('x')

    my_list = ['2']
    my_empty_list = []

    if my_empty_list:
        pass
    else:
        print('List is empty')

    # operateurs arithmetics
    var = 1 * 2 / 2 - 3 + 5
    print(5 % 2)
    print(5 // 2)

    # operateurs d'assigement
    var1 = 1
    var1 += 2

    # operateurs comparaison
    print(1 == 2)
    print(1 != 2)

    # operateurs logiques
    print(True and False)
    print(True or False)
    print(not False)

    # operateur identité
    print(var1 is str)
    True is bool

    # operateur d'appartenance
    print(' == operateur d\'appartenance == ')
    print('x' in 'axc')
    print('x' in ['a', 'x', 'c'])

    print(len('axc'))

