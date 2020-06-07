import pygame
from pygame.locals import *

class Myplane(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        super().__init__()

        self.image1 = pygame.image.load('image/me1.png').convert_alpha()
        self.image2 = pygame.image.load('image/me2.png').convert_alpha()
        self.down_image = []
        self.down_image.extend([
            pygame.image.load('image/me_destroy_1.png').convert_alpha(),
            pygame.image.load('image/me_destroy_2.png').convert_alpha(),
            pygame.image.load('image/me_destroy_3.png').convert_alpha(),
            pygame.image.load('image/me_destroy_4.png').convert_alpha()
        ])
        self.rect = self.image1.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.rect.left = (self.width-self.rect.width) // 2
        self.rect.bottom = self.height-60
        self.speed = 10
        # 判断生死的属性
        self.active = True
        # 无敌判断
        self.invincible = False
        # 碰撞的mask属性
        self.mask = pygame.mask.from_surface(self.image1)

    def moveUp(self):
        if self.rect.top > 0:
            self.rect = self.rect.move((0, -self.speed))
            # self.rect.top -= self.speed
        else:
            self.rect.top = 0
    def moveDown(self):
        if self.rect.bottom < self.height-60:
            self.rect = self.rect.move((0, self.speed))
        else:
            self.rect.bottom = self.height-60
    def moveLeft(self):
        if self.rect.left > 0:
            self.rect = self.rect.move((-self.speed, 0))
        else:
            self.rect.left = 0
    def moveRight(self):
        if self.rect.right < self.width:
            self.rect = self.rect.move((self.speed, 0))
        else:
            self.rect.right = self.width

    def reset(self):
        self.rect.left = (self.width - self.rect.width) // 2
        self.rect.bottom = self.height - 60
        self.active = True