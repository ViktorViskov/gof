from .abstract_factory import AbstractFactory
from models import Lasagna


class LasagnaFactory(AbstractFactory):
    def create_dish(self) -> Lasagna:
        return Lasagna()