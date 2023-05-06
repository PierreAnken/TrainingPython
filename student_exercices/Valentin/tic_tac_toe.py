import random


def generate_grid():
    """
    Hier wird das Spielfeld generiert
    :return: Es wird in einer 2 dimensionalen Liste wiedergegeben.
    """

    # [
    #   ['-','-','-'],     Element 1 Liste 1
    #   ['-','-','-'],     Element 2 Liste 2
    #   ['-','-','-']      Element 3 Liste 3
    # ]

    grid = []
    for _ in range(3):  # [0,1,2]       # Schleife die 3 mal durchläuft und 3 mal grid.append ausführt
        grid.append(['-', '-', '-'])    # Ich füge eine Liste min 3 minus in das Spielgfeld (grid)

    return grid                         # Wird als ergebnis zurückgegben, ohne Return wird die Funktion nicht ausgeführt.


def print_grid(grid):
    """
    Druckt eigentlich das aktuelle Spielfeld, welches in def generate_grid erstellt wurde.
    :param grid: Spielfeld 3 x 3 Liste
    :return: None (gibt nichts zurück)
    """

    #  X   X
    #  O X
    #    O O
    for linie in range(3):  # [0,1,2] mit der for werden alle linie durchgegangen
        print(*grid[linie])  # mit * werden die Elemente der Liste entpackt. ['X','O','X'] => 'X','O','X'


def grid_is_full(grid):
    """
    Prüft, ob das Spielfeld voll ist.
    :param grid: Spielfeld 3 x 3 Liste
    :return: Ist das Spielfeld voll? True/False
    """
    for linie in grid:      #wir gehen jede linie durch
        for symbol in linie:    # gleicht das Symbol ab
            if symbol == '-':  #  Wenn das Symbol "-" vorhanden ist,  wird false ausgegeben, da noch freier platz vorhanden ist.
                return False
    return True


def get_winner(grid):
    """
    Prüft, ob ein Spieler gewonnen hat.
    :param grid: Spielfeld 3 x 3 Liste
    :return: x oder o oder None / x Spieler 1 o Spieler 2 None steht für kein Spieler hat gewonnen.
    """

    # Linie
    if grid[0][0] == grid[0][1] == grid[0][
        2] != '-':  # != '-':  Es muss ungleich - abgeglichen werden, da sonst 3 mal "-" auch ein Gewinnner ist.  #Es werden alle Werte abgeglichen ausser - wegen ungleich !=
        return grid[0][0]  # gibt das Symbol welches in der Linie ist wieder, vom entsprechenden Gewinner.

    if grid[1][0] == grid[1][1] == grid[1][2] != '-':
        return grid[1][0]

    if grid[2][0] == grid[2][1] == grid[2][2] != '-':
        return grid[2][0]

    # Spalten
    if grid[0][0] == grid[1][0] == grid[2][0] != '-':
        return grid[0][0]

    if grid[0][1] == grid[1][1] == grid[2][1] != '-':
        return grid[0][1]

    if grid[0][2] == grid[1][2] == grid[2][2] != '-':
        return grid[0][2]

    # Diagonals
    if grid[0][2] == grid[1][1] == grid[2][0] != '-':
        return grid[0][2]

    if grid[0][0] == grid[1][1] == grid[2][2] != '-':
        return grid[0][0]


