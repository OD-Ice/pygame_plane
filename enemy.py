import pygame
from pygame.locals import *
import random

class SmallEnemy(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        super().__init__()

        self.image = pygame.image.load('image/enemy1.png').convert_alpha()
        self.down_image = []
        self.down_image.extend([
            pygame.image.load('image/enemy1_down1.png').convert_alpha(),
            pygame.image.load('image/enemy1_down2.png').convert_alpha(),
            pygame.image.load('image/enemy1_down3.png').convert_alpha(),
            pygame.image.load('image/enemy1_down4.png').convert_alpha()
        ])
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        # 初始位置随机
        self.rect.left = random.randint(0, self.width-self.rect.width)
        self.rect.bottom = random.randint(-5 * self.height, 0)
        # 速度
        self.speed = 2
        # 判断生死的属性
        self.active = True
        # 毁灭动画索引
        self.e1_down_index = 0
        # 碰撞的mask属性
        self.mask = pygame.mask.from_surface(self.image)

    def move(self, boss_active):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            if not boss_active:
                self.reset()

    def reset(self):
        self.rect.left = random.randint(0, self.width - self.rect.width)
        self.rect.top = random.randint(-5 * self.height, 0)
        # 重置生死状态
        self.active = True

class MidEnemy(pygame.sprite.Sprite):
    energy = 8
    def __init__(self, bg_size):
        super().__init__()

        self.image = pygame.image.load('image/enemy2.png').convert_alpha()
        self.image_hit = pygame.image.load('image/enemy2_hit.png').convert_alpha()
        self.down_image = []
        self.down_image.extend([
            pygame.image.load('image/enemy2_down1.png').convert_alpha(),
            pygame.image.load('image/enemy2_down2.png').convert_alpha(),
            pygame.image.load('image/enemy2_down3.png').convert_alpha(),
            pygame.image.load('image/enemy2_down4.png').convert_alpha()
        ])
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        # 初始位置随机
        self.rect.left = random.randint(0, self.width-self.rect.width)
        self.rect.bottom = random.randint(-10 * self.height, -self.height)
        # 速度
        self.speed = 1
        # 判断生死的属性
        self.active = True
        # 毁灭动画索引
        self.e2_down_index = 0
        # 碰撞的mask属性
        self.mask = pygame.mask.from_surface(self.image)
        self.energy = MidEnemy.energy
        self.hit = False

    def move(self, boss_active):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            if not boss_active:
                self.reset()

    def reset(self):
        self.rect.left = random.randint(0, self.width - self.rect.width)
        self.rect.top = random.randint(-10 * self.height,  -self.height)
        self.energy = MidEnemy.energy
        # 重置生死状态
        self.active = True


class BigEnemy(pygame.sprite.Sprite):
    energy = 20
    def __init__(self, bg_size):
        super().__init__()

        self.image1 = pygame.image.load('image/enemy3_n1.png').convert_alpha()
        self.image2 = pygame.image.load('image/enemy3_n2.png').convert_alpha()
        self.image_hit = pygame.image.load('image/enemy3_hit.png').convert_alpha()
        self.down_image = []
        self.down_image.extend([
            pygame.image.load('image/enemy3_down1.png').convert_alpha(),
            pygame.image.load('image/enemy3_down2.png').convert_alpha(),
            pygame.image.load('image/enemy3_down3.png').convert_alpha(),
            pygame.image.load('image/enemy3_down4.png').convert_alpha(),
            pygame.image.load('image/enemy3_down5.png').convert_alpha(),
            pygame.image.load('image/enemy3_down6.png').convert_alpha()
        ])
        self.rect = self.image1.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        # 初始位置随机
        self.rect.left = random.randint(0, self.width-self.rect.width)
        self.rect.bottom = random.randint(-15 * self.height, -5 * self.height)
        # 速度
        self.speed = 1
        # 判断生死的属性
        self.active = True
        # 毁灭动画索引
        self.e3_down_index = 0
        # 碰撞的mask属性
        self.mask = pygame.mask.from_surface(self.image1)
        self.energy = BigEnemy.energy
        self.hit = False

    def move(self, boss_active):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            if not boss_active:
                self.reset()

    def reset(self):
        self.rect.left = random.randint(0, self.width - self.rect.width)
        self.rect.top = random.randint(-15 * self.height,  -5 * self.height)
        self.energy = BigEnemy.energy
        # 重置生死状态
        self.active = True

class Boss(pygame.sprite.Sprite):
    energy = 1000
    def __init__(self, bg_size):
        super().__init__()

        self.image = pygame.image.load('image/boss.png').convert_alpha()
        self.image_hit = pygame.image.load('image/boss_hit.png').convert_alpha()
        self.down_image = []
        self.down_image.extend([
            pygame.image.load('image/boss_down1.png').convert_alpha(),
            pygame.image.load('image/boss_down2.png').convert_alpha(),
            pygame.image.load('image/boss_down3.png').convert_alpha(),
            pygame.image.load('image/boss_down4.png').convert_alpha(),
            pygame.image.load('image/boss_down5.png').convert_alpha(),
            pygame.image.load('image/boss_down6.png').convert_alpha(),
            pygame.image.load('image/boss_down7.png').convert_alpha(),
            pygame.image.load('image/boss_down8.png').convert_alpha(),
            pygame.image.load('image/boss_down9.png').convert_alpha(),
            pygame.image.load('image/boss_down10.png').convert_alpha(),
            pygame.image.load('image/boss_down11.png').convert_alpha(),
            pygame.image.load('image/boss_down12.png').convert_alpha(),
        ])
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        # 初始位置
        self.rect.left = (self.width - self.rect.width) // 2
        self.rect.bottom = -20
        # 速度
        self.speed = 2
        # 判断生死的属性
        self.active = False
        # 毁灭动画索引
        self.boss_down_index = 0
        # 碰撞的mask属性
        self.mask = pygame.mask.from_surface(self.image)
        self.energy = Boss.energy
        self.hit = False

    def move(self):
        if self.rect.top < 30:
            self.rect.top += self.speed
        else:
            self.rect.left -= self.speed
            if self.rect.left <= 0 or self.rect.right >= self.width:
                self.speed = -self.speed

