class Author:

    anzahl_author = 0

    def __init__(self, vorname, nachname):
        self.vorname = vorname
        self.nachname = nachname
        self.books = []

        Author.anzahl_author += 1

    def get_full_name(self):
        return self.vorname + ' ' + self.nachname

    def add_book(self, book):
        self.books.append(book)
