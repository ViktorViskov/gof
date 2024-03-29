from __future__ import annotations
from abc import ABC
from abc import abstractmethod


class AbstractSorting(ABC):
    @abstractmethod
    def sort(self, array: list[int], strategy: AbstractSorting) ->  list[int]:
        pass