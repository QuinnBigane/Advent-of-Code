f = open("C:\\Directory\\Advent of Code 2022\\Day 3\input.txt", "r")
dict = {'a':1,
'b':2,
'c':3,
'd':4,
'e':5,
'f':6,
'g':7,
'h':8,
'i':9,
'j':10,
'k':11,
'l':12,
'm':13,
'n':14,
'o':15,
'p':16,
'q':17,
'r':18,
's':19,
't':20,
'u':21,
'v':22,
'w':23,
'x':24,
'y':25,
'z':26,
'A':27,
'B':28,
'C':29,
'D':30,
'E':31,
'F':32,
'G':33,
'H':34,
'I':35,
'J':36,
'K':37,
'L':38,
'M':39,
'N':40,
'O':41,
'P':42,
'Q':43,
'R':44,
'S':45,
'T':46,
'U':47,
'V':48,
'W':49,
'X':50,
'Y':51,
'Z':52
}

running_total = 0
ruck1 = None
ruck2 = None
ruck3 = None

line = f.readline()
while(line != ""):
    while(ruck3 == None):
        if(ruck3 == None):
            if(ruck2 == None):
                if(ruck1 == None):
                    ruck1 = line
                else:
                    ruck2 = line
            else:
                ruck3 = line
        line = f.readline()
        if(line == ""):
            break
    for chr in ruck1:
        if chr in ruck2:
            if chr in ruck3:
                running_total += dict[chr]
                break
    ruck1 = None
    ruck2 = None
    ruck3 = None




print(running_total)
