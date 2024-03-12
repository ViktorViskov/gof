from abc import ABC
from abc import abstractmethod

from zeep import Client

from threading import Lock


class AbstractService(ABC):
    _instance = None
    _lock: Lock = Lock()
    
    # make singleton
    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self) -> None:
        self.client = Client("http://www.dneonline.com/calculator.asmx?WSDL")

    @abstractmethod
    def operation(self, num1:int, num2:int) -> int:
        pass