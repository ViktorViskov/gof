from .abstract_factory import AbstractFactory
from models import Pizza


class PizzaFactory(AbstractFactory):
    def create_dish(self) -> Pizza:
        return Pizza()