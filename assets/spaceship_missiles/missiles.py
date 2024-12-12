# ./assets/spaceship_missiles/missiles.py
import pygame

from variables import constants as cv
from assets.missile_sprite import BulletSprite


class Missiles(object):
    def __init__(self, window, size = (), speed = 0, gap_next = 0, gap = 0, delay_next = 0, delay = 0, maximum = 0):
        self.window = window
        self.size = size
        self.speed = speed
        self.gap_next = gap_next
        self.gap = gap
        self.delay_next = delay_next
        self.delay = delay
        self.maximum = maximum
        self.missiles_count = self.maximum

        self.bullet_group = pygame.sprite.Group()

    def generate_missiles(self):
        keys = pygame.key.get_pressed()
        missiles_x = cv.X + (cv.START_SIZE[0] / 2)
        missiles_y = cv.Y + (cv.START_SIZE[0] / 2) - self.size[1]

        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            self._logic_missiles(missiles_x, missiles_y)

        self.bullet_group.update()
        self.bullet_group.draw(self.window.surface)

    def _logic_missiles(self, x, y):
        current_time = pygame.time.get_ticks()

        if self.missiles_count < self.maximum and current_time >= self.gap_next:
            self.missiles_count += 1
            self.gap_next = self.gap + current_time
            bullet = BulletSprite(x, y, self.size[0], self.size[1], self.speed, cv.COLOUR_BULLET)
            self.bullet_group.add(bullet)

        if self.missiles_count >= self.maximum and current_time >= self.delay_next:
            self.delay_next = self.delay + current_time
            self.missiles_count = 0