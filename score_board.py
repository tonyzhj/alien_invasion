import pygame

#dispaly the num of ship and score
class ScoreBoard:
    def __init__(self, settings, status, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.font = pygame.font.SysFont(None, 48)
        self.ship_num_image = self.font.render(str(settings.ship_total_num), True, (0, 255, 0))
        self.ship_num_image_rect = self.ship_num_image.get_rect()
        self.ship_num_image_rect.right = self.screen_rect.right - 30
        self.ship_num_image_rect.top = self.screen_rect.top + 10

        self.score_image = self.font.render(str(status.score), True, (0, 255, 0))
        self.score_rect = self.score_image.get_rect()
        self.score_rect.centerx = self.screen_rect.centerx
        self.score_rect.top = self.screen_rect.top + 10

    def updates(self, status):
        self.ship_num_image = self.font.render(str(status.ship_num), True, (0, 255, 0))
        self.score_image = self.font.render(str(status.score), True, (0, 255, 0))

    def draw(self):
        self.screen.blit(self.ship_num_image, self.ship_num_image_rect)
        self.screen.blit(self.score_image, self.score_rect)