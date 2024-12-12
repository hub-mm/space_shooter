# ./assets/spaceship_powerups/extra_shot.py
from assets.spaceship_powerups.powerups import Powerups


class ExtraCoin(Powerups):
    def __init__(self, window, spaceship, enemy, bullets, powerup_name, size, speed, colour):
        super().__init__(window, spaceship, enemy, bullets, powerup_name, size, speed, colour)

    def powerup_activated(self):
        self.spaceship.coins += 1