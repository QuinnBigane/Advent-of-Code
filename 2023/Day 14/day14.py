path = "C:\\Directory\\Advent-of-Code\\Day 14\\"
test = open(path + "test.txt", "r")
f = open(path + "input.txt", "r")
f2 = open(path + "output.txt", "w")

t = 0
lines = f.readlines()

# t = 1
# lines = test.readlines()

class Map():
    def __init__(self):
        self.grid = []
    def tilt_north(self):
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                if self.grid[row][col] == 'O':
                    cur_row = row
                    cur_col = col
                    while(1):
                        # if cur_row == 0 or cur_row == len(self.grid) -1 or cur_col == 0  or cur_col == len(self.grid[0]) or self.grid[cur_row-1][cur_col] == '#' or self.grid[cur_row-1][cur_col] == 'O':
                        if cur_row == 0 or self.grid[cur_row-1][cur_col] == '#' or self.grid[cur_row-1][cur_col] == 'O':
    
                            break
                        cur_row -=1
                    self.grid[row][col] = '.'
                    self.grid[cur_row][cur_col] = 'O'
    def do_cycle(self):
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                if self.grid[row][col] == 'O':
                    cur_row = row
                    cur_col = col
                    while(1):
                        # if cur_row == 0 or cur_row == len(self.grid) -1 or cur_col == 0  or cur_col == len(self.grid[0]) or self.grid[cur_row-1][cur_col] == '#' or self.grid[cur_row-1][cur_col] == 'O':
                        if cur_row == 0 or self.grid[cur_row-1][cur_col] == '#' or self.grid[cur_row-1][cur_col] == 'O':
                            break
                        cur_row -=1
                    self.grid[row][col] = '.'
                    self.grid[cur_row][cur_col] = 'O'
        for col in range(len(self.grid[0])):
            for row in range(len(self.grid)):
                if self.grid[row][col] == 'O':
                    cur_row = row
                    cur_col = col
                    while(1):
                        # if cur_row == 0 or cur_row == len(self.grid) -1 or cur_col == 0  or cur_col == len(self.grid[0]) or self.grid[cur_row-1][cur_col] == '#' or self.grid[cur_row-1][cur_col] == 'O':
                        if cur_col == 0 or self.grid[cur_row][cur_col-1] == '#' or self.grid[cur_row][cur_col-1] == 'O':
                            break
                        cur_col -=1
                    self.grid[row][col] = '.'
                    self.grid[cur_row][cur_col] = 'O'

        for row in reversed(range(len(self.grid))):
            for col in range(len(self.grid[0])):
                if self.grid[row][col] == 'O':
                    cur_row = row
                    cur_col = col
                    while(1):
                        # if cur_row == 0 or cur_row == len(self.grid) -1 or cur_col == 0  or cur_col == len(self.grid[0]) or self.grid[cur_row-1][cur_col] == '#' or self.grid[cur_row-1][cur_col] == 'O':
                        if cur_row == len(self.grid) -1 or self.grid[cur_row+1][cur_col] == '#' or self.grid[cur_row+1][cur_col] == 'O':
                            break
                        cur_row +=1
                    self.grid[row][col] = '.'
                    self.grid[cur_row][cur_col] = 'O'
        for col in reversed(range(len(self.grid[0]))):
            for row in range(len(self.grid)):
                if self.grid[row][col] == 'O':
                    cur_row = row
                    cur_col = col
                    while(1):
                        # if cur_row == 0 or cur_row == len(self.grid) -1 or cur_col == 0  or cur_col == len(self.grid[0]) or self.grid[cur_row-1][cur_col] == '#' or self.grid[cur_row-1][cur_col] == 'O':
                        if cur_col == len(self.grid[0]) -1 or self.grid[cur_row][cur_col+1] == '#' or self.grid[cur_row][cur_col+1] == 'O':
                            break
                        cur_col +=1
                    self.grid[row][col] = '.'
                    self.grid[cur_row][cur_col] = 'O'

    def calculate_load(self):
        count = 1
        load = 0
        for row in reversed(self.grid):
            for chr in row:
                if chr == 'O':
                    load += (count)
            count +=1
        # print(load)
        return load



map = Map()     
for line in lines:
    map.grid.append(list(line.strip()))

scores  = {}
for _ in range(1000000000):
    map.do_cycle()
    # if _ % 10000000 == 0:
    #     print(round(_/1000000000, 2))
    ans = map.calculate_load()
    # print(ans)
    if ans not in scores:
        scores[ans] = [_]
    else:
        scores[ans].append(_)
        print(ans, scores[ans])
    if _ > 300:
        break
