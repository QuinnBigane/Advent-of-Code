f = open("C:\\Directory\\Advent of Code 2022\\New folder\\input.txt", "r")

"""
play 1
A - Rock
B - Paper
C - Siccors

Play 2
X - R
Y - P
Z - S
"""
my_total_score = 0
my_round_score = 0

for line in f.readlines():
    my_round_score = 0

    line.strip()
    toks = line.split()
    #oppenent rock
    if(toks[0] == 'A'):
        if(toks[1] == 'X'):
            my_round_score += 0
            my_round_score += 3
            #draw
        if(toks[1] == 'Y'):
            my_round_score += 3
            my_round_score += 1
            #winn
        if(toks[1] == 'Z'):
            my_round_score += 6
            my_round_score += 2
            #loss
    if(toks[0] == 'B'):
        if(toks[1] == 'X'):
            my_round_score += 0
            my_round_score += 1
            #draw
        if(toks[1] == 'Y'):
            my_round_score += 3
            my_round_score += 2
            #winn
        if(toks[1] == 'Z'):
            my_round_score += 6
            my_round_score += 3
            #loss
    if(toks[0] == 'C'):
        if(toks[1] == 'X'):
            my_round_score += 0
            my_round_score += 2
            #draw
        if(toks[1] == 'Y'):
            my_round_score += 3
            my_round_score += 3
            #winn
        if(toks[1] == 'Z'):
            my_round_score += 6
            my_round_score += 1
            #loss'
    my_total_score += my_round_score

print(my_total_score)