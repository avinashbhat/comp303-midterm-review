from song import Song
from typing import Optional, List, Dict, Iterator

class Singleton(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
    

class Library(metaclass=Singleton):
    def __init__(self):
        self.songs: List[Song] = []
        self._song_repository: Dict[str, Song] = {}
    
    # flyweight
    def add_song(self, song_name: str, artist_name: str, 
                 genre: Optional[str] = None, 
                 release_year: Optional[int] = None, 
                 duration: Optional[int] = None) -> None:
        key = f"{song_name}-{artist_name}"
        
        song = self._song_repository.get(key)
        
        if song is None:
            song = Song(song_name, artist_name)
            
            if genre:
                song.set_genre(genre)
            if release_year:
                song.set_release_year(release_year)
            if duration:
                song.set_duration(duration)
                
            self._song_repository[key] = song
            print(f"Created new song: {song_name}")
        else:
            print(f"Reused existing song: {song_name}")
            if genre:
                song.set_genre(genre)
            if release_year:
                song.set_release_year(release_year)
            if duration:
                song.set_duration(duration)
        
        self.songs.append(song)
    
    def get_songs(self) -> List[Song]:
        return self.songs
    
    def get_song_iterator(self) -> Iterator[Song]:
        return iter(self.songs)
    
    def play_all_songs(self) -> None:
        for song in self.songs:
            song.play()
        print("x-x-x-----All Songs-----x-x-x")