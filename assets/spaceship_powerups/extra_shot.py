# ./assets/spaceship_powerups/extra_shot.py
from assets.spaceship_powerups.powerups import Powerups


class ExtraShot(Powerups):
    def __init__(self, window, spaceship, enemy, bullets, powerup_name, size, speed, colour):
        super().__init__(window, spaceship, enemy, bullets, powerup_name, size, speed, colour)

    def powerup_activated(self):
        self.bullets.maximum = min(self.bullets.maximum + 1, 20)