import pygame
import game_functions as gf
from pygame.sprite import Group
from ship import Ship
from settings import Settings

def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("飞机大战")
    #创建一艘飞船
    ship = Ship(settings, screen)
    #create a aliens row
    aliens = Group() 
    gf.create_fleet(settings, screen, aliens)

    bullets = Group()
    while True:
        screen.fill(settings.bg_color)
        gf.check_events(settings, screen, ship, bullets)

        ship.updates()
        ship.blitme()

        for bullet in bullets:
            bullet.updates()
            bullet.draw_bullet()
        for alien in aliens:
            alien.blitme()
        pygame.display.flip()

        pygame.sprite.groupcollide(bullets, aliens, True, True)
        if pygame.sprite.spritecollideany(ship, aliens):
            gf.on_ship_hit(settings, screen, ship, bullets, aliens)

run_game()
