from some_services.protocol_service import ProtocolService


class AbstractProxy:
    subject: ProtocolService

    def __init__(self, service: ProtocolService) -> None:
        self.subject = service