path = "C:\\Directory\\Advent-of-Code\\Test\\"
f = open(path + "input.txt", "r")

class Map():
    def __init__(self):
        self.des = []
        self.src = []
        self.rng = []
class Seed():
    def __init__(self, start, end):
        self.start = start
        self.end = start+ end
lines = f.readlines()

seeds = []
maps = []
for line in lines:
    tks = line.strip().split()
    if seeds == []:
        for i in range(1, 21, 2):
            seeds.append(Seed(int(tks[i]), int(tks[i+1])))
    
    else:
        if len(tks) == 2:
            maps.append(Map())
        if len(tks) == 3:
            maps[-1].des.append(int(tks[0]))
            maps[-1].src.append(int(tks[1]))
            maps[-1].rng.append(int(tks[2]))


location = 0
lowest_location = -1
while(lowest_location < 0):
    #propogate backwards
    loc_location = location
    for map in reversed(maps):
        for x in range(len(map.des)):
            if map.des[x] <= loc_location < map.des[x] + map.rng[x]:
                loc_location += (map.src[x] - map.des[x])
                break
    for seed in seeds:
        if seed.start <= loc_location < seed.end:
            lowest_location = loc_location
    location +=1
    if (location % 100000) == 0:
        print(location)

print(lowest_location)