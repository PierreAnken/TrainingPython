import random

if __name__ == '__main__':

    # choisir un nombre dans sa tête et demander vérification

    print("choisissez un nombre entre 1 et 100 dans votre tête, est-ce que la valeur ci-dessous correspond ?")

    # demander à la machine de faire apparaitre un nombre entre 1 et 100
    reponse = ''
    range_min = 1
    range_max = 100

    while reponse != "=":

        # AI guess a number
        guess_ia = range_min + (range_max - range_min) // 2

        # user give feedback to AI
        reponse = input(f"Est-ce que le nombre est {guess_ia} ? (La chiffre mystère est <>=)")

        # based on feedback AI adapt the range where to search the answer
        if reponse == ">":
            range_max = guess_ia - 1

        elif reponse == "<":
            range_min = guess_ia + 1

    print('Finish')
