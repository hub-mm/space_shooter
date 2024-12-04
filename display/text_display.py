# ./display/text_display.py
from variables import constants as cv

import pygame.font

class TextDisplay(object):
    def __init__(self, window, enemy, spaceship):
        self.window = window
        self.enemy = enemy
        self.spaceship = spaceship
        self.style_text = pygame.font.SysFont('roboto', 34, True)

        self.wave = 1

    def display_title(self):
        text_title = self.style_text.render(
            '-  -  -  -  -  s  p  a  c  e     s  h  o  o  t  e  r  -  -  -  -  -',
            True,
            'green'
        )

        text_rect = text_title.get_rect()
        text_rect.topleft = (80, 8)

        self.window.surface.blit(text_title, text_rect)

    def display_lives(self):
        text_lives = self.style_text.render(f"{self.spaceship.lives}", True, 'red')

        heart_img = pygame.image.load(cv.HEART_IMG_PATH)
        heart_img = pygame.transform.scale(heart_img, (28, 26))

        self.window.surface.blit(heart_img, (5, 5))
        self.window.surface.blit(text_lives, (45, 8))

    def display_wave(self):
        text_wave = self.style_text.render(f"wave {self.enemy.round}    level {self.enemy.wave}", True, 'white')

        text_rect = text_wave.get_rect()
        text_rect.topright = (cv.WINDOW_WIDTH - 8, 8)

        self.window.surface.blit(text_wave, text_rect)