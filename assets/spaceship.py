# ./assets/spaceship.py
from variables import constants as cv

import pygame

class SpaceShip(object):
    def __init__(self, window, enemy, speed, size):
        self.window = window
        self.enemy = enemy

        self.speed = 5
        self.size = (75, 75)
        self.lives = 5

        # Create spaceship image and size
        self.spaceship_img = pygame.image.load(cv.SPACESHIP_IMG_PATH)
        self.spaceship_img = pygame.transform.scale(self.spaceship_img, cv.START_SIZE)

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

    def loose_life(self):
        for enemy in self.enemy.window.enemies:
            if enemy[1] == cv.WINDOW_HEIGHT:
                self.lives -= 1
            elif enemy.colliderect(pygame.Rect(cv.X, cv.Y, self.size[0], self.size[1])):
                self.enemy.window.enemies.remove(enemy)
                self.lives -= 1