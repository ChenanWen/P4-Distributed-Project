import math

#Generate Classes
###########################################
class Switch:

    busyness = 0
    initial_busyness = 0
    workload = 0
    excepted_load = 0
    path = []

    def __init__(self, name):
        self.name = name

    def printself(self):
        print("     Switch:", self.name)
        #print("     excepted_load:", self.excepted_load)
        print("     workload:", self.workload)
        print("     initial_busyness:",self.initial_busyness)
        print("     busyness:", self.busyness)
        print("     for each path:", self.path)


class Path:

    unarranged_flow = 0
    path_id = 0

    def __init__(self,name,flow,nodes):
        self.name = name
        self.flow = flow
        self.nodes = nodes

    def load(self):
        minbusy = min(self.nodes, key=lambda x: x.busyness)
        maxbusy = max(self.nodes, key=lambda x: x.busyness)
        if self.unarranged_flow > 0:
            minbusy = min(self.nodes, key=lambda x: x.busyness)
            self.unarranged_flow += -minbusy.excepted_load
            #minbusy.
            minbusy.workload += minbusy.excepted_load
            minbusy.path[self.path_id] += minbusy.excepted_load
            for i in self.nodes:
                if i != minbusy:
                    i.busyness += -minbusy.excepted_load
        #elif self.unarranged_flow ==0 and minbusy.workload = maxbusy.workload:
        #elif self.unarranged_flow ==0 and maxbusy.workload >= 2*minbusy.workload:
        elif self.unarranged_flow ==0 and maxbusy.path[self.path_id]>minbusy.excepted_load: #Terminate condition
            minbusy.workload += minbusy.excepted_load
            minbusy.path[self.path_id] += minbusy.excepted_load
            minbusy.busyness += minbusy.excepted_load
            maxbusy.workload += -minbusy.excepted_load
            maxbusy.path[self.path_id] += -minbusy.excepted_load
            maxbusy.busyness += -minbusy.excepted_load

    def printself(self):
        print("Path:",self.name)
        print("total workload:",self.flow)
        print("unarranged workload", self.unarranged_flow)
    

class Network:

    excepted_load = 0

    def __init__(self,topology):
        self.topology = topology

    def initialize(self):
        number_of_switches = 0
        total_flow = 0
        total_nodes = []
        path_id = 0
        for i in self.topology:
            i.path_id = path_id
            path_id += 1
            i.unarranged_flow = i.flow
            total_flow += i.flow
            for j in i.nodes:
                if j not in total_nodes:
                    j.path = [0]*len(self.topology)
                    number_of_switches += 1 
                total_nodes.append(j)
        self.excepted_load = math.floor(total_flow/number_of_switches)
        for i in self.topology:
            for j in i.nodes:
                j.busyness += i.flow
                j.initial_busyness = j.busyness
                j.excepted_load = self.excepted_load

    def loadbalance(self):
        for j in range(10):
            for i in self.topology:
                i.load();
            

    def printall(self):
        for i in self.topology:
            i.printself()
            for j in i.nodes:
                j.printself()



#Network Configuration
switch_a = Switch("a")
switch_b = Switch("b")
switch_c = Switch("c")
switch_d = Switch("d")
switch_e = Switch("e")
switch_f = Switch("f")
switch_g = Switch("g")
switch_h = Switch("h")
path_0 = Path("path_0",100,[switch_a,switch_b,switch_c,switch_d])
path_1 = Path("path_1",300,[switch_a,switch_e,switch_g,switch_h])
path_2 = Path("path_2",400,[switch_f,switch_g,switch_e,switch_c,switch_d])
net = Network([path_0,path_1,path_2])

#Network Initialize
net.initialize()
net.printall()

#Global Load Balance
net.loadbalance()
print("LOAD###############################################")
net.printall()
