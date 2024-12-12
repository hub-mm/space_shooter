# ./assets/missile_sprite.py
import pygame

class BulletSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, speed, colour):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(colour)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed

    def update(self):
        self.rect.y -= self.speed

        if self.rect.y < 0:
            self.kill()