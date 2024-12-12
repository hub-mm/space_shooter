# ./game_logic/collision_checks.py
import pygame
import random

from variables import constants as cv
from assets.spaceship_powerups.random_powerup import RandomPowerup

class CollisionChecks(object):
    def __init__(self, window, bullets, enemy, spaceship, powerups):
        self.window = window
        self.bullets = bullets
        self.enemy = enemy
        self.spaceship = spaceship
        self.powerups = powerups
        self.random_powerup = self._create_random_powerups()

    def update(self):
        self._check_enemy_on_board()
        self._check_enemy_collisions_with_enemy()
        self._check_missile_collisions_with_enemy()
        self._check_spaceship_collisions_with_enemy_shots()
        self._check_spaceship_collisions_with_enemy()

    def _create_random_powerups(self):
        return RandomPowerup(self.window, self.bullets, self.enemy, self.spaceship, self.powerups)

    def _check_enemy_on_board(self):
        for enemy_sprite in self.enemy.enemy_group:
            if enemy_sprite.rect.y > cv.WINDOW_HEIGHT:
                self.spaceship.lose_life()
                enemy_sprite.kill()

    def _check_enemy_collisions_with_enemy(self):
        collisions = pygame.sprite.groupcollide(
            self.enemy.enemy_group,
            self.enemy.enemy_group,
            False,
            False
        )
        for enemy_one, collide_list in collisions.items():
            for enemy_two in collide_list:
                if enemy_one != enemy_two:
                    enemy_two.kill()
                    self.enemy.enemy_count -= 1

    def _check_missile_collisions_with_enemy(self):
        collisions = pygame.sprite.groupcollide(
            self.bullets.bullet_group,
            self.enemy.enemy_group,
            True,
            True
        )
        for bullet, enemies_hit in collisions.items():
            for enemy_sprite in enemies_hit:
                self.enemy.killed += 1
                self.enemy.total_killed += 1
                self.enemy.kill_x, self.enemy.kill_y = enemy_sprite.rect.x, enemy_sprite.rect.y
                self.enemy.kill = True

                if (self.enemy.total_killed % random.randint(cv.MIN_SPAWN, cv.MAX_SPAWN) == 1
                        and len(self.powerups.powerups) < 5):
                    new_powerup = self.random_powerup.update()
                    self.powerups.generate_powerup(new_powerup)

                self.enemy.kill = False

    def _check_spaceship_collisions_with_enemy_shots(self):
        ship_rect = pygame.Rect(cv.X, cv.Y, self.spaceship.size[0], self.spaceship.size[1])
        for shot_rect in self.enemy.shot[:]:
            if shot_rect.colliderect(ship_rect):
                self.enemy.shot.remove(shot_rect)
                self.spaceship.lose_life()

    def _check_spaceship_collisions_with_enemy(self):
        ship_rect = pygame.Rect(cv.X, cv.Y, self.spaceship.size[0], self.spaceship.size[1])
        for enemy_sprite in self.enemy.enemy_group:
            if enemy_sprite.rect.colliderect(ship_rect):
                self.spaceship.lose_life()
                enemy_sprite.kill()