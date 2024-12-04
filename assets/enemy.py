# ./assets/enemy.py
from variables import constants as cv

import pygame
import random

class Enemy(object):
    def __init__(self, window, bullets):
        self.window = window
        self.bullets = bullets

        self.speed = 1
        self.size = (30, 30)

        self.minimum = 50
        self.maximum = 100
        self.enemy_count = 0
        self.number_random = random.randint(self.minimum, self.maximum)

    def generate_enemy(self):
        random_width = random.randint(20, cv.WINDOW_WIDTH - (self.size[0] + 20))
        random_height = random.randint(-200, -10)

        enemy = pygame.Rect(
            random_width,
            random_height,
            self.size[0],
            self.size[1]
        )

        if self.enemy_count < self.number_random:
            self.enemy_count += 1
            self.window.enemies.append(enemy)

    def move_enemy(self):
        for i, enemy in enumerate(self.window.enemies):
            enemy[1] += self.speed

            pygame.draw.rect(
                self.window.surface,
                'blue',
                enemy,
                0,
                2
            )

            rect_one = self.window.enemies[i]
            self.remove_enemy(i, rect_one)

    def remove_enemy(self, i, rect_one):
        for j in range(i + 1, len(self.window.enemies)):
            if rect_one.colliderect(self.window.enemies[j]):
                self.window.enemies.remove(self.window.enemies[j])

    def kill_enemy(self):
        for enemy in self.window.enemies:
            for bullet in self.bullets.missiles:
                if bullet.colliderect(enemy):
                    self.window.enemies.remove(enemy)
                    self.bullets.missiles.remove(bullet)