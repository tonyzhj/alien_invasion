import sys
from time import sleep
import pygame
from alien import Alien
from bullet import Bullet

FIRE = False
COUNT = 0
def create_fleet(settings, screen, aliens):
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    numbers_x = int(settings.screen_width / (alien_width * 2))
    numbers_y = 2

    for row_number in range(numbers_y):
        for alien_number in range(numbers_x):
            alien = Alien(settings, screen)
            alien.rect.left = (alien_number*2 + 1)*alien_width
            alien.top = (row_number*2 + 1)*alien_height
            aliens.add(alien)

def check_events(settings, screen, ship, bullets):
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
                #bullet = Bullet(settings, screen, ship)
                #bullets.add(bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False
            elif event.key == pygame.K_SPACE:
                FIRE = False
    global COUNT
    if FIRE:
        COUNT += 1
        if COUNT == 15:
            bullet = Bullet(settings, screen, ship)
            bullets.add(bullet)
            COUNT = 0

def on_ship_hit(settings, screen, ship, bullets, aliens):
    bullets.empty()
    aliens.empty()
    ship.center = ship.screen_rect.centerx
    sleep(0.5)
    create_fleet(settings, screen, aliens)
    print("Ship hit!!!")                