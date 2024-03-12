from random import randint


class Sender:
    @staticmethod
    def send_message(message: str) -> bool:
        was_sended = bool(randint(0,1))
        
        if was_sended:
            print(f"Sending message: {message}")
        else:
            print(f"Error sending message: {message}")
        
        return was_sended