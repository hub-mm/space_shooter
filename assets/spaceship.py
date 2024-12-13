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
        self.state_count = 0
        self.state = 'normal'

        self.spaceship_img = pygame.image.load(cv.SPACESHIP_IMG_PATH)
        self.spaceship_img = pygame.transform.scale(self.spaceship_img, cv.START_SIZE)

    def update(self):
        self._handle_movement()

        if self.state == 'invincible':
            self._check_state()
            self._end_invincibility_animation()

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

    def _check_state(self):
        self.state_count += 1
        if self.state_count > 600:
            self.state = 'normal'
            self.state_count = 0
            self.spaceship_img = pygame.image.load(cv.SPACESHIP_IMG_PATH)
            self.spaceship_img = pygame.transform.scale(self.spaceship_img, cv.START_SIZE)

    def _end_invincibility_animation(self):
        if 570 < self.state_count < 580:
            self.spaceship_img = pygame.image.load(cv.SPACESHIP_IMG_PATH)
            self.spaceship_img = pygame.transform.scale(self.spaceship_img, cv.START_SIZE)
        elif 580 < self.state_count < 585:
            self.spaceship_img = pygame.image.load(cv.SPACESHIP_INVINCIBLE_IMG_PATH)
            self.spaceship_img = pygame.transform.scale(self.spaceship_img, cv.START_SIZE)
        elif 585 < self.state_count < 590:
            self.spaceship_img = pygame.image.load(cv.SPACESHIP_IMG_PATH)
            self.spaceship_img = pygame.transform.scale(self.spaceship_img, cv.START_SIZE)
        elif 590 < self.state_count < 595:
            self.spaceship_img = pygame.image.load(cv.SPACESHIP_INVINCIBLE_IMG_PATH)
            self.spaceship_img = pygame.transform.scale(self.spaceship_img, cv.START_SIZE)

    def _lose_life_animation(self):
        self.window.surface.fill((100, 0, 0))
        self.window.surface.fill(cv.COLOUR_BACKGROUND)
        self.window.surface.fill((100, 0, 0))

    def lose_life(self):
        if self.state == 'invincible':
            return

        self._lose_life_animation()
        self.lives -= 1