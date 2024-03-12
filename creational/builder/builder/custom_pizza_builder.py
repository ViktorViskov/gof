from .abstact_pizza_builder import AbstractPizzaBuilder
from models.custom_pizza import CustomPizza


class CustomPizzaBuilder(AbstractPizzaBuilder):
    chease: int
    bacon: int
    ananas: int
    mashrooms: int
    seafood: int
    tomato: int

    def __init__(self) -> None:
        self.chease = 0
        self.bacon = 0
        self.ananas = 0
        self.mashrooms = 0
        self.seafood = 0
        self.tomato = 0

    def add_chease(self) -> None:
        self.chease += 1
    
    def add_bacon(self) -> None:
        self.bacon += 1
    
    def add_ananas(self) -> None:
        self.ananas += 1

    def add_mashrooms(self) -> None:
        self.mashrooms += 1

    def add_seafood(self) -> None:
        self.seafood += 1
    
    def add_tomato(self) -> None:
        self.tomato += 1

    def make(self) -> CustomPizza:
        return CustomPizza(self.chease, self.bacon, self.ananas, self.mashrooms, self.seafood, self.tomato)
    
    def reset(self) -> None:
        self.chease = 0
        self.bacon = 0
        self.ananas = 0
        self.mashrooms = 0
        self.seafood = 0
        self.tomato = 0
