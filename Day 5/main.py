from pathlib import Path
import time

def part1(f):
    f.seek(0)
    lines = f.readlines()
    
    ### parse the sections
    rules = {}
    updates = []
    is_rules = 1
    for line in lines:
        if is_rules:
            if line == "\n":
                is_rules = 0
                continue
            toks = line.strip().split("|")
            if int(toks[0]) not in rules.keys():
                rules[int(toks[0])] = [int(toks[1])]
            else:
                rules[int(toks[0])].append(int(toks[1]))
        else:
            toks = line.strip().split(",")
            new_list = []
            for tok in toks:
                new_list.append(int(tok))
            updates.append(new_list)

    total = 0
    for update in updates:
        update_failed = 0
        for i in range(len(update)):
            if update_failed:
                break
            # the current number needs to be in front of numbers
            if update[i] in rules.keys():
                #check if any of the numbers in the rules are before this index
                #(fail)
                for x in update[:i]:
                    if x in rules[update[i]]:
                        update_failed = 1
                        break
        if not update_failed:
            total += update[int(len(update) / 2)]

    return total

def part2(f):
    f.seek(0)
    lines = f.readlines()

    ### parse the sections
    rules = {}
    updates = []
    is_rules = 1
    for line in lines:
        if is_rules:
            if line == "\n":
                is_rules = 0
                continue
            toks = line.strip().split("|")
            if int(toks[0]) not in rules.keys():
                rules[int(toks[0])] = [int(toks[1])]
            else:
                rules[int(toks[0])].append(int(toks[1]))
        else:
            toks = line.strip().split(",")
            new_list = []
            for tok in toks:
                new_list.append(int(tok))
            updates.append(new_list)

    total = 0
    for update in updates:
        new_update = update
        failing = True
        while failing:
            failing = False
            for i in range(len(new_update)):
                # the current number needs to be in front of numbers
                if new_update[i] in rules.keys():
                    #check if any of the numbers in the rules are before this index
                    #(fail)
                    for x in new_update[:i]:
                        if x in rules[update[i]]:
                            failing = True
                            #find the error value
                            j = new_update.index(x)
                            #swap with spot that failed
                            tmp = new_update[i]
                            new_update[i] = new_update[j]
                            new_update[j] = tmp
                            #mark for re-test
             
        total += (new_update[int(len(new_update) / 2)]) 
    total -= part1(f)
    return total


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