import webbrowser

class Games():

	def __init__(self, title_game, year_game, genre_game,poster_image, trailer_youtube):
		self.title = title_game
		self.year = year_game
		self.genre = genre_game
		self.poster = poster_image
		self.trailer = trailer_youtube

	def show_gameplay(self):
		webbrowser.open(self.trailer)

