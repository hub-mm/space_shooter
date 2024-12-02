# ./game_logic/game_loop.py
from display.game_window import GameWindow
from assets.spaceship import SpaceShip
from variables import constants as cv

import sys
import pygame

class GameLoop(object):
    def __init__(self):
        window = GameWindow()
        spaceship = SpaceShip()

        run = True
        while run:
            window.surface.fill(cv.COLOUR_BACKGROUND)
            window.surface.blit(window.space_ship_img, (cv.X, cv.Y))
            spaceship.move_logic()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    run = False
                    sys.exit()

            pygame.display.update()
            window.clock.tick(60)

GameLoop()