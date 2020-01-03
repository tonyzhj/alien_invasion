import sys
from time import sleep
import pygame
from alien import Alien

FIRE = False
COUNT = 0
def create_fleet(settings, screen, aliens):
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    numbers_x = int(settings.screen_width / (alien_width * 2))
    numbers_y = 3

    for row_number in range(numbers_y):
        for alien_number in range(numbers_x):
            alien = Alien(settings, screen)
            alien.rect.left = (alien_number*2 + 1)*alien_width
            alien.top = (row_number*2 + 1)*alien_height
            aliens.add(alien)

def check_events(settings, screen, status, play_button, ship, bullets):
    global FIRE
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
            elif event.key == pygame.K_SPACE:
                FIRE = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False
            elif event.key == pygame.K_SPACE:
                FIRE = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if play_button.rect.collidepoint(mouse_x, mouse_y):
                status.game_active = True
                status.ship_num = settings.ship_total_num
                pygame.mouse.set_visible(False)

def on_ship_hit(settings, screen, status, ship, bullets, aliens):
    bullets.empty()
    aliens.empty()
    status.ship_num -= 1
    ship.center = ship.screen_rect.centerx
    ship.updates()

    if status.ship_num > 0:
        sleep(0.5)
    else:
        status.game_active = False
        pygame.mouse.set_visible(True)
    create_fleet(settings, screen, aliens)

    print("Ship hit!!!")
