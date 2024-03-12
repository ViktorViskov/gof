from typing import Protocol


class ProtocolService(Protocol):
    def operation(self, num1: int, num2: int) -> int:
        pass