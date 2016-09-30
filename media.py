import webbrowser
class Movie():
	VALID_STRINGS = ['G', 'PG', 'PG-13', 'R']
	def __init__(self, movie_title, movie_discription, movie_poster, movie_trailer):
		self.title = movie_title
		self.discription = movie_discription
		self.poster_image_url = movie_poster
		self.trailer_youtube_url = movie_trailer
	
	def openPoster(self):
		webbrowser.open(self.poster_image_url)
def testFunction(string):
	print(string)
