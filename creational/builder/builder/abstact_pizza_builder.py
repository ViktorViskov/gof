from __future__ import annotations
from abc import ABC
from abc import abstractmethod

from models.pizza import Pizza


class AbstractPizzaBuilder(ABC):
    @abstractmethod
    def add_chease(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def add_bacon(self) -> None:
        raise NotImplementedError()
    
    @abstractmethod
    def add_ananas(self) -> None:
        raise NotImplementedError()
    
    @abstractmethod
    def add_mashrooms(self) -> None:
        raise NotImplementedError()
    
    @abstractmethod
    def add_seafood(self) -> None:
        raise NotImplementedError()
    
    @abstractmethod
    def add_tomato(self) -> None:
        raise NotImplementedError()
    
    @abstractmethod
    def make(self) -> Pizza:
        raise NotImplementedError()
    
    @abstractmethod
    def reset(self) -> None:
        raise NotImplementedError()