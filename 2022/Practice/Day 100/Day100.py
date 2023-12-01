class Fish:
    def __init__(self, data = 0): 
        self.data = data
        self.data_max = 6



class FishPond:
    def __init__(self):
        self.fishes = 0
        self.day0_fishes = 0
        self.day1_fishes = 0
        self.day2_fishes = 0
        self.day3_fishes = 0
        self.day4_fishes = 0
        self.day5_fishes = 0
        self.day6_fishes = 0
        self.day7_fishes = 0
        self.day8_fishes = 0
    def sum_fish(self):
        self.fishes =self.day0_fishes + self.day1_fishes + self.day2_fishes + self.day3_fishes +self.day4_fishes +self.day5_fishes +self.day6_fishes +self.day7_fishes +self.day8_fishes
    def process_day(self):
        birthing = self.day0_fishes
        self.day0_fishes =self.day1_fishes
        self.day1_fishes =self.day2_fishes
        self.day2_fishes =self.day3_fishes
        self.day3_fishes =self.day4_fishes
        self.day4_fishes =self.day5_fishes
        self.day5_fishes =self.day6_fishes
        self.day6_fishes =self.day7_fishes
        self.day7_fishes = self.day8_fishes
        self.day6_fishes += birthing
        self.day8_fishes = birthing


f = open("C:\\Directory\\Advent of Code 2022\\Day 100\input.txt", "r")
line = f.readline()
line.strip()
toks = line.split(',')
FP = FishPond()
for tok in toks:
    tok = int(tok)
    if(tok == 1):
        FP.day1_fishes +=1
    elif(tok == 2):
        FP.day2_fishes +=1
    elif(tok == 3):
        FP.day3_fishes +=1
    elif(tok == 4):
        FP.day4_fishes +=1
    elif(tok == 5):
        FP.day5_fishes +=1
    elif(tok == 6):
        FP.day6_fishes +=1
    elif(tok == 7):
        FP.day7_fishes +=1
    elif(tok == 8):
        FP.day8_fishes +=1
    else:
        print("error")
FP.sum_fish()
for day in range(256):
    print(FP.fishes)
    FP.process_day()
    if(day == 80):
        print("-------------")
    FP.sum_fish()
print(FP.fishes)