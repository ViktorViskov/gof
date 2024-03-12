from oven import Oven


def client_code(oven: Oven) -> None:
    oven.set_oven_state(Oven.ReadyOvenState())
    oven.bake()
    oven.set_oven_state(Oven.ColdOvenState())
    oven.bake()
    oven.set_oven_state(Oven.OverheatOvenState())
    oven.bake()

oven = Oven()
client_code(oven)