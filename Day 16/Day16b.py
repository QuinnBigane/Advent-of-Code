import threading
from itertools import permutations
from multiprocessing import Process
f17 = open("C:\\Directory\\Personal\\Advent-of-Code-2022\\Day 16\checkingmywork.txt", "w")
def main_check(start_valve,start_valve2, time, flow, pressure_released, valves, ordered_list,ordered_list2,list_of_valves_to_turn_off, index, index2):
    cur_valve = start_valve
    cur_valve2 = start_valve2
    pressure_released = pressure_released
    time = time
    flow = flow
    valves = valves
    ordered_list = ordered_list
    ordered_list2 =ordered_list2
    list_of_valves_to_turn_off = list_of_valves_to_turn_off
    max_time = 25
    x = 0
    x2 = 0
    i = index
    i2 = index2
    max_cost_ben_name = None
    max_cost_ben_name2 = None
    while time < max_time:
        #print("\ncurrent time: ",time,"\nvalue: ",pressure_released, "\nflow: ", flow)
        if(max_cost_ben_name2 == None and max_cost_ben_name == None):
            if(i2 > len(ordered_list2) - 1) and (i > len(ordered_list) - 1):
                max_presh = 0
                for item in list_of_valves_to_turn_off:
                    if item not in ordered_list2 and item not in ordered_list:
                        check2 = []
                        check = []
                        for x in ordered_list:
                            check.append(x)
                        for x in ordered_list2:
                            check2.append(x)
                        check2.append(item)
                        max_presh = max(main_check(start_valve = cur_valve,start_valve2 =cur_valve2, time = time, flow = flow, pressure_released = pressure_released, valves = valves, ordered_list=check,ordered_list2=check2, list_of_valves_to_turn_off = list_of_valves_to_turn_off, index = i, index2 = i2), max_presh)
                        
                        check2 = []
                        check = []
                        for x in ordered_list:
                            check.append(x)
                        for x in ordered_list2:
                            check2.append(x)
                        check.append(item)
                        max_presh = max(main_check(start_valve = cur_valve,start_valve2 =cur_valve2, time = time, flow = flow, pressure_released = pressure_released, valves = valves, ordered_list=check,ordered_list2=check2, list_of_valves_to_turn_off = list_of_valves_to_turn_off, index = i, index2 = i2), max_presh)
                        item.on = False
                return max_presh
            elif (i2 > len(ordered_list2) - 1):
                max_presh = 0
                for item in list_of_valves_to_turn_off:
                    if item not in ordered_list2 and item not in ordered_list:
                        check2 = []
                        check = []
                        for x in ordered_list:
                            check.append(x)
                        for x in ordered_list2:
                            check2.append(x)
                        check2.append(item)
                        max_presh = max(main_check(start_valve = cur_valve,start_valve2 =cur_valve2, time = time, flow = flow, pressure_released = pressure_released, valves = valves, ordered_list=check,ordered_list2=check2, list_of_valves_to_turn_off = list_of_valves_to_turn_off, index = i, index2 = i2), max_presh)
                        item.on = False
                return max_presh

            elif ((i > len(ordered_list) - 1)):
                max_presh = 0
                for item in list_of_valves_to_turn_off:
                    if item not in ordered_list2 and item not in ordered_list:
                        check2 = []
                        check = []
                        for x in ordered_list:
                            check.append(x)
                        for x in ordered_list2:
                            check2.append(x)
                        check.append(item)
                        max_presh = max(main_check(start_valve = cur_valve,start_valve2 =cur_valve2, time = time, flow = flow, pressure_released = pressure_released, valves = valves, ordered_list=check,ordered_list2=check2, list_of_valves_to_turn_off = list_of_valves_to_turn_off, index = i, index2 = i2), max_presh)
                        item.on = False
                return max_presh

            max_cost_ben_name = ordered_list[i]
            i+=1
            x = cur_valve.distances[max_cost_ben_name.name] 
            max_cost_ben_name2 = ordered_list2[i2]
            i2+=1
            x2 = cur_valve2.distances[max_cost_ben_name2.name] 
        elif(max_cost_ben_name == None):
            if(i > len(ordered_list) - 1):
                max_presh = 0
                for item in list_of_valves_to_turn_off:
                    if item not in ordered_list and item not in ordered_list2:
                        check = []
                        check2=[]
                        for x in ordered_list:
                            check.append(x)
                        for x in ordered_list2:
                            check2.append(x)
                        check.append(item)
                        max_presh = max(main_check(start_valve = cur_valve, start_valve2 =cur_valve2, time = time, flow = flow, pressure_released = pressure_released, valves = valves, ordered_list=check,ordered_list2=check2, list_of_valves_to_turn_off = list_of_valves_to_turn_off, index = i, index2 = i2), max_presh)
                        item.on = False
                return max_presh
            max_cost_ben_name = ordered_list[i]
            i+=1
            x = cur_valve.distances[max_cost_ben_name.name] 
            #print("distance to it is :",x)
        elif(max_cost_ben_name2 == None):
            if(i2 > len(ordered_list2) - 1):
                max_presh = 0
                for item in list_of_valves_to_turn_off:
                    if item not in ordered_list2 and item not in ordered_list:
                        check2 = []
                        check = []
                        for x in ordered_list:
                            check.append(x)
                        for x in ordered_list2:
                            check2.append(x)
                        check2.append(item)
                        max_presh = max(main_check(start_valve = cur_valve,start_valve2 =cur_valve2, time = time, flow = flow, pressure_released = pressure_released, valves = valves, ordered_list=check,ordered_list2=check2, list_of_valves_to_turn_off = list_of_valves_to_turn_off, index = i, index2 = i2), max_presh)
                        item.on = False
                return max_presh
            max_cost_ben_name2 = ordered_list2[i2]
            i2+=1
            x2 = cur_valve2.distances[max_cost_ben_name2.name] 
        time+=1
        if x > 0 and x2 > 0:
            x-=1
            x2-=1
            pressure_released += (flow)
        elif x2 == 0 and max_cost_ben_name2 != None and x == 0 and max_cost_ben_name != None:    
            cur_valve2 = max_cost_ben_name2
            cur_valve2.on = True
            #print(cur_valve.name, " is now open")
            flow += cur_valve2.flow_rate
            max_cost_ben_name2 = None
            cur_valve = max_cost_ben_name
            cur_valve.on = True
            #print(cur_valve.name, " is now open")
            flow += cur_valve.flow_rate
            pressure_released += (flow)
            max_cost_ben_name = None
        elif x == 0 and max_cost_ben_name != None:    
            cur_valve = max_cost_ben_name
            cur_valve.on = True
            #print(cur_valve.name, " is now open")
            flow += cur_valve.flow_rate
            pressure_released += (flow)
            max_cost_ben_name = None

        elif x2 == 0 and max_cost_ben_name2 != None:    
            cur_valve2 = max_cost_ben_name2
            cur_valve2.on = True
            #print(cur_valve.name, " is now open")
            flow += cur_valve2.flow_rate
            pressure_released += (flow)
            max_cost_ben_name2 = None

        else:
            print("errors")
    if pressure_released > 2300:
        for x in ordered_list:
            f17.write(str(x.name))
            f17.write(",")
        f17.write("\n")
        for x in ordered_list2:
            f17.write(str(x.name))
            f17.write(",")
        f17.write("\n")
        f17.write(str(pressure_released))
        f17.write("\n")
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


