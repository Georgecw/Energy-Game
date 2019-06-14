from Energy import Energy

class Country():

    def __init__(self,He_lock,ice_lock,sun_lock):
        self.gold = 15
        self.energy = 0
        self.pollution = 0
        self.locks = {"He_lock":int(He_lock),"ice_lock":int(ice_lock),
                      "sun_lock":int(sun_lock)}

    def increase(self):
        #每年增加金币
        self.gold += 10

    def energy(self):
        #处理能源带来的各属性变化
        self.power = Energy()
        self.power.build_energy()
        for key,value in self.locks.items():
            kay = key - "_lock"
            if power.built_energy[kay] > value:
                power.built_energy[kay] = value
        for key , value in power.built_energy.item():
            self.gold -= self.power.e_list[key][0]*value
            self.energy += self.power.e_list[key][1]*value
            self.pollution += self.power.e_list[key][2]*value
            
        
        
