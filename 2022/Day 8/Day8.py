f = open("C:\\Directory\\Advent of Code 2022\\Day 8\input.txt", "r")
import time

class Tree:
    def __init__(self, height = 0,up = None, right = None, down = None, left = None, visible = None): 
        self.height = height
        self.up = up
        self.right = right
        self.down = down
        self.left = left
        self.visible = visible
        self.senic_score = 0
    def set_senic_score(self):
        up_visble = 0
        cur_tree = self.up
        while(cur_tree != None):
            up_visble +=1
            if(cur_tree.height < self.height):
                pass
            else:
                break
            cur_tree = cur_tree.up

        right_visble = 0
        cur_tree = self.right
        while(cur_tree != None):
            right_visble += 1
            if(cur_tree.height < self.height):
                pass
            else:
                break
            cur_tree = cur_tree.right

        down_visble = 0
        cur_tree = self.down
        while(cur_tree != None):
            down_visble += 1
            if(cur_tree.height < self.height):
                pass
            else:
                break
            cur_tree = cur_tree.down

        left_visible = 0
        cur_tree = self.left
        while(cur_tree != None):
            left_visible += 1
            if(cur_tree.height < self.height):
                pass
            else:
                break
            cur_tree = cur_tree.left

        self.senic_score = left_visible * right_visble * up_visble * down_visble
    def set_visiblity(self):
        up_visble = 1
        cur_tree = self.up
        while(cur_tree != None):
            if(cur_tree.height < self.height) and (up_visble != 0):
                up_visble = 1
            else:
                up_visble = 0
            cur_tree = cur_tree.up

        right_visble = 1
        cur_tree = self.right
        while(cur_tree != None):
            if(cur_tree.height < self.height) and (right_visble != 0):
                right_visble = 1
            else:
                right_visble = 0
            cur_tree = cur_tree.right

        down_visble = 1
        cur_tree = self.down
        while(cur_tree != None):
            if(cur_tree.height < self.height) and (down_visble != 0):
                down_visble = 1
            else:
                down_visble = 0
            cur_tree = cur_tree.down

        left_visible = 1
        cur_tree = self.left
        while(cur_tree != None):
            if(cur_tree.height < self.height) and (left_visible != 0):
                left_visible = 1
            else:
                left_visible = 0
            cur_tree = cur_tree.left
        if(left_visible or right_visble or up_visble or down_visble):
            self.visible = 1
        else:
            self.visible = 0



start_tree = None
prev_line = None
cur_line = []
for line in f.readlines():
    line = line.strip()
    if(prev_line == None):
        for chr in line:
            cur_tree = Tree(height = int(chr))
            if(start_tree == None):
                start_tree = cur_tree
            cur_line.append(cur_tree)
    else:
        i = 0
        for chr in line:
            cur_tree = Tree(height = int(chr), up = prev_line[i])
            prev_line[i].down = cur_tree
            cur_line.append(cur_tree)
            i+=1

    for x in range(len(cur_line)):
        if(x == 0):
            cur_line[x].right = cur_line[x+1]
        elif(x == 98):
            cur_line[x].left = cur_line[x-1]   
        else:
            cur_line[x].right = cur_line[x+1]
            cur_line[x].left = cur_line[x-1]     

    prev_line = cur_line
    cur_line = []

running_total = 0
while(start_tree != None):
    current_tree = start_tree
    while(current_tree != None):
        current_tree.set_visiblity()
        current_tree.set_senic_score()
        if(current_tree.senic_score > running_total):
            running_total = current_tree.senic_score
        current_tree = current_tree.right
    start_tree = start_tree.down


print(running_total)