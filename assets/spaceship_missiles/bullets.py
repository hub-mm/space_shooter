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
        self.size = size
        self.speed = speed

        self.gap_next = gap_next
        self.gap = gap

        self.delay_next = delay_next
        self.delay = delay

        self.maximum = maximum
        self.missiles_count = self.maximum