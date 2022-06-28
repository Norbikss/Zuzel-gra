import sys
import pygame
from math import cos, sin 
from collections import deque
from settings import Settings
from ellipse import Ellipse
from player import Player
from button import Button 


vec = pygame.math.Vector2
class Motorki:
	#glowna klasa

	def __init__(self):

		pygame.init()
		self.settings = Settings()
		

		self.screen = pygame.display.set_mode([self.settings.width, self.settings.height])
		self.settings.screen_width = self.screen.get_rect().width 
		self.settings.screen_height = self.screen.get_rect().height 
		 

		pygame.display.set_caption("Motorki")

		self.ellipse = Ellipse(self, self.settings.ellipse_color1, self.settings.ellipse_width1, self.settings.ellipse_height1, 0)
		self.ellipse2 = Ellipse(self,self.settings.ellipse_color2, self.settings.ellipse_width2, self.settings.ellipse_height2, 0)
		self.player = Player(self, self.settings.playerx, self.settings.playery, self.settings.player_color)
		self.player2 = Player(self, self.settings.player2x, self.settings.player2y, self.settings.player_color2)
		self.play_button = Button(self, "Start", self.screen.get_rect().center)


	def run_game(self):
		# glowna petla gry
		clock = pygame.time.Clock()

		while True:
			clock.tick(60)
			self.check_events()
			if self.settings.game_active:

				
				self.check_collide(self.ellipse.width, self.ellipse.height, self.ellipse.size, self.player.start.x, self.player.start.y)
				self.check_collide2(self.ellipse2.width, self.ellipse2.height, self.ellipse2.size, self.player.start.x, self.player.start.y)
				self.check_collide(self.ellipse.width, self.ellipse.height, self.ellipse.size, self.player2.start.x, self.player2.start.y)
				self.check_collide2(self.ellipse2.width, self.ellipse2.height, self.ellipse2.size, self.player2.start.x, self.player2.start.y)
				self.speed()


				


			self.update_screen()



	def check_events(self):
		#sprawdzanie akcji gracza
		#zeby wyłaczyc okno
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self.check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self.check_keyup_events(event)
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				self.check_play_button(mouse_pos)

	def check_keydown_events(self, event):
		if event.key == pygame.K_q:
			self.settings.game_active = False
			self.player.start_points.clear()
			self.player.end_points.clear()
			self.player2.start_points.clear()
			self.player2.end_points.clear()
		elif event.key == pygame.K_a:
			self.player.moving_left = True
		elif event.key == pygame.K_l:
			self.player2.moving_left = True



	def check_keyup_events(self, event):
		if event.key == pygame.K_a:
			self.player.moving_left = False
		elif event.key == pygame.K_l:
			self.player2.moving_left = False

	def check_collide(self, width, height, rect, x, y):
		#sprawdzanie pozycji przy zderzeniach z ellipsami
		a = width // 2
		b = height // 2
		scale_y = a / b
		cpt_x, cpt_y = self.ellipse.size.center
		test_x = x #self.player.start.x 
		test_y = y #self.player.start.y 
		#test_y = float(self.player.rect.y)  
		dx = float(test_x - cpt_x)
		dy = float((test_y - cpt_y) * scale_y)
		collide = float(dx*dx + dy*dy <= a*a)
		
		if collide:
			self.settings.game_active = False
			self.player.start_points.clear()
			self.player.end_points.clear()
			self.player2.start_points.clear()
			self.player2.end_points.clear()

	def check_collide2(self, width, height, rect, x,y):

		#sprawdzanie pozycji przy zderzeniach z ellipsami
		a = width // 2
		b = height // 2
		scale_y = a / b
		cpt_x, cpt_y = self.ellipse2.size.center
		test_x = x #self.player.start.x
		test_y = y #self.player.start.y 
		#test_y = self.player.rect.y  
		dx = test_x - cpt_x
		dy = (test_y - cpt_y) * scale_y
		collide = dx*dx + dy*dy <= a*a
		
		if not collide:
			self.settings.game_active = False
			self.player.start_points.clear()
			self.player.end_points.clear()
			self.player2.start_points.clear()
			self.player2.end_points.clear()



	def check_play_button(self, mouse_pos):
		button_clicked = self.play_button.rect.collidepoint(mouse_pos)
		if button_clicked and not self.settings.game_active:
			self.settings.game_active = True
			self.player.start_possition()
			self.player2.start_possition()
			pygame.mouse.set_visible(False)




	def speed(self):
		if not self.settings.game_active:
			self.settings.player_speed = 2
		else:
			self.settings.player_speed += 0.004




		

	def update_screen(self):
		if not self.settings.game_active:
			self.screen.fill(self.settings.bg_color)
			self.play_button.draw_button()
			pygame.mouse.set_visible(True)
		else:
			self.screen.fill(self.settings.bg_color)
			self.ellipse2.draw_ellipse()
			self.ellipse.draw_ellipse()
			self.player.update()
			self.player2.update()



		pygame.display.flip()

start = Motorki()
start.run_game()