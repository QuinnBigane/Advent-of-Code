path = "C:\\Directory\\Advent-of-Code\\Day 13\\"
test = open(path + "test.txt", "r")
f = open(path + "input.txt", "r")
f2 = open(path + "output.txt", "w")

t = 0
lines = f.readlines()

# t = 1
# lines = test.readlines()

class Map():
    def __init__(self):
        self.pic = []
        self.reflection_col = None
        self.reflection_row = None
    def find_reflection_point(self):
        self.reflection_col = self.find_col_reflection()
        if self.reflection_col == None:
            self.reflection_row = self.find_row_reflection()
            return self.reflection_row *100
        return self.reflection_col
    def find_row_reflection(self):
        for cur_row in range(1,len(self.pic)):
            flag = 1
            wrong_count = 0
            for cur_col in range(len(self.pic[cur_row])):
                for count in range(100):
                    if cur_row+count > len(self.pic) - 1 or cur_row - (1+count) < 0:
                        break
                    if self.pic[cur_row + count][cur_col] != self.pic[cur_row-(1 + count)][cur_col]:
                        flag = 0
                        wrong_count+=1
            # print("wrong ",wrong_count)
            if wrong_count == 1:
                return cur_row
    def find_col_reflection(self):
        for cur_col in range(1,len(self.pic[0])):
            flag = 1
            wrong_count = 0
            for cur_row in range(len(self.pic)):
                for count in range(100):
                    if cur_col+count > len(self.pic[0]) - 1 or cur_col - (1+count) < 0:
                        break
                    if self.pic[cur_row][cur_col+ count] != self.pic[cur_row][cur_col-(1+count)]:
                        flag = 0
                        wrong_count +=1
            if wrong_count == 1:
                return cur_col
maps = [Map()]
for line in lines:
    if line.strip() == '':
        maps.append(Map())
        continue
    maps[-1].pic.append(line.strip())
total = 0
for map in maps:
    total += map.find_reflection_point()
print(total)