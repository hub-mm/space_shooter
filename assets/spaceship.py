# ./assets/spaceship.py
import pygame

from variables import constants as cv


class SpaceShip(object):
    def __init__(self, window, enemy, speed, size):
        self.window = window
        self.enemy = enemy
        self.speed = speed
        self.size = size
        self.lives = 5
        self.coins = 0

        self.spaceship_img = pygame.image.load(cv.SPACESHIP_IMG_PATH)
        self.spaceship_img = pygame.transform.scale(self.spaceship_img, cv.START_SIZE)

    def update(self):
        self._handle_movement()

    def _handle_movement(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] and cv.X >= 5 or keys[pygame.K_LEFT] and cv.X >= 5:
            cv.X -= self.speed
        if (keys[pygame.K_d] and cv.X <= (cv.WINDOW_WIDTH - self.size[0]) - 5
                or keys[pygame.K_RIGHT] and cv.X <= (cv.WINDOW_WIDTH - self.size[0]) - 5):
            cv.X += self.speed
        if keys[pygame.K_w] and cv.Y >= 5 or keys[pygame.K_UP] and cv.Y >= 5:
            cv.Y -= self.speed
        if (keys[pygame.K_s] and cv.Y <= (cv.WINDOW_HEIGHT - self.size[1]) - 5
                or keys[pygame.K_DOWN] and cv.Y <= (cv.WINDOW_HEIGHT - self.size[1]) - 5):
            cv.Y += self.speed

    def lose_life(self):
        self.lives -= 1