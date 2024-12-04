# ./assets/enemy.py
from variables import constants as cv

import pygame
import random

class Enemy(object):
    def __init__(self, window, bullets):
        self.window = window
        self.bullets = bullets

        self.speed = 1
        self.size = (50, 25)

        self.minimum = 1
        self.maximum = 10
        self.enemy_count = 0
        self.killed = 0
        self.round = 0
        self.wave = 1
        self.number_random = random.randint(self.minimum, self.maximum)

        self.enemy_img = pygame.image.load(cv.ALIEN_IMG_PATH)
        self.enemy_img = pygame.transform.scale(self.enemy_img, self.size)

    def generate_enemy(self):
        random_width = random.randint(20, cv.WINDOW_WIDTH - (self.size[0] + 20))
        random_height = random.randint(-200, -10)

        enemy = pygame.Rect(
            random_width,
            random_height,
            self.size[0],
            self.size[1]
        )

        if self.enemy_count != self.number_random:
            self.enemy_count += 1
            self.window.enemies.append(enemy)

    def move_enemy(self):
        for i, enemy in enumerate(self.window.enemies):
            enemy[1] += self.speed

            x, y = enemy.x, enemy.y
            self.window.surface.blit(self.enemy_img, (x, y))

            rect_one = self.window.enemies[i]
            self.remove_enemy(i, rect_one)

    def remove_enemy(self, i, rect_one):
        for j in range(i + 1, len(self.window.enemies)):
            if rect_one.colliderect(self.window.enemies[j]):
                self.window.enemies.remove(self.window.enemies[j])
                self.enemy_count -= 1


    def kill_enemy(self):
        for enemy in self.window.enemies:
            for bullet in self.bullets.missiles:
                if bullet.colliderect(enemy):
                    self.window.enemies.remove(enemy)
                    self.bullets.missiles.remove(bullet)
                    self.killed += 1

    def new_wave(self):
        if self.killed == self.enemy_count or all(enemy[1] > cv.WINDOW_HEIGHT + 100 for enemy in self.window.enemies):
            self.window.enemies.clear()
            self.enemy_count = 0
            self.killed = 0
            self.round += 1
            self.new_number()

    def new_number(self):
        if self.round % 5 == 0:
            self.wave += 1
            self.minimum += 5
            self.maximum += 10
            self.number_random = random.randint(self.minimum, self.maximum)
        elif self.round % 5 == 4:
            self.number_random = self.maximum
        else:
            self.number_random = random.randint(self.minimum, self.maximum)

        return self.number_random