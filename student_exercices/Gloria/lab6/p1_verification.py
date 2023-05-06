def ask_float(value_min, value_max, measure):
    float_nbr = None

    # Tant que l'on a pas un float correct
    while not float_nbr:
        # Demander à l'utilisateur d'entrer un float
        entered_value = input(f"Please enter your {measure} in range[{value_min},{value_max}]")

        try:
            # On essaye de convertir l'entrée en float
            float_nbr = float(entered_value)
        except:
            # Si l'entrée n'est pas un float valide
            print(f'{entered_value} is not a valid number')
        else:
            # Si l'entrée est un float
            # On teste si le float est dans la plage demandée
            if not value_min <= float_nbr <= value_max:
                print(f'{entered_value} is not in range [{value_min},{value_max}]')

                # on reset la variable contenant le float pour refaire une boucle
                float_nbr = None

    return float_nbr


def ask_int(value_min, value_max, measure):
    int_nbr = None

    # Tant que l'on a pas un float correct
    while not int_nbr:
        float_nbr = ask_float(value_min, value_max, measure)

        if '.0' in str(float_nbr):
            int_nbr = int(float_nbr)
        else:
            print(f'{float_nbr} is not a valid integer')

    return int_nbr


# Le poids entre 30 et 300 kg
weight = ask_float(30, 300, 'weight')

# La taille entre 50 cm et 290 cm
size = ask_float(50, 290, 'size')

# Sa pointure de pied entre 10 et 55
shoes_size = ask_int(10, 55, 'shoes size')

# La longueur des cheveux entre 0 cm et deux fois la taille de l’utilisateur
hair_length = ask_float(0, 2 * size, 'hair length')

# La taille de son nez entre 5 et 15 cm
nose_size = ask_float(5, 15, 'nose size')

# Son âge entre 18 et 120 ans.
age = ask_int(18, 120, 'age')

print(weight, size, shoes_size, hair_length, nose_size, age)
