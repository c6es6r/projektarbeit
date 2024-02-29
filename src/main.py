import pygame
import math

import config
import player
import enemy

pygame.init()

screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
clock = pygame.time.Clock()

player = player.Player()
enemies = [enemy.Enemy()]

running = True

def draw():
    sprites = pygame.sprite.Group()
    sprites.add(player)
    for i in enemies:
        sprites.add(i)
    sprites.draw(screen)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(pygame.image.load("img/background.png"), (0, 0))

    player.movement()

    for i in enemies:
        if i.position.x < 0:
            enemies.remove(i)

        i.movement()

    draw()

    pygame.display.update()
    clock.tick(config.FPS)
