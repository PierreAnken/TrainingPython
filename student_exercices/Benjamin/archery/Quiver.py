from student_exercices.Benjamin.archery.ArrowType import ArrowType
from student_exercices.Benjamin.archery.Buyable import Buyable


class Quiver(Buyable):

    def __init__(self, capacity: int, price: float, name:str):
        super().__init__(price, name)
        self.capacity = capacity
        self.remaining_arrows = 0
        self.arrow_type = None

    def fill(self, amount: int, arrow_type: ArrowType):
        if not self.arrow_type or self.arrow_type == arrow_type:
            remaining_place = self.capacity - self.remaining_arrows
            amount_filled = min(remaining_place, amount)
            unfilled_arrow = amount - amount_filled
            if unfilled_arrow:
                print(f'Info: Quiver full after {remaining_place} arrow(s). {unfilled_arrow} arrow(s) were not filled.')
            self.remaining_arrows += amount_filled
            self.arrow_type = arrow_type
        else:
            print('Error: Arrow type missmatch')
