import random


class Auto:
    FARBEN = ['blau', 'rot', 'gelb', 'weiss']
    next_id = 1

    def __init__(self, farbe=None):
        self.id = Auto.next_id
        Auto.next_id += 1

        if farbe:
            self.farbe = farbe
        else:
            self.farbe = random.choice(self.FARBEN)

    def __str__(self):
        return f'Auto {self.id} mit Farbe {self.farbe}'

    def __repr__(self):
        return self.__str__()
