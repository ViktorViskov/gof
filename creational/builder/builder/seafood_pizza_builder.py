from .abstact_pizza_builder import AbstractPizzaBuilder
from models.seafood_pizza import SeafoodPizza


class SeafoodPizzaBuilder(AbstractPizzaBuilder):
    chease: int
    tomato: int
    mashrooms: int
    seafood: int

    def __init__(self) -> None:
        self.chease = 0
        self.tomato = 0
        self.mashrooms = 0
        self.seafood = 0

    def add_chease(self) -> None:
        self.chease += 1
    
    def add_bacon(self) -> None:
        raise Exception(f"{self.__class__.__name__} does not have bacon")
    
    def add_ananas(self) -> None:
        raise Exception(f"{self.__class__.__name__} does not have ananas")

    def add_mashrooms(self) -> None:
        self.mashrooms += 1

    def add_seafood(self) -> None:
        self.seafood += 1
    
    def add_tomato(self) -> None:
        self.tomato += 1

    def make(self) -> SeafoodPizza:
        return SeafoodPizza(self.chease, self.tomato, self.mashrooms, self.seafood)
    
    def reset(self) -> None:
        self.chease = 0
        self.tomato = 0
        self.mashrooms = 0
        self.seafood = 0
