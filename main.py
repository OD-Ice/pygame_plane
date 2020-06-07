import pygame
from pygame.locals import *
import sys
import traceback
import myplane
import enemy
import bullet
import supply
import random
import background

# 初始化
pygame.init()
# 混音器初始化
pygame.mixer.init()

# 窗口尺寸
bg_size = width, height = 1024, 650
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption('飞机大战')

# 载入炸弹
bomb_image = pygame.image.load('image/bomb.png')

# 载入暂停按钮
pause_nor_image = pygame.image.load('image/pause_nor.png').convert_alpha()
pause_pressed_image = pygame.image.load('image/pause_pressed.png').convert_alpha()
resume_nor_image = pygame.image.load('image/resume_nor.png').convert_alpha()
resume_pressed_image = pygame.image.load('image/resume_pressed.png').convert_alpha()

# 结束画面
again_image = pygame.image.load('image/again.png').convert_alpha()
again_rect = again_image.get_rect()
again_rect.left, again_rect.top = (width - again_rect.width) // 2, height - 250
gameover_image = pygame.image.load('image/gameover.png').convert_alpha()
gameover_rect = gameover_image.get_rect()
gameover_rect.left, gameover_rect.top = (width - gameover_rect.width) // 2, again_rect.top + 20 + gameover_rect.height

# 载入音频
pygame.mixer.music.load('sound/game_music.wav')
pygame.mixer.music.set_volume(0.2)
bullet_sound = pygame.mixer.Sound('sound/bullet.wav')
bullet_sound.set_volume(0.2)
button_sound = pygame.mixer.Sound('sound/button.wav')
bullet_sound.set_volume(0.2)
enemy1_down_sound = pygame.mixer.Sound('sound/enemy1_down.wav')
enemy1_down_sound.set_volume(0.2)
enemy2_down_sound = pygame.mixer.Sound('sound/enemy2_down.wav')
enemy2_down_sound.set_volume(0.2)
enemy3_down_sound = pygame.mixer.Sound('sound/enemy3_down.wav')
enemy3_down_sound.set_volume(0.2)
enemy3_flying_sound = pygame.mixer.Sound('sound/enemy3_flying.wav')
enemy3_flying_sound.set_volume(0.2)
get_bomb_sound = pygame.mixer.Sound('sound/get_bomb.wav')
get_bomb_sound.set_volume(0.2)
get_bullet_sound = pygame.mixer.Sound('sound/get_bullet.wav')
get_bullet_sound.set_volume(0.2)
me_down_sound = pygame.mixer.Sound('sound/me_down.wav')
me_down_sound.set_volume(0.2)
supply_sound = pygame.mixer.Sound('sound/supply.wav')
supply_sound.set_volume(0.2)
upgrade_sound = pygame.mixer.Sound('sound/upgrade.wav')
upgrade_sound.set_volume(0.2)
bomb_sound = pygame.mixer.Sound('sound/use_bomb.wav')
bomb_sound.set_volume(0.2)
boss_sound = pygame.mixer.Sound('sound/boss_sound.wav')
boss_sound.set_volume(0.2)
boss_down_sound = pygame.mixer.Sound('sound/boss_down_sound.wav')
boss_down_sound.set_volume(0.2)

# 设置声音通道数量
pygame.mixer.set_num_channels(16)

def add_small_enemys(group1, group2, num):
    for i in range(num):
        e1 = enemy.SmallEnemy(bg_size)
        while True:
            if pygame.sprite.spritecollide(e1, group1, False, pygame.sprite.collide_mask):
                e1 = enemy.SmallEnemy(bg_size)
            else:
                break
        group1.add(e1)
        group2.add(e1)

def add_mid_enemys(group1, group2, num):
    for i in range(num):
        e2 = enemy.MidEnemy(bg_size)
        while True:
            if pygame.sprite.spritecollide(e2, group1, False, pygame.sprite.collide_mask):
                e2 = enemy.MidEnemy(bg_size)
            else:
                break
        group1.add(e2)
        group2.add(e2)

def add_big_enemys(group1, group2, num):
    for i in range(num):
        e3 = enemy.BigEnemy(bg_size)
        while True:
            if pygame.sprite.spritecollide(e3, group1, False, pygame.sprite.collide_mask):
                e3 = enemy.BigEnemy(bg_size)
            else:
                break
        group1.add(e3)
        group2.add(e3)

