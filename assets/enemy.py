# ./assets/enemy.py
import pygame
import random

from variables import constants as cv
from assets.enemy_sprite import EnemySprite


class Enemy(object):
    def __init__(self, window, bullets):
        self.window = window
        self.bullets = bullets
        self.speed = 1
        self.size = (60, 25)
        self.minimum = 1
        self.maximum = 5
        self.enemy_count = 0
        self.killed = 0
        self.total_killed = 0
        self.wave = 0
        self.level = 1
        self.number_random = random.randint(self.minimum, self.maximum)
        self.kill_x = 0
        self.kill_y = 0
        self.kill = False
        self.spawn_max_dis = -200

        self.shot_count = 0
        self.shot = []

        self.enemy_img = pygame.image.load(cv.ALIEN_IMG_PATH)
        self.enemy_img = pygame.transform.scale(self.enemy_img, self.size)

        self.enemy_group = pygame.sprite.Group()

    def update(self):
        self._generate_enemy()
        self.enemy_group.update()
        self.enemy_group.draw(self.window.surface)

        self.shot_count += 1
        if self.shot_count > random.randint(10, 12000):
            self._generate_shot()
            self.shot_count = 0

        self._move_shot()

    def _generate_enemy(self):
        if self.enemy_count < self.number_random:
            random_width = random.randint(20, cv.WINDOW_WIDTH - (self.size[0] + 20))
            random_height = random.randint(self.spawn_max_dis, -10)

            new_enemy = EnemySprite(random_width, random_height, self.enemy_img, self.speed)
            self.enemy_group.add(new_enemy)
            self.enemy_count += 1

    def new_wave(self):
        if len(self.enemy_group) == 0:
            self._set_new_number()
            self.enemy_count = 0
            self.killed = 0
            self.wave += 1

    def _set_new_number(self):
        if len(self.enemy_group) == 0:
            self.number_random = random.randint(self.minimum, self.maximum)

        if self.wave % 5 == 4:
            self.number_random = self.maximum

        if self.wave % 5 == 0 and self.wave != 0:
            self.number_random = random.randint(self.minimum, self.maximum)
            self.level += 1
            self.minimum += 2
            self.maximum += 10
            self.spawn_max_dis -= 100

        if self.wave % 20 == 0 and self.wave != 0:
            self.speed = min(self.speed + 1, 10)

        return self.number_random

    def _generate_shot(self):
        enemies_list = self.enemy_group.sprites()

        if not enemies_list:
            return

        enemy_sprite = random.choice(enemies_list)
        shot_rect = pygame.Rect(
            enemy_sprite.rect.x + (self.size[0] / 2) - (5 / 2),
            enemy_sprite.rect.y + (self.size[0] / 2),
            5,
            20
        )

        if 0 < enemy_sprite.rect.y < (cv.WINDOW_HEIGHT - 200):
            self.shot.append(shot_rect)

    def _move_shot(self):
        for shot_rect in self.shot[:]:
            shot_rect.y += (self.speed + 1)

            pygame.draw.rect(self.window.surface, (255, 0, 0), shot_rect)

            if shot_rect.y > cv.WINDOW_HEIGHT:
                self.shot.remove(shot_rect)