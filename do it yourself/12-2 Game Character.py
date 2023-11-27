import sys
import pygame

class Settings():
    """A class to store all settings for Alien Invasion."""
    def __init__(self, screen):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0,0,255)

        self.screen = screen
        self.character_image = pygame.image.load("images/character.png")
        self.rect = self.character_image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx