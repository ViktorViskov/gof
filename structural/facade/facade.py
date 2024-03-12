from some_services.plus_service import PlusService
from some_services.minus_service import MinusService
from some_services.multiply_service import MultiplyService
from some_services.divide_service import DivideService


class Facade:
    _plus_service: PlusService
    _minus_service: MinusService
    _multiply_service: MultiplyService
    _divide_service: DivideService

    def __init__(self) -> None:
        self._plus_service = PlusService()
        self._minus_service = MinusService()
        self._multiply_service = MultiplyService()
        self._divide_service = DivideService()

    def plus(self, num1: int, num2: int) -> int:
        return self._plus_service.operation(num1, num2)
    
    def minus(self, num1: int, num2: int) -> int:
        return self._minus_service.operation(num1, num2)
    
    def multiply(self, num1: int, num2: int) -> int:
        return self._multiply_service.operation(num1, num2)
    
    def divide(self, num1: int, num2: int) -> int:
        return self._divide_service.operation(num1, num2)