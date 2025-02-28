import java.util.HashMap;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class SongFactory {
    static final HashMap<Integer, Song> playList = new HashMap<>();

    public static Song getSong(Song pSong) {
        Integer hash = pSong.getaSongName().hashCode() + pSong.getaArtistName().hashCode();
        if (playList.containsKey(hash)) {
            return playList.get(hash);
        } else {
            playList.put(hash, pSong);
            return playList.get(hash);
        }
    }

    private SongFactory(){}

}
