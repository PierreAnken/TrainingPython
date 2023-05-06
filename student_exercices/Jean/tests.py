communes = {
    3966: {'name': 'Chalais', 'sun': 0},
    3960: {'name': 'Sierre', 'sun': 1}
}

if __name__ == '__main__':
    # I'm a comment - indentation is important
    print('I\'m printing inside the terminal')

    print("Je peux afficher des données ici.")
    print("---------------------------------")

    # Attribute + Method call
    print('hello world'.capitalize())
    print("---------------------------------")
    print("Je peux afficher des données ici.".title())
    print("---------------------------------")

    # Assignation
    var1 = 123
    var2 = var1 + 2
    print(var2)
    print("---------------------------------")

    annee = 2022
    annee_suivante = annee + 1
    print("L'année prochaine nous serons en " + str(annee_suivante) + ".")
    print("---------------------------------")
    # Multiple assignation
    x, y, z = "Orange", "Banana", "Cherry"
    a, b, c = ["Orange", "Banana", "Cherry"]
    print(z, b, x)
    print("---------------------------------")

    # Data type
    print(' === data type === ')
    my_string = 'abc'  # my_string = ['a', 'b', 'c']
    print(my_string[0])
    print("---------------------------------")

    # Data print - exercice JB
    communes = "Aire_la_Ville,Anières,Avully,Avusy,Bardonnex,Bellevue,Bernex,Carouge,Cartigny,Céligny,Chancy,Chêne_Bougeries,Chêne_Bourg,Choulex,Collex_Bossy,CollongeBellerive,Cologny,Confignon,Corsier,Dardagny,Genève,Genthod,Gy,Hermance,Jussy,Laconnex,Lancy,Le,Grand_Saconnex,Meinier,Meyrin,Onex,Perly_Certoux,Plan_les_Ouates,Pregny_Chambésy,Presinge,Puplinge,Russin,Satigny,Soral,Thônex,Troinex,Vandœuvres,Vernier,Versoix,Veyrier"
    print(" ***** Liste des Communes *****")
    print(communes.replace('_','-'))
    print(communes[5]) # Comment sélectionner les communes commençant par la lettre V ?
    print("---------------------------------")


    my_multiline_string = ''' 
    SELECT *
    FROM animaux
    WHERE age > 10
    LIMIT 10;
    '''

    my_int = 23
    my_float = 2.4
    my_bool = True

    # Casting
    print(' === casting === ')
    var3 = '100'
    print(type(var3))
    print(int(var3) + 5)
    print(var3 + str(5))
    print(5 * 'x')
    print("---------------------------------")

    print("/\/\/\/\ - EXERCICE AGE JEAN - /\/\/\/\/")
    age = '69'
    age_avance = int(age) + 22
    print(int(age) + 22)
    print(age + str(22))
    print(int(age_avance) * 'o')
    print("---------------------------------")

    # Structures
    print(' === structures === ')
    my_list = ['a', 1, 'test', 'toto', 'Le lion est mort ce soir']
    print(my_list)
    print("---------------------------------")
    print(my_list[4])
    print("---------------------------------")



    empty_list = []  # list()

    # my_list[1] = 'dog'
    # print(my_list)
    my_str_communes = "Aire_la_Ville,Anières,Avully,Avusy,Bardonnex,Bellevue,Bernex,Carouge,Cartigny,Céligny,Chancy,Chêne_Bougeries,Chêne_Bourg,Choulex,Collex_Bossy,CollongeBellerive,Cologny,Confignon,Corsier,Dardagny,Genève,Genthod,Gy,Hermance,Jussy,Laconnex,Lancy,Le,Grand_Saconnex,Meinier,Meyrin,Onex,Perly_Certoux,Plan_les_Ouates,Pregny_Chambésy,Presinge,Puplinge,Russin,Satigny,Soral,Thônex,Troinex,Vandœuvres,Vernier,Versoix,Veyrier"
    my_list_communes = my_str_communes.split(sep=',')
    print(my_list_communes)
    my_list_communes.append("DOUDOU")
    print(my_list_communes)
    # JE NE COMPRENDS PAS CE APPEND

    my_list.append('cat')
    print(my_list)

    my_list.insert(0, 'bird')
    print(my_list)

    my_list_communes.insert(0, "DOUDOU")
    print(my_list_communes)

    print(' === tuple === ')
    my_tuple = ('abc', 1, [1, 2, 3])
    print(my_tuple[2][0])

    print(' === set === ')
    # set = no duplicates
    my_set = {'a', 'a', 'b'}
    empty_set = set()
    print(my_set)
    print(list(set([1, 1, 2, 3, 4])))

    print(' === range === ')
    my_range = range(1, 15, 2)  # [2, 4, 6, ..]
    print(list(my_range))

    print(' === dict === ')
    empty_dict = {}
    my_dict = {
        'key1': 'value1',
        2: [1, 2]
    }
    print(my_dict)
    my_dict.update(
        {
            'key1': 11,
            'key3': 123
        }
    )
    print(my_dict)

    my_dict['key4'] = 'abc'
    print(my_dict)

    del my_dict['key4']
    print(my_dict)

    print(my_dict.get('key5', 'Nothing'))  # None
    # print(my_dict['key5'])

    print(my_dict.keys())
