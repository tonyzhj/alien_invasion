import pygame

#dispaly the num of ship and score
class ScoreBoard:
    def __init__(self, settings, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.font = pygame.font.SysFont(None, 48)
        self.ship_num_image = self.font.render(str(settings.ship_total_num), True, (255, 255, 255), (0, 255, 0))
        self.ship_num_image_rect = self.ship_num_image.get_rect()
        self.ship_num_image_rect.centerx = self.screen_rect.centerx

    def updates(self, status):
        self.ship_num_image = self.font.render(str(status.ship_num), True, (255, 255, 255), (0, 255, 0))
 
    def draw(self):
        self.screen.blit(self.ship_num_image, self.ship_num_image_rect)