f = open("C:\\Directory\\Advent of Code 2022\\Day 9\input.txt", "r")
class Rope:
    def __init__(self):
        self.head = Head()
        self.tails = []
        for x in range(12):
            self.tails.append(Tail())
    def process(self, direction):
        if(direction == 'R'):
            self.head.process_right()
            prev_tail = self.head
            for tail in self.tails:
                tail.process(head = prev_tail)
                prev_tail = tail
        elif(direction == 'D'):
            self.head.process_down()
            prev_tail = self.head
            for tail in self.tails:
                tail.process(head = prev_tail)
                prev_tail = tail
        elif(direction == 'L'):
            self.head.process_left()
            prev_tail = self.head
            for tail in self.tails:
                tail.process(head = prev_tail)
                prev_tail = tail
        elif(direction == 'U'):
            self.head.process_up()
            prev_tail = self.head
            for tail in self.tails:
                tail.process(head = prev_tail)
                prev_tail = tail
        else:
            print("error")

class Head:
    def __init__(self):
        self.x = 10000
        self.y = 10000
    def process_right(self):
        self.x +=1
    def process_left(self):
        self.x -=1    
    def process_up(self):
        self.y +=1   
    def process_down(self):
        self.y -=1
class Tail:
    def __init__(self):
        self.x = 10000
        self.y = 10000
        self.set =[[0]*20000 for i in range(20000)]
        self.running_total = 1
    def check(self):
        if self.set[self.x][self.y] == 0:
            self.set[self.x][self.y] = 1
            self.running_total += 1

    def process(self, head):
        if(head.x > self.x + 1):
            self.x +=1
            if(head.y > self.y):
                self.y +=1
            elif(head.y < self.y):
                self.y -=1
            self.check()
        elif(head.x < self.x - 1):
            self.x -=1
            if(head.y > self.y):
                self.y +=1
            elif(head.y < self.y):
                self.y -=1
            self.check()
        elif(head.y > self.y + 1):
            self.y +=1
            if(head.x > self.x):
                self.x+=1
            elif(head.x < self.x):
                self.x-=1
            self.check()
        elif(head.y < self.y - 1):
            self.y -=1
            if(head.x > self.x):
                self.x+=1
            elif(head.x < self.x):
                self.x -=1
            self.check()

        



rope = Rope()

for line in f.readlines():
    line.strip()
    toks = line.split(" ")
    if toks[0] == 'R':
        for x in range(int(toks[1])):
            rope.process("R")
    elif toks[0] == 'U':
        for x in range(int(toks[1])):
            rope.process("U")
    elif toks[0] == 'D':
        for x in range(int(toks[1])):
            rope.process("D")
    elif toks[0] == 'L':
        for x in range(int(toks[1])):
            rope.process("L")
    else:
        print("error")

print(rope.tails[0].running_total)
print(rope.tails[1].running_total)
print(rope.tails[2].running_total)
print(rope.tails[3].running_total)
print(rope.tails[4].running_total)
print(rope.tails[5].running_total)
print(rope.tails[6].running_total)
print(rope.tails[7].running_total)
print(rope.tails[8].running_total)
print(rope.tails[9].running_total)
