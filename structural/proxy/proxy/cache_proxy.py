from .abstract_proxy import AbstractProxy


class CacheProxy(AbstractProxy):
    _cache: dict = {}

    def _get_from_cache(self, num1: int, num2: int) -> int:
        key = (self.subject.__class__.__name__, num1, num2)
        result = self._cache.get(key)
        if not result:
            result = self.subject.operation(num1, num2)
            self._cache[key] = result
        return result

    def operation(self, num1: int, num2: int) -> int:
        return self._get_from_cache(num1, num2)