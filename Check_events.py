import pygame
import game_functions as gf

class Check():
    """监视鼠标和键盘"""
    def __init__(self,msg_lists):
        """初始化监视文本"""
        for i in msg_lists:
            i = gf.get_variable_name(i)
            self.i = i

    def check_cross(self):
        #监视右上角红叉
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

    def check_exit(self):
        #监视exit按钮
        for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse_x,self.mouse_y = pygame.mouse.get_pos()
                    if self.exit_msg.msg_rect.collidepoint(self.mouse_x,self.mouse_y):
                        pygame.quit()

def check(x):
    """监视跳转器"""
    check_events = Check(x)
    exit_f = check_events.check_exit()
    cross_f = check_events.check_cross()
    check_dict = {"exit":exit_f,"cross":cross_f}
    for key,value in check_dict.items():
        if str(key) == str(x):
            value