def main():
    # 播放背景音乐 无限循环
    pygame.mixer.music.play(-1)

    # 暂停按钮
    pause_rect = pause_nor_image.get_rect()
    pause_rect.right, pause_rect.top = (width - 10, 10)
    pause_image = pause_nor_image

    # 炸弹
    bomb_rect = bomb_image.get_rect()
    bomb_rect.left, bomb_rect.bottom = (10, height - 10)
    bomb_num = 3

    # 设置难度
    level = 1

    # 帧数设置
    clock = pygame.time.Clock()

    # 血槽颜色
    white = (255, 255, 255)
    green = (0, 255, 0)
    red = (255, 0, 0)
    black = (0, 0, 0)
    orange = (255, 165, 0)

    # 分数统计
    score = 0
    score_font = pygame.font.Font('font/font.ttf', 36)

    # 用于限制文件打开次数
    recoded = False

    # 难度字体
    level_font = pygame.font.Font('font/font.ttf', 18)

    # 炸弹字体
    bomb_font = pygame.font.Font('font/font.ttf', 48)

    # 结束界面字体
    record_font = pygame.font.Font('font/font.ttf', 36)
    end_score_font = pygame.font.Font('font/font.ttf', 56)

    running = True

    pause = False

    # 实例化我方飞机
    me = myplane.Myplane(bg_size)

    # 命数
    life_image = pygame.image.load('image/life.png')
    life_rect = life_image.get_rect()
    life_num = 3

    # 载入补给
    bullet_supply = supply.Bullet_Supply(bg_size)
    bomb_supply = supply.Bomb_Supply(bg_size)
    laser_supply = supply.Laser_Supply(bg_size)
    wave_supply = supply.Wave_Supply(bg_size)
    defend_supply = supply.Defend_Supply(bg_size)

    # 自定义补给时间
    SUPPLY_TIME = USEREVENT

    # 剩余的下一个补给来的时间
    during_time = random.randint(10, 30) * 1000
    pygame.time.set_timer(SUPPLY_TIME, during_time)
    start_time = pygame.time.get_ticks()

    # 定义防护罩时间
    DEFEND_TIME = USEREVENT + 3
    # 防护罩闪烁计时
    defend_num = 0
    # 剩余的防护罩时间
    defend_during_time = 10 * 1000

    # 超级子弹定时器
    # BULLET2_TIME = USEREVENT + 1

    # 无敌时间计时器
    INVINCIBLE_TIME = USEREVENT + 2
    # 剩余的无敌的时间
    invincible_during_time = 3 * 1000

    # 标志是否使用子弹类型
    bullet_type = 1

    # 我方飞机毁灭动画索引
    me_down_index = 0

    # 实例化敌方飞机
    enemies = pygame.sprite.Group()

    small_enemies = pygame.sprite.Group()
    add_small_enemys(small_enemies, enemies, 15)
    mid_enemies = pygame.sprite.Group()
    add_mid_enemys(mid_enemies, enemies, 8)
    big_enemies = pygame.sprite.Group()
    add_big_enemys(big_enemies, enemies, 5)
    boss = enemy.Boss(bg_size)

    # 载入背景
    bg = background.Background1(bg_size)
    cloud = background.Cloud(bg_size)
    cloud_switch = False

    # 控制背景类型
    bg_type = 0

    # 实例化子弹
    bullet1 = []
    bullet1_index = 0
    bullet1_num = 4
    for i in range(bullet1_num):
        bullet1.append(bullet.Bullet1((0, 0)))

    # 实例化子弹2
    bullet2 = []
    bullet2_index = 0
    bullet2_num = 8
    for i in range(bullet2_num):
        bullet2.append(bullet.Bullet2((0, 0)))

    # 实例化子弹3
    bullet3 = []
    bullet3_index = 0
    bullet3_num = 20
    for i in range(bullet3_num):
        bullet3.append(bullet.Bullet3((0, 0)))

    # 实例化子弹4
    bullet4 = []
    bullet4_switch = 1
    bullet4.append(bullet.Bullet4((0, 0)))

    # 实例化子弹5
    bullet5 = []
    bullet5.append(bullet.Bullet5((0, 0)))

    # 实例化冲击波
    wave = bullet.Wave((0, 0))
    wave_flage = False

    # 实例化防护罩
    defend = bullet.Defend((0, 0))

    # 实例化炸弹爆炸
    bomb_fire = bullet.BombFire((0, 0))

    # 实例化Boss子弹
    boss_bullet = bullet.BossBullet((512, -500))
    boss_bullettwo = []
    boss_bullettwo_index = 0
    boss_bullettwo_num = 4
    boss_bullettwogroup = pygame.sprite.Group()
    for i in range(boss_bullettwo_num):
        boss_bullettwo.append(bullet.BossBulletTwo((0, 0)))
    for i in boss_bullettwo:
        boss_bullettwogroup.add(i)
    # Boss激光实例化
    boss_laser = bullet.BossLaser((0, 0))

    # 子弹放在一起
    bullet_fire1 = []
    bullet_fire1.extend(bullet1)
    bullet_fire1.extend(bullet2)
    bullet_fire1.extend(bullet3)
    bullet_fire2 = []
    bullet_fire2.extend(bullet4)
    bullet_fire2.extend(bullet5)

    # 切换飞机的延迟
    delay = 100

    # 用于切换飞机
    switch_image = True

    # 作弊开关
    cheat = 0

    # 程序启动
    while running:
        # 暂停设置
        mouse_left, mouse_top = pygame.mouse.get_pos()

        if pause_rect.collidepoint(mouse_left, mouse_top):
            if not pause:
                pause_image = pause_pressed_image
            else:
                pause_image = resume_pressed_image
        else:
            if not pause:
                pause_image = pause_nor_image
            else:
                pause_image = resume_nor_image

        for event in pygame.event.get():
            if event.type == QUIT:
               pygame.quit()
               sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                # 点击暂停
                if event.button == 1 and pause_rect.collidepoint(event.pos):
                    pause = not pause
                    if pause:
                        pause_time = pygame.time.get_ticks()
                        # 刷新剩余时间
                        if defend.active:
                            defend_during_time = defend_during_time - (pause_time - defend_start_time)
                        if me.invincible and not defend.active:
                            invincible_during_time = invincible_during_time - (pause_time - invincible_start_time)
                        during_time = during_time - (pause_time-start_time)
                        # 暂停补给计时器
                        pygame.time.set_timer(DEFEND_TIME, 0)
                        pygame.time.set_timer(INVINCIBLE_TIME, 0)
                        pygame.time.set_timer(SUPPLY_TIME, 0)
                        pygame.mixer.music.pause()
                        pygame.mixer.pause()
                    else:
                        pygame.time.set_timer(DEFEND_TIME, defend_during_time)
                        pygame.time.set_timer(INVINCIBLE_TIME, invincible_during_time)
                        pygame.time.set_timer(SUPPLY_TIME, during_time)
                        defend_start_time = pygame.time.get_ticks()
                        invincible_start_time = pygame.time.get_ticks()
                        start_time = pygame.time.get_ticks()
                        pygame.mixer.music.unpause()
                        pygame.mixer.unpause()
                # 结束界面的选择
                if life_num == 0:
                    if event.button == 1 and again_rect.collidepoint(event.pos):
                        main()
                    elif event.button == 1 and gameover_rect.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()

            # 发射炸弹
            if event.type == KEYDOWN and not pause:
                if event.key == K_SPACE and bomb_num:
                    bomb_sound.play()
                    bomb_num -= 1
                    bomb_fire.reset(me.rect.center)
                    bomb_fire.active = True
                    bomb_fire_pos = me.rect.center
                # 作弊
                if cheat != 4:
                    if event.key == K_r:
                        cheat = 1
                    elif event.key == K_y and cheat == 1:
                        cheat = 2
                    elif event.key == K_n and cheat == 2:
                        cheat = 3
                    elif event.key == K_b and cheat == 3:
                        cheat = 4
                    else:
                        cheat = 0

            # 补给
            if event.type == SUPPLY_TIME:
                supply_sound.play()
                during_time = random.randint(10, 30) * 1000
                pygame.time.set_timer(SUPPLY_TIME, during_time)
                start_time = pygame.time.get_ticks()
                if random.randint(0, 7-level) == 0:
                    laser_supply.reset()
                else:
                    supply_choice = random.choice([1, 2, 3, 4])
                    if supply_choice == 1:
                        bullet_supply.reset()
                    elif supply_choice == 2:
                        bomb_supply.reset()
                    elif supply_choice == 3:
                        wave_supply.reset()
                    elif supply_choice == 4:
                        defend_supply.reset()

            # 无敌时间结束
            if event.type == INVINCIBLE_TIME:
                pygame.time.set_timer(INVINCIBLE_TIME, 0)
                invincible_during_time = 3 * 1000
                me.invincible = False

            # 防护罩时间结束
            if event.type == DEFEND_TIME:
                pygame.time.set_timer(DEFEND_TIME, 0)
                defend_during_time = 10 * 1000
                defend.active = False
                me.invincible = False
                defend_num = 0

        # 绘制背景
        if bg_type == 2:
            # 载入背景
            bg = background.Background2(bg_size)
            bg_type = 0
        if bg_type == 3:
            # 载入背景
            bg = background.Background3(bg_size)
            bg_type = 0
        if not pause and not delay % 2:
            bg.move()
        screen.blit(bg.background1, bg.background1_rect)
        screen.blit(bg.background2, bg.background2_rect)

        if (level == 3 or level == 5) and cloud_switch:
            if not pause:
                cloud.move()
            screen.blit(cloud.image, cloud.rect)
            if level == 3 and cloud.rect.centery == height // 2:
                bg_type = 2
            if level == 5 and cloud.rect.centery == height // 2:
                bg_type = 3
            if cloud.rect.bottom == 0:
                cloud_switch = False

        if life_num and not pause:
            # 检测键盘操作
            key_pressed = pygame.key.get_pressed()
            if key_pressed[K_w] or key_pressed[KEYUP]:
                me.moveUp()
            if key_pressed[K_s] or key_pressed[KEYDOWN]:
                me.moveDown()
            if key_pressed[K_a] or key_pressed[K_LEFT]:
                me.moveLeft()
            if key_pressed[K_d] or key_pressed[K_RIGHT]:
                me.moveRight()

            # 绘制补给，并检测碰撞
            # 弹2
            if bullet_supply.active:
                bullet_supply.move()
                screen.blit(bullet_supply.image, bullet_supply.rect)
                if pygame.sprite.collide_mask(me, bullet_supply):
                    get_bullet_sound.play()
                    if bullet_type == 2 or bullet_type == 3:
                        bullet_type = 3
                    else:
                        bullet_type = 2
                    bullet_supply.active = False
            # 激光
            if laser_supply.active:
                laser_supply.move()
                screen.blit(laser_supply.image, laser_supply.rect)
                if pygame.sprite.collide_mask(me, laser_supply):
                    get_bullet_sound.play()
                    if bullet_type == 4 or bullet_type == 5:
                        bullet_type = 5
                    else:
                        bullet_type = 4
                    laser_supply.active = False
            # 炸弹
            if bomb_supply.active:
                bomb_supply.move()
                screen.blit(bomb_supply.image, bomb_supply.rect)
                if pygame.sprite.collide_mask(me, bomb_supply):
                    get_bomb_sound.play()
                    if bomb_num < 3:
                        bomb_num += 1
                    bomb_supply.active = False

            # 冲击波
            if wave_supply.active:
                wave_supply.move()
                screen.blit(wave_supply.image, wave_supply.rect)
                if pygame.sprite.collide_mask(me, wave_supply):
                    get_bomb_sound.play()
                    wave_flage = True
                    wave_supply.active = False

            # 防护罩
            if defend_supply.active:
                defend_supply.move()
                screen.blit(defend_supply.image, defend_supply.rect)
                if pygame.sprite.collide_mask(me, defend_supply):
                    get_bomb_sound.play()
                    defend.active = True
                    pygame.time.set_timer(DEFEND_TIME, defend_during_time)
                    defend_start_time = pygame.time.get_ticks()
                    defend_supply.active = False

            # 检测我方飞机是否被撞
            if cheat != 4:
                enemies_down = pygame.sprite.spritecollide(me, enemies, False, pygame.sprite.collide_mask)  # 返回碰撞的列表，以mask方法检测
                if enemies_down and not me.invincible:
                    me.active = False
                    for each in enemies_down:
                        each.active = False
                if pygame.sprite.collide_mask(me, boss):
                    if not me.invincible:
                        me.active = False
                if boss_bullet.active:
                    if pygame.sprite.collide_mask(boss_bullet, me) and not me.invincible:
                        me.active = False
                        boss_bullet.active = False
                if pygame.sprite.spritecollide(me, boss_bullettwogroup, False, pygame.sprite.collide_mask) and not me.invincible:
                    me.active = False
                if boss_laser.active:
                    if pygame.sprite.collide_mask(boss_laser, me) and not me.invincible:
                        me.active = False

            # 难度变化
            if level == 1 and score >= 50000:
                level = 2
                upgrade_sound.play()
                add_small_enemys(small_enemies, enemies, 5)
                add_mid_enemys(mid_enemies, enemies, 1)
                for each in small_enemies:
                    each.speed += 1

            elif level == 2 and score >= 100000:
                level = 3
                cloud_switch = True
                upgrade_sound.play()
                add_small_enemys(small_enemies, enemies, 5)
                add_mid_enemys(mid_enemies, enemies, 3)
                add_big_enemys(big_enemies, enemies, 2)
                for each in small_enemies:
                    each.speed += 1
                for each in mid_enemies:
                    each.speed += 1

            elif level == 3 and score >= 150000:
                level = 4
                upgrade_sound.play()
                add_small_enemys(small_enemies, enemies, 5)
                add_mid_enemys(mid_enemies, enemies, 3)
                add_big_enemys(big_enemies, enemies, 2)
                for each in small_enemies:
                    each.speed += 1
                for each in mid_enemies:
                    each.speed += 1
                for each in big_enemies:
                    each.speed += 1

            elif level == 4 and score >= 200000:
                level = 5
                cloud_switch = True
                upgrade_sound.play()
                add_small_enemys(small_enemies, enemies, 5)
                add_mid_enemys(mid_enemies, enemies, 3)
                add_big_enemys(big_enemies, enemies, 2)
                for each in small_enemies:
                    each.speed += 2
                for each in mid_enemies:
                    each.speed += 2
                for each in big_enemies:
                    each.speed += 1

            elif level == 5 and score >= 270000:
                level = 6
                score_time = pygame.time.get_ticks()
                boss.active = True
                for e in enemies:
                    e.active = False

            # 绘制我方飞机
            if me.active:
                if not me.invincible or defend.active:
                    if not (delay % 5):
                        switch_image = not switch_image
                    if switch_image:
                        screen.blit(me.image1, me.rect)
                    else:
                        screen.blit(me.image2, me.rect)
                elif me.invincible and defend.active == False:
                    if not (delay % 3):
                        if not (delay % 5):
                            switch_image = not switch_image
                        if switch_image:
                            screen.blit(me.image1, me.rect)
                        else:
                            screen.blit(me.image2, me.rect)
            else:
                # 毁灭
                if me_down_index == 0:
                    me_down_sound.play()
                screen.blit(me.down_image[me_down_index], me.rect)
                if not delay % 5:
                    me_down_index = (me_down_index + 1) % 4
                    if me_down_index == 0:
                        if life_num > 0:
                            life_num -= 1
                            me.reset()
                            bullet_type = 1
                            bomb_num = 3
                            wave_flage = False
                            # 无敌时间
                            me.invincible = True
                            pygame.time.set_timer(INVINCIBLE_TIME, 3 * 1000)
                            invincible_start_time = pygame.time.get_ticks()

            # 绘制子弹
            if not (delay % 10):
                if bullet_type == 2:
                    bullet2[bullet2_index].reset((me.rect.centerx - 38, me.rect.centery))  # 只有这里调用了子弹的reset
                    bullet2[bullet2_index + 1].reset((me.rect.centerx + 26, me.rect.centery))  # 只有这里调用了子弹的reset
                    bullet2_index = (bullet2_index + 2) % bullet2_num
                elif bullet_type == 3:
                    bullet3[bullet3_index].reset((me.rect.centerx - 38, me.rect.centery))  # 只有这里调用了子弹的reset
                    bullet3[bullet3_index + 1].reset((me.rect.centerx + 26, me.rect.centery))  # 只有这里调用了子弹的reset
                    bullet3[bullet3_index + 2].reset(me.rect.midtop)  # 只有这里调用了子弹的reset
                    bullet3[bullet3_index + 3].reset((me.rect.centerx - 18, me.rect.centery))  # 只有这里调用了子弹的reset
                    bullet3[bullet3_index + 4].reset((me.rect.centerx + 6, me.rect.centery))  # 只有这里调用了子弹的reset
                    bullet3_index = (bullet3_index + 5) % bullet3_num
                elif bullet_type == 1:
                    bullet1[bullet1_index].reset(me.rect.midtop)  # 只有这里调用了子弹的reset
                    bullet1_index = (bullet1_index + 1) % bullet1_num
            if bullet_type == 4:
                bullet4[0].reset(me.rect.midtop)  # 只有这里调用了子弹的reset
            else:
                bullet4[0].active = False
            if bullet_type == 5:
                bullet5[0].reset(me.rect.midtop)  # 只有这里调用了子弹的reset
            else:
                bullet5[0].active = False

            # 冲击波绘制
            if not delay % 200:
                if wave_flage:
                    wave.reset(me.rect.midtop)

            # 防护罩绘制
            if defend.active:
                defend_num += 1
                me.invincible = True
                defend.reset(me.rect.center)
                if defend_num < 420:
                    screen.blit(defend.image, defend.rect)
                else:
                    if not delay % 5:
                        screen.blit(defend.image, defend.rect)
                # 检测防护罩是否被撞
                enemies_down = pygame.sprite.spritecollide(defend, enemies, False,
                                                           pygame.sprite.collide_mask)  # 返回碰撞的列表，以mask方法检测
                for each in enemies_down:
                    each.active = False

            # 炸弹爆炸绘制
            if bomb_fire.active:
                bomb_fire.move(bomb_fire_pos)
                screen.blit(bomb_fire.image, bomb_fire.rect)
                enemies_down = pygame.sprite.spritecollide(bomb_fire, enemies, False,
                                                           pygame.sprite.collide_mask)
                for each in enemies_down:
                    each.active = False

                # Boss与炸弹碰撞检测
                if boss.active:
                    if pygame.sprite.collide_mask(bomb_fire, boss) and boss.rect.top > 0:
                        if not delay % 5:
                            boss.hit = True
                            boss.energy -= 30
                            if boss.energy <= 0:
                                boss.active = False

            # Boss子弹绘制
            if boss.active and not delay % 400:
                boss_bullet.reset(boss.rect.center)

            if boss.active and not delay % 50 and boss.energy <= 0.5 * enemy.Boss.energy:
                boss_bullettwo[boss_bullettwo_index].reset(boss.rect.midtop)
                boss_bullettwo_index = (boss_bullettwo_index + 1) % boss_bullettwo_num

            # 子弹移动 碰撞检测
            # 子弹检测
            for b in bullet_fire1:
                if b.active:
                    b.move()
                    screen.blit(b.image, b.rect)
                    enemy_hit = pygame.sprite.spritecollide(b, enemies, False, pygame.sprite.collide_mask)
                    if enemy_hit:
                        b.active = False  # active = False并不会毁灭子弹，子弹只是不再显示，也不再检测碰撞, 不再移动
                        for e in enemy_hit:
                            if e in small_enemies:
                                e.active = False
                            else:
                                e.hit = True
                                e.energy -= 1
                                if e.energy <= 0:
                                    e.active = False
                    # Boss与子弹碰撞检测
                    if boss.active:
                        if pygame.sprite.collide_mask(b, boss) and boss.rect.top > 0:
                            b.active = False
                            boss.hit = True
                            boss.energy -= 1
                            if boss.energy <= 0:
                                boss.active = False

            # 激光检测
            for b in bullet_fire2:
                if b.active:
                    if bullet4_switch == 0:
                        screen.blit(b.image1, b.rect)
                    elif bullet4_switch == 1:
                        screen.blit(b.image2, b.rect)
                    enemy_hit = pygame.sprite.spritecollide(b, enemies, False, pygame.sprite.collide_mask)
                    if enemy_hit:
                        for e in enemy_hit:
                            if e.rect.bottom > 0:
                                if e in small_enemies:
                                    e.active = False
                                else:
                                    if bullet_type == 4:
                                        if not delay % 8:
                                            e.hit = True
                                            e.energy -= 1
                                            if e.energy <= 0:
                                                e.active = False
                                    elif bullet_type == 5:
                                        if not delay % 8:
                                            e.hit = True
                                            e.energy -= 3
                                            if e.energy <= 0:
                                                e.active = False
                    # Boss与激光碰撞检测
                    if boss.active:
                        if pygame.sprite.collide_mask(b, boss) and boss.rect.top > 0:
                            if bullet_type == 4:
                                if not delay % 10:
                                    boss.hit = True
                                    boss.energy -= 3
                                    if boss.energy <= 0:
                                        boss.active = False
                            elif bullet_type == 5:
                                if not delay % 10:
                                    boss.hit = True
                                    boss.energy -= 6
                                    if boss.energy <= 0:
                                        boss.active = False

            # 冲击波检测
            if wave.active:
                wave.move()
                if bullet4_switch == 0:
                    screen.blit(wave.image1, wave.rect)
                elif bullet4_switch == 1:
                    screen.blit(wave.image2, wave.rect)
                enemy_hit = pygame.sprite.spritecollide(wave, enemies, False, pygame.sprite.collide_mask)
                if enemy_hit:
                    for e in enemy_hit:
                        if e in small_enemies:
                            e.active = False
                        else:
                            if not delay % 12:
                                e.hit = True
                                e.energy = int(e.energy * 0.9 - 7)
                                if e.energy <= 0:
                                    e.active = False
                # Boss与冲击波碰撞检测
                if boss.active:
                    if pygame.sprite.collide_mask(wave, boss) and boss.rect.top > 0:
                        if not delay % 12:
                            boss.hit = True
                            boss.energy = int(boss.energy * 0.95 - 7)
                            if boss.energy <= 0:
                                boss.active = False

            # Boss子弹绘制
            if boss.active:
                if boss_bullet.active:
                    boss_bullet.move()
                    screen.blit(boss_bullet.image[boss_bullet.index], boss_bullet.rect)
                    if not delay % 10 and boss_bullet.index != 7:
                        boss_bullet.index += 1
                # 二号Boss子弹
                if boss.energy <= 0.5 * enemy.Boss.energy:
                    for b in boss_bullettwo:
                        if b.active:
                            b.move()
                            screen.blit(b.image, b.rect)
                        elif boss.energy <= 0.2 * enemy.Boss.energy:
                            # 子弹消失时出现激光
                            boss_laser.reset(b.rect.midtop)
                            if switch_image:
                                screen.blit(boss_laser.image1, boss_laser.rect)
                            else:
                                screen.blit(boss_laser.image2, boss_laser.rect)

            if not delay % 5:
                bullet4_switch = (bullet4_switch + 1) % 2

            # 绘制敌方飞机

            # Boss
            if boss.active:
                boss.move()
                if boss.hit:
                    if boss.energy > 0.5 * enemy.Boss.energy:
                        screen.blit(boss.image_hit, boss.rect)
                    elif 0.5 * enemy.Boss.energy >= boss.energy > 0.2 * enemy.Boss.energy:
                        screen.blit(boss.down_image[1], boss.rect)
                    else:
                        screen.blit(boss.down_image[2], boss.rect)
                    boss.hit = False
                else:
                    screen.blit(boss.image, boss.rect)

                # 绘制血槽
                pygame.draw.line(screen, white,
                                 (boss.rect.left, boss.rect.top - 5),
                                 (boss.rect.right, boss.rect.top - 5),
                                 5)
                # 不同血量显示不同颜色
                energy_remain = boss.energy / enemy.Boss.energy
                if energy_remain > 0.5:
                    energy_color = green
                elif 0.5 >= energy_remain > 0.2:
                    energy_color = orange
                else:
                    energy_color = red
                pygame.draw.rect(screen, energy_color,
                                 (boss.rect.left, boss.rect.top - 10,
                                  int((boss.rect.right - boss.rect.left) * energy_remain), 10))
                # 绘制血槽框
                pygame.draw.rect(screen, black, (boss.rect.left, boss.rect.top - 10, boss.rect.width, 10), 2)

                # 即将出现时播放音效
                if boss.rect.bottom == -18:
                    boss_sound.play()

            else:
                # 毁灭
                if boss.boss_down_index == 0 and boss.rect.top > 0:
                    boss_down_sound.play()
                    score_time_end = pygame.time.get_ticks()
                    score += 200000 - (score_time_end - score_time)
                screen.blit(boss.down_image[boss.boss_down_index], boss.rect)
                if not (delay % 10) and boss.rect.top > 0:
                    boss.boss_down_index = (boss.boss_down_index + 1) % 12
                    if boss.boss_down_index == 0:
                        life_num = 0


            # 大型飞机
            for each in big_enemies:
                if each.active:
                    each.move(boss.active)
                    if each.hit:
                        screen.blit(each.image_hit, each.rect)
                        each.hit = False
                    else:
                        if switch_image:
                            screen.blit(each.image1, each.rect)
                        else:
                            screen.blit(each.image2, each.rect)

                    # 绘制血槽
                    pygame.draw.line(screen, white,
                                     (each.rect.left, each.rect.top - 5),
                                     (each.rect.right, each.rect.top - 5),
                                     5)
                    # 不同血量显示不同颜色
                    energy_remain = each.energy / enemy.BigEnemy.energy
                    if energy_remain > 0.5:
                        energy_color = green
                    elif 0.5 >= energy_remain > 0.2:
                        energy_color = orange
                    else:
                        energy_color =red
                    pygame.draw.rect(screen, energy_color,
                                     (each.rect.left, each.rect.top - 10,
                                      int((each.rect.right - each.rect.left) * energy_remain), 10))
                    # 绘制血槽框
                    pygame.draw.rect(screen, black, (each.rect.left, each.rect.top - 10, each.rect.width, 10), 2)

                    # 即将出现时播放音效
                    if each.rect.bottom == -50 or each.rect.bottom == -51 or each.rect.bottom == -52:
                        enemy3_flying_sound.play(-1)
                    if each.rect.top > height:
                        enemy3_flying_sound.stop()
                else:
                    # 毁灭
                    enemy3_flying_sound.stop()
                    if each.e3_down_index == 0:
                        enemy3_down_sound.play()
                    screen.blit(each.down_image[each.e3_down_index], each.rect)
                    if not (delay % 5):
                        each.e3_down_index = (each.e3_down_index + 1) % 6
                        if each.e3_down_index == 0:
                            score += 10000
                            if not boss.active:
                                each.reset()
                                big_enemies.remove(each)
                                while True:
                                    if pygame.sprite.spritecollide(each, big_enemies, False, pygame.sprite.collide_mask):
                                        each.reset()
                                    else:
                                        break
                                big_enemies.add(each)
                            else:
                                big_enemies.remove(each)
                                enemies.remove(each)

            # 中型飞机
            for each in mid_enemies:
                if each.active:
                    each.move(boss.active)
                    if each.hit:
                        screen.blit(each.image_hit, each.rect)
                        each.hit = False
                    else:
                        screen.blit(each.image, each.rect)
                    # 绘制血槽
                    pygame.draw.line(screen, white,
                                     (each.rect.left, each.rect.top - 5),
                                     (each.rect.right, each.rect.top - 5),
                                     5)
                    # 不同血量显示不同颜色
                    energy_remain = (each.energy / enemy.MidEnemy.energy)
                    if energy_remain > 0.5:
                        energy_color = green
                    elif 0.5 >= energy_remain > 0.2:
                        energy_color = orange
                    else:
                        energy_color = red
                    pygame.draw.rect(screen, energy_color,
                                     (each.rect.left, each.rect.top - 10,
                                     int((each.rect.right - each.rect.left) * energy_remain), 10))
                    # 绘制血槽框
                    pygame.draw.rect(screen, black, (each.rect.left, each.rect.top - 10, each.rect.width, 10), 2)

                else:
                    # 毁灭
                    if each.e2_down_index == 0:
                        enemy2_down_sound.play()
                    screen.blit(each.down_image[each.e2_down_index], each.rect)
                    if not (delay % 5):
                        each.e2_down_index = (each.e2_down_index + 1) % 4
                        if each.e2_down_index == 0:
                            score += 3000
                            if not boss.active:
                                each.reset()
                                mid_enemies.remove(each)
                                while True:
                                    if pygame.sprite.spritecollide(each, mid_enemies, False, pygame.sprite.collide_mask):
                                        each.reset()
                                    else:
                                        break
                                mid_enemies.add(each)
                            else:
                                mid_enemies.remove(each)
                                enemies.remove(each)

            # 小型飞机
            for each in small_enemies:
                if each.active:
                    each.move(boss.active)
                    screen.blit(each.image, each.rect)
                else:
                    # 毁灭
                    if each.e1_down_index == 0:
                        enemy1_down_sound.play()
                    screen.blit(each.down_image[each.e1_down_index], each.rect)
                    if not (delay % 5):
                        each.e1_down_index = (each.e1_down_index + 1) % 4
                        if each.e1_down_index == 0:
                            score += 1000
                            if not boss.active:
                                each.reset()
                                small_enemies.remove(each)
                                while True:
                                    if pygame.sprite.spritecollide(each, small_enemies, False, pygame.sprite.collide_mask):
                                        each.reset()
                                    else:
                                        break
                                small_enemies.add(each)
                            else:
                                small_enemies.remove(each)
                                enemies.remove(each)

            # 绘制炸弹
            bomb_text = bomb_font.render('X %d' % bomb_num, True, white)
            bomb_text_rect = bomb_rect.copy()
            bomb_text_rect.left = bomb_rect.width + 20
            screen.blit(bomb_image, bomb_rect)
            screen.blit(bomb_text, bomb_text_rect)

            # 绘制生命数
            for i in range(life_num):
                screen.blit(life_image, (width - 10 - (i + 1) * (life_rect.width + 20),
                                         height - 10 - life_rect.height))

        # 绘制结束画面
        elif life_num == 0:
            pygame.mixer.music.stop()
            pygame.mixer.stop()
            pygame.time.set_timer(SUPPLY_TIME, 0)
            if not recoded:
                # 读取历史最高分
                with open('record.txt', 'r') as f:
                    record_score = int(f.read())

                # 如果玩家打破纪录
                if score > record_score:
                    record_score = score
                    with open('record.txt', 'w') as f:
                        f.write(str(score))
                recoded = True

            # 结束界面
            record_score_text = record_font.render('BestScore : %s' % record_score, True, white)
            screen.blit(record_score_text, (10, 10))
            end_score_text1 = end_score_font.render('Your Score', True, white)
            end_score_text2 = end_score_font.render(str(score), True, white)
            end_score_rect1 = end_score_text1.get_rect()
            end_score_rect2 = end_score_text2.get_rect()
            screen.blit(end_score_text1,
                        ((width - end_score_rect1.width) // 2, (height - end_score_rect1.height) // 2 - 80))
            screen.blit(end_score_text2,
                        ((width - end_score_rect2.width) // 2, (height - end_score_rect1.height) // 2 - 100 + end_score_rect1.height))
            screen.blit(again_image, again_rect)
            screen.blit(gameover_image, gameover_rect)

        if life_num:
            # 绘制难度
            level_text = level_font.render('level : %s' % str(level), True, white)
            screen.blit(level_text, (10, 50))
            # 绘制暂停按钮
            screen.blit(pause_image, pause_rect)
            # 绘制分数
            score_text = score_font.render('Score : %d' % score, True, white)
            screen.blit(score_text, (10, 10))
        delay -= 1
        if not delay:
            delay = 1000

        pygame.display.flip()

        # 帧数
        clock.tick(60)

if __name__ == '__main__':
    try:
        main()
    except SystemExit:
        pass
    except:
        # 打印报错信息
        traceback.print_exc()
        pygame.quit()
        input()