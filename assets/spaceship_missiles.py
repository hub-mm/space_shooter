# ./assets/spaceship_missiles.py
from variables import constants as cv
from display.game_window import GameWindow

import pygame

class Missiles(object):
    def __init__(self):
        self.window = GameWindow()

        self.bullet_size = (10, 10)
        self.bullet_speed = 10
        self.next_bullet = 0
        self.next_bullet_delay = 500

    def generate_bullet(self):
        keys = pygame.key.get_pressed()

        bullet = pygame.Rect(
            cv.X + (cv.START_SIZE[0] / 2) - 5,
            cv.Y + (cv.START_SIZE[1] / 2) + 10,
            self.bullet_size[0],
            self.bullet_size[1],
        )

        current_time = pygame.time.get_ticks()

        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT] and current_time > self.next_bullet:
            self.next_bullet_delay = 500
            self.next_bullet = self.next_bullet_delay + current_time

            self.window.bullets.append(bullet)

    def move_bullet(self):
        for bullet in self.window.bullets[:]:
            bullet[1] -= self.bullet_speed

            pygame.draw.rect(
                self.window.surface,
                cv.COLOUR_BULLET,
                bullet,
                3,
                2
            )

            if bullet[1] <= 0:
                self.window.bullets.remove(bullet)