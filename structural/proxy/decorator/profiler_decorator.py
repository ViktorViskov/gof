from datetime import datetime

from proxy.abstract_proxy import AbstractProxy


class ProfilerDecorator(AbstractProxy):
    _cache: dict = {}

    def _count_execution_time(self, num1: int, num2: int) -> int:
        start = datetime.now()
        result = self.subject.operation(num1, num2)
        stop = datetime.now()
        print(f"Execution time: {stop - start} for ", end="")
        return result

    def operation(self, num1: int, num2: int) -> int:
        return self._count_execution_time(num1, num2)