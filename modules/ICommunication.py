from abc import ABC, abstractmethod

class ICommunication(ABC):
    @abstractmethod
    def send_command(self, command, repetition_times=5):
        pass

    @abstractmethod
    def send_command_when_expect(self, command, expected_response, repetition_times=5):
        pass

    @abstractmethod
    def open_port(self, repetition_times=20, waiting_seconds=5):
        pass

    @abstractmethod
    def close_port(self):
        pass