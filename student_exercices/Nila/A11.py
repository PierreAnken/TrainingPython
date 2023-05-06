import math


def funct(p, q):
    teil_1 = -(p / 2)
    inhalt_wurzel = (p / 2) ** 2 - q
    x1 = teil_1 + math.sqrt(inhalt_wurzel)
    x2 = teil_1 - math.sqrt(inhalt_wurzel)
    return x1, x2


print(funct(10, 15))
