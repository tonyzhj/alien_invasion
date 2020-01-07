import pygame

#dispaly the num of ship and score
class ScoreBoard:
    def __init__(self, settings, status, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.font = pygame.font.SysFont(None, 48)
        self.font_color = (0, 255, 0)
        self.ship_num_image = self.font.render(str(settings.ship_total_num), True, self.font_color)
        self.ship_num_image_rect = self.ship_num_image.get_rect()
        self.ship_num_image_rect.right = self.screen_rect.right - self.ship_num_image_rect.width
        self.ship_num_image_rect.top = self.screen_rect.top + 50

        self.score_image = self.font.render(str(status.score), True, self.font_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - self.score_rect.width
        self.score_rect.top = self.screen_rect.top + 5

        self.high_score_image = self.font.render(str(status.high_score), True, self.font_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top + 5

    def updates(self, status):
        self.ship_num_image = self.font.render(str(status.ship_num), True, self.font_color)
        self.score_image = self.font.render(str(status.score), True, self.font_color)
        self.score_rect.right = self.screen_rect.right - self.score_image.get_rect().width
        self.high_score_image = self.font.render(str(status.high_score), True, self.font_color)

    def draw(self):
        self.screen.blit(self.ship_num_image, self.ship_num_image_rect)
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
