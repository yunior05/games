import fresh_tomatoes
import main

League_of_Legends = main.Games("League of Legends",
								"27/10/2009",
								"Moba",
								"https://upload.wikimedia.org/wikipedia/commons/f/f7/League_of_Legends.png",
								"https://www.youtube.com/watch?v=vzHrjOMfHPY") 

Legend_of_Zelda = main.Games("The Legend of Zelda: Ocarina of Time",
								"21/11/1998",
								"Action-Adventure",
								"https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/The_Legend_of_Zelda_Ocarina_of_Time.svg/500px-The_Legend_of_Zelda_Ocarina_of_Time.svg.png",
								"https://www.youtube.com/watch?v=pF7p9hruSeY")

Fortnite = main.Games("Fortnite",
						"21/07/2017",
						"Battle Royale",
						"https://upload.wikimedia.org/wikipedia/commons/3/36/Fortnite.png",
						"https://www.youtube.com/watch?v=2gUtfBmw86Y")

Portal = main.Games("Portal",
						"9/10/2007",
						"Puzzle, Logic",
						"https://upload.wikimedia.org/wikipedia/commons/d/df/Portal_logo.png",
						"https://www.youtube.com/watch?v=TluRVBhmf8w")

Pokemon_Perla = main.Games("Pokemon Pearl",
							"28/09/2006",
							"RPG",
							"https://images-na.ssl-images-amazon.com/images/I/41cg5eaAdjL.jpg",
							"https://www.youtube.com/watch?v=4WanmE8BUC4")

games = [League_of_Legends, Legend_of_Zelda, Fortnite, Portal, Pokemon_Perla]

fresh_tomatoes.open_movies_page(games)