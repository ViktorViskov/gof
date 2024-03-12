from .abstract_factory import AbstractFactory
from models import Cake


class CakeFactory(AbstractFactory):
    def create_dish(self) -> Cake:
        return Cake()