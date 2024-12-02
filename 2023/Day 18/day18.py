path = "C:\\Directory\\Advent-of-Code\\Day 18\\"
test = open(path + "test.txt", "r")
f = open(path + "input.txt", "r")
f2 = open(path + "output.txt", "w")

t = 0
lines = f.readlines()

t = 1
lines = test.readlines()

# cur_row = 0
# cur_col = 0

# f_right = 0
# f_left = 0
# f_up = 0
# f_down = 0
# for line in lines:
#     toks = line.strip().split(" ")
#     steps = int(toks[2][2:7], 16)
#     dir = int(toks[2][-2])

#     if dir == 0:
#         cur_col += steps
#     if dir == 2:
#         cur_col -= steps
#     if dir == 1:
#         cur_row += steps
#     if dir == 3:
#         cur_row -= steps
    
#     if cur_col < f_left:
#         f_left = cur_col
#     if cur_col > f_right:
#         f_right = cur_col
#     if cur_row < f_up:
#         f_up = cur_col
#     if cur_row > f_down:
#         f_down = cur_col
#     print(dir, steps)

# print(f_up, f_down, f_left,f_right)

map = []
for _ in range(1000):
    print(_)
    list = []
    for _ in range(1000):
        list.append('.')
    map.append(list)

points = []
cur_x = 500
cur_y = 0
for line in lines:
    print(line)
    toks = line.strip().split(" ")
    steps = int(toks[1])
    dir = toks[0]
    first = 0
    # steps = int(toks[2][2:7], 16)
    # dir = int(toks[2][-2])

    if dir == 0:
        while(steps > 0):
            cur_x +=1
            map[cur_y][cur_x] = '#'
            if steps == 1:
                points.append([cur_y,cur_x])
                map[cur_y][cur_x] = '#'
            steps -=1
    if dir == 2:
        while(steps > 0):
            cur_x -=1
            map[cur_y][cur_x] = '#'
            if steps == 1:
                 points.append([cur_y,cur_x])
                 map[cur_y][cur_x] = '#'
            steps -=1
    if dir == 3:
        print("up")
        while(steps > 0):
            cur_y -=1
            map[cur_y][cur_x] = '#'
            if steps == 1:
                points.append([cur_y,cur_x])
                
            steps -=1
    if dir == 1:
        print("down")
        while(steps > 0):
            cur_y +=1
            map[cur_y][cur_x] = '#'
            if steps == 1:
                points.append([cur_y,cur_x])
            steps -=1

for l in map:
    f2.write(str(l))
    f2.write("\n")

def check_cords(row, col):
    cur_row = row
    cur_col = col
    prev_point_x = 500
    prev_point_y = 0
    for point in points:
        if prev_point_x <= cur_col <= point[1] and prev_point_y <= cur_row <= point[0]:
            return 1
        prev_point_x = point[1]
        prev_point_y = point[0]
    count = 0
    while(cur_col > 0):
        cur_col -=1
        prev_point_x = 3029642
        prev_point_y = 0
        for point in points:
            if prev_point_x <= cur_col <= point[1] and prev_point_y <= cur_row <= point[0] and prev_point_y <= cur_row -1 <= point[0]:
                count+=1
            prev_point_x = point[1]
            prev_point_y = point[0]
    if (count % 2) == 0:
        return 0
    # print(row, col)
    return 1
total = 0
for row in range(8800754):
    print(row / 8800754)
    for col in range(14048781):
        print(col/14048781)
        total += check_cords(row,col)
print(total)
