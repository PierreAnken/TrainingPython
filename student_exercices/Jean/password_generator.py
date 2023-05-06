import random
import string


def generate_password(taille=10, lettre=True, speciaux=True):

    choix = string.digits
    if lettre:
        choix += string.ascii_uppercase
    if speciaux:
        choix += string.punctuation

    mdp = ''
    for _ in range(taille):
        mdp += choix[random.randint(0, len(choix)-1)]

    return mdp


if __name__ == '__main__':
    print(generate_password(30, speciaux=False))
    print(generate_password(lettre=False))
