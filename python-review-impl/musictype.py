from abc import ABC, abstractmethod

class MusicType(ABC):
    @abstractmethod
    def play(self) -> None:
        pass