from models.idish import IDish
from models.first_dish import FirstDish
from models.second_dish import SecondDish
from .abstract_factory import AbstractFactory


class UkrainianDishFactory(AbstractFactory):
    def create_first(self) -> IDish:
        return FirstDish()
    
    def create_second(self) -> IDish:
        return SecondDish()