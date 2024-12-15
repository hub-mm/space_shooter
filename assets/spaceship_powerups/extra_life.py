# ./assets/spaceship_powerups/extra_life.py
from assets.spaceship_powerups.powerups import Powerups


class ExtraLife(Powerups):
    def __init__(self, window, spaceship, enemy, bullets, powerup_name, size, speed, colour):
        super().__init__(window, spaceship, enemy, bullets, powerup_name, size, speed, colour)

    def powerup_activated(self):
        self.spaceship.lives = min(self.spaceship.lives + 1, 10)