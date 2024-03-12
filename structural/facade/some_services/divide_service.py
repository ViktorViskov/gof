from .abstract_service import AbstractService


class DivideService(AbstractService):
    def operation(self, num1: int, num2: int) -> int:
        return self.client.service.Divide(num1, num2)