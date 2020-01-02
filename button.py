import pygame

class Button():
    def __init__(self, settings, screen, msg):
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 200, 50)
        self.screen_rect = screen.get_rect()
        self.rect.center = self.screen_rect.center
        self.font = pygame.font.SysFont(None, 48)
        self.msg_image = self.font.render(msg, True, (255, 255, 255), (0, 255, 0))
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.screen_rect.center

    def draw_button(self):
        self.screen.fill((0, 255, 0), self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

