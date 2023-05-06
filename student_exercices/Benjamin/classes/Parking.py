from student_exercices.Benjamin.classes.Auto import Auto


class Parking:

    def __init__(self, max_autos=20):
        self.max_autos = max_autos
        self.parkplaetze = []

    def park_auto(self, some_auto: Auto):
        if self.anzahl_freie_plaetze():
            self.parkplaetze.append(some_auto)
            print('Auto wurde parkiert')
        else:
            print('Parkplatz voll')

    def __str__(self):
        text = ''
        text += f'Parking mit {self.anzahl_freie_plaetze()}/{self.max_autos} parkplätze\n'
        for some_auto in self.parkplaetze:
            text += f' - {some_auto}\n'
        return text

    def anzahl_freie_plaetze(self):
        return self.max_autos - len(self.parkplaetze)
