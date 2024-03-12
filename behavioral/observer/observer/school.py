from .observer import Observer


class School(Observer):
    _emergency_messages = {
        1: "School is closed!",
        2: "School is working!",
        3: "School is working!"
    }
    
    def notify(self, notify_type: str, emergency_lvl: int) -> None:
        self._status = self._emergency_messages.get(emergency_lvl, "Unknown emergency level!")
        print(f"Now is {notify_type}. School status changed to: {self._status}")
        