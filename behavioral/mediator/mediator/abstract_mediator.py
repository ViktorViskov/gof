from abc import (
    ABC, 
    abstractmethod
)


class AbstractMediator(ABC):
    @abstractmethod
    def send_message(self, message: str) -> bool:
        pass