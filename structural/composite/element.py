from abc import ABC
from abc import abstractmethod


class Element(ABC):
    number = 0
    
    @abstractmethod
    def increment(self):
        pass
    
    @abstractmethod
    def decrement(self):
        pass