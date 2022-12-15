import threading
class Node:
    def __init__(self, data): 
        self.data = data

class Map:
    def __init__(self,y_offset = 2000000):
        self.map = [0]*4000000
        self.y_offset = y_offset
        f = open("C:\\Directory\\Advent-of-Code-2022\\Day 15\input.txt", "r")
        for line in f.readlines():
            toks = line.strip().split(" ")
            sensor_x = toks[2]
            sensor_x = int(sensor_x[2:len(sensor_x)-1])
            sensor_y = toks[3]
            sensor_y = int(sensor_y[2:len(sensor_y)-1])
            beacon_x = toks[8]
            beacon_x = int(beacon_x[2:len(beacon_x)-1])
            beacon_y = toks[9]
            beacon_y = int(beacon_y[2:len(beacon_y)])
            if(sensor_y == self.y_offset):
                self.map[sensor_x]=1
            if(beacon_y == self.y_offset):
                self.map[beacon_x]=2

            cur_cell_x = sensor_x
            cur_cell_y = sensor_y
            sensor_beacon_manhattan_distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
            sensor_cur_cell_manhattan_distance = abs(sensor_x - cur_cell_x) + abs(sensor_y - cur_cell_y)
            sensor_y_offset_row_manhattan_distance = abs(sensor_x - sensor_x) + abs(sensor_y - self.y_offset)
            
            if(sensor_y_offset_row_manhattan_distance > sensor_beacon_manhattan_distance):
                continue
            while(sensor_cur_cell_manhattan_distance < sensor_beacon_manhattan_distance):
                if cur_cell_y == self.y_offset and cur_cell_x < 4000000:
                    if self.map[cur_cell_x] == 0:
                        self.map[cur_cell_x] = 3
                cur_cell_x +=1
                sensor_cur_cell_manhattan_distance = abs(sensor_x - cur_cell_x) + abs(sensor_y - cur_cell_y)
            main_row_pos_x = cur_cell_x - 1

            cur_cell_x = sensor_x
            cur_cell_y = sensor_y
            sensor_cur_cell_manhattan_distance = abs(sensor_x - cur_cell_x) + abs(sensor_y - cur_cell_y)
            while(sensor_cur_cell_manhattan_distance < sensor_beacon_manhattan_distance):
                if cur_cell_y == self.y_offset and cur_cell_x < 4000000:
                    if self.map[cur_cell_x] == 0:
                        self.map[cur_cell_x] = 3
                cur_cell_x -=1
                sensor_cur_cell_manhattan_distance = abs(sensor_x - cur_cell_x) + abs(sensor_y - cur_cell_y)
            main_row_neg_x = cur_cell_x + 1

            cur_row_pos_x = main_row_pos_x 
            cur_row_neg_x = main_row_neg_x 
            while(cur_row_pos_x - cur_row_neg_x > 0):
                cur_cell_y +=1
                if cur_cell_y > self.y_offset:
                    break
                if cur_cell_y == self.y_offset:
                    for x in range(cur_row_neg_x, cur_row_pos_x):
                        cur_cell_x = x
                        if cur_cell_x < 4000000:
                            if self.map[cur_cell_x] == 0:
                                self.map[cur_cell_x] = 3
                cur_row_pos_x-=1
                cur_row_neg_x+=1

            cur_row_pos_x = main_row_pos_x 
            cur_row_neg_x = main_row_neg_x 
            cur_cell_y = sensor_y
            while(cur_row_pos_x - cur_row_neg_x > 0):
                cur_cell_y -=1
                if cur_cell_y < self.y_offset:
                    break
                if cur_cell_y == self.y_offset:
                    for x in range(cur_row_neg_x, cur_row_pos_x):
                        cur_cell_x = x
                        if cur_cell_x < 4000000:
                            if self.map[cur_cell_x] == 0:
                                self.map[cur_cell_x] = 3
                cur_row_pos_x-=1
                cur_row_neg_x+=1
            

"""
running_total = 0
for x in map.map[0]:
    if x != 0:
        running_total +=1
        if x == 2:
            print("hitter")
"""
def threading_func(start, end):
    y_offset = start
    while(y_offset < end):
        print(y_offset)
        map = Map(y_offset=y_offset)
        for x in range(0,4000000):
            if map.map[x] == 0:
                print(x)
                print(y_offset)
                print('\n')
                y_offset = 8000000000
        y_offset+=1


if __name__ == "__main__":

    x = threading.Thread(target=threading_func, args=(0,1000000,))
    x2 = threading.Thread(target=threading_func, args=(1000000,2000000,))
    x3 = threading.Thread(target=threading_func, args=(2000000,3000000,))
    x4 = threading.Thread(target=threading_func, args=(3000000,4000000,))
    x.start()
    x2.start()
    x3.start()
    x4.start()

"""
f2 = open("C:\\Directory\\Advent-of-Code-2022\\Day 15\output.txt", "w")

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
"""