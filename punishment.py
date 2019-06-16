from random import shuffle

def punishment_1(x):
    print("今年人民对污染极度敏感\n(如果污染过于严重，能量产量减小)")
    if x.pollution >= 20:
        x.energy -= x.pollution
        x.pollution = 0

def punishment_2(x):
    print("核电站发生核泄漏\n(如果有核电站，污染增加，能量减少)")
    if x.power.built_list.get("nuclear"):
        x.pollution += 5
        x.energy -= 12

def punishment_3(x):
    print("由于今年下雨少，海洋运动又不剧烈"
          "\n(水能和海洋能无产量,如果有的话)")
    if x.power.built_list.get("sea"):
        x.energy -= 6
    if x.power.built_list.get("water"):
        x.energy -= 9

def punishment_4(x):
    print("由于经常加班，全国水能发电厂和海洋能发电厂要求加班费"
          "\n(水能和海洋能额外支出,如果有的话）")
    if x.power.built_list.get("sea"):
        x.gold -= 3
    if x.power.built_list.get("water"):
        x.gold -= 4

def random_punishment(x):
    punishment_lists = [1,2,3,4]
    shuffle(punishment_lists)
    punishment = punishment_lists[1]
    if punishment == 1:
        punishment_1(x)
    elif punishment == 2:
        punishment_2(x)
    elif punishment == 3:
        punishment_3(x)
    elif punishment == 4:
        punishment_4(x)
        
    
