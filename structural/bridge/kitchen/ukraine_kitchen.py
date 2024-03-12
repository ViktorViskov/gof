from kitchen.abstract_kitchen import AbstractKitchen
from dish.abstract_dish import AbstractDish
from dish.first_dish import FirstDish
from dish.second_dish import SecondDish
from dish.third_dish import ThirdDish
from dish.desert_dish import DesertDish


class UkrainianKitchen(AbstractKitchen):
    def create_first(self) -> AbstractDish:
        return FirstDish("Ukrainian")
    
    def create_second(self) -> AbstractDish:
        return SecondDish("Ukrainian")
    
    def create_third(self) -> AbstractDish:
        return ThirdDish("Ukrainian")
    
    def create_desert(self) -> AbstractDish:
        return DesertDish("Ukrainian")