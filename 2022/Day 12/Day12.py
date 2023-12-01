f = open("C:\\Directory\\Advent-of-Code-2022\\Day 12\input.txt", "r")

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
'E':27,
'S':0
}

start_row = 0
start_column = 0
end_row = 0
end_column = 0

map = []
row = 0
column = 0
for line in f.readlines():
    map.append([])
    for chr in line.strip():
        map[row].append(chr)
        if(chr == 'S'):
            start_row = row
            start_column = column
        if(chr == 'E'):
            end_column = column
            end_row = row
        column +=1
    column = 0
    row+=1



def main():
    test = main_helper(start_row, start_column, 0, 0)
    print(test)

def main_helper(row, column, steps, prev_val):
    if(prev_val + 1 < dict[map[row][column]]):
        return 0
    if(map[row][column] == 'E'):
        return steps
    if steps > 500: 
        return 0
    cur_val = dict[map[row][column]]
    output1 =0
    output2 =0
    output3 =0
    output4 =0
    if row == 0 and 161 >column > 0:
        output1 = main_helper(row, column - 1 , steps + 1, cur_val)
        output2 = main_helper(row, column + 1 , steps + 1, cur_val)
        output3 = main_helper(row + 1, column , steps + 1, cur_val)
    elif row == 40 and 161 > column > 0:
        output1 =main_helper(row, column - 1 , steps + 1, cur_val)
        output2 =main_helper(row, column + 1 , steps + 1, cur_val)
        output3 =main_helper(row - 1, column , steps + 1, cur_val)
    elif column == 0 and 40 > row > 0:
        output1 =main_helper(row + 1, column , steps + 1, cur_val)
        output2 =main_helper(row, column + 1 , steps + 1, cur_val)
        output3 =main_helper(row - 1, column , steps + 1, cur_val)
    elif column == 161 and 40 > row > 0:
        output1 =main_helper(row + 1, column , steps + 1, cur_val)
        output2 =main_helper(row, column - 1 , steps + 1, cur_val)
        output3 =main_helper(row - 1, column , steps + 1, cur_val)
    elif row == 0 and column == 0:
        output1 =main_helper(row, column + 1 , steps + 1, cur_val)
        output2 =main_helper(row + 1, column , steps + 1, cur_val)
    elif row == 40 and column == 0:
        output1 =main_helper(row, column + 1 , steps + 1, cur_val)
        output2 =main_helper(row - 1, column , steps + 1, cur_val)
    elif column == 161 and row == 0:
        output1 =main_helper(row + 1, column , steps + 1, cur_val)
        output2 =main_helper(row, column - 1 , steps + 1, cur_val)
    elif column == 161 and row == 40:
        output1 =main_helper(row, column - 1 , steps + 1, cur_val)
        output2 =main_helper(row - 1, column , steps + 1, cur_val)
    else:
        output1 =main_helper(row, column - 1 , steps + 1, cur_val)
        output2 =main_helper(row, column + 1 , steps + 1, cur_val)
        output3 =main_helper(row + 1, column , steps + 1, cur_val)
        output4 =main_helper(row - 1, column , steps + 1, cur_val)


  
    my_list = [output1,output2,output3,output4]
    if(output1 == 0 and output2 == 0 and output3 == 0 and output4 == 0):
        return 0
    else:
        return min(number for number in my_list if number > 0)

main()