from pathlib import Path
import time
import re
import itertools

class Node():
    def __init__ (self, id = None):
        if id == None:
            self.id = "."
        else:
            self.id = id
    def __str__(self):
        return str(self.id)

def part1(f):
    f.seek(0)
    lines = f.readlines()
    line = lines[0].strip()

    expanded_file = []
    cur_id = 0
    is_empty = False
    for c in line:
        if is_empty:
            for _ in range(int(c)):
                expanded_file.append(Node())
            is_empty = False
        else:
            for _ in range(int(c)):
                expanded_file.append(Node(cur_id))
            cur_id +=1
            is_empty = True

    # output = ""
    # for node in expanded_file:
    #     output += str(node)
    # print(output)
    last_empty = 0
    for i1 in reversed(range(len(expanded_file))):
        if expanded_file[i1].id != ".":
            first_empty_index = len(expanded_file)
            for i2 in range(last_empty,len(expanded_file)):
                if expanded_file[i2].id == ".":
                    first_empty_index = i2
                    break
            if first_empty_index > i1:
                #fully sorted
                break
            else:
                expanded_file[first_empty_index].id = expanded_file[i1].id
                expanded_file[i1].id = "."
                #this is a huge optimization 
                last_empty = first_empty_index

    # output = ""
    # for node in expanded_file:
    #     output += str(node)
    # print(output)

    ans = 0
    for i in range(len(expanded_file)):
        if expanded_file[i].id != '.':
            ans += (i * int(expanded_file[i].id))

    return ans

def part2(f):
    f.seek(0)
    lines = f.readlines()
    line = lines[0].strip()

    expanded_file = []
    cur_id = 0
    is_empty = False
    for c in line:
        if is_empty:
            for _ in range(int(c)):
                expanded_file.append(Node())
            is_empty = False
        else:
            for _ in range(int(c)):
                expanded_file.append(Node(cur_id))
            cur_id +=1
            is_empty = True

    # output = ""
    # for node in expanded_file:
    #     output += str(node)
    # print(output)

    last_id = None
    for i1 in reversed(range(len(expanded_file))):
        if last_id == None and expanded_file[i1].id != ".":
            last_id = int(expanded_file[i1].id)
            break
    
    prev_s_i1 = len(expanded_file)
    #prev_s_i2 = 0  #can't use b/c may not fill all mem
    first_empty_mem = 0
    for cur_id in reversed(range(last_id+1)):
        if (cur_id / (last_id + 1) * 100) % 10 == 0:
            print((cur_id / (last_id + 1) * 100))
        cur_len = 0
        s_i1 = None
        s_i2 = None
        for i1 in reversed(range(prev_s_i1)):
            if expanded_file[i1].id != '.' and int(expanded_file[i1].id) == cur_id:
                cur_len +=1
                e_i1 = i1 + 1
            if i1 == 0:
                s_i1 = 0
                break
            if (cur_len > 0 and str(expanded_file[i1].id) != str(cur_id)):
                s_i1 = i1 + 1
                break
        new_first_empty_mem = None
        for i2 in range(first_empty_mem, len(expanded_file[:s_i1])):
            if new_first_empty_mem == None and expanded_file[i2].id == '.':
                new_first_empty_mem = i2
            viable = True
            for offset in range(cur_len):
                if expanded_file[i2 + offset].id != '.':
                    viable = False
                    break
            if viable:
                s_i2 = i2
                break

        if s_i2 != None:
            for offset in range(cur_len):
                expanded_file[s_i2 + offset].id = expanded_file[s_i1 + offset].id
                expanded_file[s_i1 + offset].id = "."

        prev_s_i1 = s_i1
        if new_first_empty_mem != None:
            first_empty_mem = new_first_empty_mem
        # output = ""
        # for node in expanded_file:
        #     output += str(node)
        # print(output)

    ans = 0
    for i in range(len(expanded_file)):
        if expanded_file[i].id != '.':
            ans += (i * int(expanded_file[i].id))

    return ans


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