path = "C:\\Directory\\Advent-of-Code\\Day 1\\"
f = open(path + "input.txt", "r")


lines = f.readlines()

l_lst = []
r_lst = []

for line in lines:
    toks = line.strip().split("   ")
    l_lst.append(int(toks[0]))
    r_lst.append(int(toks[1]))

l_lst.sort()
r_lst.sort()

distance_total = 0

for x,y in zip(l_lst,r_lst):
    distance_total += abs(y - x)

print(distance_total)

sim_score = 0
r_lst_occ = {}
for num in r_lst:
    if num in r_lst_occ.keys():
        r_lst_occ[num]+=1
        print(num, r_lst_occ[num])
    else:
        r_lst_occ[num]=1

for num in l_lst:
    if num in r_lst_occ.keys():
        sim_score += (num * r_lst_occ[num])

print(sim_score)
