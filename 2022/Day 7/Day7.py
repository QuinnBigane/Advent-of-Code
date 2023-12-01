f = open("C:\\Directory\\Advent of Code 2022\\Day 7\input.txt", "r")
import time

class dir:
    def __init__(self, data = 0,parent = None, children = []): 
        self.data = data
        self.children = children
        self.parent = parent
    def get_child(self):
        output = self.children[0]
        self.children.append(self.children.pop(0))
        return output
    """
    def __str__(self):
        string = ""
        for x in range(int(len(self.children)/2)):
            string += '        '
        string += "Dir\n"
        for x in range(int(len(self.children)/2)):
            string += '       '
        string += str(self.data)
        string += '\n'
        for child in self.children:
            string += str(child.data) + ' '
        return string
    """
cur_directory = None
temp_directory = None
super_parent_directory = None
for line in f.readlines():
    if '$ cd /' in line:
        cur_directory = dir(parent = None)
        super_parent_directory = cur_directory
    elif '$ cd ..' in line:
        cur_directory = cur_directory.parent
    elif '$ cd ' in line:
        cur_directory = cur_directory.get_child()
    elif '$ ls' in line:
        pass
    else:
        if 'dir' in line:
            cur_directory.children.append(dir(parent = cur_directory, children = [], data = 0))

        else:
            toks =line.split(" ")
            cur_directory.data += int(toks[0])
            temp_directory = cur_directory
            while(temp_directory.parent != None):
                temp_directory.parent.data += int(toks[0])
                temp_directory = temp_directory.parent

def main_check(parent):
    running_total = 0
    for child in parent.children:
        if(child.data <= 100000):
            running_total+= child.data
        running_total += main_check(child)
    return running_total

def main_check2(parent, size):
    for child in parent.children:
        if child.data >= 8381165 and size > child.data:
            size = child.data
        test_size = main_check2(child, size)
        if test_size >= 8381165 and size > test_size:
            size = test_size
    return size

if __name__ == '__main__':
    #17914680 wrong
    print('\n\n')
    print(super_parent_directory.children)
    #print(main_check2(super_parent_directory, super_parent_directory.data))
 