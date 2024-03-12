from .abstract_notification import AbstractNotification


class RainNotification(AbstractNotification):
    def __init__(self):
        super().__init__()
        
    def notify(self, emergency_lvl: int) -> None:
        if emergency_lvl > 0 and emergency_lvl < 4:
            print("Rain is coming! LVL: ", emergency_lvl)
            self._notify(self.__class__.__name__, emergency_lvl)