def threading_func(skip):
    f = open("C:\\Directory\\Personal\\Advent-of-Code-2022\\Day 16\input.txt", "r")
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
    f2 = open("C:\\Directory\\Personal\\Advent-of-Code-2022\\Day 16\output_main_read.txt", "r")
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
    f2.close()
#    for valve in valves:
 #       print(valve.distances)

    passing = skip * 15 * 15 / 2
    max_presh = 0
    time = 0
    flow = 0
    test = 0
    list_of_valves_to_turn_off = []
    pressure_released = 0
    for main_valve in valves:
        if main_valve.name == 'AA':
            for valve in valves:
                if valve.on == False:
                    list_of_valves_to_turn_off.append(valve)
            for item in list_of_valves_to_turn_off:
                check = []
                check.append(item)
                for item2 in list_of_valves_to_turn_off:
                    test +=1
                    if passing > 0:
                        passing -=1
                        continue
                    print(test)
                    check2 = []
                    if item2 not in check:
                        check2.append(item2)
                        max_presh = max(main_check(start_valve = main_valve,start_valve2 = main_valve, time = 0, flow =0, pressure_released = 0, valves = valves, ordered_list=check, ordered_list2 =check2, list_of_valves_to_turn_off = list_of_valves_to_turn_off, index = 0, index2 = 0), max_presh)
                        for valve in valves:
                            if valve.flow_rate > 0:
                                valve.on = False
    print(max_presh)

if __name__ == "__main__":
    P1=Process(target=threading_func, args=(0,))
    P2=Process(target=threading_func, args=(1,))
    P3=Process(target=threading_func, args=(2,))
    P1.start()
    P2.start()
    P3.start()
