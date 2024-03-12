from .observer import Observer

class RoadService(Observer):
    _emergency_messages = {
        1: "Road service is working!",
        2: "Road service is working!",
        3: "Road service is dont working!",
    }
    
    def notify(self, notify_type: str, emergency_lvl: int) -> None:
        self._status = self._emergency_messages.get(emergency_lvl, "Unknown emergency level!")
        print(f"Now is {notify_type}. Road service status changed to: {self._status}")
        