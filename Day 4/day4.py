from pathlib import Path
import re


def part1(f):
    f.seek(0)
    lines = f.readlines()

    x_lim = len(lines[0]) - 1
    y_lim = len(lines) - 1

    count = 0
    for y in range(len(lines)):
        for x in range(len(lines[0])-1):
            if lines[y][x] == "X":
                # >
                if (x < x_lim - 2 and 
                    lines[y][x+1] == "M" and lines[y][x+2] == "A" and lines[y][x+3] == "S"):
                    count+=1
                # >^
                if (x < x_lim - 2 and y > 2 and 
                    lines[y-1][x+1] == "M" and lines[y-2][x+2] == "A" and lines[y-3][x+3] == "S"):
                    count+=1
                # ^
                if (y > 2 and 
                    lines[y-1][x] == "M" and lines[y-2][x] == "A" and lines[y-3][x] == "S"):
                    count+=1
                # <^
                if (y > 2 and x > 2 and 
                    lines[y-1][x-1] == "M" and lines[y-2][x-2] == "A" and lines[y-3][x-3] == "S"):
                    count+=1
                # <
                if (x > 2 and 
                    lines[y][x-1] == "M" and lines[y][x-2] == "A" and lines[y][x-3] == "S"):
                    count+=1
                # <v
                if  (y < y_lim - 2 and x > 2 and 
                    lines[y+1][x-1] == "M" and lines[y+2][x-2] == "A" and lines[y+3][x-3] == "S"):
                    count+=1
                # v
                if  (y < y_lim - 2 and 
                    lines[y+1][x] == "M" and lines[y+2][x] == "A" and lines[y+3][x] == "S"):
                    count+=1
                # >v
                if (x < x_lim - 2 and  y < y_lim - 2 and 
                    lines[y+1][x+1] == "M" and lines[y+2][x+2] == "A" and lines[y+3][x+3] == "S"):
                    count+=1
    return count

def part2(f):
    f.seek(0)
    lines = f.readlines()
    x_lim = len(lines[0]) - 1
    y_lim = len(lines) - 1
    count = 0
    for y in range(len(lines)):
        for x in range(len(lines[0])-1):
            if lines[y][x] == "A":
                if ((x < x_lim and y < y_lim and x > 0 and y > 0) and
                    ((lines[y+1][x+1] == "M" and lines[y+1][x-1] == "M" and lines[y-1][x-1] == "S" and lines[y-1][x+1] == "S") or
                    (lines[y+1][x+1] == "S" and lines[y+1][x-1] == "M" and lines[y-1][x-1] == "M" and lines[y-1][x+1] == "S") or
                    (lines[y+1][x+1] == "S" and lines[y+1][x-1] == "S" and lines[y-1][x-1] == "M" and lines[y-1][x+1] == "M") or 
                    (lines[y+1][x+1] == "M" and lines[y+1][x-1] == "S" and lines[y-1][x-1] == "S" and lines[y-1][x+1] == "M"))):   
                    count+=1
    return count


if __name__ == "__main__":
    test_file = open(str(Path(__file__).parent) + '\\input_test.txt', "r")
    input_file = open(str(Path(__file__).parent) + '\\input.txt', "r")
    
    part_1_test = part1(test_file)
    part_2_test = part2(test_file)
    part_1_input = part1(input_file)
    part_2_input = part2(input_file)


    print("--- Test File Results ---")
    print("Part 1:", part_1_test)
    print("Part 1:", part_2_test)

    print("--- Input File Results ---")
    print("Part 1:", part_1_input)
    print("Part 1:", part_2_input)