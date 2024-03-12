from abc import ABC
from abc import abstractmethod


class AbstractCommand(ABC):
    @abstractmethod
    def invoke(self):
        pass

    @abstractmethod
    def undo(self):
        pass