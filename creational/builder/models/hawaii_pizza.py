from .pizza import Pizza
from builder.abstact_pizza_builder import AbstractPizzaBuilder


class HawaiiPizza(Pizza):
    ananas = 0
    chease = 0
    tomato = 0

    @staticmethod
    def get_builder() -> AbstractPizzaBuilder:
        from builder.hawaii_pizza_builder import HawaiiPizzaBuilder
        return HawaiiPizzaBuilder()
    
    def __init__(self, ananas: int, chease: int, tomato: int) -> None:
        self.ananas = ananas
        self.chease = chease
        self.tomato = tomato

    def show_ingradients(self) -> None:
        print(f"{self.__class__.__name__} Ingredients:")
        print(f"Ananas: {self.ananas}")
        print(f"Chease: {self.chease}")
        print(f"Tomato: {self.tomato}")
