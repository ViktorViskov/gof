from some_services.protocol_service import ProtocolService
from some_services.plus_service import PlusService
from some_services.minus_service import MinusService
from some_services.multiply_service import MultiplyService
from some_services.divide_service import DivideService
from proxy.cache_proxy import CacheProxy
from decorator.profiler_decorator import ProfilerDecorator


class Facade:
    _plus_service: ProtocolService
    _minus_service: ProtocolService
    _multiply_service: ProtocolService
    _divide_service: ProtocolService

    def __init__(self) -> None:
        self._plus_service = ProfilerDecorator(CacheProxy(PlusService()))
        self._minus_service = ProfilerDecorator(CacheProxy(MinusService()))
        self._multiply_service = ProfilerDecorator(CacheProxy(MultiplyService()))
        self._divide_service = ProfilerDecorator(CacheProxy(DivideService()))

    def plus(self, num1: int, num2: int) -> int:
        return self._plus_service.operation(num1, num2)
    
    def minus(self, num1: int, num2: int) -> int:
        return self._minus_service.operation(num1, num2)
    
    def multiply(self, num1: int, num2: int) -> int:
        return self._multiply_service.operation(num1, num2)
    
    def divide(self, num1: int, num2: int) -> int:
        return self._divide_service.operation(num1, num2)