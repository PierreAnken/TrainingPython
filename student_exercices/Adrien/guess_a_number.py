import random

if __name__ == '__main__':

    # Je definis un nombre entre 1 et 100
    random_number = random.randint(1, 100)

    # Il essaye de deviner le nombre tant qu'il n'a pas la bonne réponse
    guess = -1

    # défini une variable vie
    vie = 7

    while guess != random_number and vie > 0:

        guess = input("veuillez entrer un chiffre entre 1 et 100")

        # verifier si c'est un chiffre valide
        if not guess.isdigit():
            print(f"{guess} est invalide")
            continue

        guess = int(guess)  # écrase la valeur

        # soit le résultat est :
        # inférieur --> j'annonce que le nombre est inférieur
        if guess < random_number:
            print("votre valeur est inférieur")
            vie -= 1

        # supérieur --> j'annonce que le nombre est supérieur
        elif guess > random_number:
            print("votre valeur est supérieur")
            vie -= 1

    # égale --> j'annonce que le résultat est correcte et que le joueur a gagné
    if guess == random_number:
        print(f'Félicitations, votre nombre {guess} est correct')

    else:
        print(f'Désolé vous avez perdu, le nombre correct était {guess}')