def get_move(grid, ist_ki):
    # Falls Spieler 2 ist eine KI
    if ist_ki:
        freie_positionen = []       #Eine neue Variabel mit einer neuen leeren Liste.
        for linie in range(3):      #Jede linie wird durchgegangen 3 mal
            for spalte in range(3): # Spalte wird durchggangen 3mal
                if grid[linie][spalte] == '-':  #Falls ein "-" vorhanden ist, wird es in die neue Liste (freie_positionen) gespeichert.
                    freie_positionen.append((linie, spalte))

        # random.sample => [(2,2),(0,2),(1,1)] => [(0,2)]   Random.sample wählt ein Teil von der Liste aus.
        gewalte_position = random.choice(freie_positionen) # mit der 1 wird ein Element vom Teilbestand der liste ausgewählt.
        print('KI wahl:', gewalte_position[0] + 1,      # gibt aus, was der Computer gewählt hat.
              gewalte_position[1] + 1)  # + eins wieder für den Computer, da die Liste bei 0 startet. gehört auch noch zur Print funkiton.
        return gewalte_position

    # Falls Spieler 2 ist keine KI
    else:

        while True:
            # Der aktuelle Spieler setzt sein Symbol
            position_str = input('Wo wird das Symbol gesetzt ? (Linie/Spalte) Zb 3/2 ')
            linie_index = int(position_str[0]) - 1  # Für die Benutzer ist in der Liste
            spalte_index = int(position_str[2]) - 1

            # Prüfung ob das Feld bereits besetzt ist
            current_value = play_grid[linie_index][spalte_index]
            if current_value != '-':  # Wert abgeglichen, ob ein - vorhanden ist (Zelle leer) !Ungleich
                print('Position schon besetzt!')
            else:  # Falls frei wird hier weitergefahren
                return linie_index, spalte_index        # wird umgesetzt, was man eingesetzt hat.


# unten ist der "eigentliche Code vom Ablauf" welcher dann auf die einzelnen Funktionen, welche oberhalb aufgelistet sind bei Bedarf zugreift.

# Benutzer 1 / Benutzer 2 / Computer 1 Wer spielt gegen wen.
antwort = input('Ist der Erste Spieler ein Computer? Y / N ')
spieler1_ki = antwort == "Y"

antwort = input('Ist der Zweite Spieler ein Computer? Y / N ')
spieler2_ki = antwort == "Y"

while True:         #Endlose Schleife, für am Schluss zum fragen, ob das Spiel neu startet.

    # Leeres Grid erstelle 3x3
    play_grid = generate_grid()     #Hier wird die Variabel play grid festgelegt, welche die Funktion oberhalb (generate_grid) wiedergibt

    # Werte festlegen für x und o sind die werte als string
    symbols = ['x', 'o']        # Eine Variabel mit einer Liste der zwei wählbaren Symbolen. Werden später dann darauf zurückgreiffen.
    aktueller_spieler = 0  # 0 = Spieler 1  und 1 = Spieler 2

    # Bedingung der Schleife, bis ein Spieler gewonnen hat, oder das Brett (3x3) ist voll und die Bedingung für den Sieg nicht erfüllt ist.
    while not grid_is_full(play_grid) and not get_winner(
            play_grid):  # not ist wieder invertiert, Hängt zusammen mit def grid_is_full(grid): / and / hier noch keiner hat gewonnen.

        # Spielfeld Drucken
        print_grid(play_grid)

        # Der aktuelle Spieler setzt sein Symbol
        print('Spieler', aktueller_spieler + 1, '[', symbols[aktueller_spieler], ']:')      #Hier wird der Spieler ausgegeben mit + 1 beim Wechsel wird aktueller spieler den Wert =1 haben und somit zum Spieler 2.

        # Muss die Ki antworten?
        ki_spielt = (spieler1_ki and aktueller_spieler == 0) or (spieler2_ki and aktueller_spieler == 1)
        position = get_move(play_grid, ki_spielt)
        play_grid[position[0]][position[1]] = symbols[
            aktueller_spieler]  # Der Wert den wir bei Positionsabfrage gesetzt haben wird nun entsprechend gespeichert.

        # Spieler Wechseln
        if aktueller_spieler == 1:
            aktueller_spieler = 0
        else:
            aktueller_spieler = 1

    # Resultat Gewinner wird gedruckt
    gewinner = get_winner(play_grid)
    if gewinner == "x":
        print("Spieler 1 hat gewonnen")
    elif gewinner == "o":
        print("Spieler 2 hat gewonnen")
    else:
        print("Es ist unentschieden")

    antwort = input('Wieder spielen? Y / N ')       # Fragt um weiterzuspielen.
    if antwort != 'Y': # Bei Y läuft die schleife oben automatisch weiter.
        print('Bye bye')
        break               # Die schleife ist dann zu Ende.
