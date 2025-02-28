from musictype import MusicType
from typing import Optional

class Song(MusicType):
    def __init__(self, song_name: str, artist_name: str):
        self.song_name = song_name
        self.artist_name = artist_name
        self.genre: Optional[str] = None
    
    def set_genre(self, genre: str) -> None:
        self.genre = genre
    
    def play(self) -> None:
        print(f"Playing song: {self.song_name} by {self.artist_name}")
        
        if self.genre:
            print(f"Genre: {self.genre}")
    
    
    # flyweight equality
    def __eq__(self, other):
        if not isinstance(other, Song):
            return False
        return self.song_name == other.song_name and self.artist_name == other.artist_name
    
    def __hash__(self):
        return hash((self.song_name, self.artist_name))