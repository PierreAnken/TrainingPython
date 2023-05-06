# Klasse für Garage

class Garage:

    def __init__(self, autos):
        self.autos = autos

    def print_garage(self):
        for auto in self.autos:
            print(auto)

