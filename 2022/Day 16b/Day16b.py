import threading
from itertools import permutations
def main_check(start_valve, time, flow, pressure_released, valves, ordered_list):
    cur_valve = start_valve
    max_time = 30
    i = 0
    x = 0
    flow = 0
    pressure_released = 0
    time = 0
    max_cost_ben_name = None
    while time < max_time:
        #print("\ncurrent time: ",time,"\nvalue: ",pressure_released, "\nflow: ", flow)
        time+=1
        if(max_cost_ben_name == None):
            if(i > len(ordered_list) - 1):
                print("hit end of list")
                print(max_time - time)
                return pressure_released + (flow * (max_time - time))
            max_cost_ben_name = ordered_list[i]
            i+=1
            x = cur_valve.distances[max_cost_ben_name.name] 
            #print("distance to it is :",x)
        if x > 0:
            x-=1
            pressure_released += (flow)
        elif x == 0 and max_cost_ben_name != None:    
            cur_valve = max_cost_ben_name
            cur_valve.on = True
            #print(cur_valve.name, " is now open")
            flow += cur_valve.flow_rate
            pressure_released += (flow)
            max_cost_ben_name = None
        else:
            print("errors")
            #print("\ncurrent time: ",time,"\nvalue = ",pressure_released, "\nflow", flow)

    return pressure_released


    
class PressureValve:
    def __init__(self, flow_rate, name, neighbors):
        self.flow_rate = flow_rate
        self.name = name
        self.neighbors = neighbors
        self.tunnel = []
        if flow_rate > 0:
            self.on = False
        else:
            self.on = True
        self.distances ={}
    def calculate_distances(self, valves):
        self.distances[self.name] = 0
        for valve in self.tunnel:
            self.distances[valve.name] = 1
        print(self.distances.keys())
        for valve in valves:
            if valve.name not in self.distances.keys():
                self.calculate_distance(start = self, end = valve.name, distance = 0)
    def calculate_distance(self, start, end, distance = 0):
        distance +=1
        if distance > 23:
            return 30000
        if end in self.distances.keys():
            if distance > self.distances[end]:
                return distance
        for valve in start.tunnel:
            if valve.name == end:
                if valve.name in self.distances.keys():
                    self.distances[valve.name] = min(distance, self.distances[valve.name])
                    valve.distances[self.name] = min(distance, self.distances[valve.name])
                else:
                    self.distances[valve.name] = distance
                    valve.distances[self.name] = distance
                return
            else:
                self.calculate_distance(start= valve, end = end, distance = distance)
        return




if __name__ == "__main__":
    f = open("C:\\Directory\\Advent-of-Code-2022\\Day 16\input.txt", "r")
    valves=[]
    for line in f.readlines():
        toks = line.strip().split(" ")
        name = toks[1]
        flow_rate = int(toks[4][5:len(toks[4])-1])
        neighbors = []
        for i in range(len(toks)):
            if i > 8: 
                neighbors.append((toks[i][:2]))

        valves.append(PressureValve(flow_rate=flow_rate,name=name,neighbors=neighbors))



    f.close()
    for cur_valve in valves:
        for neighbor in cur_valve.neighbors:
            for valve in valves:
                if valve.name == neighbor:
                    cur_valve.tunnel.append(valve)

    """
    for valve in valves:
        valve.calculate_distances(valves)
        print(valve.name)
        print(valve.distances)
        if (len(valves) != len(valve.distances)):
            print("Error Error")
            break
        print('\n')

    f2 = open("C:\\Directory\\Advent-of-Code-2022\\Day 16\output_main_read.txt", "w")
    for valve in valves:
        f2.write(valve.name)
        f2.write('\n')
        string = str(valve.distances)
        f2.write(string[1:len(string)-1])
        f2.write('\n')

    f2.close()
    """
    f2 = open("C:\\Directory\\Advent-of-Code-2022\\Day 16\output_main_read.txt", "r")
    name = None
    for line in f2.readlines():
        if name == None:
            name = line.strip()
        else:
            for valve in valves:
                if valve.name == name:
                    toks = line.strip().split(" ")
                    dist_name = None
                    for tok in toks:
                        if dist_name == None:
                            dist_name = tok[1:3]
                        else:
                            valve.distances[dist_name] = int(tok[:len(tok)-1])
                            dist_name = None
                            
            name = None

#    for valve in valves:
 #       print(valve.distances)
    max_presh = 0
    time = 0
    flow = 0
    list_of_valves_to_turn_off = []
    pressure_released = 0
    for main_valve in valves:
        if main_valve.name == 'AA':
            for valve in valves:
                if valve.on == False:
                    list_of_valves_to_turn_off.append(valve)
            test = list(permutations(list_of_valves_to_turn_off, len(list_of_valves_to_turn_off)- 6))
            max_test = len(test)
            tested = 0
            for check in test:
                if((tested/max_test) * 100 % 10 == 0):
                    print(tested/max_test)
                max_presh = max(main_check(start_valve = main_valve, time = 0, flow =0, pressure_released = 0, valves = valves, ordered_list=check), max_presh)
                tested+=1
                for valve in valves:
                    if valve.flow_rate > 0:
                        valve.on = False
    print(max_presh)
