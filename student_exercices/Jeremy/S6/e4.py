def triangle(n):
    largeur_base = n * 2 - 1

    for i in range(1, n + 1):
        decalage_gauche = int((largeur_base - (i * 2 - 1)) / 2)
        print(decalage_gauche * ' ', i * '* ')

triangle(5)

#    *
#   * *
#  * * *
