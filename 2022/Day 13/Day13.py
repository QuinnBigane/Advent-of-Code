

import itertools




def compare_ints(int1, int2):
    if int1 < int2:
        return 1
    elif int1 == int2:
        return 0
    else: 
        return -1


def process_list(lst):
    output_list = []
    output_str = ''
    cur_index = 0
    internal_list_start_index = None
    open_count = 0
    if(len(lst) > 2):
        for chr in (lst[1:len(lst) - 1] + ','):
            cur_index +=1
            if chr == '[':
                open_count +=1
                if internal_list_start_index == None:
                    internal_list_start_index = cur_index
            elif chr == ']':
                open_count -=1
            elif chr == ',' and open_count == 0:
                if internal_list_start_index != None:
                    output_list.append(process_list(lst[internal_list_start_index:cur_index]))
                    internal_list_start_index = None
                elif output_str == '':
                    output_list.append([])
                else:
                    output_list.append(int(output_str))
                output_str = ""
            elif open_count == 0:
                output_str += chr
    

    return output_list




def check(lst1,lst2):
    for item1,item2 in itertools.zip_longest(lst1,lst2):
        if item1 is None:
            return 1
        if item2 is None:
            return -1
        if type(item1) is int and type(item2) is int: 
            if item1 < item2:
                return 1
            if item1 > item2:
                return -1
        if type(item1) is list and type(item2) is list:
            val = check(item1,item2)
            if(val == 1):
                return 1
            if (val == -1):
                return -1
        if type(item1) is list and type(item2) is int:
            val = check(item1,[item2])
            if(val == 1):
                return 1
            if (val == -1):
                return -1
        if type(item1) is int and type(item2) is list:
            val = check([item1],item2)
            if(val == 1):
                return 1
            if (val == -1):
                return -1


def maincheck(pair1, pair2):
    pair1 = process_list(pair1)
    pair2 = process_list(pair2)
    for item1,item2 in itertools.zip_longest(pair1,pair2):
        if item1 is None:
            return 1
        if item2 is None:
            return -1
        if type(item1) is int and type(item2) is int:
            if item1 < item2:
                return 1
            if item1 > item2:
                return -1
        if type(item1) is list and type(item2) is list:
            val = check(item1,item2)
            if(val == 1):
                return 1
            if (val == -1):
                return -1
        if type(item1) is list and type(item2) is int:
            val = check(item1,[item2])
            if(val == 1):
                return 1
            if (val == -1):
                return -1
        if type(item1) is int and type(item2) is list:
            val = check([item1],item2)
            if(val == 1):
                return 1
            if (val == -1):
                return -1


    return 1
pair1 = None
pair2 = None
index = 0
running_total = 0
wrong_running_total = 1
odd = 1
first_skipped = 0
while(wrong_running_total > 0):
    f = open("C:\\Directory\\Advent-of-Code-2022\\Day 13\input.txt", "r")
    f2 = open("C:\\Directory\\Advent-of-Code-2022\\Day 13\input2.txt", "w")
    wrong_running_total = 0
    for line in f.readlines():
        if line == '\n':
            pass
        elif odd and not first_skipped:
            first_skipped = 1
            f2.write(line)
        elif pair1 == None:
            pair1 = line.strip()
        elif pair2 == None:
            pair2 = line.strip()
        if pair1 != None and pair2 != None:
            index +=1
            print(index)
            val= maincheck(pair1, pair2)
            print(pair1)
            print(pair2)
            print(val)
            print('\n')
            if  val== 1:
                running_total += 1
                f2.write(pair1)
                f2.write('\n')
                f2.write(pair2)
                f2.write('\n')

            else:
                wrong_running_total +=1
                f2.write(pair2)
                f2.write('\n')
                f2.write(pair1)
                f2.write('\n')

            pair1 = None
            pair2 = None
    if pair1 != None:
        f2.write(pair1)
        f2.write('\n')
        pair1 = None
    if odd == 1:
        odd = 0
        first_skipped = 0
    else:
        odd = 1
        first_skipped = 0
    f.close()
    f2.close()
    f = open("C:\\Directory\\Advent-of-Code-2022\\Day 13\input.txt", "w")
    f2 = open("C:\\Directory\\Advent-of-Code-2022\\Day 13\input2.txt", "r")
    for line in f2.readlines():
        f.write(line)
    f.close()
    f2.close()
print('\n\n\n')
print(running_total)
print(wrong_running_total)


print(running_total+wrong_running_total)
