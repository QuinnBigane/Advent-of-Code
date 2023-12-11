path = "C:\\Directory\\Advent-of-Code\\Day 8\\"
f = open(path + "input.txt", "r")
"""
lines = f.readlines()

class Node():
    def __init__(self,n, l, r):
        self.name = n
        self.left = l
        self.right = r

leftrights = None
nodes = []
for line in lines:
    if leftrights == None:
        leftrights = line.strip()
    else:
        if(len(line) > 4):
            nodes.append(Node(line.strip()[0:3],line.strip()[7:10],line.strip()[12:15]))
starts = []
#link the nodes
for n in nodes:
    if n.name[2] == 'A':
        starts.append(n)
    for x in nodes:
        if x.name == n.left:
            n.left = x
        if x.name == n.right:
            n.right = x
steps_arr = []           
local = starts
# local = []
# for n in nodes:
#     if n.name == 'AAA':
#         local.append(n)
steps = 0
flag = 1
for start in starts:
    print(start.name)
count = 0
while(flag):
    for i in leftrights:
        # if steps % 100000 == 0:
        #     print("steps: ", steps)
        new_locals = []
        steps +=1
        for l in local:
            if type(l) == type(int()):
                print("hit")
                continue
            if i == 'L':
                new_locals.append(l.left)
            elif i == 'R': 
                new_locals.append(l.right)
            else:
                print("error")
        local = new_locals
        new_locals = []
        count = 0
        for x in range(len(local)):
            if local[x].name[2] == 'Z':
                count +=1
                print(x, steps)
            new_locals.append(local[x])
        local = new_locals
        if count > 3:
            print(count)
        if count == len(local):
            flag = 0
            print(steps)
            for l in local:
                print(l.name)
"""
steps_arr = [12599,17287,17873,19631,20803,21389]
totals = [0,0,0,0,0,0] 
print(steps_arr)
min_x = 0
count = 15746133679061
max1 = (steps_arr[0] *steps_arr[1]*steps_arr[2]*steps_arr[3]*steps_arr[4]*steps_arr[5]) / 293
print(max1)
max = (steps_arr[0] *steps_arr[1]*steps_arr[2]*steps_arr[3]*steps_arr[4]*steps_arr[5])
print(max)
while(1):
    if count > max:
        print("error")
        break
    if ((count % steps_arr[0]) == 0 and 
        (count %steps_arr[1]) == 0 and
        (count %steps_arr[2]) == 0 and
        (count %steps_arr[3]) == 0 and
        (count %steps_arr[4]) == 0 and
        (count %steps_arr[5]) == 0):
        print(count)
        break
    count +=steps_arr[0]
    #print(count/max)116049805134016600000000
    #              34002592904266863793513273