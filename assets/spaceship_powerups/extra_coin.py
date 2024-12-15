# ./assets/spaceship_powerups/extra_shot.py
from assets.spaceship_powerups.powerups import Powerups
from saved_info.extra_coin_value.info_extra_coin_value import InfoExtraCoin


class ExtraCoin(Powerups):
    def __init__(self, window, spaceship, enemy, bullets, powerup_name, size, speed, colour):
        super().__init__(window, spaceship, enemy, bullets, powerup_name, size, speed, colour)
        self.amount = InfoExtraCoin().get_extra_coin()

    def powerup_activated(self):
        self.spaceship.coins += self.amount