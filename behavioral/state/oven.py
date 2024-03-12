from abstract_oven import AbstractOven


class Oven(AbstractOven):
    class ColdOvenState(AbstractOven):
        def bake(self) -> None:
            raise Exception("The oven is cold.")
        
    class ReadyOvenState(AbstractOven):
        def bake(self) -> None:
            print("Baking ...")

    class OverheatOvenState(AbstractOven):
        def bake(self) -> None:
            raise Exception("The oven is overheated.")

    _state: AbstractOven

    def set_oven_state(self, state: AbstractOven) -> None:
        self._state = state

    def bake(self) -> None:
        self._state.bake()