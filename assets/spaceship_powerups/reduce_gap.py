# ./assets/spaceship_powerups/reduce_gap.py
from assets.spaceship_powerups.powerups import Powerups


class ReduceGap(Powerups):
    def __init__(self, window, spaceship, enemy, bullets, powerup_name, size, speed, colour):
        super().__init__(window, spaceship, enemy, bullets, powerup_name, size, speed, colour)

    def powerup_activated(self):
        self.bullets.gap = max(50, self.bullets.gap - 5)