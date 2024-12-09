from pathlib import Path
import time
import re
import itertools

class Node:
    def __init__(self,x,y,freq):
        self.antinode = False
        self.x = x
        self.y = y
        self.freq = freq

def part1(f):
    f.seek(0)
    lines = f.readlines()

    map = []
    freqs = []
    cur_y = 0
    cur_x = 0
    for line in lines:
        map.append([])
        for n in line.strip():
            map[-1].append(Node(x=cur_x,y=cur_y,freq=n))
            if (n not in freqs) and (n != "."):
                freqs.append(n)
            cur_x +=1
        cur_y +=1
        cur_x = 0
    y_lim = len(map)
    x_lim = len(map[0])
    for freq in freqs:
        cords = []
        for row in map:
            for cur_node in row:
                if cur_node.freq == freq:
                    cords.append((cur_node.y, cur_node.x))
        # print(freq, cords)
        for i in itertools.permutations(cords, 2):
            # print(i)
            y_dis = i[0][0] - i[1][0]
            x_dis = i[0][1] - i[1][1]
            # print(y_dis, x_dis)
            anti_y = i[0][0] + y_dis
            anti_x = i[0][1] + x_dis
            if anti_x >= 0 and anti_x < x_lim and anti_y >= 0 and anti_y < y_lim:
                map[anti_y][anti_x].antinode = True
                
    count = 0
    output = ""
    for row in map:
        for n in row:
            if n.antinode:
                count +=1
                output += "#"
            else:
                output += "."
        output += "\n"
    print(output) 
    return count

def part2(f):
    f.seek(0)
    lines = f.readlines()

    map = []
    freqs = []
    cur_y = 0
    cur_x = 0
    for line in lines:
        map.append([])
        for n in line.strip():
            map[-1].append(Node(x=cur_x,y=cur_y,freq=n))
            if (n not in freqs) and (n != "."):
                freqs.append(n)
            cur_x +=1
        cur_y +=1
        cur_x = 0
    y_lim = len(map)
    x_lim = len(map[0])
    for freq in freqs:
        cords = []
        for row in map:
            for cur_node in row:
                if cur_node.freq == freq:
                    cords.append((cur_node.y, cur_node.x))
        # print(freq, cords)
        for i in itertools.permutations(cords, 2):
            print(i)
            y_dis = i[0][0] - i[1][0]
            x_dis = i[0][1] - i[1][1]
            print(y_dis, x_dis)
            anti_y = i[0][0] + y_dis
            anti_x = i[0][1] + x_dis
            while anti_x >= 0 and anti_x < x_lim and anti_y >= 0 and anti_y < y_lim:
                map[anti_y][anti_x].antinode = True
                anti_y += y_dis
                anti_x +=x_dis
    count = 0
    output = ""
    for row in map:
        for n in row:
            if n.antinode or n.freq != ".":
                count +=1
                output += "#"
            else:
                output += "."
        output += "\n"
    print(output) 
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