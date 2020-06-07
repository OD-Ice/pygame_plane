import pygame
from pygame.locals import *

pygame.mixer.init()
bullet_sound = pygame.mixer.Sound('sound/bullet.wav')
bullet_sound.set_volume(0.2)
boss_bullet_sound = pygame.mixer.Sound('sound/boss_bullet_sound.wav')
boss_bullet_sound.set_volume(0.2)


class Bullet1(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()

        self.image = pygame.image.load('image/bullet1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.center = position
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = 12
        self.active = True

    def move(self):
        if self.rect.top > 0:
            self.rect.top -= self.speed
        else:
            self.active = False

    def reset(self, position):
        self.rect.center = position
        self.active = True
        bullet_sound.play()

class Bullet2(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()

        self.image = pygame.image.load('image/bullet2.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = 14
        self.active = True

    def move(self):
        if self.rect.top > 0:
            self.rect.top -= self.speed
        else:
            self.active = False

    def reset(self, position):
        self.rect.left, self.rect.top = position
        self.active = True
        bullet_sound.play()

class Bullet3(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()

        self.image = pygame.image.load('image/bullet3.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = 16
        self.active = True

    def move(self):
        if self.rect.top > 0:
            self.rect.top -= self.speed
        else:
            self.active = False

    def reset(self, position):
        self.rect.center = position
        self.active = True
        bullet_sound.play()

class Bullet4(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()

        self.image1 = pygame.image.load('image/bullet4_1.png').convert_alpha()
        self.image2 = pygame.image.load('image/bullet4_2.png').convert_alpha()
        self.rect = self.image1.get_rect()
        self.rect.midbottom = position
        self.mask = pygame.mask.from_surface(self.image1)
        self.active = False

    def reset(self, position):
        self.rect.midbottom = position
        self.active = True

class Bullet5(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()

        self.image1 = pygame.image.load('image/bullet5_1.png').convert_alpha()
        self.image2 = pygame.image.load('image/bullet5_2.png').convert_alpha()
        self.rect = self.image1.get_rect()
        self.rect.midbottom = position
        self.mask = pygame.mask.from_surface(self.image1)
        self.active = False

    def reset(self, position):
        self.rect.midbottom = position
        self.active = True

class Wave(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()

        self.image1 = pygame.image.load('image/wave1.png').convert_alpha()
        self.image2 = pygame.image.load('image/wave2.png').convert_alpha()
        self.rect = self.image1.get_rect()
        self.rect.center = position
        self.mask = pygame.mask.from_surface(self.image1)
        self.speed = 12
        self.active = False

    def move(self):
        if self.rect.bottom > 0:
            self.rect.top -= self.speed
        else:
            self.active = False

    def reset(self, position):
        self.rect.midtop = position
        self.active = True

class Defend(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()

        self.image = pygame.image.load('image/defend.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.mask = pygame.mask.from_surface(self.image)
        self.active = False

    def reset(self, position):
        self.rect.center = position
        self.active = True

class BombFire(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()

        self.oimage = pygame.image.load('image/bomb_fire.png').convert_alpha()
        self.image = self.oimage
        self.orect = self.oimage.get_rect()
        self.rect = self.orect
        self.rect.left, self.rect.top = position
        self.mask = pygame.mask.from_surface(self.image)
        self.ratio = 1.00
        self.active = False

    def move(self, position):
        self.ratio += 0.3
        self.image = pygame.transform.smoothscale(self.oimage,
                                                  (int(self.orect.width*self.ratio), int(self.orect.height*self.ratio)))
        self.rect.width, self.rect.height = int(self.orect.width*self.ratio), int(self.orect.height*self.ratio)
        self.rect.center = position
        if self.ratio > 10:
            self.active = False
            self.ratio = 1
        self.mask = pygame.mask.from_surface(self.image)

    def reset(self, position):
        self.image = self.oimage
        self.rect = self.oimage.get_rect()
        self.rect.center = position

class BossBullet(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()

        self.image = []
        self.image.extend([
            pygame.image.load('image/boss_bullet1.png').convert_alpha(),
            pygame.image.load('image/boss_bullet2.png').convert_alpha(),
            pygame.image.load('image/boss_bullet3.png').convert_alpha(),
            pygame.image.load('image/boss_bullet4.png').convert_alpha(),
            pygame.image.load('image/boss_bullet5.png').convert_alpha(),
            pygame.image.load('image/boss_bullet6.png').convert_alpha(),
            pygame.image.load('image/boss_bullet7.png').convert_alpha(),
            pygame.image.load('image/boss_bullet8.png').convert_alpha()
        ])
        self.rect = self.image[0].get_rect()
        self.center = position
        self.mask = pygame.mask.from_surface(self.image[0])
        self.speed = 4
        self.active = False
        self.index = 0

    def move(self):
        if self.rect.top < 650:
            self.rect.top += self.speed
        else:
            self.active = False

    def reset(self, position):
        self.rect.center = position
        self.active = True
        self.index = 0
        boss_bullet_sound.play()

class BossBulletTwo(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()

        self.image = pygame.image.load('image/boss_bullettwo.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.center = position
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = [-5, 5]
        self.active = False

    def move(self):
        if self.rect.top < 650:
            self.rect = self.rect.move(self.speed)
            if self.rect.left <= 0 or self.rect.right >= 1024:
                self.image = pygame.transform.flip(self.image, True, False)
                self.speed[0] = -self.speed[0]
        else:
            self.active = False

    def reset(self, position):
        self.rect.center = position
        self.active = True
        bullet_sound.play()

class BossLaser(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()

        self.image1 = pygame.image.load('image/boss_laser1.png').convert_alpha()
        self.image2 = pygame.image.load('image/boss_laser2.png').convert_alpha()
        self.rect = self.image1.get_rect()
        self.rect.midbottom = position
        self.mask = pygame.mask.from_surface(self.image1)
        self.active = False

    def reset(self, position):
        self.rect.midbottom = position
        self.active = True