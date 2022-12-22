import threading

def main_check(start_valve, time, flow, pressure_released, valves):
    highest_pressure_released = 0
    if time > 30:
        return pressure_released
    
    if start_valve.flow_rate > 0 and start_valve.on == False:
        print(start_valve.flow_rate)
        time +=1
        pressure_released += flow
        flow += start_valve.flow_rate
        start_valve.on = True
    pressure_released += flow
    time += 1
    for tunnel in start_valve.tunnel:
        for valve in valves:
            valve.on = False
        print("hit")
        press_rel = main_check_helper(tunnel, time, flow, pressure_released, prev_tunnel= start_valve.name, valves=valves)
        if press_rel > highest_pressure_released:
            highest_pressure_released = press_rel
    return highest_pressure_released

def main_check_helper(start_valve, time, flow, pressure_released, prev_tunnel, valves):
    if time < 5:
        print(time)
    highest_pressure_released = 0
    if time > 30:
        return pressure_released
    
    if start_valve.flow_rate > 0 and start_valve.on == False:
        time +=1
        pressure_released += flow
        flow += start_valve.flow_rate
        start_valve.on = True
    pressure_released += flow
    time += 1
    test = 0
    for valve in valves:
        if valve.on == False:
            test +=1
    if(test > 0):
        for tunnel in start_valve.tunnel:
            press_rel = main_check_helper(tunnel, time, flow, pressure_released, prev_tunnel=start_valve.name, valves = valves)
            if press_rel > highest_pressure_released:
                highest_pressure_released = press_rel
        return highest_pressure_released
    else:
        return pressure_released + (flow * (30 - time))

    
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


if __name__ == "__main__":
    f = open("C:\\Directory\\Advent-of-Code-2022\\Day 16\input2.txt", "r")
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
    for cur_valve in valves:
        for neighbor in cur_valve.neighbors:
            for valve in valves:
                if valve.name == neighbor:
                    cur_valve.tunnel.append(valve)

    time = 0
    flow = 0
    pressure_released = 0
    for valve in valves:
        if valve.name == 'AA':
            print(main_check(start_valve = valve, time = 0, flow =0, pressure_released = 0, valves = valves))

