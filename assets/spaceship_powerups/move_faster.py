# ./assets/spaceship_powerups/move_faster.py
from assets.spaceship_powerups.powerups import Powerups


class MoveFaster(Powerups):
    def __init__(self, window, spaceship, enemy, bullets, powerup_name, size, speed, colour):
        super().__init__(window, spaceship, enemy, bullets, powerup_name, size, speed, colour)

    def powerup_activated(self):
        self.spaceship.default_speed = min(self.spaceship.speed + 1, 10)