from Energy import Energy
from Country import Country
from game_functions import *

line= lambda : print("----------------------------------------")
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
    for i in [Z,M,E]:
        bout(i)
    input("Please Press <enter>")
