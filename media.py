#import webbrowser module
import webbrowser

# creating Movie class that provides a way to stroe movie related information
class Movie():

    """Class variable"""
    VALID_RATINGS = ["G", "PG", "PG_13", "R"]
    
    """This function provides constructors and initializes objects when called."""
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    """This function is used to open youtube url"""
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
            
