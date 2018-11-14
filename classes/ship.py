import pygame


class Ship():

    def __init__(self, screen, ai_settings):
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('img/rocket.bmp')
        self.image = pygame.transform.scale(self.image, (55, 70))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        self.moving_left = False
        self.moving_right = False

    def update(self):
        """Uaktualnienie polozenia statku na podstawie przytrzymania danego klawisza"""
        # Uaktualnienie wartosci punktu srodkowego statku, a nie jego prostokata
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # Uaktualnienie obiektu rect na podstawie wartosci self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Wyswietlenie statku kosm. w jego aktualnym polozeniu."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Umieszcz. statku na srodku przy dolnej krawedzi"""
        self.center = self.screen_rect.centerx