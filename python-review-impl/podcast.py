from musictype import MusicType
from typing import Optional

class Podcast(MusicType):
    def __init__(self, podcast_name: str):
        self.podcast_name = podcast_name
        self.host: Optional[str] = None
        self.episode_number: Optional[int] = None
        self.category: Optional[str] = None
    
    def set_host(self, host: str) -> None:
        self.host = host
    
    def set_episode_number(self, episode_number: int) -> None:
        self.episode_number = episode_number
    
    def set_category(self, category: str) -> None:
        self.category = category
    
    def play(self) -> None:
        print(f"Playing podcast: {self.podcast_name}")
        
        if self.host:
            print(f"Host: {self.host}")
        
        if self.episode_number:
            print(f"Episode: {self.episode_number}")
        
        if self.category:
            print(f"Category: {self.category}")
        
        print("x-x-x-----Playing Podcast-----x-x-x")