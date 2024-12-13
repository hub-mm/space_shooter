# ./assets/spaceship_powerups/invincible.py
import pygame

from variables import constants as cv
from assets.spaceship_powerups.powerups import Powerups


class Invincible(Powerups):
    def __init__(self, window, spaceship, enemy, bullets, powerup_name, size, speed, colour):
        super().__init__(window, spaceship, enemy, bullets, powerup_name, size, speed, colour)

    def powerup_activated(self):
        self.spaceship.state = 'invincible'
        self.spaceship.spaceship_img = pygame.image.load(cv.SPACESHIP_INVINCIBLE_IMG_PATH)
        self.spaceship.spaceship_img = pygame.transform.scale(self.spaceship.spaceship_img, cv.START_SIZE)