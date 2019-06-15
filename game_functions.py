from Country import Country

def country_init_1(x):
    init_input = "请输入" + str(x) + "国的"
    nuclear_lock = input("\n"+ init_input + "核能上限: ")
    ice_lock = input("\n"+ init_input + "可燃冰上限: ")
    creature_lock = input("\n"+ init_input + "生物质能上限: ")
    oil_lock = input("\n" + init_input + "石油上限: ")
    coal_lock = input("\n"+ init_input + "煤上限: ")
    x = Country(nuclear_lock,ice_lock,creature_lock,oil_lock,coal_lock)

def country_init_2():
    global Z
    global M
    global E
    Z = Country(4,6,3,4,3)
    M = Country(4,4,3,6,3)
    E = Country(4,5,2,5,4)

def bout(x):
    print("\n" + str(x) + "国")
    x.deal_with_energy()
    x.show()
    line()

    
