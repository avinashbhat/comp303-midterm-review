from musictype import MusicType
from typing import Optional

class Song(MusicType):
    def __init__(self, song_name: str, artist_name: str):
        self.song_name = song_name
        self.artist_name = artist_name
        self.genre: Optional[str] = None
        self.release_year: Optional[int] = None
        self.duration: Optional[int] = None
    
    def set_genre(self, genre: str) -> None:
        self.genre = genre
    
    def set_release_year(self, year: int) -> None:
        self.release_year = year
    
    def set_duration(self, duration: int) -> None:
        self.duration = duration
    
    def play(self) -> None:
        print(f"Playing song: {self.song_name} by {self.artist_name}")
        
        if self.genre:
            print(f"Genre: {self.genre}")
        
        if self.release_year:
            print(f"Released in: {self.release_year}")
        
        if self.duration:
            minutes = self.duration // 60
            seconds = self.duration % 60
            print(f"Duration: {minutes}:{seconds:02d}")
    
    # flyweight equality
    def __eq__(self, other):
        if not isinstance(other, Song):
            return False
        return self.song_name == other.song_name and self.artist_name == other.artist_name
    
    def __hash__(self):
        return hash((self.song_name, self.artist_name))