from memento import Memento
from ordinator import Ordinator


class CareTaker:
    _states: list[Memento] = []

    def save_state(self, ordinator: Ordinator) -> None:
        self._states.append(ordinator.get_state())

    def get_state(self, index: int) -> Memento:
        return self._states[index]