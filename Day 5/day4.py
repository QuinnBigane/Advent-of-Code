import keyboard
from pynput.keyboard import Key, Controller

path = "C:\\Directory\\Advent-of-Code\\Day 5\\"
f = open(path + "input.txt", "r")

lines = f.readlines()

min = 0

class Seed:
    def __init__(self,seed):
        self.factors = []
        self.factors.append(seed)

class Seed2:
    def __init__(self,start, end):
        self.start = start
        self.end = start + end

class Map:
    def __init__(self,id):
        self.id = id
        self.destinations = []
        self.sources = []
        self.ranges = []

seeds = []
# source = None
# destination = 'seeds'
cur_factors = 0
for line in lines:
    if len(seeds) == 0:
        for tk in line.split()[1:]:
            #seeds.append(Seed(int(tk)))
            seeds.append(Seed(3267749434))
        continue
    toks = line.strip().split()
    if(len(toks) == 2):
        # source = destination
        destination = toks[0].split('-')[2]
        cur_factors +=1
        print(destination)
        for seed in seeds:
            seed.factors.append(seed.factors[-1])
    elif(len(toks) == 3):
        for seed in seeds:
            #check edge cases of range function
            if seed.factors[cur_factors  - 1] in range(int(toks[1]), int(toks[1])+int(toks[2])):
                #print(range(int(toks[1]), int(toks[1])+int(toks[2])))
                #print(int(toks[1]) in range(int(toks[1])+int(toks[2]), int(toks[1])+int(toks[2])))
                seed.factors[cur_factors] = (seed.factors[cur_factors - 1] + (int(toks[0]) - int(toks[1])))
            else:
                pass

low_loc = 10000000000000000000000000
for seed in seeds:
    if seed.factors[-1] < low_loc:
        low_loc = seed.factors[-1]
print("part 1: " + str(low_loc) + "\n\n")



maps = []

#get conversion factors 
for line in lines:
    toks = line.strip().split()
    if(len(toks) == 2):
        maps.append(Map(id=toks[0]))
    elif(len(toks) == 3):
        maps[-1].destinations.append(int(toks[0]))
        maps[-1].sources.append(int(toks[1]))
        maps[-1].ranges.append(int(toks[2]))

#get all seed values
seeds = []
for line in lines:
    if seeds == []:
        tks = line.strip().split()
        for x in range(1, 20, 2):
        #for x in range(1, 4, 2):
            seeds.append(Seed2(int(tks[x]), int(tks[x+1])))
#(0 to 31000000)
#3267749434 too high
closest_seed = -1
location = 29161857
while closest_seed == -1:
    #propogate through location value to seed
    tmp_location = location
    for map in reversed(maps):
        #print("did map" , map.id)
        for x in range(len(map.destinations)):
            # print("did range check")
            #if tmp_location in range(map.destinations[x], map.destinations[x] + map.ranges[x]):
            if map.destinations[x] <= tmp_location < map.destinations[x] + map.ranges[x]:
                tmp_location += map.sources[x] - map.destinations[x]
                # print(tmp_location, map.sources[x], map.destinations[x])
                break
    #print(tmp_location)
    #closest_seed = 0            
    #check if seed in init
    for seed in seeds:
        if seed.start <= tmp_location < seed.end:
            closest_seed = tmp_location
    #increment location value
    location +=1
    if location % 1000000 == 0:
        print(location, tmp_location)


print("part 2: " + str(closest_seed) +" " + str(location - 1))