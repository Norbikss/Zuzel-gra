class Settings:
	def __init__(self):
		#ustawienia ekranu
		self.width = 1200
		self.height = 800
		self.bg_color = (135, 135, 135)

		#ellipsy
		self.ellipse_color1 = (255, 255, 255)
		self.ellipse_color2 = (128, 128, 128)
		self.ellipse_width1 = 400
		self.ellipse_height1 = 200
		self.ellipse_width2 = 1200
		self.ellipse_height2 = 800

		#gracz


		self.player_width = 10
		self.player_speed = 2
		#player1
		self.player_color = (0,0,0)
		self.playerx = 580
		self.playery = 590
		#player2
		self.player_color2 = "Blue"
		self.player2x = 580
		self.player2y = 650

		#ustawienia gry

		self.game_active = False