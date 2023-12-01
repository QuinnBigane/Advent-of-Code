f = open("C:\\Directory\\Advent-of-Code-2022\\Day 12\input.txt", "r")
import numpy as np
dict = {'a':1,
'b':2,
'c':3,
'd':4,
'e':5,
'f':6,
'g':7,
'h':8,
'i':9,
'j':10,
'k':11,
'l':12,
'm':13,
'n':14,
'o':15,
'p':16,
'q':17,
'r':18,
's':19,
't':20,
'u':21,
'v':22,
'w':23,
'x':24,
'y':25,
'z':26,
'E':27,
'S':0
}

class Map:
    def __init__(self):
        self.map = []
        
        self.start_row = 0
        self.start_column = 0
        self.end_row = 0
        self.end_column = 0
        self.row = 0
        self.column = 0
        for line in f.readlines():
            self.map.append([])
            for chr in line.strip():
                self.map[self.row].append(chr)
                if(chr == 'S'):
                    self.start_row = self.row
                    self.start_column = self.column
                if(chr == 'E'):
                    self.end_column = self.column
                    self.end_row = self.row
                self.column +=1
            self.column = 0
            self.row+=1

    def get_cost(cur_node, next_node):
        if dict[cur_node] + 1 < dict[next_node]:
            return 1000000
        else:
            return 1

    def dijkstra(self):
        self.cost_map = []
        for row in self.map:
            self.cost_map.append([])
            for vertice in row:
                if vertice == 'S':
                    self.cost_map[row].append(0)
                else:
                    self.cost_map[row].append(1000000)
            row += 1
        
        for row in self.map:
            for column in row:
                self.cost_map

        print(self.cost_map[self.end_row][self.end_column])