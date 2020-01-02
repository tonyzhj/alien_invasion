import pygame
import game_functions as gf
from pygame.sprite import Group
from ship import Ship
from settings import Settings
from button import Button
from bullet import Bullet
from game_status import Gamestatus

def run_game():
    pygame.init()
    settings = Settings()
    status = Gamestatus(settings)
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("飞机大战")
    #创建一艘飞船
    ship = Ship(settings, screen)
    #create a aliens row
    aliens = Group()
    gf.create_fleet(settings, screen, aliens)
    #create a begin button
    play_button = Button(settings, screen, "Play")
    play_button.draw_button()
    bullets = Group()

    while True:
        screen.fill(settings.bg_color)
        gf.check_events(settings, screen, status, play_button, ship, bullets)

        if status.game_active:
            ship.updates()
            for alien in aliens:
                alien.updates()
            for bullet in bullets:
                bullet.updates()

            if gf.FIRE:
                gf.COUNT += 1
                if gf.COUNT == 15:
                    bullet = Bullet(settings, screen, ship)
                    bullets.add(bullet)
                    gf.COUNT = 0

            if not aliens:
                gf.create_fleet(settings, screen, aliens)

        ship.blitme()
        for bullet in bullets:
            bullet.draw_bullet()
        for alien in aliens:
            alien.blitme()
        if not status.game_active:
            play_button.draw_button()

        pygame.sprite.groupcollide(bullets, aliens, True, True)

        if pygame.sprite.spritecollideany(ship, aliens):
            gf.on_ship_hit(settings, screen, status, ship, bullets, aliens)

        pygame.display.flip()

run_game()
