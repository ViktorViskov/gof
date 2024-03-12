from .pizza_decorator import PizzaDecorator
from models.abstract_pizza import AbstractPizza


class BaconDecorator(PizzaDecorator):            
    def create(self) -> AbstractPizza:     
        self.subject.add_bacon()
        return self.subject.create()
