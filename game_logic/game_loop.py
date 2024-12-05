# ./game_logic/game_loop.py
from variables import constants as cv
from display.game_window import GameWindow
from assets.spaceship_missiles.bullets import Bullets
from assets.enemy import Enemy
from assets.spaceship import SpaceShip
from display.text_display import TextDisplay

import sys
import pygame

class GameLoop(object):
    def __init__(self):
        self.window = GameWindow()
        bullets = self.bullets()
        self.enemy = Enemy(self.window, bullets)
        spaceship = self.spaceship()
        text_display = TextDisplay(self.window, self.enemy, spaceship)

        self.run = True
        while self.run:
            # Background
            self.window.surface.fill(cv.COLOUR_BACKGROUND)

            # Text
            text_display.display_title()
            text_display.display_lives()
            text_display.display_wave()

            # Spaceship
            self.window.surface.blit(spaceship.spaceship_img, (cv.X, cv.Y))
            spaceship.move_logic()
            spaceship.loose_life()

            # Missile bullets
            bullets.generate_missiles()
            bullets.move_missiles()

            # Enemy
            self.enemy.generate_enemy()
            self.enemy.move_enemy()
            self.enemy.kill_enemy()
            self.enemy.new_wave()

            for event in pygame.event.get():
                keys = pygame.key.get_pressed()

                if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                    self.close_game()

            if spaceship.lives <= 0:
                self.close_game()

            pygame.display.update()
            self.window.clock.tick(60)

    def spaceship(self):
        speed = 5
        size = (75, 75)

        spaceship = SpaceShip(self.window, self.enemy, speed, size)

        return spaceship


    def bullets(self):
        size = (5, 15)
        speed = 10

        gap_next = 0
        gap = 30

        delay_next = 0
        delay = 500

        maximum = 1

        bullets = Bullets(self.window, size, speed, gap_next, gap, delay_next, delay, maximum)

        return bullets

    def close_game(self):
        self.run = False
        sys.exit()