import unittest
from song import Song
from songfactory import SongFactory
from library import Library

class TestSongFactory(unittest.TestCase):
    def setUp(self):
        SongFactory.playlist = {}
        Library._instance = None
    
    def test_song_factory_no_size_increase(self):
        s1 = Song("Kerala", "Bonobo")
        Library().add_song(s1)
        Library().add_song(s1)
        self.assertEqual(1, len(SongFactory.playlist))
    
    def test_song_factory_size_increase(self):
        s1 = Song("Kerala", "Bonobo")
        s2 = Song("Navajo", "Masego")
        Library().add_song(s1)
        Library().add_song(s2)
        self.assertEqual(2, len(SongFactory.playlist))

if __name__ == "__main__":
    unittest.main()