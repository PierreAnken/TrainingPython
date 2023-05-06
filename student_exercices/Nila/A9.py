import random


def spielen():
    zahl_1 = random.randint(0, 10)
    zahl_2 = random.randint(0, 10)
    zahl_3 = random.randint(0, 10)

    print('Ergebnis', zahl_1, zahl_2, zahl_3)

    # Alles gleich?
    if zahl_1 == zahl_2 == zahl_3:
        print("grosse gewinn")

    # 2 gleich?
    elif zahl_1 == zahl_2 or zahl_1 == zahl_3 or zahl_2 == zahl_3:
        print("kleine gewinn")
        
    # Keine Gleich
    else:
        print("kein gewinn")


while True:

    spielen()

    # Weiter Spielen?
    antwort = input('willst du weiter? j/n ')
    if antwort != "j":
        break
