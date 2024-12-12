# ./assets/spaceship_powerups/less_delay.py
from assets.spaceship_powerups.powerups import Powerups


class LessDelay(Powerups):
    def __init__(self, window, spaceship, enemy, bullets, powerup_name, size, speed, colour):
        super().__init__(window, spaceship, enemy, bullets, powerup_name, size, speed, colour)

    def powerup_activated(self):
        self.bullets.delay = max(200, self.bullets.delay - 100)