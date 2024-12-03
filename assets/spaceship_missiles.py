# ./assets/spaceship_missiles.py
from variables import constants as cv
from assets.spaceship import SpaceShip
from display.game_window import GameWindow

import pygame

class Missiles(SpaceShip):
    def __init__(self):
        self.window = GameWindow()

        super().__init__()
        self.spike_size = (10, 10)
        self.speed_spike = 20
        self.y = cv.Y

    def generate_spike(self):
        keys = pygame.key.get_pressed()

        spike = pygame.Rect(
            cv.X + (cv.START_SIZE[0] / 2) - 5,
            self.y + (cv.START_SIZE[1] / 2) + 10,
            self.spike_size[0],
            self.spike_size[1],
        )

        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            self.y = cv.Y
            self.window.spikes.append(spike)

    def move_spike(self):
        for spike in self.window.spikes:
            spike[1] -= self.speed_spike

            pygame.draw.rect(
                self.window.surface,
                cv.COLOUR_SPIKE,
                spike,
                3,
                2
            )

            if spike[1] <= 0:
                self.window.spikes.remove(spike)