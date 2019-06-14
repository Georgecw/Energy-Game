class  Energy():

    def __init__(self):
        self.e_list = {"water":[15,9,0,0],"sea":[8,6,0,0],
                        "He":[12,36,8,1],"ice":[4,8,1,1],"creature":[1,1,2,1],
                        "oil":[5,10,2,1],"coal":[2,2,3,1]}
        self.built_list = {}

    def build_energy(self):
        #建造能源
        while True:
            self.i_energy = input('请输入要建造的能源: ')
            if self.i_energy == 'exit':
                break
            else:
                try:
                    self.built_list[self.i_energy] += 1
                except KeyError:
                    self.built_list[self.i_energy] = 1
            for key in self.built_list.keys():
                if self.e_list[key][3] == 0:
                    self.built_list[key] = 1
