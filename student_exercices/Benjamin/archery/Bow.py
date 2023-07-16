from student_exercices.Benjamin.archery.Buyable import Buyable


class Bow(Buyable):

    def __init__(self, price: float, max_distance: int, name:str):
        super().__init__(price, name)
        self.max_distance = max_distance
