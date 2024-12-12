# ./display/game_window.py
import pygame

from variables import constants as cv


class GameWindow(object):
    def __init__(self):
        # Initialise pygame and clock
        pygame.init()
        self.clock = pygame.time.Clock()

        # Create window and window name
        self.surface = pygame.display.set_mode((cv.WINDOW_WIDTH, cv.WINDOW_HEIGHT))
        pygame.display.set_caption(cv.WINDOW_TEXT)

        # Create window icon
        icon_img = pygame.image.load(cv.ICON_IMG_PATH)
        pygame.display.set_icon(icon_img)