from abc import ABC
from abc import abstractmethod


class Pizza(ABC):
    @staticmethod
    def get_builder():
        raise NotImplementedError()
    
    @abstractmethod
    def show_ingradients(self):
        raise NotImplementedError()