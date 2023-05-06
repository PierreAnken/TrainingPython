from student_exercices.Tobias.library_poo.author import Author
from student_exercices.Tobias.library_poo.book import Book

if __name__ == '__main__':

    author = Author('Tobias', 'Frassa')
    author2 = Author('Pierre', 'Anken')

    for x in range(5):
        book = Book(100, f'Book {x}', author)

    for b in author.books:
        print(b)