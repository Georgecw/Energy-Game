import pygame
import pygame.font

class Msg():

    def __init__(self,msg,msg_width,msg_height,msg_size,
                 msg_color,back_color,msg_x,msg_y,):
        "初始化按钮属性"
        pygame.init()
        self.screen = pygame.display.set_mode((1280,960))
        pygame.display.set_caption("Test")
        #以上的屏幕初始化是为了测试
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
        #创建按钮
        self.msg_image = self.font.render(self.msg,True,self.msg_color,
                                          self.back_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.msg_rect.center

    def draw_msg(self):
        #绘制按钮
        self.screen.fill(self.back_color,self.msg_rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)
        pygame.display.flip()

test = Msg("fuck you",200,200,28,(255,255,255),(0,0,255),0,0)
test.create_msg()
test.draw_msg()
