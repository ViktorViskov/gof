from notification.abstract_notification import AbstractNotification
from notification.storm import StormNotification
from notification.rain import RainNotification
from observer.airport import Airport
from observer.school import School
from observer.road_service import RoadService


def client_code(notification: AbstractNotification) -> None:
    print("-" * 30)
    notification.notify(1)
    print("-" * 30)
    notification.notify(3)
    


school = School()
airport = Airport()
road_service = RoadService()

storm = StormNotification()
storm.add_observer(school)
storm.add_observer(airport)
storm.add_observer(road_service)

rain = RainNotification()
rain.add_observer(school)
rain.add_observer(airport)
rain.add_observer(road_service)

client_code(storm)

storm.remove_observer(school)

client_code(storm)
client_code(rain)

    
    