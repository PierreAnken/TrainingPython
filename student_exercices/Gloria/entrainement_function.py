import random
from math import pi


def division(c1, c2):
    """
    :param c1: nominateur
    :param c2: dénominateur
    :return: None ou le résulat de la division
    """
    if c2 == 0:
        print("erreur /0 ")
    else:
        return c1 / c2


def multiple(chiffre, diviseur):
    """
    :param chiffre: un chiffre
    :param diviseur: un second chiffre
    :return: est ce que le chiffre est un multiple de diviseur? boolean
    Hint: modulo => %
    """
    return chiffre % diviseur == 0


# print('Multiple 27 de 4?', multiple(27, 4))

def volume_sphere(rayon):
    """
    Formule: V = 4/3*π*R3
    Puissance: **
    :param rayon: rayon de la sphere
    :return: le volume de la sphere
    """

    return 4 / 3 * pi * rayon ** 3


# print(volume_sphere(1))

def pile_face(truque):
    """
    :param truque: Si True => 2x + de chance de retourner True
    :return: True ou False à 50%, si triche: return True à 75% et False à 25%
    """

    # Pièce non truquée 50 True % 50 False
    if not truque:
        valeur_random = random.randint(0, 1)
        return valeur_random == 0

    # Pièce truquée 75 True % 25 False
    else:
        valeur_random = random.randint(0, 3)  # [0,1,2,3]
        return valeur_random != 3


piles, faces = 0, 0
for _ in range(1000):  # répetition 1000x, "_" car la valeur de la boucle n'est pas importante
    resultat = pile_face(True)
    if resultat:
        piles += 1
    else:
        faces += 1

print(piles, faces)
