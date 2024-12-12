# ./display/text_display.py
import pygame.font

from variables import constants as cv


class TextDisplay(object):
    def __init__(self, window, enemy, spaceship):
        self.window = window
        self.enemy = enemy
        self.spaceship = spaceship
        self.style_text = pygame.font.SysFont('roboto', 34, True)

        self.wave = 1

    def update_game(self):
        self._display_title()
        self._display_lives()
        self._display_coins()
        self._display_wave()
        self._display_level()
        self._display_score()

    def update_start_menu(self, score):
        self._display_title()
        self._display_high_score(score)

    def _display_title(self):
        text_title = self.style_text.render(
            '- - - - - - - - -  s  p  a  c  e     s  h  o  o  t  e  r  - - - - - - - - -',
            True,
            'green'
        )

        text_rect = text_title.get_rect()
        text_rect.center = (cv.WINDOW_WIDTH / 2, 16)

        self.window.surface.blit(text_title, text_rect)

    def _display_lives(self):
        text_lives = self.style_text.render(f"{self.spaceship.lives}", True, (255, 0, 0))

        heart_img = pygame.image.load(cv.HEART_IMG_PATH)
        heart_img = pygame.transform.scale(heart_img, (28, 26))

        self.window.surface.blit(heart_img, (5, 5))
        self.window.surface.blit(text_lives, (45, 8))

    def _display_coins(self):
        text_coins = self.style_text.render(f"{self.spaceship.coins}", True, (255, 215, 0))

        coin_img = pygame.image.load(cv.COIN_IMG_PATH)
        coin_img = pygame.transform.scale(coin_img, (28, 26))

        self.window.surface.blit(coin_img, (5, 45))
        self.window.surface.blit(text_coins, (45, 49))

    def _display_wave(self):
        text_wave = self.style_text.render(f"wave {self.enemy.wave}", True, (255, 255, 255))

        text_rect = text_wave.get_rect()
        text_rect.topright = (cv.WINDOW_WIDTH - 8, 8)

        self.window.surface.blit(text_wave, text_rect)

    def _display_level(self):
        text_level = self.style_text.render(f"level {self.enemy.level - 1}", True, (255, 255, 255))

        text_rect = text_level.get_rect()
        text_rect.topright = (cv.WINDOW_WIDTH - 8, 49)

        self.window.surface.blit(text_level, text_rect)

    def _display_score(self):
        text_score = self.style_text.render(
            f"s c o r e     {self.enemy.total_killed * (self.spaceship.coins + 1)}",
            True,
            (0, 0, 255)
        )

        text_rect = text_score.get_rect()
        text_rect.center = (cv.WINDOW_WIDTH / 2, 40)

        self.window.surface.blit(text_score, text_rect)

    def _display_high_score(self, highscore):
        text_highscore = self.style_text.render(
            f"h i g h s c o r e     {highscore}",
            True,
            (255, 0, 0)
        )

        text_rect = text_highscore.get_rect()
        text_rect.center = (cv.WINDOW_WIDTH / 2, 40)

        self.window.surface.blit(text_highscore, text_rect)