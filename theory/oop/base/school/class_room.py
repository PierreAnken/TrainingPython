
class ClassRoom:

    def __init__(self, number: str):
        self.number = number
        print(f'New class room {self.number} built')

    def __str__(self):
        return self.number
