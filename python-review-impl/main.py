from library import Library
from podcast import Podcast

def main():
    library = Library()
    
    library.add_song("Bohemian Rhapsody", "Queen", "Rock", 1975, 355)
    library.add_song("Yesterday", "The Beatles", "Pop", 1965, 125)
    library.add_song("Bohemian Rhapsody", "Queen")  # reuse the existing song
    library.add_song("Imagine", "John Lennon", "Pop", 1971, 183)
    
    print("\nPlaying all songs in library:")
    library.play_all_songs()
    
    print("\nUsing iterator:")
    for song in library.get_song_iterator():
        print(f"{song.song_name} by {song.artist_name}")
    
    podcast = Podcast("Tech Talk")
    podcast.set_host("John Doe")
    podcast.set_episode_number(42)
    podcast.set_category("Technology")
    
    print("\nPlaying a podcast:")
    podcast.play()


if __name__ == "__main__":
    main()