from .pizza_decorator import PizzaDecorator
from models.abstract_pizza import AbstractPizza


class SeafoodDecorator(PizzaDecorator):       
    def create(self) -> AbstractPizza:
        self.subject.add_seafood()
        return self.subject.create()
