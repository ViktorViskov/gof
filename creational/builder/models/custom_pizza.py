from .pizza import Pizza
from builder.abstact_pizza_builder import AbstractPizzaBuilder


class CustomPizza(Pizza):
    chease = 0
    bacon = 0
    ananas = 0
    mashrooms = 0
    seafood = 0
    tomato = 0

    @staticmethod
    def get_builder() -> AbstractPizzaBuilder:
        from builder.custom_pizza_builder import CustomPizzaBuilder
        return CustomPizzaBuilder()
    
    def __init__(self, chease: int, bacon:int , ananas: int, mashrooms: int, seafood: int, tomato: int) -> None:
        self.chease = chease
        self.bacon = bacon
        self.ananas = ananas
        self.tomato = tomato
        self.mashrooms = mashrooms
        self.seafood = seafood

    def show_ingradients(self) -> None:
        print(f"{self.__class__.__name__} Ingredients:")
        print(f"Chease: {self.chease}")
        print(f"Bacon: {self.bacon}")
        print(f"Ananas: {self.ananas}")
        print(f"Tomato: {self.tomato}")
        print(f"Mashrooms: {self.mashrooms}")
        print(f"Seafood: {self.seafood}")
