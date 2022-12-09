f = open("C:\\Directory\\Advent of Code 2022\\Day 5\input.txt", "r")
import time

class cargobay():
    def __init__(self):
        self.stacks = [stack(),stack(),stack(),stack(),stack(),stack(),stack(),stack(),stack(),stack()]

class stack():
    def __init__(self):
        self.data = []
    def add_to_stack(self, data):
        self.data.append(data)
    def remove_from_stack(self):
        return self.data.pop()
    def add_to_front_stack(self,data):
        self.data.insert(0,data)
        print(self.data)
    def get_top(self):
        return self.data[-1]



def read_current(cargobay):
    read_flag = 1
    while(read_flag):
        line = f.readline()
        if(line == " 1   2   3   4   5   6   7   8   9 \n"):
            read_flag = 0
        else:
            #for every stack
            stack_counter = 0
            while(line != ""):
                if(line[0:4] == '    '):
                    pass
                else:    
                    cargobay.stacks[stack_counter].add_to_front_stack(line[1:2])
                print(stack_counter)
                stack_counter+=1
                line = line[4:]

def read_actions(cargobay):
    for line in f.readlines():
        if(line != '\n'):
            print(line)
            if(line[6:7] == ' '):
                move_counter = int(line[5:6])
                source_stack = int(line[12:13])
                destination_stack = int(line[17:18])
            else:
                move_counter = int(line[5:7])
                source_stack = int(line[13:14])
                destination_stack = int(line[18:19])
            while(move_counter > 0):
                cargo = cargobay.stacks[source_stack - 1].remove_from_stack()
                cargobay.stacks[9].add_to_stack(cargo)
                move_counter -=1
            while(len(cargobay.stacks[9].data) > 0):
                cargo = cargobay.stacks[9].remove_from_stack()
                cargobay.stacks[destination_stack - 1].add_to_stack(cargo)
if(__name__ == '__main__'):
    cargobay = cargobay()
    read_current(cargobay)
    read_actions(cargobay)
    for stack in cargobay.stacks:
        print(stack.get_top())