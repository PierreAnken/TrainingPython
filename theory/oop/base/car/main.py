from theory.oop.base.car.car import Car
from theory.oop.base.car.parking import Parking

if __name__ == '__main__':

    parking1 = Parking()
    print(parking1.count_car())

    for _ in range(25):
        car = Car()
        parking1.park_car(car)

    print(parking1.count_car())



