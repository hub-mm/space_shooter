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
        window = GameWindow()
        bullets = Bullets(window)
        enemy = Enemy(window, bullets)
        spaceship = SpaceShip(window, enemy)
        text_display = TextDisplay(window, enemy, spaceship)

        self.run = True
        while self.run:
            # Background
            window.surface.fill(cv.COLOUR_BACKGROUND)

            # Text
            text_display.display_title()
            text_display.display_lives()
            text_display.display_wave()

            # Spaceship
            window.surface.blit(spaceship.spaceship_img, (cv.X, cv.Y))
            spaceship.move_logic()
            spaceship.loose_life()

            # Missile bullets
            bullets.generate_missiles()
            bullets.move_missiles()

            # Enemy
            enemy.generate_enemy()
            enemy.move_enemy()
            enemy.kill_enemy()
            enemy.new_wave()

            for event in pygame.event.get():
                keys = pygame.key.get_pressed()

                if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                    self.close_game()

            if spaceship.lives <= 0:
                self.close_game()

            pygame.display.update()
            window.clock.tick(60)

    def close_game(self):
        self.run = False
        sys.exit()