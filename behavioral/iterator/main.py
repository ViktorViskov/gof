from book import Book
from iterator.abstract_iterator import AbstractIterator
from iterator.year_iterator import YearIterator
from iterator.title_iterator import TitleIterator
from iterator.author_iterator import AuthorIterator


def client_code(iterator: AbstractIterator) -> None:
    while iterator.has_next():
        book = iterator.next()
        print(book.year, book.author, book.title, sep='\t')

books = [
    Book("The Hobbit", "Jon Ronald", 1937),
    Book("The Lord of the Rings", "Tolkien", 1954),
    Book("The Hitchhiker's Guide to the Galaxy", "Tolkien", 1979),
    Book("Fish", "Jane Austen", 1881),
    Book("Something", "Jane Austen", 1981),
    Book("The Old Man and the Sea", "Jane Austen", 1952),
    Book("The Catcher in the Rye", "Jane Austen", 1951),
    Book("The Grapes of Wrath", "Jane Austen", 1940)    
]

client_code(YearIterator(books))
print("-" * 30)
client_code(TitleIterator(books))
print("-" * 30)
client_code(AuthorIterator(books))