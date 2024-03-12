from .observer import Observer


class Airport(Observer):
    _emergency_messages = {
        1: "Airport closed!",
        2: "Airport closed!",
        3: "Airport is working!",
    }
    
    def notify(self, notify_type: str, emergency_lvl: int) -> None:
        if notify_type == "StormNotification":
            self._status = self._emergency_messages.get(emergency_lvl, "Unknown emergency level!")
            print(f"Now is {notify_type}. Airport status changed to: {self._status}")
        elif notify_type == "RainNotification":
            print(f"Now is {notify_type}. Airport working alwais in rainy weather!")
