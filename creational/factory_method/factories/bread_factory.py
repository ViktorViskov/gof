from .abstract_factory import AbstractFactory
from models import Bread


class BreadFactory(AbstractFactory):
    def create_dish(self) -> Bread:
        return Bread()