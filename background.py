import pygame
from pygame.locals import *

class Background1(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        super().__init__()
        self.background1 = pygame.image.load('image/background1.jpg').convert()
        self.background1_rect = self.background1.get_rect()
        self.background1_rect.left, self.background1_rect.top = 0, 0
        self.background2 = pygame.image.load('image/background1.jpg').convert()
        self.background2_rect = self.background2.get_rect()
        self.background2_rect.left, self.background2_rect.bottom = \
            0, 0
        self.speed = 1
        self.width, self.height = bg_size[0], bg_size[1]

    def move(self):
        if self.background1_rect.top < self.height:
            self.background1_rect.top += self.speed
        else:
            self.background1_rect.bottom = 0
        if self.background2_rect.top < self.height:
            self.background2_rect.top += self.speed
        else:
            self.background2_rect.bottom = 0

class Background2(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        super().__init__()
        self.background1 = pygame.image.load('image/background2.jpg').convert()
        self.background1_rect = self.background1.get_rect()
        self.background1_rect.left, self.background1_rect.top = 0, 0
        self.background2 = pygame.image.load('image/background2.jpg').convert()
        self.background2_rect = self.background2.get_rect()
        self.background2_rect.left, self.background2_rect.bottom = \
            0, 0
        self.speed = 1
        self.width, self.height = bg_size[0], bg_size[1]

    def move(self):
        if self.background1_rect.top < self.height:
            self.background1_rect.top += self.speed
        else:
            self.background1_rect.bottom = 0
        if self.background2_rect.top < self.height:
            self.background2_rect.top += self.speed
        else:
            self.background2_rect.bottom = 0

class Background3(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        super().__init__()
        self.background1 = pygame.image.load('image/background3.jpg').convert()
        self.background1_rect = self.background1.get_rect()
        self.background1_rect.left, self.background1_rect.top = 0, 0
        self.background2 = pygame.image.load('image/background3.jpg').convert()
        self.background2_rect = self.background2.get_rect()
        self.background2_rect.left, self.background2_rect.bottom = \
            0, 0
        self.speed = 1
        self.width, self.height = bg_size[0], bg_size[1]

    def move(self):
        if self.background1_rect.top < self.height:
            self.background1_rect.top += self.speed
        else:
            self.background1_rect.bottom = self.height - self.background2_rect.height
        if self.background2_rect.top < self.height:
            self.background2_rect.top += self.speed
        else:
            self.background2_rect.bottom = self.height - self.background1_rect.height

class Cloud(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        super().__init__()
        self.width, self.height = bg_size[0], bg_size[1]
        self.image = pygame.image.load('image/cloud.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.bottom = 0, 0
        self.speed = 5

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.rect.bottom = 0