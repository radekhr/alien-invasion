class GameStats():
    """Monitorowanie danych statycznych w grze 'Inwazja Obcych' """

    def __init__(self, ai_settings):
        """Inic. danych statycznych"""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        """Inic. danych staycznych, ktore moga sie zmieniac w trakcie gry"""
        self.ships_left = self.ai_settings.ship_limit
