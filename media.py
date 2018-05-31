class Movie():
    """This class serves as a way to store movie related information
    Attributes:
        movie_title (str): Title of movie
        movie_poster_url (str): Link to the movie's poster image
        movie_trailer_url (str): Link to the movie's trailer
    """

    # initialization of class, taking input in to initialize object variables
    def __init__(self, movie_title, movie_poster_url, movie_trailer_url):
        self.title = movie_title
        self.poster_image_url = movie_poster_url
        self.trailer_youtube_url = movie_trailer_url
