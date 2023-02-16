import sys
import pygame
from config import *
import player
import map


class Mygame:
    """游戏"""

    def __init__(self):
        pygame.init()  # 初始
        pygame.display.set_caption(MYGAME_NAME)  # 设置标题
        self.screen = pygame.display.set_mode(
            (SCREEN_WIDTH, SCREEN_HEIGHT))  # 设置屏幕
        self.clock = pygame.time.Clock()  # 时钟
        self.font = pygame.freetype.Font(FONT_PATH, FONT_SIZE)  # 设置字体
        self.map = map.Map()  # 创建地图
        self.player = player.Player()  # 创建玩家

    def run(self):
        while True:
            dt = self.clock.tick() / 1000  # 增量时间
            self.screen.fill(color=SCREEN_COLOR)  # 背景
            self.event()  # 事件
            self.map.drw(self.player.offset)  # 地图
            self.player.drw(dt, self.map.wall)  # 玩家
            # self.text(self.player,self.map)
            pygame.display.update()  # 更新

    def text(self):
        pass
        # a = player.rect.colliderect(map.rect)
        # sur, rec = self.font.render(str(map_pos), fgcolor=FONT_COLOR)
        # self.screen.blit(sur, rec)

    def event(self):
        event = pygame.event.get()
        for i in event:
            if i.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


if __name__ == '__main__':
    mygame = Mygame()
    mygame.run()
