# ./assets/spaceship_powerups/powerups.py
import pygame

from variables import constants as cv


class Powerups(object):
    def __init__(self, window, spaceship, enemy, bullets, powerup_name, size = (), speed = 0, colour = ()):
        self.window = window
        self.spaceship = spaceship
        self.enemy = enemy
        self.bullets = bullets
        self.powerup_name = powerup_name
        self.size = size
        self.speed = speed
        self.colour = colour
        self.powerups = {}
        self.count = 0
        self.img = None

    def generate_powerup(self, powerup_type):
        powerup_rect = pygame.Rect(
            self.enemy.kill_x + 10,
            self.enemy.kill_y,
            powerup_type.size[0],
            powerup_type.size[1]
        )

        key = f"{powerup_type.powerup_name} #{self.count}"
        self.powerups[key] = {
            'type': powerup_type,
            'rect': powerup_rect
        }

        self.count += 1

    def load_img(self, powerup_type):

        if powerup_type.powerup_name == 'extra_life':
            self.img = pygame.image.load(cv.HEART_IMG_PATH)
            self.img = pygame.transform.scale(self.img, (30, 30))

        if powerup_type.powerup_name == 'extra_coin':
            self.img = pygame.image.load(cv.COIN_IMG_PATH)
            self.img = pygame.transform.scale(self.img, (30, 30))

        if powerup_type.powerup_name == 'invincible':
            self.img = pygame.image.load(cv.INVINCIBLE_IMG_PATH)
            self.img = pygame.transform.scale(self.img, (30, 30))

        return self.img

    def move_all_powerups(self):
        for entry in self.powerups.values():
            p_type = entry['type']
            p_rect = entry['rect']
            p_rect.y += p_type.speed

            if (p_type.powerup_name == 'extra_life' or
                    p_type.powerup_name == 'extra_coin' or
                    p_type.powerup_name == 'invincible'):
                self.window.surface.blit(self.load_img(p_type), (p_rect.x, p_rect.y))
            else:
                pygame.draw.rect(self.window.surface, p_type.colour, p_rect, 0, 5)

    def check_collisions(self):
        spaceship_rect = pygame.Rect(
            cv.X,
            cv.Y,
            self.spaceship.size[0],
            self.spaceship.size[1]
        )

        to_remove = []

        for key, entry in self.powerups.items():
            p_type = entry['type']
            p_rect = entry['rect']

            if p_rect.colliderect(spaceship_rect):
                if p_type.powerup_name == 'invincible':
                    self.spaceship.state_count = 0

                p_type.powerup_activated()
                to_remove.append(key)

            if p_rect.y > cv.WINDOW_HEIGHT:
                to_remove.append(key)

        for key in to_remove:
            self.powerups.pop(key, None)