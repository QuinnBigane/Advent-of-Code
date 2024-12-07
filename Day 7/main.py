from pathlib import Path
import time
import itertools

def test_calc(vals, opeartors, ans):
    cur_ans = vals[0]
    for val,op in zip(vals[1:],opeartors):
        if op == "*":
            cur_ans *= val
        if op == "+":
            cur_ans += val
        if op == "|":
            cur_ans = int(str(cur_ans) + str(val))
        if cur_ans > ans:
            return False
    if ans == cur_ans:
        return True
    else: 
        return False

def part1(f):
    f.seek(0)
    lines = f.readlines()
    
    base_operators = ["+", "*"]
    result = 0
    for line in lines:
        toks = line.split(":")
        ans = int(toks[0])
        vals = [int(x) for x in toks[1].strip().split(" ")]
        #could optimise by only generating iterations once per length
        for ops in itertools.product(base_operators, repeat=len(vals)-1):
            if test_calc(vals, ops, ans):
                result += ans
                break

    return result

def part2(f):
    f.seek(0)
    lines = f.readlines()
    
    base_operators = ["+", "*", "|"]
    result = 0
    for line in lines:
        toks = line.split(":")
        ans = int(toks[0])
        vals = [int(x) for x in toks[1].strip().split(" ")]
        #could optimise by only generating iterations once per length
        for ops in itertools.product(base_operators, repeat=len(vals)-1):
            if test_calc(vals, ops, ans):
                result += ans
                break

    return result


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