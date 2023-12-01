digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

path = "C:\\Directory\\Advent-of-Code\\Day 1\\"
f = open(path + "input.txt", "r")

def check_rev(buffer):
    if len(buffer) >2:
        if buffer[-3:] == "one":
            buffer = buffer[:-3]
            return buffer + "1"
        if buffer[-3:] == "two":
            buffer = buffer[:-3]
            return buffer + "2"
        if buffer[-3:] == "six":
            buffer = buffer[:-3]
            return buffer + "6"
    if len(buffer) >3:
        if buffer[-4:] == "four":
            buffer = buffer[:-4]
            return buffer + "4"
        if buffer[-4:] == "five":
            buffer = buffer[:-4]
            return buffer + "5"
        if buffer[-4:] == "nine":
            buffer = buffer[:-4]
            return buffer + "9"       
    if len(buffer) >4:
        if buffer[-5:] == "three":
            buffer = buffer[:-5]
            return buffer + "3"
        if buffer[-5:] == "seven":
            buffer = buffer[:-5]
            return buffer + "7"
        if buffer[-5:] == "eight":
            buffer = buffer[:-5]
            return buffer + "8"
    return buffer

def check(buffer):
    if len(buffer) >2:
        if buffer[:3] == "one":
            buffer = buffer[3:]
            return "1" + buffer
        if buffer[:3] == "two":
            buffer = buffer[3:]
            return "2" + buffer
        if buffer[:3] == "six":
            buffer = buffer[3:]
            return "6" + buffer
    if len(buffer) >3:
        if buffer[:4] == "four":
            buffer = buffer[4:]
            return "4" + buffer
        if buffer[:4] == "five":
            buffer = buffer[4:]
            return "5" + buffer
        if buffer[:4] == "nine":
            buffer = buffer[4:]
            return "9" + buffer       
    if len(buffer) >4:
        if buffer[:5] == "three":
            buffer = buffer[5:]
            return "3" + buffer
        if buffer[:5] == "seven":
            buffer = buffer[5:]
            return "7" + buffer
        if buffer[:5] == "eight":
            buffer = buffer[5:]
            return "8" + buffer
    return buffer

lines = f.readlines()
total = 0
for line in lines:
    first = None
    last = None
    buffer = ""
    write_buffer = ""
    buffer = line
    #go through the buffer from left to right, changing letters to numbers
    #could stop after I discover a number, but not neccesary given time 
    while len(buffer) > 0:
        buffer = check(buffer)
        write_buffer += buffer[:1]
        buffer = buffer[1:]
    for chr in write_buffer:
        if chr.isdigit():
            first = chr
            break
    buffer = line
    write_buffer = ""
    #go through the buffer from right to left, changing letters to numbers
    #could stop after I discover a number, but not neccesary given time 
    while len(buffer) > 0:
        buffer = check_rev(buffer)
        write_buffer = buffer[-1] + write_buffer
        buffer = buffer[:-1]
    #loop through chars in reverse, checking for first digit
    for chr in write_buffer[::-1]:
        if chr.isdigit():
            last = chr
            break        
    cal_point = str(first) + str(last)
    total += int(cal_point)
print(total)
