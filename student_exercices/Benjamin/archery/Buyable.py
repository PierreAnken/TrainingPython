
class Buyable:

    def __init__(self, price: float, name: str):
        self.price = price
        self.name = name

    def __str__(self):
        return f'{self.__class__.__name__}: {self.name}'
