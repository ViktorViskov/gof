from router import Router
from handlers.error_handler import ErrorHandler
from handlers.fire_handler import FireHandler
from handlers.hospital_handler import HospitalHandler
from handlers.police_handler import PoliceHandler


def client_code(router: Router)-> None:
    print(router.handle("police"))
    print(router.handle("health"))
    print(router.handle("fire"))
    print(router.handle("car"))

error_handler = ErrorHandler()
handlers = [
    FireHandler(),
    HospitalHandler(),
    PoliceHandler()
]

router = Router(handlers, error_handler)

client_code(router)