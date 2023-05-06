class Book:

    def __init__(self, seitenzahl, titel, author):
        self.author = author
        self.seitenzahl = seitenzahl
        self.titel = titel
        author.add_book(self)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.titel
