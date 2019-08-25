from Init import Init

def start():
<<<<<<< HEAD
    """创建游戏开始页面并创建屏幕对象"""

    init = Init()
    init.init_screen()
    init.init_start_msg()
    init.init_draw_screen()
    init.init_check_start()
    
start()
=======
    """创建游戏初始页面并创建屏幕对象"""
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(
        (settings.screen_width,settings.screen_height))
    screen_rect = screen.get_rect()
    pygame.display.set_caption("Energy Game")
    screen.fill(settings.screen_color)

    #创建文本
    bk = (0,0,0)
    title_msg = Msg(screen,'Energy Game',300,70,80,
                bk,(230,230,230),375,40)
    continue1_msg = Msg(screen,'Continue',200,70,60,
                    bk,(230,230,230),425,180)
    new_game_msg = Msg(screen,'New Game',200,70,60,
                    bk,(230,230,230),425,280)
    options_msg = Msg(screen,'Options',200,70,60,
                    bk,(230,230,230),425,380)
    rules_msg = Msg(screen,'Game Rules',200,70,60,
                    bk,(230,230,230),425,480)
    exit_msg = Msg(screen,'Exit',200,70,60,
                    bk,(230,230,230),425,580)

    #绘制文本
    start_msgs = [title_msg,continue1_msg,new_game_msg,
                  options_msg,rules_msg,exit_msg]
    for i in start_msgs:
        i.create_msg()
        i.draw_msg()

    #使绘制的屏幕可见
    pygame.display.flip()

    #监视鼠标
    while True:
        gf.check_exit()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x,mouse_y = pygame.mouse.get_pos()
                if start_msgs[-1].msg_rect.collidepoint(mouse_x,mouse_y):
                    pygame.quit()
                    
if __name__ == "__main__":
    start()

>>>>>>> e4aea95e4a9eca60c7056b1f83b8021661ad3953
