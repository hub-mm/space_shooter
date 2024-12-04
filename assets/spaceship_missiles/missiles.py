# ./assets/spaceship_missiles/missiles.py
from variables import constants as cv

import pygame

class Missiles(object):
    def __init__(
            self,
            window,
            size = (),
            speed = 0,
            gap_next = 0,
            gap = 0,
            delay_next = 0,
            delay = 0,
            maximum = 0,
    ):
        self.window = window

        self.size = size
        self.speed = speed

        self.gap_next = gap_next
        self.gap = gap

        self.delay_next = delay_next
        self.delay = delay

        self.maximum = maximum
        self.missiles_count = self.maximum

        self.missiles = []

    def generate_missiles(self):
        keys = pygame.key.get_pressed()

        missile = pygame.Rect(
            cv.X + (cv.START_SIZE[0] / 2) - (self.size[0] / 2),
            cv.Y + (cv.START_SIZE[1] / 2) - (self.size[1]),
            self.size[0],
            self.size[1],
        )

        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            self.logic_missiles(missile)

    def logic_missiles(self, missile):
        current_time = pygame.time.get_ticks()
        if self.missiles_count < self.maximum and current_time >= self.gap_next:
            self.missiles_count += 1
            self.gap_next = self.gap + current_time

            self.missiles.append(missile)

        if self.missiles_count >= self.maximum and current_time >= self.delay_next:
            self.delay_next = self.delay + current_time
            self.missiles_count = 0

    def move_missiles(self):
        for missile in self.missiles:
            missile[1] -= self.speed

            pygame.draw.rect(
                self.window.surface,
                cv.COLOUR_BULLET,
                missile
            )

            if missile[1] <= 0:
                self.missiles.remove(missile)