from student_exercices.Benjamin.archery.Buyable import Buyable


class Bow(Buyable):

    def __init__(self, price: float, accuracy: float, strength: int, name:str):
        super().__init__(price, name)
        self.accuracy = accuracy
        self.strength = strength
