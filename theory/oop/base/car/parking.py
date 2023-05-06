from theory.oop.base.car.car import Car


class Parking:

    max_car = 20

    def __init__(self):
        self.places = []

    def count_car(self):
        return len(self.places)

    def park_car(self, car: Car):
        if self.count_car() == self.max_car:
            print('Sorry the parking is full.')
        else:
            self.places.append(car)
            print(f'Your car is parked on place {self.count_car()}')


