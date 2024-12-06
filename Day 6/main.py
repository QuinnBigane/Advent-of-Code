from pathlib import Path
import time

class Node:
    def __init__(self):
        self.visted = False
        self.inf_obs = False
        self.obs = False
        self.N = False
        self.W = False
        self.E = False
        self.S = False

    def reset(self):
        self.N = False
        self.W = False
        self.E = False
        self.S = False

def part1(f):
    f.seek(0)
    lines = f.readlines()

    map = []
    for y in range(len(lines)):
        map.append([])
        for x in range(len(lines[0].strip())):
            map[y].append(Node())
            if lines[y][x] == "^":
                start_x = x
                start_y = y
            if lines[y][x] == "#":
                map[y][x].obs = True
    
    cur_x = start_x
    cur_y = start_y
    direction = "N"
    map[cur_y][cur_x].visted = True
    #start marching
    while 1:
        if direction == "N":
            cur_y-=1
            if cur_y < 0:
                break
            elif map[cur_y][cur_x].obs:
                cur_y +=1
                direction = "E"
            else:
                map[cur_y][cur_x].visted = True
        if direction == "E":
            cur_x+=1
            if cur_x > len(map[0]) - 1:
                break
            elif map[cur_y][cur_x].obs:
                cur_x-=1
                direction = "S"
            else:
                map[cur_y][cur_x].visted = True
        if direction == "S":
            cur_y+=1
            if cur_y > len(map[0]) - 1:
                break
            elif map[cur_y][cur_x].obs:
                cur_y -=1
                direction = "W"
            else:
                map[cur_y][cur_x].visted = True
        if direction == "W":
            cur_x-=1
            if cur_x < 0:
                break
            elif map[cur_y][cur_x].obs:
                cur_x+=1
                direction = "N"
            else:
                map[cur_y][cur_x].visted = True
    
    count = 0
    output = "\n\n"
    for row in map:
        for node in row:
            if node.visted == True:
                count +=1
                output += "X"
            elif node.obs ==True:
                output += "#"
            else:
                output += "."
        output+="\n"
    #print(output)
    return count

def part2(f):
    f.seek(0)
    lines = f.readlines()

    map = []
    for y in range(len(lines)):
        map.append([])
        for x in range(len(lines[0].strip())):
            map[y].append(Node())
            if lines[y][x] == "^":
                start_x = x
                start_y = y
            if lines[y][x] == "#":
                map[y][x].obs = True

    for test_obs_y in range(len(map)):
        for test_obs_x in range(len(map[0])):
            if map[test_obs_y][test_obs_x].obs or (test_obs_y == start_y and test_obs_x == start_x):
                continue
            
            #test adding new obs
            map[test_obs_y][test_obs_x].obs = True
            
            #starting conditions
            for row in map:
                for node in row:
                    node.reset()      
            cur_x = start_x
            cur_y = start_y
            direction = "N"
            map[cur_y][cur_x].n = True

            #start marching
            while 1:
                if direction == "N":
                    cur_y-=1
                    if cur_y < 0:
                        break
                    elif map[cur_y][cur_x].obs:
                        cur_y +=1
                        direction = "E"
                    elif map[cur_y][cur_x].N == True:
                        map[test_obs_y][test_obs_x].inf_obs = True
                        break
                    else:
                        map[cur_y][cur_x].N = True
                if direction == "E":
                    cur_x+=1
                    if cur_x > len(map[0]) - 1:
                        break
                    elif map[cur_y][cur_x].obs:
                        cur_x-=1
                        direction = "S"
                    elif map[cur_y][cur_x].E == True:
                        map[test_obs_y][test_obs_x].inf_obs = True
                        break
                    else:
                        map[cur_y][cur_x].E = True
                if direction == "S":
                    cur_y+=1
                    if cur_y > len(map[0]) - 1:
                        break
                    elif map[cur_y][cur_x].obs:
                        cur_y -=1
                        direction = "W"
                    elif map[cur_y][cur_x].S == True:
                        map[test_obs_y][test_obs_x].inf_obs = True
                        break
                    else:
                        map[cur_y][cur_x].S = True
                if direction == "W":
                    cur_x-=1
                    if cur_x < 0:
                        break
                    elif map[cur_y][cur_x].obs:
                        cur_x+=1
                        direction = "N"
                    elif map[cur_y][cur_x].W == True:
                        map[test_obs_y][test_obs_x].inf_obs = True
                        break
                    else:
                        map[cur_y][cur_x].W = True
            
            map[test_obs_y][test_obs_x].obs = False
    
    count = 0
    for row in map:
        for node in row:
            if node.inf_obs == True:
                count +=1
    return count


if __name__ == "__main__":
    test_file = open(str(Path(__file__).parent) + '\\input_test.txt', "r")
    input_file = open(str(Path(__file__).parent) + '\\input.txt', "r")
    
    p1_test_start = time.time()
    part_1_test = part1(test_file)
    p1_test_end = time.time()

    p2_test_start = time.time()
    part_2_test = part2(test_file)
    p2_test_end = time.time()

    p1_start = time.time()
    part_1_input = part1(input_file)
    p1_end = time.time()

    p2_start = time.time()
    part_2_input = part2(input_file)
    p2_end = time.time()



    print("--- Test File Results ---")
    print("Part 1:", part_1_test, "Runtime:", f"{p1_test_end - p1_test_start:.6f}"+"s")
    print("Part 2:", part_2_test, "Runtime:", f"{p2_test_start - p2_test_start:.6f}"+"s")

    print("--- Input File Results ---")
    print("Part 1:", part_1_input, "Runtime:", f"{p1_end - p1_start:.6f}"+"s")
    print("Part 2:", part_2_input, "Runtime:", f"{p2_end - p2_start:.6f}"+"s")