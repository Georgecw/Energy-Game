from random import shuffle

def do_target(x, number):
    if number == 1:
        print("任务:工厂要求提供焦炭，酒精，煤油以提高产能"
          "\n(请提供对应一次能源：1个煤，1个生物质能，1个石油）")
        respon = input("请回答：Y(接任务)或 N(不接任务) ")
        if respon.upper() == "Y":
            x.input_energy()
            if x.power.built_list.get("coal") and x.power.built_list.get("creature") and x.power.built_list.get("oil"):
                for i in ["coal","creature","oil"]:
                    x.gold -= x.power.e_list[i][0]
                    x.pollution += x.power.e_list[i][2]
                    x.power.built_list[i] -= 1
                x.energy += 30
            else:
                print("对不起，你没有足够的能源")
    elif number == 2:
        print("任务：气象学家预测今年冬天将比往常更寒冷，"
          "城市将需要石油气和沼气\n(请提供对应一次能源：1个石油,2个生物质能")
        respon = input("请回答：Y(接任务)或 N(不接任务) ")
        if respon.upper() == "Y":
            x.input_energy()
            if x.power.built_list.get("creature") == 2 and x.power.built_list.get("oil"):
                x.gold -= x.power.e_list["creature"][0]*2
                x.gold -= x.power.e_list["oil"][0]
                x.pollution += x.power.e_list["creature"][2]*2
                x.pollution += x.power.e_list["oil"][2]
                x.power.built_list["creature"] -= 2
                x.power.built_list["oil"] -= 1
                x.energy += 30
    elif number == 3:
        print("任务：今年，人们迫切需要：汽油，煤气"
        "\n(请提供相应一次能源：1个石油，2个煤)")
        respon = input("请回答：Y(接任务)或 N(不接任务) ")
        if respon.upper() == "Y":
            x.input_energy()
            if x.power.built_list.get("oil") and x.power.built_list.get("coal") == 2:
                x.gold -= x.power.e_list["oil"][0]
                x.gold -= x.power.e_list["coal"][0]*2
                x.pollution += x.power.e_list["oil"][2]
                x.pollution += x.power.e_list["coal"][2]*2
                x.power.built_list["oil"] -= 1
                x.power.built_list["coal"] -= 2
                x.energy += 30
    else:
        print("Function target.py/target error: selection is not correct.")
              
#def target_1(x):
   # print("任务:工厂要求提供焦炭，酒精，煤油以提高产能"
          #"\n(请提供对应一次能源：1个煤，1个生物质能，1个石油）")
    #respon = input("请回答：Y(接任务)或 N(不接任务) ")
    #if respon.upper() == "Y":
        #x.input_energy()
        #if x.power.built_list.get("coal") and x.power.built_list.get("creature") and x.power.built_list.get("oil"):
            #for i in ["coal","creature","oil"]:
                #x.gold -= x.power.e_list[i][0]
                #x.pollution += x.power.e_list[i][2]
                #x.power.built_list[i] -= 1
            #x.energy += 30
        #else:
            #print("对不起，你没有足够的能源")

#def target_2(x):
    #print("任务：气象学家预测今年冬天将比往常更寒冷，"
          #"城市将需要石油气和沼气\n(请提供对应一次能源：1个石油,2个生物质能")
    #respon = input("请回答：Y(接任务)或 N(不接任务) ")
    #if respon.upper() == "Y":
        #x.input_energy()
        #if x.power.built_list.get("creature") == 2 and x.power.built_list.get("oil"):
            #x.gold -= x.power.e_list["creature"][0]*2
            #x.gold -= x.power.e_list["oil"][0]
            #x.pollution += x.power.e_list["creature"][2]*2
            #x.pollution += x.power.e_list["oil"][2]
            #x.power.built_list["creature"] -= 2
            #x.power.built_list["oil"] -= 1
            #x.energy += 30
            
#def target_3(x):
    #print("任务：今年，人们迫切需要：汽油，煤气"
          #"\n(请提供相应一次能源：1个石油，2个煤)")
    #respon = input("请回答：Y(接任务)或 N(不接任务) ")
    #if respon.upper() == "Y":
        #x.input_energy()
        #if x.power.built_list.get("oil") and x.power.built_list.get("coal") == 2:
            #x.gold -= x.power.e_list["oil"][0]
            #x.gold -= x.power.e_list["coal"][0]*2
            #x.pollution += x.power.e_list["oil"][2]
            #x.pollution += x.power.e_list["coal"][2]*2
            #x.power.built_list["oil"] -= 1
            #x.power.built_list["coal"] -= 2
            #x.energy += 30

def random_target(x):
    target_lists = [1,2,3]
    shuffle(target_lists)
    target = target_lists[1]
    do_target(x, target)
    #if target == 1:
        #target_1(x)
    #elif target == 2:
        #target_2(x)
    #elif target == 3:
        #target_3(x)
    
          
