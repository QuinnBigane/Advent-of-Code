f = open("C:\\Directory\\Advent of Code 2022\\Day 6\input.txt", "r")
import time

def main():
    line = f.readline()
    start_message_index = 14
    while(True):
        buffer = line[0:14]
        print(buffer)
        test = 0
        for chr in buffer:
            if buffer.count(chr) > 1:
                print('repeated chr')
                line = line[1:]
                start_message_index +=1
                test = 1     
                break
        if(test == 0):
            print(start_message_index)
            return


main()