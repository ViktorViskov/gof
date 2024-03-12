from threading import Lock


class Shared:
    _instance = None
    _lock: Lock = Lock()
    
    # make singleton
    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
        return cls._instance