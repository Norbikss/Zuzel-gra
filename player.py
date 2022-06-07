import math
import pygame
#from collections import deque

vec = pygame.math.Vector2
class Player:
	#klasa gracza
	def __init__(self, game, x, y, color):
		self.screen = game.screen
		self.settings = game.settings 

		#własciwiosci gracza
		self.color = color
		self.width = game.settings.player_width



		#dokladne wartosci x i y
		self.x = float(x)
		self.y = float(y)
		self.x2 = self.x - 10
		self.y2 = self.y
		#kat obrotu vektora
		self.angle = 0
		#szybkosc inkrementacji x(poruszania sie gracza)
		self.speed = game.settings.player_speed
		#pozycje startowe vektorów
		#self.vel = vec(0, 0)
		self.pos = vec(self.x , self.y)
		self.start = vec(self.x2, self.y2)
		#punkty do rysowania lini
		self.start_points = []
		self.end_points = []



		#przytrzymanie klawisza dla poruszania sie
		self.moving_left = False


	def update(self):
		#do przodu

		self.vel = vec(self.settings.player_speed,0).rotate(-self.angle)

		#zmiana pozycji o vektor
		self.pos += self.vel
		self.start_points.append(self.pos)
		if len(self.start_points) >= 10:
			del self.start_points[:6]


		
		if len(self.start_points) > 2:
			for point in self.start_points:
				x = self.pos.x + math.cos(math.radians(self.angle)) * self.width
				y = self.pos.y - math.sin(math.radians(self.angle)) * self.width
				self.start = vec(x, y)
				self.end_points.append(self.start)

			pygame.draw.lines(self.screen, self.color, False, self.end_points, width = 3)



		if len(self.end_points) >=10:
			del self.end_points[:6]



		if self.moving_left:
			#update rotation
			self.angle = (self.angle + 1) % 360


	def start_possition(self):
		self.x = self.x 
		self.y = self.y
		self.angle = 0
		self.pos = vec(self.x, self.y)
		self.start = vec(self.x2, self.y2)

	def points(self):
		return self.x



			

		