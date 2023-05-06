# Ecrivez un programme qui affiche un carré de
# longueur n avec le caractère 'X', mais seulement le contour.

# # # #
#     #
# # # #


n = int(input('Entrez n: '))

for ligne in range(n):  # [0,1,2,3,4]
    # Si 1ère ou dernière ligne
    if ligne == 0 or ligne == n - 1:
        print('X' * n)

    # lignes du milieu
    else:
        # chaque lettre
        line_text = ''
        # Si 1ère ou dernière colonne
        for col in range(n):  # [0,1,2,3,4]
            if col == 0 or col == n - 1:
                line_text += 'X'
            else:
                line_text += ' '
        print(line_text)
