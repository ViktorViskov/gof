from .abstract_service import AbstractService


class MinusService(AbstractService):
    def operation(self, num1: int, num2: int) -> int:
        return self.client.service.Subtract(num1, num2)