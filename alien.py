import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        self.speed_factor = settings.alien_speed_factor
        self.top = float(self.rect.top)

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        if self.top < self.screen.get_rect().height:
            self.top += self.speed_factor
        self.rect.top = self.top
        