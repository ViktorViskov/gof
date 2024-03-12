from abc import ABC
from abc import abstractmethod


class AbstractDish(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass
