import unittest
from library import Library

class TestSongFactory(unittest.TestCase):
    def setUp(self):
        Library._instance = None
    
    def test_song_factory_no_size_increase(self):
        Library().add_song("Kerala", "Bonobo")
        Library().add_song("Kerala", "Bonobo")
        self.assertEqual(1, len(Library()._song_repository))
    
    def test_song_factory_size_increase(self):
        Library().add_song("Kerala", "Bonobo")
        Library().add_song("Navajo", "Masego")
        self.assertEqual(2, len(Library()._song_repository))

if __name__ == "__main__":
    unittest.main()