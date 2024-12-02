# ./display/game_window.py
from variables import constants as cv

import pygame

class GameWindow(object):

    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()

        self.surface = pygame.display.set_mode((cv.WINDOW_WIDTH, cv.WINDOW_HEIGHT))
        pygame.display.set_caption(cv.WINDOW_TEXT)

        icon_img = pygame.image.load(cv.ICON_IMG_PATH)
        pygame.display.set_icon(icon_img)

        self.space_ship_img = pygame.image.load(cv.SPACESHIP_IMG_PATH)
        self.space_ship_img = pygame.transform.scale(self.space_ship_img, cv.START_SIZE)