from Country import Country
from game_functions import *

line = lambda : print("----------------------------------------")
year = 0
Z = Country(4,6,3,4,3)
M = Country(4,4,3,6,3)
E = Country(4,5,2,5,4)
while True:
    year += 1
    Z.increase()
    M.increase()
    E.increase()
    print("第" + str(year) + "年")
    line()
    if year%2 == 1:
        print("Z国")
        bout(Z)
        line()
        print("M国")
        bout(M)
        line()
        print("E国")
        bout(E)
        line()
    elif year%2 == 0:
        for i in [Z,M,E]:
            i.change_country()
            i.del_energy()
    
