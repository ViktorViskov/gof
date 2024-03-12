from .pizza_decorator import PizzaDecorator
from models.abstract_pizza import AbstractPizza


class CheaseDecorator(PizzaDecorator):       
    def create(self) -> AbstractPizza:
        self.subject.add_chease()
        return self.subject.create()
