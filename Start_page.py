from Init import Init

def start():
    """创建游戏开始页面并创建屏幕对象"""

    init = Init()
    init.init_screen()
    init.init_start_msg()
    init.init_draw_screen()
    init.init_check_start()
    
start()
