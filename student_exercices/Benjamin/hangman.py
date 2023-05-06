# die Liste der Zitate aus der website hohlen: https://type.fit/api/quotes
from string import ascii_letters as alle_buchstaben
import random

import requests

response = requests.get('https://type.fit/api/quotes')
data = response.json()

# ein Zitat per zufall wählen
random_index = random.randint(0, len(data) - 1)
zitat_dict = data[random_index]
joker = True
zitat = zitat_dict['text']
zitat = zitat.split()[: 7]
zitat = ' '.join(zitat)
gebraucht = []

# den ganzen satz duplizieren und ausblenden
zitat_ausgeblendet = zitat[:]
for buchstabe in alle_buchstaben:
    zitat_ausgeblendet = zitat_ausgeblendet.replace(buchstabe, '_')

# solange der satz nicht fertig ist und noch leben hat
leben = 7
while leben != 0 and '_' in zitat_ausgeblendet:
    antwort = ''

    print(f'{zitat_ausgeblendet}\nLeben:{leben}')
    # wir fragen den Benutzer für einen Buchstaben
    while (len(antwort) != 1 or not antwort.isalpha()) and antwort != 'joker':
        antwort = input('Bitte buchstabe eingeben ')

        if antwort in gebraucht:
            print('Dieser Buchstabe ist bereits gebraucht :) ...')
            antwort = ''
    
    if antwort == 'joker':
        if joker:
            joker = False
            position = zitat_ausgeblendet.index('_')
            antwort = zitat[position]
            print(f'Joker hat buchstabe {antwort} gegeben')
        else:
            print('Joker wurde schon benutzt.')
            continue

    gebraucht.append(antwort)

    # wir schauen ob er in dem Zitat vor kommt
    if antwort in zitat:
        # falls es im zitat ist dann den buchstaben einblenden
        for buchstabe_index, buchstabe in enumerate(zitat):
            if antwort.lower() == buchstabe.lower():
                zitat_ausgeblendet = zitat_ausgeblendet[:buchstabe_index] + buchstabe + zitat_ausgeblendet[
                                                                                        buchstabe_index + 1:]

    # wenn es nicht drin ist dann zieht man ein leben ab
    else:
        leben -= 1

# dem Benuzer zeigen ob er gewonnen oder verloren hat
if leben == 0:
    print('Du hast verloren')
else:
    print('Du hast Gewonnen!!')
