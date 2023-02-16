import pygame
import pathlib


class Animations:
    """动画素材"""

    def __init__(self, path):
        self.animations = {}
        for i in pathlib.Path(path).iterdir():# 最后一级文件夹下所有图片
            key = str(i).split("\\")[-1]
            paths = pathlib.Path(i).glob("*")
            temp = [pygame.image.load(ii).convert_alpha() for ii in paths]
            self.animations[key] = temp
