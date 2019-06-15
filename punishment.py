def punishment_1(x):
    if x.pollution >= 20:
        x.energy -= x.pollution
        x.pollution = 0

def punishment_2(x):
    print("核电站发生核泄漏，污染增加，能量减少")
    if x.power.built_list.get(nuclear):
        x.pollution += 5
        x.energy -= 24
    
