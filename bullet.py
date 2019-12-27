import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, settings, screen, ship):
        """初始化飞船并设置其初始设置"""
        super(Bullet, self).__init__()
        self.ship = ship
        self.screen = screen
        self.color = settings.bullet_color
        self.speed_factor = settings.bullet_speed_factor
        self.rect = pygame.Rect(self.ship.rect.centerx, self.ship.rect.top - settings.bullet_height,
                                settings.bullet_width, settings.bullet_height)
        self.top = float(self.rect.top)

    def updates(self):
        self.top -= self.speed_factor
        self.rect.top = self.top  

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
