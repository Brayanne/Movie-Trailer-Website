#import webbrowser #used to open website, in this case trailer url
class Movie():
		"""This class serves as a way to store movie related information"""

		def __init__(self, movie_title, movie_poster_url, movie_trailer_url):
			self.title = movie_title
			self.poster_image_url = movie_poster_url
			self.trailer_youtube_url = movie_trailer_url

		#def show_trailer(self):
		#	webbrowser.open(self.trailer_youtube_url)