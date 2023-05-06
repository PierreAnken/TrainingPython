from student_exercices.Benjamin.archery.Buyable import Buyable


class ArrowType(Buyable):

    def __init__(self, price: float, accuracy: float, name:str):
        super().__init__(price, name)
        self.accuracy = accuracy
