import os
import csv
import pygame
from config import *


class Map():
    """地图类"""

    def __init__(self):
        super().__init__()
        self.screen = pygame.display.get_surface()  # 获取屏幕
        self.map_data = self.load_data()  # 加载地图数据
        self.base = Base()  # 生成底图
        self.wall = self.set_wall(self.map_data)  # 生成墙 精灵组

    def drw(self, offset):
        self.base.drw(offset)
        self.wall.update(offset)
        self.wall.draw(self.screen)

    @staticmethod
    def load_data():
        temp = []
        with open(os.path.join(MAP_DATA_PATH)) as temp_data:
            temp_data = csv.reader(temp_data, delimiter=',')
            for i in temp_data:
                temp.append(list(i))
        return temp

    @staticmethod
    def set_wall(map_data):
        wall = pygame.sprite.Group()
        row = 0
        for i in map_data:
            col = 0
            for tile in i:
                if tile == BRICK_ID:
                    Brick(wall, row, col)
                col += 1
            row += 1
        return wall


class Base(pygame.sprite.Sprite):
    """底图精灵类"""

    def __init__(self):
        super().__init__()
        self.screen = pygame.display.get_surface()  # 获取屏幕
        self.image = pygame.image.load(BASE_PATH).convert_alpha()  # 图像
        self.rect = self.image.get_rect(center=SCREEN_CENTER)  # 区域
        self.pos = pygame.math.Vector2(self.rect.center)  # pos

    def drw(self, offset):
        self.rect.center = self.pos-offset
        self.screen.blit(self.image, self.rect)  # 绘制


class Brick(pygame.sprite.Sprite):
    """砖块精灵类"""

    def __init__(self, group, row, col):
        super().__init__(group)
        self.image = pygame.image.load(BRICK_PATH).convert_alpha()  # 图像
        self.image = pygame.transform.scale(
            self.image, (BRICK_WIDTH, BRICK_HEIGHT))  # 规整图像
        temp = pygame.math.Vector2(
            ((col * BRICK_WIDTH)+BRICK_WIDTH/2, (row * BRICK_HEIGHT)+BRICK_HEIGHT/2))  # 相对地图位置
        temp = temp-MAP_CENTER+SCREEN_CENTER
        self.rect = self.image.get_rect(center=temp)  # 区域
        self.pos = pygame.math.Vector2(self.rect.center)  # pos

    def update(self, offset):
        self.rect.center = self.pos-offset
