import pygame
import game_functions as gf
from pygame.sprite import Group
from ship import Ship
from settings import Settings
from button import Button
from bullet import Bullet
from game_status import Gamestatus
from score_board import ScoreBoard

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
    bullets = Group()
    score_board = ScoreBoard(settings, status, screen)
    alien_success = False

    while True:
        screen.fill(settings.bg_color)
        gf.check_events(settings, screen, status, play_button, ship, bullets, score_board)

        aliens_collide = pygame.sprite.groupcollide(aliens, bullets, True, False)

        if aliens_collide:
            status.score += len(aliens_collide) * 10

        if pygame.sprite.spritecollideany(ship, aliens):
            alien_success = True

        if status.game_active:
            ship.updates()

            for alien in aliens:
                if alien.rect.top >= screen.get_rect().height:
                    alien_success = True
                if status.alien_move_x:
                    alien.left += settings.alien_speed_factor
                    if alien.left >= settings.screen_width - alien.rect.width:
                        status.alien_move_x = False
                else:
                    alien.left -= settings.alien_speed_factor
                    if alien.left <= 0:
                        status.alien_move_x = True
                alien.updates()
                
            if alien_success:
                gf.on_ship_hit(settings, screen, status, ship, bullets, aliens)
                alien_success = False

            for bullet in bullets:
                bullet.updates()

            score_board.updates(status)

            if not aliens:
                gf.create_fleet(settings, screen, aliens)
                status.alien_move_x = True

        ship.blitme()
        for bullet in bullets:
            bullet.draw_bullet()
        for alien in aliens:
            alien.blitme()
        if not status.game_active:
            play_button.draw_button()

        score_board.draw()

        pygame.display.flip()

run_game()
