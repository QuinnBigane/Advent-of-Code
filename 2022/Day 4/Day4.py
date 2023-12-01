f = open("C:\\Directory\\Advent of Code 2022\\Day 4\input.txt", "r")
count = 0
for line in f.readlines():
    line = line.strip()
    print(line)
    toks = line.split(",")
    range1_low = None
    range1_high = None
    range2_low =None
    range2_high = None
    for tok in toks:
        toks2 = tok.split("-")
        if(range1_high == None):
            range1_low = toks2[0]
            range1_high = toks2[1]
        else:
            range2_low = toks2[0] 
            range2_high = toks2[1]
    #check if range 2 is within range 1
    if(int(range1_low) <= int(range2_high) and int(range1_high) >= int(range2_low)):
        print("counted")
        count+=1

    elif(int(range2_low) <= int(range1_high) and int(range2_high) >= int(range1_low)):
        print("counted")
        count+=1
    else:
        print("---------------------")
        
print(count)

