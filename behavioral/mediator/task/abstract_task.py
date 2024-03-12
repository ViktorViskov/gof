from abc import (
    ABC,
    abstractmethod
)


class AbstractTask(ABC):
    @abstractmethod
    def do(self) -> None:
        pass