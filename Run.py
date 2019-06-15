from Energy import Energy
from Country import Country
from game_functions import *
from punishment import *

line = lambda : print("----------------------------------------")
year = 0
while True:
    year += 1
    Z = Country(4,6,3,4,3)
    M = Country(4,4,3,6,3)
    E = Country(4,5,2,5,4)
    Z.increase()
    M.increase()
    E.increase()
    print("第" + str(year) + "年")
    line()
    if year%2 == 1:
        print("Z国")
        Z.deal_with_energy()
        ramdom_punishment(Z)
        Z.show()
        line()
        print("M国")
        M.deal_with_energy()
        ramdom_punishment(M)
        M.show()
        line()
        print("E国")
        E.deal_with_energy()
        ramdom_punishment(E)
        E.show()
        line()
    input("Please Press <enter>")
