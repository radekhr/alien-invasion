import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	
	def __init__(self, ai_settings, screen, ship):
		"""Utworzenie obiektu pocisku w aktualnym polozeniu statku"""
		super(Bullet, self).__init__()
		self.screen = screen
		
		self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
		
		#polozenie pocisku jest zdef. za pomoca wartosci float
		self.y = float(self.rect.y)
		
		self.color = ai_settings.bullet_color
		self.speed_factor = ai_settings.bullet_speed_factor
		
	def update(self):
		"""Poruszanie pociskiem po ekranie"""
		self.y -= self.speed_factor
		self.rect.y = self.y
		
	def draw_bullet(self):
		"""Wyswietlenie pociskow na ekranie"""
		pygame.draw.rect(self.screen, self.color, self.rect)
		
