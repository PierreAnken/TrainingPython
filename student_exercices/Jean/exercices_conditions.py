if __name__ == '__main__':  # quel est la valeur de cette formule name / main ?

    user_input = input('Devinez le bon chiffre allant de 0 à 100. Entrez à présent votre chiffre.  ')
    x = int(user_input)

    if x > 50 and not x >= 100:
        print("Dommage, c'est raté, mais vous avez encore 2 possibilités de gagner le gros lot.")
    if x == 50:
        print("Vous avez gagné le gros lot qui vous parviendra par la poste ces prochains jours.")
    if x > 100:
        print("Vous dépassez les bornes et n'avez pas respecté la règle de max. 100")
        print("Fin du jeu")
    if not int(user_input) :
        print("ERREUR: Entrez un nombre et aucun autre signe")
    elif x < 50:
        print("Vous êtes un looser, dommage pour vous. il fallait miser plus haut.")
    else:

        print("Essayez encore.") # Ne devrait pas apparaître en cas de victoire
        print("Fin du jeu")
# Comment conditionner le else quand on a gagné ?
# Où trouve-ton le script final Precess finished with exite code 0 ?


    user_input = input('Enter a number ')

    # Is the string only composed of integers?
    if user_input.isdigit():
        x = int(user_input)

        if x > 150:
            print("x > 150")
        elif x < 150:
            print("x < 150")
        else:
            print("x == 150")

    else:
        print('Invalid number', user_input)