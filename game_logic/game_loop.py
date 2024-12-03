# ./game_logic/game_loop.py
from variables import constants as cv
from display.game_window import GameWindow
from assets.spaceship import SpaceShip
from assets.spaceship_missiles import Missiles

import sys
import pygame

class GameLoop(object):
    def __init__(self):
        window = GameWindow()
        spaceship = SpaceShip()
        missiles = Missiles()

        run = True
        while run:
            # Background
            window.surface.fill(cv.COLOUR_BACKGROUND)

            # Spaceship
            window.surface.blit(spaceship.space_ship_img, (cv.X, cv.Y))

            spaceship.move_logic()

            # Missile spike
            missiles.generate_spike()
            missiles.move_spike()


            for event in pygame.event.get():
                keys = pygame.key.get_pressed()

                if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                    run = False
                    sys.exit()

            pygame.display.update()
            window.clock.tick(60)
