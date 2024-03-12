from .pizza import Pizza
from builder.abstact_pizza_builder import AbstractPizzaBuilder


class SeafoodPizza(Pizza):
    chease = 0
    tomato = 0
    mashrooms = 0
    seafood = 0

    @staticmethod
    def get_builder() -> AbstractPizzaBuilder:
        from builder.seafood_pizza_builder import SeafoodPizzaBuilder
        return SeafoodPizzaBuilder()
    
    def __init__(self, chease: int, tomato: int, mashrooms: int, seafood: int) -> None:
        self.chease = chease
        self.tomato = tomato
        self.mashrooms = mashrooms
        self.seafood = seafood

    def show_ingradients(self) -> None:
        print(f"{self.__class__.__name__} Ingredients:")
        print(f"Chease: {self.chease}")
        print(f"Tomato: {self.tomato}")
        print(f"Mashrooms: {self.mashrooms}")
        print(f"Seafood: {self.seafood}")
