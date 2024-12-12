# ./assets/spaceship_powerups/random_powerup.py
import random

from assets.spaceship_powerups.extra_shot import ExtraShot
from assets.spaceship_powerups.less_delay import LessDelay
from assets.spaceship_powerups.move_faster import MoveFaster
from assets.spaceship_powerups.reduce_gap import ReduceGap
from assets.spaceship_powerups.extra_life import ExtraLife
from assets.spaceship_powerups.extra_coin import ExtraCoin

class RandomPowerup(object):
    def __init__(self, window, bullets, enemy, spaceship, powerups):
        self.window = window
        self.bullets = bullets
        self.enemy = enemy
        self.spaceship = spaceship
        self.powerups = powerups

    def update(self):
        return self._create_random_powerup()

    def _create_random_powerup(self):
        speed = random.randint(1, 10)

        extra_shot = ExtraShot(
            self.window,
            self.spaceship,
            self.enemy,
            self.bullets,
            'extra_shot',
            (30, 30),
            speed,
            (0, 0, 255)
        )
        less_delay = LessDelay(
            self.window,
            self.spaceship,
            self.enemy,
            self.bullets,
            'less_delay',
            (30, 30),
            speed,
            (255, 0, 0)
        )
        move_faster = MoveFaster(
            self.window,
            self.spaceship,
            self.enemy,
            self.bullets,
            'move_faster',
            (30, 30),
            speed,
            (0, 255, 0)
        )
        reduce_gap = ReduceGap(
            self.window,
            self.spaceship,
            self.enemy,
            self.bullets,
            'reduce_gap',
            (30, 30),
            speed,
            (255, 0, 255)
        )
        extra_life = ExtraLife(
            self.window,
            self.spaceship,
            self.enemy,
            self.bullets,
            'extra_life',
            (30, 30),
            speed,
            ()
        )
        extra_coin = ExtraCoin(
            self.window,
            self.spaceship,
            self.enemy,
            self.bullets,
            'extra_coin',
            (30, 30),
            speed,
            (255, 215, 0)
        )

        powerup_list = self._powerup_logic(extra_shot, less_delay, move_faster, reduce_gap, extra_life, extra_coin)

        return random.choice(powerup_list)

    def _powerup_logic(self, extra_shot, less_delay, move_faster, reduce_gap, extra_life, extra_coin):
        powerup_list = [extra_shot, less_delay, move_faster, reduce_gap, extra_life, extra_coin]

        if self.bullets.maximum == 20:
            powerup_list.remove(extra_shot)

        if self.bullets.delay == 200:
            powerup_list.remove(less_delay)

        if self.spaceship.speed == 10:
            powerup_list.remove(move_faster)

        if self.bullets.gap == 50:
            powerup_list.remove(reduce_gap)

        if self.spaceship.lives == 10 or extra_life in self.powerups.powerups:
            powerup_list.remove(extra_life)

        return powerup_list