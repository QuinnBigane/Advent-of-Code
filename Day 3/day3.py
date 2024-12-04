import re

path = "C:\\Directory\\Advent-of-Code\\Day 3\\"
f = open(path + "input.txt", "r")

#part 1

lines = f.readlines()

total = 0
for line in lines:
    matches = re.findall(r"(mul\((?:\d+),(?:\d+)\))",line)
    for item in matches:
        # print(item)
        # print(int(re.search(r"\((\d+),", item).group()[1:-1]))
        # print(int(re.search(r",(\d+)\)", item).group()[1:-1]))
        total += ((int(re.search(r"\((\d+),", item).group()[1:-1])) * (int(re.search(r",(\d+)\)", item).group()[1:-1])))
print(total)


#part 2

is_do = 1
new_str = ""
for line in lines:
    cur_index = 0
    while 1:
        if is_do:
            #find the next don't()
            match = re.search(r"don't\(\)", line[cur_index:])
            if match:
                #include the line up to that dont
                new_str += line[cur_index:cur_index + (match.span()[1])].strip()
                #update the line index and switch to looking for do
                cur_index += int(match.span()[1])
                is_do = 0
            else:
                #edge case, if do goes to end of line, include whole line but do not change state
                new_str += line[cur_index:].strip()
                break

        else:
            match = re.search(r"do\(\)", line[cur_index:])
            if match:
                #throw away line up to the next do
                #update the index and switch to looking for next dont
                cur_index += int(match.span()[1])
                is_do = 1
            else:
                #throw away rest of line
                break

# run match from p1 on new string
total = 0
matches = re.findall(r"(mul\((?:\d+),(?:\d+)\))",new_str)
for item in matches:
    total += ((int(re.search(r"\((\d+),", item).group()[1:-1])) * (int(re.search(r",(\d+)\)", item).group()[1:-1])))

print(total)
