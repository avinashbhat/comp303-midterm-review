public class Main {
    public static void main(String[] args) {

        Song s1 = new Song("Kerala", "Bonobo");
        Song s2 = new Song("Navajo", "Masego", "Blues");
        Song s3 = new Song("Wonderwall", "Oasis", "Rock");
        Song s4 = new Song("I'm Yours", "Jason Mraz");
        Podcast p1 = new Podcast("The Daily Show");

        Library.getInstance().addSong(s1);
        Library.getInstance().addSong(s2);
        Library.getInstance().addSong(s3);

        Library.getInstance().playSongs();

    }
}