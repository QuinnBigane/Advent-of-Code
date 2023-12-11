path = "C:\\Directory\\Advent-of-Code\\Day 11\\"
f = open(path + "input.txt", "r")
f2 = open(path + "output.txt", "w")
lines = f.readlines()


class Galaxy:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.shortest_pathes = {}
        self.others = {}
    def find_shortest_path(self):
        for key in self.shortest_pathes:
            if self.shortest_pathes[key] == None:
                print(key)
                steps = 0
                cur_x = self.x
                cur_y = self.y
                end_x = self.others[key].x
                end_y = self.others[key].y
                while(cur_y != end_y or cur_x != end_x):
                    if real_galaxy[cur_x][cur_y] == '-':
                        stepsize = 999999
                    else:
                        stepsize = 1
                    if cur_y > end_y:
                        #minus y
                        steps+=stepsize
                        cur_y -=1
                    elif cur_y < end_y:
                        #plus y
                        steps+=stepsize
                        cur_y +=1
                    elif cur_x < end_x:
                        #plus x
                        steps+=stepsize
                        cur_x +=1
                    elif cur_x > end_x:
                        #minus x
                        steps+=stepsize
                        cur_x -=1
                self.shortest_pathes[key] = steps
                #adding 0 to others so it doesnt count twice, but could add here if it helps for part 2
                self.others[key].shortest_pathes[self.id]=0

real_galaxy = []
for row in range(len(lines)):
    real_galaxy.append(lines[row])
    if '#' not in lines[row]:
        #print(row)
        real_galaxy.append("--------------------------------------------------------------------------------------------------------------------------------------------\n")
        #real_galaxy.append("----------\n")

temp_galazy = []
for row in real_galaxy:
    temp_galazy.append(row)

count = 0
for col in range(len(lines[0].strip())):
    flag = 1
    for row in range(len(temp_galazy)):
        if temp_galazy[row][col] == '#':
            flag = 0
    if flag:
        #print(col)
        for row in range(len(temp_galazy)):
            real_galaxy[row] = real_galaxy[row][:col+count] + "-" + real_galaxy[row][col+count:]
        count +=1

for line in real_galaxy:
    f2.write(line)

galaxies = {}
id = 0
for row in range(len(real_galaxy)):
    for col in range(len(real_galaxy[row])):
        if real_galaxy[row][col] == '#':
            galaxies[id] = Galaxy(id,row,col)
            id+=1

for key in galaxies:
    for i in range(id):
        galaxies[key].shortest_pathes[i] = None
        galaxies[key].others = galaxies

for key in galaxies:
    print("ID: ", key)
    galaxies[key].find_shortest_path()

total = 0
for main in galaxies:
    for key in galaxies:
        total += galaxies[main].shortest_pathes[key]
print(total)

#too low 159730955545