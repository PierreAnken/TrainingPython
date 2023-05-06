# Autoklasse

class Auto:

    def __init__(self, name, kilometer, land, owner=None):
        self.name = name
        self.kilometer = kilometer
        self.land = land
        self.owner = owner

    def __str__(self):

        text = f'{self.name} aus {self.land.iso_code} hat {self.kilometer} Kilometers '
        if self.owner:
            text += f'hat {self.owner} als Besitzer.'
        else:
            text += 'und hat keinen Besitzer.'

        return text
