import pygame
from Msg import Msg
from Settings import Settings
import game_functions as gf

class Init():
    """初始化游戏"""

    def init_screen(self):
        #创建屏幕对象
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Energy Game")
        self.screen.fill(self.settings.screen_color)

    def init_draw_screen(self):
        #绘制屏幕
        pygame.display.flip()

    def init_start_msg(self):
        #绘制开始页面文本
        self.bk = (0,0,0)
        self.title_msg = Msg(self.screen,'Energy Game',300,70,80,
                            self.bk,(230,230,230),375,40)
        self.continue1_msg = Msg(self.screen,'Continue',200,70,60,
                            self.bk,(230,230,230),425,180)
        self.new_game_msg = Msg(self.screen,'New Game',200,70,60,
                            self.bk,(230,230,230),425,280)
        self.options_msg = Msg(self.screen,'Options',200,70,60,
                            self.bk,(230,230,230),425,380)
        self.rules_msg = Msg(self.screen,'Game Rules',200,70,60,
                            self.bk,(230,230,230),425,480)
        self.exit_msg = Msg(self.screen,'Exit',200,70,60,
                            self.bk,(230,230,230),425,580)
        self.start_msgs = [self.title_msg,self.continue1_msg,
                           self.new_game_msg,self.options_msg,
                           self.rules_msg,self.exit_msg]
        for i in self.start_msgs:
            i.create_msg()
            i.draw_msg()

    def init_check_start(self):
        #监视开始页面
        gf.check(self.start_msgs)
