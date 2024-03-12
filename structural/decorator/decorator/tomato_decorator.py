from .pizza_decorator import PizzaDecorator
from models.abstract_pizza import AbstractPizza


class TomatoDecorator(PizzaDecorator):
    def create(self) -> AbstractPizza:
        self.subject.add_tomato()
        return self.subject.create()
