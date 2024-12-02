# ./assets/spaceship.py
from variables import constants as cv

import pygame

class SpaceShip(object):
    def __init__(self):
        self.speed = 5
        self.size = (75, 75)

    def move_logic(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] and cv.X >= 5:
            cv.X -= self.speed

        if keys[pygame.K_d] and cv.X <= (cv.WINDOW_WIDTH - self.size[0]) - 5:
            cv.X += self.speed

        if keys[pygame.K_w] and cv.Y >= 5:
            cv.Y -= self.speed

        if keys[pygame.K_s] and cv.Y <= (cv.WINDOW_HEIGHT - self.size[1]) - 5:
            cv.Y += self.speed