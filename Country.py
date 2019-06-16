from Energy import Energy

class Country():

    def __init__(self,nuclear_lock,ice_lock,creature_lock,oil_lock,coal_lock):
        self.gold = 15
        self.energy = 0
        self.pollution = 0
        self.locks = {"nuclear":int(nuclear_lock),"ice":int(ice_lock),
                      "creature":int(creature_lock),"coal":int(coal_lock),
                      "oil":int(oil_lock)}
        self.power = Energy()

    def increase(self):
        #每年增加金币
        self.gold += 10

    def change_country(self):
        #处理能源带来的各属性变化
        for key , value in self.power.built_list.items():
            if self.power.e_list[key][3] == 1:
                self.gold -= self.power.e_list[key][0]*value
                self.energy += self.power.e_list[key][1]*value
                self.pollution += self.power.e_list[key][2]*value
            else:
                self.energy +=self.power.e_list[key][1]
                self.pollution += self.power.e_list[key][2]

    def deal_with_energy(self):
        self.power.build_energy()
        for key,value in self.locks.items():
            try:
                if self.power.built_list[key] > value:
                    self.power.built_list[key] = value
                    print("\n某能源数量超出上限，超出上限部分不产能")
            except KeyError:
                self.power.built_list[key] = 0
        for key , value in self.power.built_list.items():
            if self.power.e_list[key][3] == 1:
                self.gold -= self.power.e_list[key][0]*value
                self.energy += self.power.e_list[key][1]*value
                self.pollution += self.power.e_list[key][2]*value
            else:
                self.energy +=self.power.e_list[key][1]
                self.pollution += self.power.e_list[key][2]

    def show(self):
        print("\n能量总产量：" + str(self.energy) + "KJ")
        print("\n金币剩余: " + str(self.gold) + "G")
        print("\n污染情况：" + str(self.pollution) + "平方千米")

    def del_energy(self):
        for key in self.power.built_list.keys():
            if self.power.e_list[key][3] == 1:
                self.power.built_list[key] = 0
        
