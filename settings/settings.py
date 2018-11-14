class Settings():
    """Klasa przeznaczona do przechowywania wsyzstkich ustawien w grze"""

    def __init__(self):
        """Inicjalizacja ustawien gry"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (66, 244, 176)

        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        self.alien_speed_factor = 15

        self.fleet_drop_speed = 10
        self.fleet_direction = 1  # 1 - prawo, -1 - lewo
