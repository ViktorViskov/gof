from .abstact_pizza_builder import AbstractPizzaBuilder
from models.hawaii_pizza import HawaiiPizza


class HawaiiPizzaBuilder(AbstractPizzaBuilder):
    ananas: int
    chease: int
    tomato: int

    def __init__(self) -> None:
        self.ananas = 0
        self.chease = 0
        self.tomato = 0

    def add_chease(self) -> None:
        self.chease += 1
    
    def add_bacon(self) -> None:
        raise Exception(f"{self.__class__.__name__} does not have bacon")
    
    def add_ananas(self) -> None:
        self.ananas += 1

    def add_mashrooms(self) -> None:
        raise Exception(f"{self.__class__.__name__} does not have mashrooms")

    def add_seafood(self) -> None:
        raise Exception(f"{self.__class__.__name__} does not have seafood")
    
    def add_tomato(self) -> None:
        self.tomato += 1

    def make(self) -> HawaiiPizza:
        return HawaiiPizza(self.ananas, self.chease, self.tomato)
    
    def reset(self) -> None:
        self.ananas = 0
        self.chease = 0
        self.tomato = 0
