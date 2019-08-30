"""
Text.py: 文字对象
"""

from iced.game_object import *
import pygame.font
import pygame
import iced.system
from iced.functions import *

class Text(Object):
    def __init__(self):
        super().__init__()
        self.text = ""
        self.text_width = 0
        self.text_height = 0
        self.text_size = 0
        self.font = None
        self.text_color = (0, 0, 0)
        self.back_color = (255, 255, 255)
        self.image_surface = pygame.surface.Surface((0, 0))

    def create(self, text: str, text_width: int, 
                text_height: int, text_size: int,
                text_color: (int, int, int), 
                back_color: (int, int, int)):
        self.text = text
        self.text_width = text_width
        self.text_height = text_height
        self.text_size = text_size
        self.font = pygame.font.SysFont(None, self.text_size)
        self.text_color = text_color
        self.back_color = back_color
        self.image_surface = self.font.render(self.text, True, self.text_color, self.back_color)
