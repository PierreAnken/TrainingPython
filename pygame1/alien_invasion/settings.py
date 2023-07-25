import pygame.time


from screenresolution import ScreenResolution
from aliengame import AlienInvasion  # Fehler weil import loop


class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        screen_res = ScreenResolution()
        self.screen_width = screen_res.screen_resolution_width
        self.screen_height = screen_res.screen_resolution_height
        self.bg_color = (230, 230, 230)

        self.fps = 60
        self.clock = pygame.time.Clock()

        # Ship settings
        self.ship_speed = 3
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # How quickly the game speeds up
        self.speedup_scale = 1.1
        # How quickly the alien point values increase
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""

        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        # Scoring
        self.alien_points = 100
        self.bullet_points = -10

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        count_bullet = AlienInvasion()  # Objekt um den Wert bullet_fired zu importieren
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(((self.alien_points + (self.bullet_points * count_bullet.bullet_fired)) * self.score_scale))  # alien points - bullet points * bullet fired
