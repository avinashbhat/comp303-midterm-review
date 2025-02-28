import java.util.*;

public class Library implements Iterable<Song> {

    private static Library instance = new Library();

    private List<Song> songList = new ArrayList<Song>();
    private Library(){
    }

    public static Library getInstance() {
        return instance;
    }

    public void addSong(Song s) {
        Song val = SongFactory.getSong(s);
        songList.add(val);
    }

    @Override
    public Iterator<Song> iterator() {
        return songList.iterator();
    }

    public void playSongs() {
        for (Song song : this) {
            song.play();
        }
    }
}
