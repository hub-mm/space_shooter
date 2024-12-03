# ./assets/spaceship_missiles.py
from variables import constants as cv
from display.game_window import GameWindow

import pygame

class Missiles(object):
    def __init__(self):
        self.window = GameWindow()

        self.bullet_size = (10, 10)
        self.bullet_speed = 20

        self.bullet_gap_next = 0
        self.bullet_gap = 30

        self.bullet_delay_next = 0
        self.bullet_delay = 500

        self.max_bullets = 1
        self.bullet_count = self.max_bullets

    def generate_bullet(self):
        keys = pygame.key.get_pressed()

        bullet = pygame.Rect(
            cv.X + (cv.START_SIZE[0] / 2) - 5,
            cv.Y + (cv.START_SIZE[1] / 2) + 10,
            self.bullet_size[0],
            self.bullet_size[1],
        )

        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            self.bullet_logic(bullet)

    def bullet_logic(self, bullet):
        current_time = pygame.time.get_ticks()
        if self.bullet_count < self.max_bullets and current_time >= self.bullet_gap_next:
            self.bullet_count += 1
            self.bullet_gap_next = self.bullet_gap + current_time
            self.window.bullets.append(bullet)

        if self.bullet_count >= self.max_bullets and current_time >= self.bullet_delay_next:
            self.bullet_delay_next = self.bullet_delay + current_time
            self.bullet_count = 0

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