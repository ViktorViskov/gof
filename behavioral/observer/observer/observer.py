from abc import (
    ABC,
    abstractmethod
)


class Observer(ABC):
    _status: str
    
    @abstractmethod
    def notify(self, notify_type:str, emergency_lvl: int) -> None:
        pass
    
    def get_status(self) -> str:
        return self._status