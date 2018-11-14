import pygame
from funcs import game_functions as gf
from settings.settings import Settings
from classes.ship import Ship
from classes.button import Button
from classes.game_stats import GameStats
from pygame.sprite import Group



def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Inwazja OBCYCH!')

    play_button = Button(screen, ai_settings, 'Rozpocznij gre')

    stats = GameStats(ai_settings)
    ship = Ship(screen, ai_settings)
    bullets = Group()  # przechowywanie pociskow
    aliens = Group()

    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:
        gf.check_events(screen, ai_settings, stats, ship, aliens, bullets, play_button)
        gf.update_screen(screen, ai_settings, stats, ship, aliens, bullets, play_button)
        if stats.game_active:
            ship.update()
            gf.update_bullets(screen, ai_settings, ship, aliens, bullets)
            gf.update_aliens(screen, ai_settings, stats, ship, aliens, bullets)



run_game()
