from.abstract_iterator import AbstractIterator
from book import Book


class TitleIterator(AbstractIterator):
    def __init__(self, books: list[Book]) -> None:
        self._books = sorted(books, key=lambda book: book.title)
        self._index = 0
    
    def has_next(self) -> bool:
        return self._index < len(self._books)
    
    def next(self) -> Book:
        book = self._books[self._index]
        self._index += 1
        return book

    