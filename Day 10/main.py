from pathlib import Path
import time
import re
import itertools

class Node:
    def __init__(self, val):
        self.val = val
        self.visited = False
        self.visit_count = 0
    
def check_sur(map, cur_y, cur_x):
    ans = 0
    map[cur_y][cur_x].visited = True
    if cur_x > 0:
        if (map[cur_y][cur_x - 1].val - map[cur_y][cur_x].val == 1) and map[cur_y][cur_x - 1].visited == False:
            if map[cur_y][cur_x - 1].val == 9:
                ans +=1
                map[cur_y][cur_x - 1].visited = True
            ans += check_sur(map, cur_y, cur_x - 1)
    if cur_y > 0:
        if (map[cur_y - 1][cur_x].val - map[cur_y][cur_x].val == 1) and map[cur_y - 1][cur_x].visited == False:
            if map[cur_y - 1][cur_x].val == 9:
                ans +=1
                map[cur_y - 1][cur_x].visited = True
            else:
                ans += check_sur(map, cur_y - 1, cur_x)
    if cur_x < len(map[0]) - 1:
        if (map[cur_y][cur_x + 1].val - map[cur_y][cur_x].val == 1) and map[cur_y][cur_x + 1].visited == False:
            if map[cur_y][cur_x + 1].val == 9:
                ans +=1
                map[cur_y][cur_x + 1].visited = True
            else:
                ans += check_sur(map, cur_y, cur_x + 1)
    if cur_y < len(map) - 1:
        if (map[cur_y + 1][cur_x].val - map[cur_y][cur_x].val == 1) and map[cur_y + 1][cur_x].visited == False:
            if map[cur_y + 1][cur_x].val == 9:
                ans +=1
                map[cur_y + 1][cur_x].visited = True
            else:
                ans += check_sur(map, cur_y + 1, cur_x)
    return ans

def check_sur2(map, cur_y, cur_x):
    if cur_x > 0:
        if (map[cur_y][cur_x - 1].val - map[cur_y][cur_x].val in [1]):
            if map[cur_y][cur_x - 1].val == 9:
                map[cur_y][cur_x - 1].visit_count +=1
            check_sur2(map, cur_y, cur_x - 1)
    if cur_y > 0:
        if (map[cur_y - 1][cur_x].val - map[cur_y][cur_x].val in [1]):
            if map[cur_y - 1][cur_x].val == 9:
                map[cur_y - 1][cur_x].visit_count +=1
            check_sur2(map, cur_y - 1, cur_x)
    if cur_x < len(map[0]) - 1:
        if (map[cur_y][cur_x + 1].val - map[cur_y][cur_x].val in [1]):
            if map[cur_y][cur_x + 1].val == 9:
                map[cur_y][cur_x + 1].visit_count +=1
            check_sur2(map, cur_y, cur_x + 1)
    if cur_y < len(map) - 1:
        if (map[cur_y + 1][cur_x].val - map[cur_y][cur_x].val in [1]):
            if map[cur_y + 1][cur_x].val == 9:
                map[cur_y + 1][cur_x].visit_count +=1
            check_sur2(map, cur_y + 1, cur_x)
    return 

def part1(f):
    f.seek(0)
    lines = f.readlines()

    map = []
    for line in lines:
        map.append([Node(int(n)) for n in line.strip()])
    
    y_lim = len(map)
    x_lim = len(map[0])

    trail_heads = []
    for y in range(y_lim):
        for x in range(x_lim):
            if map[y][x].val == 0:
                trail_heads.append((y,x))

    total = 0
    for trail_head in trail_heads:
        check2 = 0
        check1 = check_sur(map, trail_head[0], trail_head[1])
        #total += tmp
        #reset the map
        output = ""
        for row in map:  
            output += "\n"  
            for n in row:
                if n.visited:
                    if n.val == 9:
                        check2 +=1
                    output += str(n.val)
                else:
                    output += "."
                n.visited = False
        total += check1
        # if check1 != check2:
        #     print(total)
        #     print(output, "\n\n")
        # print(check1, check2)
        # print(output, "\n\n")
    return total

def part2(f):
    f.seek(0)
    lines = f.readlines()

    map = []
    for line in lines:
        map.append([Node(int(n)) for n in line.strip()])
    
    y_lim = len(map)
    x_lim = len(map[0])

    trail_heads = []
    for y in range(y_lim):
        for x in range(x_lim):
            if map[y][x].val == 0:
                trail_heads.append((y,x))

    total = 0
    for trail_head in trail_heads:
        ans = 0
        check_sur2(map, trail_head[0], trail_head[1])
        output = ""
        for row in map:  
            output += "\n"  
            for n in row:
                if n.val == 9:
                    ans += n.visit_count
                    n.visit_count = 0
                    output += str(n.val)
                else:
                    output += "."
        total += ans
        #print(ans, total)
    return total


if __name__ == "__main__":
    test_file = open(str(Path(__file__).parent) + '\\input_test.txt', "r")
    input_file = open(str(Path(__file__).parent) + '\\input.txt', "r")
    
    p1_test_start = time.perf_counter()
    part_1_test = part1(test_file)
    p1_test_end = time.perf_counter()

    p2_test_start = time.perf_counter()
    part_2_test = part2(test_file)
    p2_test_end = time.perf_counter()

    p1_start = time.perf_counter()
    part_1_input = part1(input_file)
    p1_end = time.perf_counter()

    p2_start = time.perf_counter()
    part_2_input = part2(input_file)
    p2_end = time.perf_counter()



    print("--- Test File Results ---")
    print("Part 1:", part_1_test, "Runtime:", f"{p1_test_end - p1_test_start:.6f}"+"s")
    print("Part 2:", part_2_test, "Runtime:", f"{p2_test_start - p2_test_start:.6f}"+"s")

    print("--- Input File Results ---")
    print("Part 1:", part_1_input, "Runtime:", f"{p1_end - p1_start:.6f}"+"s")
    print("Part 2:", part_2_input, "Runtime:", f"{p2_end - p2_start:.6f}"+"s")