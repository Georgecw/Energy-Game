class  Energy():

    def __init__(self):
        self.e_list = {'water':[9,2,0,0],'wind':[11,2,0,0],
                  'He':[6,30,3,1],'ice':[8,4,1,1],'sun':[9,3,0,1]}
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
