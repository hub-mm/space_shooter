# ./game_logic/game_loop.py
import sys
import pygame

from saved_info.spaceship_build.info_spaceship import InfoSpaceship
from variables import constants as cv
from display.game_window import GameWindow
from display.text_display import TextDisplay
from assets.spaceship_missiles.bullets import Bullets
from assets.enemy import Enemy
from assets.spaceship import SpaceShip
from assets.spaceship_powerups.powerups import Powerups
from game_logic.collision_checks import CollisionChecks
from saved_info.highscore.info_highscore import InfoHighscore
from saved_info.coins.info_coins import InfoCoins
from saved_info.bullet_build.info_bullets import InfoBullets


class GameLoop:
    def __init__(self):
        self.window = GameWindow()
        self.run = True

        self._reset_game_full_initial()

        self.game_state = 'start_menu'

        while self.run:
            self._handle_events()

            if self.game_state == 'start_menu':
                self.window.start_menu()

                score = self._update_highscore()
                coins = self._update_coins()
                self._update_start_menu_display(score, coins)

            elif self.game_state == 'shop':
                self.window.shop()
                coins = self._update_coins()
                self._update_shop_display(coins)

            elif self.game_state == 'guide':
                self.window.guide()
                coins = self._update_coins()
                self._update_guide_display(coins)

            elif self.game_state == 'game':
                self.window.game()

                game_state = self.game_state
                self._update_game_display(game_state)
                self._update_spaceship()
                self._update_bullets()
                self._update_enemy()
                self._update_powerups()
                self._update_collisions()

                self.enemy.new_wave()

                self._check_game_over()

            pygame.display.update()
            self.window.clock.tick(60)

    def _reset_game_full_initial(self):
        self.spaceship_build = self._create_spaceship_build()
        self.bullets_build = self._create_bullets_build()

        self.bullets = self._create_bullets()
        self.enemy = self._create_enemy()
        self.spaceship = self._create_spaceship()
        self.powerup_class = self._create_powerups()
        self.collision_checks = self._create_collision_checks()
        self.text_display = self._create_text_display()
        self.highscore_info = self._create_highscore_info()
        self.coin_info = self._create_coins_info()

    def _handle_events(self):
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                self.close_game()

            if self.game_state == 'start_menu':
                if keys[pygame.K_RETURN]:
                    self._reset_game()

            if self.game_state in ['start_menu', 'shop', 'guide']:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse = pygame.mouse.get_pos()
                    home_button_rect = self.text_display.button_home()

                    if self.game_state == 'start_menu':
                        start_button_rect = self.text_display.button_start_game()
                        shop_button_rect = self.text_display.button_shop()
                        guide_button_rect = self.text_display.button_guide()
                        exit_button_rect = self.text_display.button_exit_home()

                        if start_button_rect.collidepoint(mouse):
                            self._reset_game()
                        elif shop_button_rect.collidepoint(mouse):
                            self.game_state = 'shop'
                        elif guide_button_rect.collidepoint(mouse):
                            self.game_state = 'guide'
                        elif exit_button_rect.collidepoint(mouse):
                            self.close_game()
                    elif self.game_state == 'shop':
                        shop_speed_button_rect = self.text_display.button_shop_speed()
                        shop_extra_shot_button_rect = self.text_display.button_shop_extra_shot()

                        if shop_speed_button_rect.collidepoint(mouse):
                            if self.coin_info.total_coins >= cv.PRICE_SPEED:
                                self.coin_info.set_total_coins(self.coin_info.total_coins - cv.PRICE_SPEED)
                                self.spaceship_build.buy_speed()
                                speed, size = self.spaceship_build.get_spaceship_build()
                                self.spaceship.speed = speed
                            else:
                                print('Not enough coins to buy speed')
                        elif shop_extra_shot_button_rect.collidepoint(mouse):
                            if self.coin_info.total_coins >= cv.PRICE_EXTRA_SHOT:
                                self.coin_info.set_total_coins(self.coin_info.total_coins - cv.PRICE_EXTRA_SHOT)
                                self.bullets_build.buy_extra_bullet()
                                max_bullet = self.bullets_build.get_bullet()
                                self.bullets.maximum = max_bullet
                            else:
                                print('Not enough coins to buy extra bullet')
                        elif home_button_rect.collidepoint(mouse):
                            self.game_state = 'start_menu'
                    elif self.game_state == 'guide':
                        if home_button_rect.collidepoint(mouse):
                            self.game_state = 'start_menu'

            if self.game_state == 'game':
                if keys[pygame.K_p]:
                    self.game_state = 'pause'
                    self.window.pause()
                    self._pause_game()


    @staticmethod
    def _create_spaceship_build():
        return InfoSpaceship()

    @staticmethod
    def _create_bullets_build():
        return InfoBullets()

    def _create_spaceship(self):
        speed, size = self.spaceship_build.get_spaceship_build()
        return SpaceShip(self.window, self.enemy, speed, size)

    def _create_bullets(self):
        size = (5, 15)
        speed = 10
        gap_next = 0
        gap = 250
        delay_next = 0
        delay = 2000
        maximum = self.bullets_build.get_bullet()
        return Bullets(self.window, size, speed, gap_next, gap, delay_next, delay, maximum)

    def _create_enemy(self):
        return Enemy(self.window, self.bullets)

    def _create_text_display(self):
        return TextDisplay(self.window, self.enemy, self.spaceship)

    def _create_powerups(self):
        return Powerups(
            self.window,
            self.spaceship,
            self.enemy,
            self.bullets,
            'name',
            (0, 0),
            0,
            (0, 0)
        )

    def _create_collision_checks(self):
        return CollisionChecks(self.window, self.bullets, self.enemy, self.spaceship, self.powerup_class)

    def _create_highscore_info(self):
        return InfoHighscore(self.enemy, self.spaceship)

    def _create_coins_info(self):
        return InfoCoins(self.spaceship)

    def _update_start_menu_display(self, score, coins):
        self.text_display.update_start_menu(score, coins)

    def _update_shop_display(self, coins):
        self.text_display.update_shop(coins)

    def _update_guide_display(self, coins):
        self.text_display.update_guide(coins)

    def _update_game_display(self, game_state):
        self.text_display.update_game(game_state)

    def _update_spaceship(self):
        self.window.surface.blit(self.spaceship.spaceship_img, (cv.X, cv.Y))
        self.spaceship.update()

    def _update_bullets(self):
        self.bullets.generate_missiles()

    def _update_enemy(self):
        self.enemy.update()

    def _update_powerups(self):
        self.powerup_class.move_all_powerups()
        self.powerup_class.check_collisions()

    def _update_collisions(self):
        self.collision_checks.update()

    def _update_highscore(self):
        return self.highscore_info.update_highscore()

    def _update_coins(self):
        return self.coin_info.update_coins()

    def _check_game_over(self):
        if self.spaceship.lives <= 0:
            self._update_highscore()
            self.coin_info.set_total_coins(self.coin_info.total_coins + self.spaceship.coins)
            self.game_state = 'start_menu'

    def _pause_game(self):
        while self.game_state == 'pause':
            self._update_game_display(self.game_state)

            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                    self.close_game()

                if keys[pygame.K_p]:
                    self.game_state = 'game'

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse = pygame.mouse.get_pos()
                    pause_home_button_rect = self.text_display.button_pause_home()
                    pause_continue_button_rect = self.text_display.button_pause_continue()
                    pause_exit_button_rect = self.text_display.button_pause_exit_game()
                    if pause_home_button_rect.collidepoint(mouse):
                        self.game_state = 'start_menu'
                    elif pause_continue_button_rect.collidepoint(mouse):
                        self.game_state = 'game'
                    elif pause_exit_button_rect.collidepoint(mouse):
                        self.close_game()

            pygame.display.update()
            self.window.clock.tick(60)


    def _reset_game(self):
        self.spaceship_build = self._create_spaceship_build()
        self.bullets = self._create_bullets()
        self.enemy = self._create_enemy()
        self.spaceship = self._create_spaceship()
        self.powerup_class = self._create_powerups()
        self.collision_checks = self._create_collision_checks()
        self.text_display = self._create_text_display()
        self.highscore_info = self._create_highscore_info()
        self.coin_info = self._create_coins_info()

        cv.X = cv.START_X
        cv.Y = cv.START_Y

        self.enemy.enemy_group.empty()
        self.bullets.bullet_group.empty()
        self.powerup_class.powerups.clear()
        self.enemy.shot.clear()

        self.game_state = 'game'

    def close_game(self):
        self.run = False
        sys.exit()