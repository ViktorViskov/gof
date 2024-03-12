from .pizza_decorator import PizzaDecorator
from models.abstract_pizza import AbstractPizza


class MashroomsDecorator(PizzaDecorator):      
    def create(self) -> AbstractPizza:
        self.subject.add_mashrooms()
        return self.subject.create()
