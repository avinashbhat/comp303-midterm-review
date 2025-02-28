import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class FlyweightTest {
    @Test
    public void testSongFactoryNoSizeIncrease() {
        Song s1 = new Song("Kerala", "Bonobo");
        Library.getInstance().addSong(s1);
        Library.getInstance().addSong(s1);
        assertEquals(1, SongFactory.playList.size());
    }

    @Test
    public void testSongFactorySizeIncrease() {
        Song s1 = new Song("Kerala", "Bonobo", "Blues");
        Song s2 = new Song("Navajo", "Masego", "Jazz/House");
        Library.getInstance().addSong(s1);
        Library.getInstance().addSong(s2);
        assertEquals(2, SongFactory.playList.size());
    }

}