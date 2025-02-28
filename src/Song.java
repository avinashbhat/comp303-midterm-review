import java.util.Optional;

public class Song implements MusicType{

    private final String aSongName;
    private final String aArtistName;
    private Optional<String> aGenre;

    Song(String sname, String aname, String genre) {
        aSongName = sname;
        aArtistName = aname;
        aGenre = Optional.ofNullable(genre);
    }

    Song(String sname, String aname) {
        aSongName = sname;
        aArtistName = aname;
        aGenre = Optional.empty();
    }

    public Optional<String> getGenre() {
        return aGenre;
    }

    public void setGenre(String genre) {
        aGenre = Optional.ofNullable(genre);
    }

    public String getaSongName(){
        return aSongName;
    }

    public String getaArtistName(){
        return aArtistName;
    }

    public void play(){
        System.out.println("Song: " + aSongName + "\t Artist:" + aArtistName + "\t Genre:" + aGenre.orElse("Unknown"));
    }
}
