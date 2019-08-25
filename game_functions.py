from Country import Country
from punishment import *
from target import *
import pygame

def country_init(x):
    """自定义你的国家"""
    init_input = "请输入" + str(x) + "国的"
    nuclear_lock = input("\n"+ init_input + "核能上限: ")
    ice_lock = input("\n"+ init_input + "可燃冰上限: ")
    eature_lock = input("\n"+ init_input + "生物质能上限: ")
    oil_lock = input("\n" + init_input + "石油上限: ")
    coal_lock = input("\n"+ init_input + "煤上限: ")
    x = Country(nuclear_lock,ice_lock,creature_lock,oil_lock,coal_lock)

def bout(x):
    """x国家的一个回合"""
    random_target(x)
    print("")
    x.change_country()
    print("")
    random_punishment(x)
    x.show()
    input("\nPlease Press <enter>")

def get_variable_name(hh):
    """获取一个变量名"""
    name_dict = locals()
    print(name_dict)
    for key in name_dict.keys():
        if name_dict[key] == hh:
            print(key)
            
haha = 55
get_variable_name(haha)
