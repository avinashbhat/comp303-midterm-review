class SongFactory:
    playlist = {}
    
    @staticmethod
    def get_song(song):
        key = f"{song.song_name}-{song.artist_name}"
        if key not in SongFactory.playlist:
            SongFactory.playlist[key] = song
            print(f"Created new song: {song.song_name}")
        else:
            print(f"Reused existing song: {song.song_name}")
        return SongFactory.playlist[key]