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

    def update_start_menu(self, score, coins):
        self._display_title()
        self._display_score_start_menu()
        self._display_highscore(score)
        self._display_total_coins(coins)
        self.button_start_game()
        self.button_shop()

    def update_shop(self, coins):
        self._display_title()
        self._display_total_coins(coins)
        self.button_shop_speed()
        self.button_home()

    def update_game(self):
        self._display_title()
        self._display_lives()
        self._display_coins()
        self._display_wave()
        self._display_level()
        self._display_score()

    def _display_title(self):
        text_title = self.style_text.render(
            '- - - - - - - - -  s  p  a  c  e     s  h  o  o  t  e  r  - - - - - - - - -',
            True,
            'green'
        )

        text_rect = text_title.get_rect()
        text_rect.center = (cv.WINDOW_WIDTH / 2, 16)
        self.window.surface.blit(text_title, text_rect)

    def _display_coins(self):
        text_coins = self.style_text.render(f"{self.spaceship.coins}", True, (255, 215, 0))

        coin_img = pygame.image.load(cv.COIN_IMG_PATH)
        coin_img = pygame.transform.scale(coin_img, (28, 26))

        self.window.surface.blit(coin_img, (5, 5))
        self.window.surface.blit(text_coins, (45, 8))

    def _display_lives(self):
        text_lives = self.style_text.render(f"{self.spaceship.lives}", True, (255, 0, 0))

        heart_img = pygame.image.load(cv.HEART_IMG_PATH)
        heart_img = pygame.transform.scale(heart_img, (28, 26))

        self.window.surface.blit(heart_img, (5, 45))
        self.window.surface.blit(text_lives, (45, 49))

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

    def _display_score_start_menu(self):
        text_score = self.style_text.render(
            f"s c o r e     {self.enemy.total_killed * (self.spaceship.coins + 1)}",
            True,
            (0, 0, 255)
        )

        text_rect = text_score.get_rect()
        text_rect.center = (cv.WINDOW_WIDTH / 2, 40)
        self.window.surface.blit(text_score, text_rect)

    def _display_highscore(self, highscore):
        text_highscore = self.style_text.render(
            f"h i g h s c o r e     {highscore}",
            True,
            (255, 0, 0)
        )

        text_rect = text_highscore.get_rect()
        text_rect.center = (cv.WINDOW_WIDTH / 2, 200)
        self.window.surface.blit(text_highscore, text_rect)

    def _display_total_coins(self, coins):
        text_coins = self.style_text.render(f"{coins}", True, (255, 215, 0))

        coin_img = pygame.image.load(cv.COIN_IMG_PATH)
        coin_img = pygame.transform.scale(coin_img, (28, 26))

        self.window.surface.blit(coin_img, (5, 5))
        self.window.surface.blit(text_coins, (45, 8))

    # Buttons
    def button_start_game(self):
        start_button = pygame.Rect(cv.WINDOW_WIDTH / 2 - 100, cv.WINDOW_HEIGHT / 2 - 100, 200, 50)
        mouse = pygame.mouse.get_pos()

        if start_button.collidepoint(mouse):
            pygame.draw.rect(self.window.surface, (200, 0, 0), start_button, 0, 10)
            text_start = self.style_text.render(f"start game", True, (0, 0, 0))
        else:
            pygame.draw.rect(self.window.surface, (255, 0, 0), start_button, 0, 10)
            text_start = self.style_text.render(f"start game", True, (255, 255, 255))

        text_rect = text_start.get_rect()
        text_rect.center = (cv.WINDOW_WIDTH / 2, cv.WINDOW_HEIGHT / 2 - 75)
        self.window.surface.blit(text_start, text_rect)

        return start_button

    def button_shop(self):
        shop_button = pygame.Rect(cv.WINDOW_WIDTH / 2 - 100, cv.WINDOW_HEIGHT / 2 - 25, 200, 50)
        mouse = pygame.mouse.get_pos()

        if shop_button.collidepoint(mouse):
            pygame.draw.rect(self.window.surface, (200, 0, 0), shop_button, 0, 10)
            text_shop = self.style_text.render(f"shop", True, (0, 0, 0))
        else:
            pygame.draw.rect(self.window.surface, (255, 0, 0), shop_button, 0, 10)
            text_shop = self.style_text.render(f"shop", True, (255, 255, 255))

        text_rect = text_shop.get_rect()
        text_rect.center = (cv.WINDOW_WIDTH / 2, cv.WINDOW_HEIGHT / 2)
        self.window.surface.blit(text_shop, text_rect)

        return shop_button

    def button_shop_speed(self):
        shop_speed_button = pygame.Rect(cv.WINDOW_WIDTH / 2 - 100, cv.WINDOW_HEIGHT / 2 - 25, 200, 50)
        mouse = pygame.mouse.get_pos()

        if shop_speed_button.collidepoint(mouse):
            pygame.draw.rect(self.window.surface, (200, 0, 0), shop_speed_button, 0, 10)
            text_shop_speed = self.style_text.render(f"buy speed {cv.PRICE_SPEED}", True, (0, 0, 0))
        else:
            pygame.draw.rect(self.window.surface, (255, 0, 0), shop_speed_button, 0, 10)
            text_shop_speed = self.style_text.render(f"buy speed {cv.PRICE_SPEED}", True, (255, 255, 255))

        text_rect = text_shop_speed.get_rect()
        text_rect.center = (cv.WINDOW_WIDTH / 2, cv.WINDOW_HEIGHT / 2)
        self.window.surface.blit(text_shop_speed, text_rect)

        return shop_speed_button

    def button_home(self):
        home_button = pygame.Rect(cv.WINDOW_WIDTH / 2 - 100, cv.WINDOW_HEIGHT - 75, 200, 50)
        mouse = pygame.mouse.get_pos()

        if home_button.collidepoint(mouse):
            pygame.draw.rect(self.window.surface, (200, 0, 0), home_button, 0, 10)
            text_home = self.style_text.render(f"home", True, (0, 0, 0))
        else:
            pygame.draw.rect(self.window.surface, (255, 0, 0), home_button, 0, 10)
            text_home = self.style_text.render(f"home", True, (255, 255, 255))

        text_rect = text_home.get_rect()
        text_rect.center = (cv.WINDOW_WIDTH / 2, cv.WINDOW_HEIGHT - 50)
        self.window.surface.blit(text_home, text_rect)

        return home_button