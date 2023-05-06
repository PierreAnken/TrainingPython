# def summe(zahl1: int, zahl2: int) -> int:
#     try:
#         zahl = zahl1 + zahl2
#         return zahl
#     except:
#         print(f"Ungültiger Paramenter {zahl1} oder {zahl2}")


# def summe(zahl1: int, zahl2: int) -> int:
#
#     if type(zahl1) != int:
#         print(f"Ungültiger Paramenter {zahl1}")
#     elif type(zahl2) != int:
#         print(f"Ungültiger Paramenter {zahl2}")
#     else:
#         return zahl1 + zahl2

# def multi_summe(*nummern):
#     for nummer in nummern:
#         if type(nummer) != int:
#             print(f"Ungültiger Paramenter {nummer}")
#             break
#     else:
#         return sum(nummern)

# def benuetzer_woertbuch():
#     woerterbuch = {}
#     # { 'auto': 4, 'bus': 2}
#
#     while True:
#         wort = input("Gebe eine Wort!")
#         if wort == 'stop':
#             break
#
#         anzahl = woerterbuch.get(wort, 0)
#         woerterbuch[wort] = anzahl + 1
#     return woerterbuch

def anzahl_buchstaben(string: str):
    anzahl = len(string)
    return anzahl


if __name__ == '__main__':
    print(anzahl_buchstaben('djaflahdféafvlaei4'))
