class Car:

    # static variable != self.next_car_id
    next_car_id = 1
    price = 10000

    # constructor
    def __init__(self):
        self.kilometers = 0
        self.id = Car.next_car_id
        Car.next_car_id += 1

    def __str__(self):
        return f'Car {self.id}, value: {Car.price}, km: {self.kilometers}'

    # class method
    def drive(self, kilometers):
        self.kilometers += kilometers

    # static method
    @staticmethod
    def set_price(new_price):
        Car.price = new_price
