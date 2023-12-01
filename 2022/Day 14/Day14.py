
class Node:
    def __init__(self, data): 
        self.data = data

class Map:
    def __init__(self):
        self.map = [[0]*1000 for i in range(1000)]
        self.edited =0
        self.sand_placed = 0
        self.highest_y = 0
        f = open("C:\\Directory\\Advent-of-Code-2022\\Day 14\input.txt", "r")
        for line in f.readlines():
            toks = line.strip().split(' -> ')
            prev_token = None
            for tok in toks:
                if prev_token != None:
                    toks1 = prev_token.split(',')
                    toks2 = tok.split(',')
                    if toks1[0] == toks2[0]:
                        if int(toks1[1]) <  int(toks2[1]):
                            if(int(toks2[1]) > self.highest_y):
                                self.highest_y = int(toks2[1])
                            for i in range(int(toks1[1]), int(toks2[1]) + 1):
                                if self.map[int(toks1[0])][i] != 1:
                                    self.map[int(toks1[0])][i] = 1
                                    self.edited+=1
                        else:
                            if(int(toks1[1]) > self.highest_y):
                                self.highest_y = int(toks1[1])
                            for i in range(int(toks2[1]),int(toks1[1]) + 1):
                                if self.map[int(toks1[0])][i] != 1:
                                    self.map[int(toks1[0])][i] = 1
                                    self.edited+=1
                    elif toks1[1] == toks2[1]:
                        if(int(toks1[1]) > self.highest_y):
                                self.highest_y = int(toks1[1])
                        if int(toks1[0]) <  int(toks2[0]):
                            for i in range(int(toks1[0]), int(toks2[0]) + 1):
                                if self.map[i][int(toks1[1])] != 1:
                                    self.map[i][int(toks1[1])] = 1
                                    self.edited+=1
                        else:
                            for i in range(int(toks2[0]), int(toks1[0]) + 1):
                                if self.map[i][int(toks1[1])] != 1:
                                    self.map[i][int(toks1[1])] = 1
                                    self.edited+=1
                    else:
                        print("error")
                prev_token = tok
        for x in range(1000):
            self.map[x][self.highest_y + 2] = 1
        self.map[500][0] = 0
        void = 0
        while(True):
            if(void == 1):
                print('void break')
                break
            if(self.map[500][0] == 2):
                print("sand break")
                break
            cur_x = 500
            cur_y = 0
            while(True):
                if(cur_y > 1000):
                    void = 1
                    break
                elif(self.map[cur_x][cur_y+1] == 0):
                    cur_y +=1
                elif(self.map[cur_x-1][cur_y+1] == 0):
                    cur_y +=1
                    cur_x -=1
                elif(self.map[cur_x+1][cur_y+1] == 0):
                    cur_y +=1
                    cur_x +=1
                else:
                    self.map[cur_x][cur_y] = 2
                    self.sand_placed +=1
                    break


            

f2 = open("C:\\Directory\\Advent-of-Code-2022\\Day 14\output.txt", "w")
map = Map()
output_str=''
test = 0
for y in range (0, 300):
    output_str +='\n'
    for x in range(300,1000):
        if map.map[x][y] == 1:
            output_str += '#'
            test +=1
        elif map.map[x][y] == 8:
            output_str += '+'
        elif map.map[x][y] == 2:
            output_str += 'O'
        else:
            output_str += '.'
f2.write(output_str)
f2.close()
print(test)
print(map.edited)

print('\n\n\n\n')
print(map.sand_placed)
