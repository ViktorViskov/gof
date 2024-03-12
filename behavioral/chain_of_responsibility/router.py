from handlers.abstract_handler import AbstractHandler


class Router:
    _handlers: list[AbstractHandler]
    _error_handler: AbstractHandler

    def __init__(self, handlers: list[AbstractHandler], error_handler: AbstractHandler) -> None:
        self._handlers = handlers
        self._error_handler = error_handler

    def add_handler(self, handler: AbstractHandler) -> None:
        self._handlers.append(handler)
    
    def handle(self, target: str) -> str:
        handler = next((handler for handler in self._handlers if handler.can_do(target)), self._error_handler)
        return handler.do()


