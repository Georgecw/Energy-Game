from random import shuffle

def punishment_1(x):
    print("由于污染过于严重，能量产量减小")
    if x.pollution >= 20:
        x.energy -= x.pollution
        x.pollution = 0

def punishment_2(x):
    print("核电站发生核泄漏，污染增加，能量减少")
    if x.power.built_list.get("nuclear"):
        x.pollution += 5
        x.energy -= 24

def punishment_3(x):
    print("由于今年下雨少，海洋运动又不剧烈，水能和风能无产量")
    if x.power.built_list.get("sea"):
        x.energy -= 6
    if x.power.built_list.get("water"):
        x.energy -= 9

def ramdom_punishment(x):
    punishment_lists = [1,2,3]
    shuffle(punishment_lists)
    punishment = punishment_lists[1]
    if punishment == 1:
        punishment_1(x)
    elif punishment == 2:
        punishment_2(x)
    elif punishment == 3:
        punishment_3(x)
        
    
