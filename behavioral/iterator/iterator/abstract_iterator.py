from abc import (
    ABC,
    abstractmethod,
)

from book import Book


class AbstractIterator(ABC):
    @abstractmethod
    def has_next(self) -> bool:
        pass

    @abstractmethod
    def next(self) -> Book:
        pass