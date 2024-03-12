from __future__ import annotations


class Multiton:
    _instance = []

    def __new__(cls):
        if len(cls._instance) < 10:
            obj = super().__new__(cls)

            if obj not in cls._instance:
                cls._instance.append(obj)
        else:
            obj = cls._instance[9]

        return obj

    @staticmethod
    def get_instance() -> Multiton:        
        return Multiton()