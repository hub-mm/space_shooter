# ./display/text_display.py
import pygame.font

from variables import constants as cv


class TextDisplay(object):
    def __init__(self, window, enemy, spaceship):
        self.window = window
        self.enemy = enemy
        self.spaceship = spaceship
        self.style_text_bold = pygame.font.SysFont('roboto', 34, True)
        self.style_text_not_bold = pygame.font.SysFont('roboto', 34, False)
        self.wave = 1

    def update_start_menu(self, score, coins, game_state):
        self._display_title()
        self._display_score_start_menu()
        self._display_highscore(score)
        self._display_total_coins(coins)
        self._display_menu()
        self.button_start_game()
        self.button_shop()
        self.button_guide()
        self.button_keyboard_shortcuts()
        if game_state == 'show_shortcuts':
            self.display_keyboard_shortcuts()
        self.button_exit_home()

    def update_shop(self, coins):
        self._display_title()
        self._display_total_coins(coins)
        self.button_shop_speed()
        self.button_shop_extra_shot()
        self.button_shop_reduce_gap()
        self.button_shop_extra_coin()
        self.button_home()

    def update_guide(self, coins):
        self._display_title()
        self._display_total_coins(coins)
        self._display_guide_rect()
        self._display_guide_move()
        self._display_guide_shoot()
        self._display_guide_powerup()
        self.button_home()

    def update_game(self, game_state):
        self._display_title()
        self._display_lives()
        self._display_coins()
        self._display_wave()
        self._display_level()
        self._display_score()

        if game_state == 'pause':
            self._pause_background()
            self.button_pause_continue()
            self.button_pause_exit_game()
            self.button_pause_home()

    def _display_title(self):
        text_title = self.style_text_bold.render(
            '- - - - - - - - -  s  p  a  c  e     s  h  o  o  t  e  r  - - - - - - - - -',
            True,
            'green'
        )

        text_rect = text_title.get_rect()
        text_rect.center = (cv.WINDOW_WIDTH / 2, 16)
        self.window.surface.blit(text_title, text_rect)

    def _display_coins(self):
        text_coins = self.style_text_bold.render(f"{self.spaceship.coins}", True, (255, 215, 0))

        coin_img = pygame.image.load(cv.COIN_IMG_PATH)
        coin_img = pygame.transform.scale(coin_img, (28, 26))

        self.window.surface.blit(coin_img, (5, 5))
        self.window.surface.blit(text_coins, (45, 8))

    def _display_lives(self):
        text_lives = self.style_text_bold.render(f"{self.spaceship.lives}", True, (255, 0, 0))

        heart_img = pygame.image.load(cv.HEART_IMG_PATH)
        heart_img = pygame.transform.scale(heart_img, (28, 26))

        self.window.surface.blit(heart_img, (5, 45))
        self.window.surface.blit(text_lives, (45, 49))

    def _display_wave(self):
        text_wave = self.style_text_bold.render(f"wave {self.enemy.wave}", True, (255, 255, 255))

        text_rect = text_wave.get_rect()
        text_rect.topright = (cv.WINDOW_WIDTH - 8, 8)
        self.window.surface.blit(text_wave, text_rect)

    def _display_level(self):
        text_level = self.style_text_bold.render(f"level {self.enemy.level - 1}", True, (255, 255, 255))

        text_rect = text_level.get_rect()
        text_rect.topright = (cv.WINDOW_WIDTH - 8, 49)
        self.window.surface.blit(text_level, text_rect)

    def _display_score(self):
        text_score = self.style_text_bold.render(
            f"s c o r e     {self.enemy.total_killed * (self.spaceship.coins + 1)}",
            True,
            (0, 0, 255)
        )

        text_rect = text_score.get_rect()
        text_rect.center = (cv.WINDOW_WIDTH / 2, 40)
        self.window.surface.blit(text_score, text_rect)

    def _display_score_start_menu(self):
        text_score = self.style_text_bold.render(
            f"s c o r e     {self.enemy.total_killed * (self.spaceship.coins + 1)}",
            True,
            (0, 0, 255)
        )

        text_rect = text_score.get_rect()
        text_rect.center = (cv.WINDOW_WIDTH / 2, 40)
        self.window.surface.blit(text_score, text_rect)

    def _display_highscore(self, highscore):
        text_highscore = self.style_text_bold.render(
            f"h i g h s c o r e     {highscore}",
            True,
            (255, 0, 0)
        )

        highscore_rect = pygame.Rect(5, 187.5, cv.WINDOW_WIDTH - 10, 25)
        pygame.draw.rect(self.window.surface, (0, 255, 0), highscore_rect, 0, 2)

        text_rect = text_highscore.get_rect()
        text_rect.center = (cv.WINDOW_WIDTH / 2, 200)
        self.window.surface.blit(text_highscore, text_rect)

    def _display_total_coins(self, coins):
        text_coins = self.style_text_bold.render(f"{coins}", True, (255, 215, 0))

        coin_img = pygame.image.load(cv.COIN_IMG_PATH)
        coin_img = pygame.transform.scale(coin_img, (28, 26))

        self.window.surface.blit(coin_img, (5, 5))
        self.window.surface.blit(text_coins, (45, 8))

    def _display_menu(self):
        menu_rect = pygame.Rect(cv.WINDOW_WIDTH / 2 - 150, cv.WINDOW_HEIGHT / 2 - 175, 300, 375)
        pygame.draw.rect(self.window.surface, (0, 0, 150), menu_rect, 0, 10)

        text_menu = self.style_text_bold.render(f"m e n u", True, (255, 255, 255))
        text_rect = text_menu.get_rect()
        text_rect.center = (cv.WINDOW_WIDTH / 2, cv.WINDOW_HEIGHT / 2 - 150)
        self.window.surface.blit(text_menu, text_rect)

    def display_keyboard_shortcuts(self):
        shortcut_rect = pygame.Rect(cv.WINDOW_WIDTH / 2 - 250, cv.WINDOW_HEIGHT / 2 + 210, 500, 105)
        pygame.draw.rect(self.window.surface, (0, 255, 0), shortcut_rect, 0, 10)

        text_enter = self.style_text_not_bold.render(f"enter  -->  start game", True, (255, 0, 0))
        text_rect = text_enter.get_rect()
        text_rect.center = (cv.WINDOW_WIDTH / 2, cv.WINDOW_HEIGHT / 2 + 235)
        self.window.surface.blit(text_enter, text_rect)

        text_escape = self.style_text_not_bold.render(f"escape  -->  quit game", True, (255, 0, 0))
        text_rect = text_enter.get_rect()
        text_rect.center = (cv.WINDOW_WIDTH / 2, cv.WINDOW_HEIGHT / 2 + 260)
        self.window.surface.blit(text_escape, text_rect)

        text_pause = self.style_text_not_bold.render(f"p  -->  pause game", True, (255, 0, 0))
        text_rect = text_enter.get_rect()
        text_rect.center = (cv.WINDOW_WIDTH / 2, cv.WINDOW_HEIGHT / 2 + 285)
        self.window.surface.blit(text_pause, text_rect)

    def _display_guide_rect(self):
        guide_rect = pygame.Rect(cv.WINDOW_WIDTH / 2 - 250, cv.WINDOW_HEIGHT / 2 - 350, 500, 700)
        pygame.draw.rect(self.window.surface, (0, 0, 150), guide_rect, 0, 10)

    def _display_guide_move(self):
        text_move_title = self.style_text_bold.render(f"-  -  -  -  -  -  -  -  -  -  m o v e  -  -  -  -  -  -  -  -  -  -", True, (255, 0, 0))
        text_rect = text_move_title.get_rect()
        text_rect.center = (cv.WINDOW_WIDTH / 2, cv.WINDOW_HEIGHT / 2 - 300)
        self.window.surface.blit(text_move_title, text_rect)

        text_move_wasd = self.style_text_not_bold.render(f"WASD", True, (255, 255, 255))
        text_rect = text_move_wasd.get_rect()
        text_rect.center = (cv.WINDOW_WIDTH / 2, cv.WINDOW_HEIGHT / 2 - 250)
        self.window.surface.blit(text_move_wasd, text_rect)

        text_move_arrow_keys = self.style_text_not_bold.render(f"up, right, down, left keys", True, (255, 255, 255))
        text_rect = text_move_arrow_keys.get_rect()
        text_rect.center = (cv.WINDOW_WIDTH / 2, cv.WINDOW_HEIGHT / 2 - 225)
        self.window.surface.blit(text_move_arrow_keys, text_rect)

    def _display_guide_shoot(self):
        text_shoot_title = self.style_text_bold.render(f"-  -  -  -  -  -  -  -  -  s h o o t  -  -  -  -  -  -  -  -  -", True, (255, 0, 0))
        text_rect = text_shoot_title.get_rect()
        text_rect.center = (cv.WINDOW_WIDTH / 2, cv.WINDOW_HEIGHT / 2 - 150)
        self.window.surface.blit(text_shoot_title, text_rect)

        text_shoot = self.style_text_not_bold.render(f"left SHIFT or right SHIFT", True, (255, 255, 255))
        text_rect = text_shoot.get_rect()
        text_rect.center = (cv.WINDOW_WIDTH / 2, cv.WINDOW_HEIGHT / 2 - 100)
        self.window.surface.blit(text_shoot, text_rect)

    def _display_guide_powerup(self):
        text_powerup_title = self.style_text_bold.render(f"-  -  -  -  -  -  -  -  p o w e r u p s  -  -  -  -  -  -  -  -", True, (255, 0, 0))
        text_rect = text_powerup_title.get_rect()
        text_rect.center = (cv.WINDOW_WIDTH / 2, cv.WINDOW_HEIGHT / 2 - 25)
        self.window.surface.blit(text_powerup_title, text_rect)

        text_square_colour = self.style_text_not_bold.render(f"square colours", True, (255, 0, 0))
        text_rect = text_square_colour.get_rect()
        text_rect.center = (cv.WINDOW_WIDTH / 2, cv.WINDOW_HEIGHT / 2 + 25)
        self.window.surface.blit(text_square_colour, text_rect)

        extra_shot_rect = pygame.Rect(cv.WINDOW_WIDTH / 2 - 100, cv.WINDOW_HEIGHT / 2 + 40, 200, 20)
        pygame.draw.rect(self.window.surface, (0, 0, 255), extra_shot_rect, 0, 5)
        text_extra_shot = self.style_text_not_bold.render(f"extra shot", True, (255, 255, 255))
        text_rect = text_extra_shot.get_rect()
        text_rect.center = (cv.WINDOW_WIDTH / 2, cv.WINDOW_HEIGHT / 2 + 50)
        self.window.surface.blit(text_extra_shot, text_rect)

        less_delay_rect = pygame.Rect(cv.WINDOW_WIDTH / 2 - 100, cv.WINDOW_HEIGHT / 2 + 65, 200, 20)
        pygame.draw.rect(self.window.surface, (255, 0, 0), less_delay_rect, 0, 5)
        text_less_delay = self.style_text_not_bold.render(f"less delay", True, (255, 255, 255))
        text_rect = text_less_delay.get_rect()
        text_rect.center = (cv.WINDOW_WIDTH / 2, cv.WINDOW_HEIGHT / 2 + 75)
        self.window.surface.blit(text_less_delay, text_rect)

        move_faster_rect = pygame.Rect(cv.WINDOW_WIDTH / 2 - 100, cv.WINDOW_HEIGHT / 2 + 90, 200, 20)
        pygame.draw.rect(self.window.surface, (0, 255, 0), move_faster_rect, 0, 5)
        text_move_faster = self.style_text_not_bold.render(f"move faster", True, (255, 255, 255))
        text_rect = text_move_faster.get_rect()
        text_rect.center = (cv.WINDOW_WIDTH / 2, cv.WINDOW_HEIGHT / 2 + 100)
        self.window.surface.blit(text_move_faster, text_rect)

        reduce_bullet_gap_rect = pygame.Rect(cv.WINDOW_WIDTH / 2 - 100, cv.WINDOW_HEIGHT / 2 + 115, 200, 20)
        pygame.draw.rect(self.window.surface, (255, 0, 255), reduce_bullet_gap_rect, 0, 5)
        text_reduce_bullet_gap = self.style_text_not_bold.render(f"reduce bullet gap", True, (255, 255, 255))
        text_rect = text_reduce_bullet_gap.get_rect()
        text_rect.center = (cv.WINDOW_WIDTH / 2, cv.WINDOW_HEIGHT / 2 + 125)
        self.window.surface.blit(text_reduce_bullet_gap, text_rect)

        text_icon = self.style_text_not_bold.render(f"icon", True, (255, 0, 0))
        text_rect = text_icon.get_rect()
        text_rect.center = (cv.WINDOW_WIDTH / 2, cv.WINDOW_HEIGHT / 2 + 175)
        self.window.surface.blit(text_icon, text_rect)

        heart_img = pygame.image.load(cv.HEART_IMG_PATH)
        heart_img = pygame.transform.scale(heart_img, (22, 20))
        self.window.surface.blit(heart_img, (cv.WINDOW_WIDTH / 2 - 90, cv.WINDOW_HEIGHT / 2 + 192))
        text_extra_life = self.style_text_not_bold.render(f"extra life", True, (255, 255, 255))
        text_rect = text_extra_life.get_rect()
        text_rect.center = (cv.WINDOW_WIDTH / 2, cv.WINDOW_HEIGHT / 2 + 200)
        self.window.surface.blit(text_extra_life, text_rect)

        coin_img = pygame.image.load(cv.COIN_IMG_PATH)
        coin_img = pygame.transform.scale(coin_img, (22, 20))
        self.window.surface.blit(coin_img, (cv.WINDOW_WIDTH / 2 - 90, cv.WINDOW_HEIGHT / 2 + 215))
        text_extra_coin = self.style_text_not_bold.render(f"extra coin", True, (255, 255, 255))
        text_rect = text_extra_coin.get_rect()
        text_rect.center = (cv.WINDOW_WIDTH / 2, cv.WINDOW_HEIGHT / 2 + 225)
        self.window.surface.blit(text_extra_coin, text_rect)

        invincibility_img = pygame.image.load(cv.INVINCIBLE_IMG_PATH)
        invincibility_img = pygame.transform.scale(invincibility_img, (22, 20))
        self.window.surface.blit(invincibility_img, (cv.WINDOW_WIDTH / 2 - 90, cv.WINDOW_HEIGHT / 2 + 238))
        text_invincible = self.style_text_not_bold.render(f"invincibility", True, (255, 255, 255))
        text_rect = text_invincible.get_rect()
        text_rect.center = (cv.WINDOW_WIDTH / 2, cv.WINDOW_HEIGHT / 2 + 250)
        self.window.surface.blit(text_invincible, text_rect)

    def _pause_background(self):
        pause_background_rect = pygame.Rect(cv.WINDOW_WIDTH / 2 - 125, cv.WINDOW_HEIGHT / 2 - 175, 250, 300)
        pygame.draw.rect(self.window.surface, (0, 255, 0, 128), pause_background_rect, 0 , 10)

        text_menu = self.style_text_bold.render(f"p a u s e", True, (255, 0, 0))
        text_rect = text_menu.get_rect()
        text_rect.center = (cv.WINDOW_WIDTH / 2, cv.WINDOW_HEIGHT / 2 - 150)
        self.window.surface.blit(text_menu, text_rect)


    # Buttons

    def button_start_game(self):
        start_button = pygame.Rect(cv.WINDOW_WIDTH / 2 - 125, cv.WINDOW_HEIGHT / 2 - 100, 250, 50)
        mouse = pygame.mouse.get_pos()

        if start_button.collidepoint(mouse):
            pygame.draw.rect(self.window.surface, (200, 0, 0), start_button, 0, 10)
            text_start = self.style_text_bold.render(f"start game", True, (0, 0, 0))
        else:
            pygame.draw.rect(self.window.surface, (255, 0, 0), start_button, 0, 10)
            text_start = self.style_text_bold.render(f"start game", True, (255, 255, 255))

        text_rect = text_start.get_rect()
        text_rect.center = (cv.WINDOW_WIDTH / 2, cv.WINDOW_HEIGHT / 2 - 75)
        self.window.surface.blit(text_start, text_rect)

        return start_button

    def button_shop(self):
        shop_button = pygame.Rect(cv.WINDOW_WIDTH / 2 - 125, cv.WINDOW_HEIGHT / 2 - 25, 250, 50)
        mouse = pygame.mouse.get_pos()

        if shop_button.collidepoint(mouse):
            pygame.draw.rect(self.window.surface, (200, 0, 0), shop_button, 0, 10)
            text_shop = self.style_text_bold.render(f"shop", True, (0, 0, 0))
        else:
            pygame.draw.rect(self.window.surface, (255, 0, 0), shop_button, 0, 10)
            text_shop = self.style_text_bold.render(f"shop", True, (255, 255, 255))

        text_rect = text_shop.get_rect()
        text_rect.center = (cv.WINDOW_WIDTH / 2, cv.WINDOW_HEIGHT / 2)
        self.window.surface.blit(text_shop, text_rect)

        return shop_button

    def button_guide(self):
        guide_button = pygame.Rect(cv.WINDOW_WIDTH / 2 - 125, cv.WINDOW_HEIGHT / 2 + 50, 250, 50)
        mouse = pygame.mouse.get_pos()

        if guide_button.collidepoint(mouse):
            pygame.draw.rect(self.window.surface, (200, 0, 0), guide_button, 0, 10)
            text_guide = self.style_text_bold.render(f"guide", True, (0, 0, 0))
        else:
            pygame.draw.rect(self.window.surface, (255, 0, 0), guide_button, 0, 10)
            text_guide = self.style_text_bold.render(f"guide", True, (255, 255, 255))

        text_rect = text_guide.get_rect()
        text_rect.center = (cv.WINDOW_WIDTH / 2, cv.WINDOW_HEIGHT / 2 + 75)
        self.window.surface.blit(text_guide, text_rect)

        return guide_button

    def button_keyboard_shortcuts(self):
        key_shortcuts_button = pygame.Rect(cv.WINDOW_WIDTH / 2 - 125, cv.WINDOW_HEIGHT / 2 + 125, 250, 50)
        mouse = pygame.mouse.get_pos()

        if key_shortcuts_button.collidepoint(mouse):
            pygame.draw.rect(self.window.surface, (200, 0, 0), key_shortcuts_button, 0, 10)
            text_key_shortcuts = self.style_text_bold.render(f"keyboard shortcuts", True, (0, 0, 0))
        else:
            pygame.draw.rect(self.window.surface, (255, 0, 0), key_shortcuts_button, 0, 10)
            text_key_shortcuts = self.style_text_bold.render(f"keyboard shortcuts", True, (255, 255, 255))

        text_rect = text_key_shortcuts.get_rect()
        text_rect.center = (cv.WINDOW_WIDTH / 2, cv.WINDOW_HEIGHT / 2 + 150)
        self.window.surface.blit(text_key_shortcuts, text_rect)

        return key_shortcuts_button

    def button_shop_speed(self):
        shop_speed_button = pygame.Rect(cv.WINDOW_WIDTH / 2 - 150, cv.WINDOW_HEIGHT / 2 - 100, 300, 50)
        mouse = pygame.mouse.get_pos()

        if shop_speed_button.collidepoint(mouse):
            pygame.draw.rect(self.window.surface, (200, 0, 0), shop_speed_button, 0, 10)
            text_shop_speed = self.style_text_bold.render(f"buy speed {cv.PRICE_SPEED}", True, (0, 0, 0))
        else:
            pygame.draw.rect(self.window.surface, (255, 0, 0), shop_speed_button, 0, 10)
            text_shop_speed = self.style_text_bold.render(f"buy speed {cv.PRICE_SPEED}", True, (255, 255, 255))

        text_rect = text_shop_speed.get_rect()
        text_rect.center = (cv.WINDOW_WIDTH / 2, cv.WINDOW_HEIGHT / 2 - 75)
        self.window.surface.blit(text_shop_speed, text_rect)

        return shop_speed_button

    def button_shop_extra_shot(self):
        shop_extra_shot_button = pygame.Rect(cv.WINDOW_WIDTH / 2 - 150, cv.WINDOW_HEIGHT / 2 - 25, 300, 50)
        mouse = pygame.mouse.get_pos()

        if shop_extra_shot_button.collidepoint(mouse):
            pygame.draw.rect(self.window.surface, (200, 0, 0), shop_extra_shot_button, 0, 10)
            text_shop_speed = self.style_text_bold.render(f"buy extra shot {cv.PRICE_EXTRA_SHOT}", True, (0, 0, 0))
        else:
            pygame.draw.rect(self.window.surface, (255, 0, 0), shop_extra_shot_button, 0, 10)
            text_shop_speed = self.style_text_bold.render(f"buy extra shot {cv.PRICE_EXTRA_SHOT}", True, (255, 255, 255))

        text_rect = text_shop_speed.get_rect()
        text_rect.center = (cv.WINDOW_WIDTH / 2, cv.WINDOW_HEIGHT / 2)
        self.window.surface.blit(text_shop_speed, text_rect)

        return shop_extra_shot_button

    def button_shop_reduce_gap(self):
        shop_reduce_gap_button = pygame.Rect(cv.WINDOW_WIDTH / 2 - 150, cv.WINDOW_HEIGHT / 2 + 50, 300, 50)
        mouse = pygame.mouse.get_pos()

        if shop_reduce_gap_button.collidepoint(mouse):
            pygame.draw.rect(self.window.surface, (200, 0, 0), shop_reduce_gap_button, 0, 10)
            text_shop_reduce_gap = self.style_text_bold.render(f"buy reduce bullet gap {cv.PRICE_REDUCE_BULLET_GAP}", True, (0, 0, 0))
        else:
            pygame.draw.rect(self.window.surface, (255, 0, 0), shop_reduce_gap_button, 0, 10)
            text_shop_reduce_gap = self.style_text_bold.render(f"buy reduce bullet gap {cv.PRICE_REDUCE_BULLET_GAP}", True, (255, 255, 255))

        text_rect = text_shop_reduce_gap.get_rect()
        text_rect.center = (cv.WINDOW_WIDTH / 2, cv.WINDOW_HEIGHT / 2 + 75)
        self.window.surface.blit(text_shop_reduce_gap, text_rect)

        return shop_reduce_gap_button

    def button_shop_extra_coin(self):
        shop_extra_coin_button = pygame.Rect(cv.WINDOW_WIDTH / 2 - 150, cv.WINDOW_HEIGHT / 2 + 125, 300, 50)
        mouse = pygame.mouse.get_pos()

        if shop_extra_coin_button.collidepoint(mouse):
            pygame.draw.rect(self.window.surface, (200, 0, 0), shop_extra_coin_button, 0, 10)
            text_shop_extra_coin = self.style_text_bold.render(f"buy extra coin {cv.PRICE_EXTRA_COIN}", True, (0, 0, 0))
        else:
            pygame.draw.rect(self.window.surface, (255, 0, 0), shop_extra_coin_button, 0, 10)
            text_shop_extra_coin = self.style_text_bold.render(f"buy extra coin {cv.PRICE_EXTRA_COIN}", True, (255, 255, 255))

        text_rect = text_shop_extra_coin.get_rect()
        text_rect.center = (cv.WINDOW_WIDTH / 2, cv.WINDOW_HEIGHT / 2 + 150)
        self.window.surface.blit(text_shop_extra_coin, text_rect)

        return shop_extra_coin_button

    def button_home(self):
        home_button = pygame.Rect(cv.WINDOW_WIDTH / 2 - 100, cv.WINDOW_HEIGHT - 75, 200, 50)
        mouse = pygame.mouse.get_pos()

        if home_button.collidepoint(mouse):
            pygame.draw.rect(self.window.surface, (200, 0, 0), home_button, 0, 10)
            text_home = self.style_text_bold.render(f"home", True, (0, 0, 0))
        else:
            pygame.draw.rect(self.window.surface, (255, 0, 0), home_button, 0, 10)
            text_home = self.style_text_bold.render(f"home", True, (255, 255, 255))

        text_rect = text_home.get_rect()
        text_rect.center = (cv.WINDOW_WIDTH / 2, cv.WINDOW_HEIGHT - 50)
        self.window.surface.blit(text_home, text_rect)

        return home_button

    def button_exit_home(self):
        exit_button = pygame.Rect(cv.WINDOW_WIDTH / 2 - 100, cv.WINDOW_HEIGHT - 75, 200, 50)
        mouse = pygame.mouse.get_pos()

        if exit_button.collidepoint(mouse):
            pygame.draw.rect(self.window.surface, (200, 0, 0), exit_button, 0, 10)
            text_exit = self.style_text_bold.render(f"exit game", True, (0, 0, 0))
        else:
            pygame.draw.rect(self.window.surface, (255, 0, 0), exit_button, 0, 10)
            text_exit = self.style_text_bold.render(f"exit game", True, (255, 255, 255))

        text_rect = text_exit.get_rect()
        text_rect.center = (cv.WINDOW_WIDTH / 2, cv.WINDOW_HEIGHT - 50)
        self.window.surface.blit(text_exit, text_rect)

        return exit_button

    def button_pause_continue(self):
        continue_pause_button = pygame.Rect(cv.WINDOW_WIDTH / 2 - 100, cv.WINDOW_HEIGHT / 2 - 100, 200, 50)
        mouse = pygame.mouse.get_pos()

        if continue_pause_button.collidepoint(mouse):
            pygame.draw.rect(self.window.surface, (200, 0, 0), continue_pause_button, 0, 10)
            text_pause_continue = self.style_text_bold.render(f"continue", True, (0, 0, 0))
        else:
            pygame.draw.rect(self.window.surface, (255, 0, 0), continue_pause_button, 0, 10)
            text_pause_continue = self.style_text_bold.render(f"continue", True, (255, 255, 255))

        text_rect = text_pause_continue.get_rect()
        text_rect.center = (cv.WINDOW_WIDTH / 2, cv.WINDOW_HEIGHT / 2 - 75)
        self.window.surface.blit(text_pause_continue, text_rect)

        return continue_pause_button

    def button_pause_home(self):
        home_pause_button = pygame.Rect(cv.WINDOW_WIDTH / 2 - 100, cv.WINDOW_HEIGHT / 2 - 25, 200, 50)
        mouse = pygame.mouse.get_pos()

        if home_pause_button.collidepoint(mouse):
            pygame.draw.rect(self.window.surface, (200, 0, 0), home_pause_button, 0, 10)
            text_pause_home = self.style_text_bold.render(f"home", True, (0, 0, 0))
        else:
            pygame.draw.rect(self.window.surface, (255, 0, 0), home_pause_button, 0, 10)
            text_pause_home = self.style_text_bold.render(f"home", True, (255, 255, 255))

        text_rect = text_pause_home.get_rect()
        text_rect.center = (cv.WINDOW_WIDTH / 2, cv.WINDOW_HEIGHT / 2)
        self.window.surface.blit(text_pause_home, text_rect)

        return home_pause_button

    def button_pause_exit_game(self):
        exit_game_pause_button = pygame.Rect(cv.WINDOW_WIDTH / 2 - 100, cv.WINDOW_HEIGHT / 2 + 50, 200, 50)
        mouse = pygame.mouse.get_pos()

        if exit_game_pause_button.collidepoint(mouse):
            pygame.draw.rect(self.window.surface, (200, 0, 0), exit_game_pause_button, 0, 10)
            text_pause_exit_game = self.style_text_bold.render(f"exit game", True, (0, 0, 0))
        else:
            pygame.draw.rect(self.window.surface, (255, 0, 0), exit_game_pause_button, 0, 10)
            text_pause_exit_game = self.style_text_bold.render(f"exit game", True, (255, 255, 255))

        text_rect = text_pause_exit_game.get_rect()
        text_rect.center = (cv.WINDOW_WIDTH / 2, cv.WINDOW_HEIGHT / 2 + 75)
        self.window.surface.blit(text_pause_exit_game, text_rect)

        return exit_game_pause_button