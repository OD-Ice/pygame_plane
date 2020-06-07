import pygame
from pygame.locals import *
import random

class Bullet_Supply(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        super().__init__()
        self.image = pygame.image.load('image/bullet_supply.png')
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.rect.left, self.rect.bottom = \
            (random.randint(0, self.width - self.rect.width),-100)
        self.speed = 4
        self.active = False
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.active = False

    def reset(self):
        self.rect.left, self.rect.bottom = \
            (random.randint(0, self.width - self.rect.width), -100)
        self.active = True

class Bomb_Supply(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        super().__init__()
        self.image = pygame.image.load('image/bomb_supply.png')
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.rect.left, self.rect.bottom = \
            (random.randint(0, self.width - self.rect.width), -100)
        self.speed = 4
        self.active = False
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.active = False

    def reset(self):
        self.rect.left, self.rect.bottom = \
            (random.randint(0, self.width - self.rect.width), -100)
        self.active = True

class Laser_Supply(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        super().__init__()
        self.image = pygame.image.load('image/laser_supply.png')
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.rect.left, self.rect.bottom = \
            (random.randint(0, self.width - self.rect.width), -100)
        self.speed = 4
        self.active = False
        self.mask = pygame.mask.from_surface(self.image)
        # self.angle = 0
        # self.transform_origin = (self.rect.centerx, self.rect.centery)
        # self.center = (0, 0)
    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
            # self.center = self.rect.center
            # self.angle = -((self.angle + 1) % 360)
            # self.image = pygame.transform.rotate(self.image, self.angle)
            # self.rect = self.image.get_rect()
            # self.rect.center = self.center
        else:
            self.active = False

    def reset(self):
        self.rect.left, self.rect.bottom = \
            (random.randint(0, self.width - self.rect.width), -100)
        # self.angle = 0
        # self.image = pygame.image.load('image/laser_supply.png')
        self.active = True

class Wave_Supply(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        super().__init__()
        self.image = pygame.image.load('image/wave_supply.png')
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.rect.left, self.rect.bottom = \
            (random.randint(0, self.width - self.rect.width), -100)
        self.speed = 4
        self.active = False
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.active = False

    def reset(self):
        self.rect.left, self.rect.bottom = \
            (random.randint(0, self.width - self.rect.width), -100)
        self.active = True

class Defend_Supply(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        super().__init__()
        self.image = pygame.image.load('image/defend_supply.png')
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.rect.left, self.rect.bottom = \
            (random.randint(0, self.width - self.rect.width), -100)
        self.speed = 4
        self.active = False
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.active = False

    def reset(self):
        self.rect.left, self.rect.bottom = \
            (random.randint(0, self.width - self.rect.width), -100)
        self.active = True