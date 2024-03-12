from mediator.sender_mediator import SenderMediator

from task.abstract_task import AbstractTask
from task.master_task import MasterTask
from task.flowers_task import FlowersTask
from task.taxi_task import TaxiTask


def client_code(task: AbstractTask) -> None:
    task.do()

mediator = SenderMediator()
tasks = [
    MasterTask(mediator),
    FlowersTask(mediator),
    TaxiTask(mediator)
]

for task in tasks:
    client_code(task)