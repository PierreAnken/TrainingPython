class Person:
    name = 'Pierre'

    def __bool__(self):
        return self.name != 'Pierre'

    def __str__(self):
        return self.name


person = Person()
print(f'{person} of type {type(person).__name__} => {bool(person)}')
