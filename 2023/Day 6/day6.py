path = "C:\\Directory\\Advent-of-Code\\Day 6\\"
f = open(path + "input.txt", "r")

lines = f.readlines()

total = 0

class Race:
    def __init__(self, time, distance):
        self.time = time
        self.record_distance = distance
        self.wins = 0
    def calculate_winning_options(self):
        #cut all the times in buckets of 100
        self.offsets = []
        self.time_start = 0
        self.time_end = self.time
        prev_time_end = self.time
        prev_time_start = 0
        
        while(1):
            self.offsets = []
            for i in range(0, 10001):
                #print("offsets")
                self.offsets.append(round(self.time_start + (self.time_end - self.time_start) * i / 10000))
            for x in range(1, len(self.offsets)):
                #print("distance")
                distance = self.offsets[x] * (self.time - self.offsets[x])
                prev_distance = self.offsets[x-1] * (self.time - self.offsets[x-1])
                if distance > self.record_distance and prev_distance < self.record_distance:
                    self.time_start = self.offsets[x-1]
                    break
            for x in reversed(range(1, len(self.offsets))):
                distance = self.offsets[x] * (self.time - self.offsets[x])
                prev_distance = self.offsets[x-1] * (self.time - self.offsets[x-1])
                if distance < self.record_distance and prev_distance > self.record_distance:
                    self.time_end = self.offsets[x]
                    break
            print(prev_time_end, prev_time_start)
            print(self.time_end, self.time_start)
            
            if self.time_end == prev_time_end and self.time_start == prev_time_start:
                print("start distance: ", self.time_start * (self.time - self.time_start ))
                print("end distance: ", self.time_end * (self.time - self.time_end ))
                break
            prev_time_end = self.time_end 
            prev_time_start = self.time_start
        print("solving 1 at a time")
        print(self.time_start)
        print(self.time)
        i = 1000000
        prev = self.time_start
        while(i >= 1):
            #print(i,self.time_start, distance)
            distance = self.time_start * (self.time - self.time_start )
            if distance > self.record_distance or distance < 0:
                if distance < 0: 
                    #print("Help")
                    pass
                if i > 1:
                    i *= .1
                    self.time_start = prev
                else:
                    break
            else:
                prev = self.time_start
                self.time_start +=i  
                
        i = 1000000
        print(self.time_end)  
        prev = self.time  
        self.time_end = self.time
        while(i >= 1):
            print(i,self.time_end, distance, distance > self.record_distance)
            distance = self.time_end * (self.time - self.time_end )
            if distance > self.record_distance or distance < 0:
                if distance < 0: 
                    print("help")
                if i > 1:
                    i *= .1
                    self.time_end = prev
                else:
                    break
            else:
                prev = self.time_end
                self.time_end -= i 

            
        print("start: " + str(self.time_start) + "\nend: " + str(self.time_end))


        print(self.time_start * (self.time - self.time_start ) > self.record_distance)
        print((self.time_start-1) * (self.time - self.time_start-1 )< self.record_distance)
        print(self.record_distance, "\n")

        print(self.time_end * (self.time - self.time_end ) > self.record_distance)
        print((self.time_end + 1) * (self.time - self.time_end + 1 ) < self.record_distance)
        print(self.record_distance)
        print("\n\n\nanswer: ",round(self.time_end - self.time_start))
        return 0
races = [Race(40817772,219101213651089)]
#races = [Race(7,9) , Race(15,40) ,Race(30,200)]
#noit 28101346
total = 1
for race in races:
    total *= race.calculate_winning_options()
print(total)

print("\n\n\n\n")

for x in range(6358213 - 10, 6358213 +10):
    print(x, x * (40817772 - x) > 219101213651089)
print("\n\n\n")
for x in range(34459559 - 10, 34459559+10):
    print(x, x * (40817772 - x) > 219101213651089)

print( 34459560 - 6358213)