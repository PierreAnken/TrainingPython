class Cat:

    def hello(self):
        print('Miaou')

    def hello(self, dog):
        dog.hello(self)

    def hello(self, name):
        print(f'Miaou {name}')

    def x():
        print('x')