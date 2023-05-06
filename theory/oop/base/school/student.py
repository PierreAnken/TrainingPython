class Student:

    # Class constructor called by new class instance creation Student()
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    # String representation of the class instances of Student
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
