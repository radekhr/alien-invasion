import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	
	def __init__(self, screen, ai_settings):
		
		super().__init__()
		self.screen = screen
		self.ai_settings = ai_settings
		self.image = pygame.image.load('img/ufo.bmp')
		self.image = pygame.transform.scale(self.image, (80, 40))
		self.rect = self.image.get_rect()
		
		#umieszczenie obcego w poblizu lewego gornego rogu ekranu
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		self.x = float(self.rect.x)
		
	def blitme(self):
		"""Wyswietlenie statku kosm. w jego aktualnym polozeniu."""
		self.screen.blit(self.image, self.rect)
		
	def update(self):
		self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
		self.rect.x = self.x
		
	def check_edges(self):
		"""Zwraca True jesli obcy znajduje sie przy krawedzi ekranu"""
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right or self.rect.left <= 0:
			return True
		
