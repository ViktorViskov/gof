from abc import ABC
from abc import abstractmethod

from observer.observer import Observer

class AbstractNotification(ABC):
    _observers: list[Observer]
    
    def __init__(self):
        self._observers = []
    
    def add_observer(self, observer:Observer):
        if observer not in self._observers:
            self._observers.append(observer)
    
    def remove_observer(self, observer:Observer):
        if observer in self._observers:
            self._observers.remove(observer)
    
    def _notify(self, notify_type:str, emergency_lvl: int) -> None:
        for observer in self._observers:
            observer.notify(notify_type ,emergency_lvl)
    
    @abstractmethod
    def notify(self, emergency_lvl: int) -> None:
        pass