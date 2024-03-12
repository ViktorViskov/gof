from .pizza_decorator import PizzaDecorator
from models.abstract_pizza import AbstractPizza


class AnanasDecorator(PizzaDecorator):
    def create(self) -> AbstractPizza:
        self.subject.add_ananas()
        return self.subject.create()
