import random


def wurfel_100():
    werfe = [0, 0, 0, 0, 0, 0]

    # 100x
    for _ in range(100):
        wert = random.randint(1, 6)
        werfe[wert-1] += 1

    print(werfe)


wurfel_100()
