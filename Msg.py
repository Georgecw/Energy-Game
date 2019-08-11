import pygame
import pygame.font

class Msg():

    def __init__(self,screen,msg,msg_width,msg_height,msg_size,
                 msg_color,back_color,msg_x,msg_y,):
        """初始化文本属性"""
        self.screen = screen
        self.msg = str(msg)
        self.msg_width = msg_width
        self.msg_height = msg_height
        self.msg_size = msg_size
        self.font = pygame.font.SysFont(None,self.msg_size)
        self.msg_color = msg_color
        self.back_color = back_color
        self.msg_x = msg_x
        self.msg_y = msg_y
        self.msg_rect = pygame.Rect(self.msg_x,self.msg_y,
                                    self.msg_width,self.msg_height)

    def create_msg(self):
        #创建文本
        self.msg_image = self.font.render(self.msg,True,self.msg_color,
                                          self.back_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.msg_rect.center

    def draw_msg(self):
        #绘制文本
        self.screen.blit(self.msg_image,self.msg_image_rect)
