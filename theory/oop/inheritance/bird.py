from theory.oop.inheritance.animal import Animal


class Bird(Animal):
    def __init__(self, name: str):
        super().__init__(name)
        self.can_fly = True

    @staticmethod
    def cry():
        print('Cui cui')