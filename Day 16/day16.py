path = "C:\\Directory\\Advent-of-Code\\Day 16\\"
test = open(path + "test.txt", "r")
f = open(path + "input.txt", "r")
f2 = open(path + "output.txt", "w")

t = 0
lines = f.readlines()

# t = 1
# lines = test.readlines()


class Node:
    def __init__(self):
        self.val = '.'
        self.directions = []
map = []
for line in lines:
    map.append(list(line.strip()))

def beam(start_row, start_col, start_direction):
    #while this beam is in bound
    cur_row = start_row
    cur_col = start_col
    if start_direction == 'N':
        cur_row -=1

    if start_direction == 'S':
        cur_row +=1

    if start_direction == 'E':
        cur_col +=1

    if start_direction == 'W':
        cur_col -=1
    while(cur_row >= 0 and cur_row < len(map) and cur_col >= 0 and cur_col < len(map[0])):
        # print(start_row,start_col,start_direction)
        if energized_map[cur_row][cur_col].val == '#':
            if start_direction in energized_map[cur_row][cur_col].directions:
                # print(start_direction)
                return
            else:
                energized_map[cur_row][cur_col].directions.append(start_direction)
        else: 
            energized_map[cur_row][cur_col].val = '#'
            energized_map[cur_row][cur_col].directions.append(start_direction)
        if start_direction == 'N':
            if map[cur_row][cur_col] == "\\":
                beam(cur_row, cur_col, 'W')
                return
            if map[cur_row][cur_col] == "/":
                beam(cur_row, cur_col, 'E')
                return
            if map[cur_row][cur_col] == "-":
                beam(cur_row, cur_col, 'W')
                beam(cur_row, cur_col, 'E')
                return
        if start_direction == 'S':
            if map[cur_row][cur_col] == "\\":
                beam(cur_row, cur_col, 'E')
                return
            if map[cur_row][cur_col] == "/":
                beam(cur_row, cur_col, 'W')
                return
            if map[cur_row][cur_col] == "-":
                beam(cur_row, cur_col, 'W')
                beam(cur_row, cur_col, 'E')
                return
        if start_direction == 'E':
            if map[cur_row][cur_col] == "\\":
                beam(cur_row, cur_col, 'S')
                return
            if map[cur_row][cur_col] == "/":
                beam(cur_row, cur_col, 'N')
                return
            if map[cur_row][cur_col] == "|":
                beam(cur_row, cur_col, 'N')
                beam(cur_row, cur_col, 'S')
                return
        if start_direction == 'W':
            if map[cur_row][cur_col] == "\\":
                beam(cur_row, cur_col, 'N')
                return
            if map[cur_row][cur_col] == "/":
                beam(cur_row, cur_col, 'S')
                return
            if map[cur_row][cur_col] == "|":
                beam(cur_row, cur_col, 'N')
                beam(cur_row, cur_col, 'S')
                return
        if start_direction == 'N':
            cur_row -=1

        if start_direction == 'S':
            cur_row +=1

        if start_direction == 'E':
            cur_col +=1

        if start_direction == 'W':
            cur_col -=1
    return   





max = 0

for x in range(len(map)):
    print(x/len(map))
    energized_map = []
    for row in range(len(map)):
        energized_map.append([])
        for col in range(len(map[0])):
            energized_map[-1].append(Node())

    # energized_map[0][0].val = '#'
    beam(x,-1,'E')

    total = 0
    for line in energized_map:
        for node in line:
            # f2.write(node.val)
            if node.val == '#':
                total+=1
        # f2.write('\n')
    if total > max:
        max = total

for x in range(len(map)):
    print(x/len(map))
    energized_map = []
    for row in range(len(map)):
        energized_map.append([])
        for col in range(len(map[0])):
            energized_map[-1].append(Node())

    # energized_map[0][0].val = '#'
    beam(x,len(map[0]),'W')

    total = 0
    for line in energized_map:
        for node in line:
            # f2.write(node.val)
            if node.val == '#':
                total+=1
        # f2.write('\n')
    if total > max:
        max = total
for x in range(len(map[0])):
    print(x/len(map[0]))
    energized_map = []
    for row in range(len(map)):
        energized_map.append([])
        for col in range(len(map[0])):
            energized_map[-1].append(Node())

    # energized_map[0][0].val = '#'
    beam(-1,x,'S')

    total = 0
    for line in energized_map:
        for node in line:
            # f2.write(node.val)
            if node.val == '#':
                total+=1
        # f2.write('\n')
    if total > max:
        max = total
for x in range(len(map[0])):
    print(x/len(map[0]))
    energized_map = []
    for row in range(len(map)):
        energized_map.append([])
        for col in range(len(map[0])):
            energized_map[-1].append(Node())

    # energized_map[0][0].val = '#'
    beam(len(map),x,'N')

    total = 0
    for line in energized_map:
        for node in line:
            # f2.write(node.val)
            if node.val == '#':
                total+=1
        # f2.write('\n')
    if total > max:
        max = total
print(max)