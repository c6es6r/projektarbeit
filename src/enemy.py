import pygame

import config

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = 8
        self.position = pygame.Vector2(config.SCREEN_WIDTH, config.SCREEN_HEIGHT/1.125)
        self.velocity = pygame.Vector2()
        self.image = pygame.image.load("img/enemy.png")
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.base = self.image
        self.rect = self.base.get_rect(center=self.position)

    def movement(self):
        self.velocity = pygame.Vector2()
        self.position.x -= self.speed

        # check out of bounds
        if self.position.x > config.SCREEN_WIDTH:
            pass

        self.rect = self.base.get_rect(center=self.position)
