from .abstract_service import AbstractService


class MultiplyService(AbstractService):
    def operation(self, num1: int, num2: int) -> int:
        return self.client.service.Multiply(num1, num2)