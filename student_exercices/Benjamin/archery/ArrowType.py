from student_exercices.Benjamin.archery.Buyable import Buyable


class ArrowType(Buyable):

    def __init__(self, price: float, max_deviation: float, name:str):
        super().__init__(price, name)
        self.max_deviation = max_deviation
