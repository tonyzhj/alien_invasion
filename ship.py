import pygame
from pygame.sprite import Sprite

class Ship(Sprite):    
    def __init__(self, settings, screen):
        """初始化飞船并设置其初始设置"""
        super(Ship, self).__init__()
        self.screen = screen        
        #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()        
        #将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False
        self.ship_speed_factor = settings.ship_speed_factor
            
    def updates(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.ship_speed_factor

    def blitme(self):
        """在指定位置绘制飞船"""
        self.rect.centerx = self.center
        self.screen.blit(self.image,self.rect)