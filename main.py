import webbrowser

class Games():

	def __init__(self, title_game, year_game, genre_game, gameplay_youtube):
		self.title = title
		self.year = year_game
		self.genre = genre_game
		self.gameplay = gameplay_youtube

	def show_gameplay(self):
		webbrowser.open(self.gameplay)
		
