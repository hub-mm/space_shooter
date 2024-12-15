# ./display/game_window.py
import pygame

from variables import constants as cv


class GameWindow(object):
    def __init__(self):
        # pygame.init()
        self.clock = pygame.time.Clock()

        self.surface = pygame.display.set_mode((cv.WINDOW_WIDTH, cv.WINDOW_HEIGHT))
        self.surface_transparent = pygame.Surface((cv.WINDOW_WIDTH, cv.WINDOW_HEIGHT), pygame.SRCALPHA)

        icon_img = pygame.image.load(cv.ICON_IMG_PATH)
        pygame.display.set_icon(icon_img)

    def start_menu(self):
        self.surface.fill(cv.COLOUR_BACKGROUND)
        pygame.display.set_caption(cv.WINDOW_START_TEXT)

    def game(self):
        self.surface.fill(cv.COLOUR_BACKGROUND)
        pygame.display.set_caption(cv.WINDOW_TEXT)

    def shop(self):
        self.surface.fill(cv.COLOUR_BACKGROUND)
        pygame.display.set_caption(cv.WINDOW_SHOP_TEXT)

    def guide(self):
        self.surface.fill(cv.COLOUR_BACKGROUND)
        pygame.display.set_caption(cv.WINDOW_GUIDE_TEXT)

    def pause(self):
        self.surface_transparent.fill((255, 255, 255, 128))
        pygame.display.set_caption(cv.WINDOW_GAME_PAUSE)