path = "C:\\Directory\\Advent-of-Code\\Day 3\\"
f = open(path + "input.txt", "r")

lines = f.readlines()

total = 0

class gear:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.ratios = []
        self.count = 1
        self.used = 0
        self.in_use = 0
        self.ratios.append(r)
gears = []
def search_for_special_gear(y,x1,x2):
    len_num = x2-x1
    if y > 0:
        for offset in range(len_num + 1):
            if lines[y-1][x1+offset] == "*":
                gears.append(gear(y-1,x1+offset,int(lines[y][x1:x2+1])))
                return 1
        if x > 0:
            if lines[y-1][x1-1] == "*":
                gears.append(gear(y-1,x1-1,int(lines[y][x1:x2+1])))
                return 1
        if x < len(lines[0]) - 1:
            if lines[y-1][x2 + 1] == "*":
                gears.append(gear(y-1,x2+1,int(lines[y][x1:x2+1])))
                return 1
    if y < len(lines) - 1:
        for offset in range(len_num + 1):
            if lines[y+1][x1+offset] == "*":
                gears.append(gear(y+1,x1+offset,int(lines[y][x1:x2+1])))
                return 1
        if x > 0:
            if lines[y+1][x1-1] == "*":
                gears.append(gear(y+1,x1-1,int(lines[y][x1:x2+1])))
                return 1
        if x < len(lines[0]) -1:
            if lines[y+1][x2 + 1] == "*":
                gears.append(gear(y+1,x2+1,int(lines[y][x1:x2+1])))
                return 1
    if x > 0:
        if lines[y][x1-1] == "*":
            gears.append(gear(y,x1-1,int(lines[y][x1:x2+1])))
            return 1
    if x < len(lines[0]) - 1:
        if lines[y][x2 + 1] == "*":
            gears.append(gear(y,x2+1,int(lines[y][x1:x2+1])))
            return 1
    #print("not", lines[y][x1:x2+1])
    return 0



def search_for_special(y,x1,x2,):
    len_num = x2-x1
    if y > 0:
        for offset in range(len_num + 1):
            if not lines[y-1][x1+offset].isdigit() and lines[y-1][x1+offset] != ".":
                return 1
        if x > 0:
            if not lines[y-1][x1 - 1].isdigit() and lines[y-1][x1-1] != ".":
                return 1
        if x < len(lines[0]) - 1:
            if not lines[y-1][x2 + 1].isdigit() and lines[y-1][x2 + 1] != ".":
                return 1
    if y < len(lines) - 1:
        for offset in range(len_num + 1):
            if not lines[y+1][x1+offset].isdigit() and lines[y+1][x1+offset] != ".":
                return 1
        if x > 0:
            if not lines[y+1][x1 - 1].isdigit() and lines[y+1][x1-1] != ".":
                return 1
        if x < len(lines[0]) -1:
            if not lines[y+1][x2 + 1].isdigit() and lines[y+1][x2 + 1] != ".":
                return 1
    if x > 0:
        if not lines[y][x1 - 1].isdigit() and lines[y][x1-1] != ".":
            return 1
    if x < len(lines[0]) - 1:
        if not lines[y][x2 + 1].isdigit() and lines[y][x2 + 1] != ".":
            return 1
    print("not", lines[y][x1:x2+1])
    return 0

getting_number = 0
for y in range(len(lines)):
    # print(lines[t])
    for x in range(len(lines[y])):
        if lines[y][x].isdigit() or getting_number:
            if getting_number == 0:
                #first of digit
                start_digit_y = y
                start_digit_x = x
                getting_number = 1
            if getting_number == 1 and not lines[y][x].isdigit():
                #end of digit
                end_digit_y = y
                end_digit_x = x - 1
                getting_number = 0
                if search_for_special_gear(start_digit_y,start_digit_x ,end_digit_x):
                    #print(lines[start_digit_y][start_digit_x:end_digit_x+1])
                    total += int(lines[start_digit_y][start_digit_x:end_digit_x + 1])

        else: 
            pass
        
print(total)


print("8".isdigit())

for g in gears:
    g.in_use = 1
    if g.used != 1:
        for t in gears:
            if g.x == t.x and t.in_use != 1:
                if g.y == t.y:
                    g.ratios.append(t.ratios[0])
                    t.used = 1
    g.in_use = 0

t = 0
for g in gears:
    if g.used != 1:
        print(g.ratios, g.x, g.y)
    if g.used == 0: 
        print("skipped")
    if len(g.ratios) == 2:
        t+= (int(g.ratios[0]) * int(g.ratios[1]))
print(t)
    # for r in g.ratios:
    #     print       