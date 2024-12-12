# ./game_logic/game_loop.py
import sys
import pygame

from variables import constants as cv
from display.game_window import GameWindow
from display.text_display import TextDisplay
from assets.spaceship_missiles.bullets import Bullets
from assets.enemy import Enemy
from assets.spaceship import SpaceShip
from assets.spaceship_powerups.powerups import Powerups
from game_logic.collision_checks import CollisionChecks
from saved_info.save_info import SaveInfo


class GameLoop:
    def __init__(self):
        self.window = GameWindow()
        self.run = True

        self.bullets = self._create_bullets()
        self.enemy = self._create_enemy()
        self.spaceship = self._create_spaceship()
        self.powerup_class = self._create_powerups()
        self.collision_checks = self._create_collision_checks()
        self.text_display = self._create_text_display()
        self.save_info = self._create_saved_info()

        self.game_state = 'start_menu'

        while self.run:
            self._handle_events()

            if self.game_state == 'start_menu':
                self.window.start_menu()
                score = self._update_highscore()
                self._update_start_menu_display(score)

            if self.game_state == 'game':
                self.window.game()

                self._update_game_display()
                self._update_spaceship()
                self._update_bullets()
                self._update_enemy()
                self._update_powerups()
                self._update_collisions()

                self.enemy.new_wave()

                self._check_game_over()

            pygame.display.update()
            self.window.clock.tick(60)

    def _create_spaceship(self):
        speed = 3
        size = (75, 75)
        return SpaceShip(self.window, self.enemy, speed, size)

    def _create_bullets(self):
        size = (5, 15)
        speed = 10
        gap_next = 0
        gap = 250
        delay_next = 0
        delay = 2000
        maximum = 1

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

    def _create_saved_info(self):
        return SaveInfo(self.enemy, self.spaceship)

    def _handle_events(self):
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                self.close_game()

            if keys[pygame.K_RETURN]:
                self._reset_game()
                self.game_state = 'game'

    def _update_start_menu_display(self, score):
        self.text_display.update_start_menu(score)

    def _update_game_display(self):
        self.text_display.update_game()

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
        return self.save_info.update_highscore()

    def _check_game_over(self):
        if self.spaceship.lives <= 0:
            self._update_highscore()
            self.game_state = 'start_menu'

    def _reset_game(self):
        self.bullets = self._create_bullets()
        self.enemy = self._create_enemy()
        self.spaceship = self._create_spaceship()
        self.powerup_class = self._create_powerups()
        self.collision_checks = self._create_collision_checks()
        self.text_display = self._create_text_display()
        self.save_info = self._create_saved_info()

        cv.X = cv.START_X
        cv.Y = cv.START_Y

    def close_game(self):
        self.run = False
        sys.exit()