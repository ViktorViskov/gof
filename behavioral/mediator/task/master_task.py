from .abstract_task import AbstractTask
from mediator.abstract_mediator import AbstractMediator


class MasterTask(AbstractTask):
    _mediator: AbstractMediator
    def __init__(self, mediator) -> None:
        self._mediator = mediator
    
    def do(self) -> None:
        if not self._mediator.send_message("Need master!"):
            print("Was not sent!")