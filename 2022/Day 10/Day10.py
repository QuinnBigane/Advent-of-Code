f = open("C:\\Directory\\Advent-of-Code-2022\\Day 10\input.txt", "r")

class Registers:
    def __init__ (self):
        self.cycle = 0
        self.x = 1
        self.image =[['0']*40 for i in range(6)]
    def render(self):
        print(self.cycle)
        print(self.x)
        print('\n')
        if self.cycle < 41:
            if(self.cycle + 1 >= self.x + 1 >= self.cycle - 1):
                self.image[0][self.cycle - 1] = '#'
            else:
                self.image[0][self.cycle - 1] = '.'
        elif self.cycle < 81:
            if(self.cycle + 1 >= self.x + 41 >= self.cycle - 1):
                self.image[1][self.cycle - 41]= '#'
            else:
                self.image[1][self.cycle - 41]= '.'

        elif self.cycle < 121:
            if(self.cycle + 1 >= self.x + 81 >= self.cycle - 1):
                self.image[2][self.cycle - 81]= '#'
            else:
                self.image[2][self.cycle - 81]= '.'

        elif self.cycle < 161:
            if(self.cycle + 1 >= self.x + 121 >= self.cycle - 1):
                self.image[3][self.cycle - 121]= '#'
            else:
                self.image[3][self.cycle - 121]= '.'

        elif self.cycle < 201:
            if(self.cycle + 1 >= self.x + 161 >= self.cycle - 1):
                self.image[4][self.cycle - 161]= '#'
            else:
                self.image[4][self.cycle - 161]= '.'

        elif self.cycle < 241:
            if(self.cycle + 1 >= self.x + 201 >= self.cycle - 1):
                self.image[5][self.cycle - 201]= '#'
            else:
                self.image[5][self.cycle - 201]= '.'

        else:
            print("error")
running_total = 0
check = [20,60,100,140,180,220]
#check = [0,1,2,3,4,5]
reg = Registers()
for line in f.readlines():
    line.strip()
    if line == "noop":
        reg.cycle +=1
        reg.render()
        if reg.cycle in check:
            running_total += (reg.x * reg.cycle)
    else:
        reg.cycle += 1
        reg.render()
        if reg.cycle in check:
            running_total += (reg.x * reg.cycle)
        toks = line.split(" ")
        if toks[0] == "addx":
            # print(reg.x)
            # print(int(toks[1]))
            # print('\n')
            reg.cycle += 1
            reg.render()
            if reg.cycle in check:
                running_total += (reg.x * reg.cycle)
            reg.x += int(toks[1])

print(reg.image[0])
print(reg.image[1])
print(reg.image[2])
print(reg.image[3])
print(reg.image[4])
print(reg.image[5])
image = "" 
for row in reg.image:
    image+= '\n'
    for chr in row:
        image += chr

print(image)