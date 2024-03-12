from abc import ABC
from abc import abstractmethod

from dish.abstract_dish import AbstractDish


class AbstractKitchen(ABC):      
    @abstractmethod
    def create_first(self) -> AbstractDish:
        raise NotImplementedError()

    @abstractmethod
    def create_second(self) -> AbstractDish:
        raise NotImplementedError()
    
    @abstractmethod
    def create_third(self) -> AbstractDish:
        raise NotImplementedError()
    
    @abstractmethod
    def create_desert(self) -> AbstractDish:
        raise NotImplementedError()
