class Animal:
    def __init__(self, name: str = 'No name'):
        self.name = name

    def __str__(self):
        return f'{type(self).__name__} with name {self.name} '

    @staticmethod
    def cry():
        print('Unknown animal sound')
