from Country import Country
from punishment import random_punishment
from target import random_target

def country_init(x):
    init_input = "请输入" + str(x) + "国的"
    nuclear_lock = input("\n"+ init_input + "核能上限: ")
    ice_lock = input("\n"+ init_input + "可燃冰上限: ")
    creature_lock = input("\n"+ init_input + "生物质能上限: ")
    oil_lock = input("\n" + init_input + "石油上限: ")
    coal_lock = input("\n"+ init_input + "煤上限: ")
    x = Country(nuclear_lock,ice_lock,creature_lock,oil_lock,coal_lock)

def bout(x):
    random_target(x)
    print("")
    x.change_country()
    print("")
    random_punishment(x)
    x.show()
    input("\nPlease Press <enter>")
