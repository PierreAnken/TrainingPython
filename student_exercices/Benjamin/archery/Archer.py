from student_exercices.Benjamin.archery.Bow import Bow
from student_exercices.Benjamin.archery.Buyable import Buyable
from student_exercices.Benjamin.archery.Quiver import Quiver


class Archer:

    def __init__(self, money: float, name: str):
        self.money = money
        self.name = name
        self.quiver = None
        self.bow = None
        self.inventory = []

    def buy(self, buyable: Buyable, amount: int):
        total_price = buyable.price * amount

        # if enough money
        if self.money >= total_price:
            self.money -= total_price
            for x in range(amount):
                self.inventory.append(buyable)
        else:
            # if NOT enough money
            print(f'Total price: {total_price} is bigger then your money: {self.money}')

    def equipe(self, equipment: Buyable):
        # check if the object is in inventory
        if equipment in self.inventory:
            if type(equipment) is Bow:
                if self.bow:
                    self.inventory.append(self.bow)
                self.bow = equipment

            elif type(equipment) is Quiver:
                if self.quiver:
                    self.inventory.append(self.quiver)
                self.quiver = equipment

            self.inventory.remove(equipment)

    def __str__(self):
        detail = f'{self.name} inventory:\n'
        if self.inventory:
            for value in self.inventory:
                detail += f'- {value}\n'
        else:
            detail += ' - Empty inventory'

        detail += f'equipped:\n bow:{self.bow}\n quiver: {self.quiver}\n'


        return detail
