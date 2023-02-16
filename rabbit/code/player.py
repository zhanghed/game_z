import pygame
import tools
from config import *


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.screen = pygame.display.get_surface()  # 屏幕
        self.animations = tools.Animations(PLAYER_PATH).animations  # 动画
        self.status = 'down_idle'  # 状态
        self.index = 0  # 序号
        self.image = self.animations[self.status][self.index]  # 图像
        self.rect = self.image.get_rect(center=SCREEN_CENTER)  # 区域
        self.pos = pygame.math.Vector2(self.rect.center)  # pos
        self.direction = pygame.math.Vector2()  # 向量
        self.offset = pygame.math.Vector2(0, 0)  # 偏移量
        self.backup_pos = self.pos  # 上一次

    def drw(self, dt, wall):
        self.move(dt, wall)  # 移动
        self.animate(dt)  # 动画
        self.screen.blit(self.image, self.rect)  # 绘制

    def move(self, dt, wall):
        keys = pygame.key.get_pressed()  # 键盘
        self.direction.x = keys[pygame.K_LEFT] * -1 + keys[pygame.K_RIGHT] * 1
        self.direction.y = keys[pygame.K_UP] * -1 + keys[pygame.K_DOWN] * 1
        # 状态
        if self.direction.x < 0:
            self.status = "left"
        elif self.direction.x > 0:
            self.status = "right"
        if self.direction.y < 0:
            self.status = "up"
        elif self.direction.y > 0:
            self.status = "down"
        if self.direction.x + self.direction.y == 0:
            self.status = self.status.split('_')[0] + '_idle'
        # 偏移量
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()
            line_x = MAP_CENTER[0]-SCREEN_CENTER[0]
            line_y = MAP_CENTER[1]-SCREEN_CENTER[1]

            # 撞墙 回上一次
            if len(pygame.sprite.spritecollide(self, wall, False)) > 0:
                self.pos = self.backup_pos

            self.backup_pos = self.pos.copy()  # 备份

            self.pos += self.direction*200*dt  # pos
            self.offset = self.pos-SCREEN_CENTER  # 偏移量                

    def animate(self, dt):
        self.index += 4 * dt
        if self.index >= len(self.animations[self.status]):  # 超出处理
            self.index = 0
        self.image = self.animations[self.status][int(self.index)]
