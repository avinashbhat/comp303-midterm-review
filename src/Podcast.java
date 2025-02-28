public class Podcast implements MusicType {

    private String aPodcastName;

    /**
     * Creates a new Podcast
     * @pre podcastName != null && podcastName contains only letters and spaces
     * @param podcastName the name of the podcast (must not be null and must contain only letters and spaces)
     */
    public Podcast(String podcastName) {
        assert podcastName != null : "Podcast name cannot be null";
        assert isValidPodcastName(podcastName) : "Podcast name must contain only letters and spaces";

        aPodcastName = podcastName;
    }

    private boolean isValidPodcastName(String name) {
        return name.matches("^[a-zA-Z ]+$");
    }

    public String getPodcastName() {
        return aPodcastName;
    }

    /**
     * Sets podcast name
     * @pre podcastName != null && podcastName contains only letters and spaces
     * @param podcastName
     */
    public void setPodcastName(String podcastName) {
        assert podcastName != null : "Podcast name cannot be null";
        assert isValidPodcastName(podcastName) : "Podcast name must contain only letters and spaces";
        aPodcastName = podcastName;
    }

    /**
     * Play the podcast
     * @pre aPodcastName is not null
     */
    public void play() {
        assert aPodcastName != null : "Podcast name cannot be null when playing";
        System.out.println(aPodcastName);
    }

}