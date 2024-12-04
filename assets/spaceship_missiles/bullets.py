# ./assets/spaceship_missiles/bullets.py
from assets.spaceship_missiles.missiles import Missiles

class Bullets(Missiles):
    def __init__(
            self,
            window,
            size = 0,
            speed = 0,
            gap_next = 0,
            gap = 0,
            delay_next = 0,
            delay = 0,
            maximum = 0,
    ):
        super().__init__(
            window,
            size,
            speed,
            gap_next,
            gap,
            delay_next,
            delay,
            maximum,
        )
        self.size = (5, 10)
        self.speed = 10

        self.gap_next = 0
        self.gap = 30

        self.delay_next = 0
        self.delay = 500

        self.maximum = 1
        self.missiles_count = self.maximum