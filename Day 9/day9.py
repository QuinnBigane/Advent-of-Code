path = "C:\\Directory\\Advent-of-Code\\Day 9\\"
f = open(path + "input.txt", "r")

lines = f.readlines()

class Seq():
    def __init__(self):
        self.vals = []
    def find_next_val(self):
        l_seq = [0]
        l_seq[0] = self.vals
        while(1):
            # print(l_seq[-1], len(l_seq[-1]))
            flag = 1
            for val in l_seq[-1]:
                if val != 0:
                    flag = 0
            if flag:
                break
            l_seq.append([])
            for x in range(len(l_seq[-2]) - 1):
                l_seq[-1].append(l_seq[-2][x+1] - l_seq[-2][x])
        for x in reversed(range(len(l_seq))):
            if x == len(l_seq) - 1:
                l_seq[x].append(0)
            else:
                l_seq[x].append(l_seq[x+1][-1] + l_seq[x][-1])
        return l_seq[0][-1]
    def find_first_val(self):
        l_seq = [0]
        l_seq[0] = self.vals
        while(1):
            # print(l_seq[-1], len(l_seq[-1]))
            flag = 1
            for val in l_seq[-1]:
                if val != 0:
                    flag = 0
            if flag:
                break
            l_seq.append([])
            for x in range(len(l_seq[-2]) - 1):
                l_seq[-1].append(l_seq[-2][x+1] - l_seq[-2][x])
        for x in reversed(range(len(l_seq))):
            if x == len(l_seq) - 1:
                l_seq[x].insert(0, 0)
            else:
                l_seq[x].insert(0 , l_seq[x][0] - l_seq[x+1][0] )
        return l_seq[0][0]
seqs = []
for line in lines:
    seqs.append(Seq())
    for val in line.strip().split():
        seqs[-1].vals.append(int(val))

total = 0
for s in seqs:
    total += s.find_next_val()
print(total)

total = 0
for s in seqs:
    total += s.find_first_val()
print(total)

#712 too high

lines = "test", "testsssnn"

for line in lines:
    if "n" not in line:
        print ('good')