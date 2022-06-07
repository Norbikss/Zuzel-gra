import pygame

class Ellipse:
	def __init__(self, game, color, width, height, fill):
		self.screen = game.screen
		self.settings = game.settings
		self.screen_rect = game.screen.get_rect()
		self.color = color 
		self.width = width 
		self.height = height 
		self.fill = fill
		self.size = pygame.Rect(0,0, self.width, self.height)
		self.size.center = self.screen_rect.center

	def draw_ellipse(self):
		pygame.draw.ellipse(self.screen, self.color, self.size, self.fill)