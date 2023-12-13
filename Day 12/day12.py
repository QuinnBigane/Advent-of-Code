path = "C:\\Directory\\Advent-of-Code\\Day 12\\"
test = open(path + "test.txt", "r")
f = open(path + "input.txt", "r")
f2 = open(path + "output.txt", "w")

t = 0
lines = f.readlines()

t = 1
lines = test.readlines()

def is_possible(sec, nums):
    print("check", sec, nums)
    if nums == []:
        return 1
    start_offsets = [0]
    for i in range(1,len(nums)):
        start_offsets.append(1 + int(nums[i-1]) + start_offsets[-1])
    print("test", nums, start_offsets)

    offsets = [start_offsets]
    offsets_to_move = []
    for index in reversed(range(len(start_offsets))): #for every offset
        offsets_to_move.insert(0, index)
        for i in offsets_to_move:
            count = 1
            while(1):
                test_offset = start_offsets[:i]
                test_offset.append(start_offsets[i] + count)
                while(i != len(nums) - 1):
                    i+=1
                    test_offset.append(test_offset[-1] + int(nums[i-1]) + 1)
                # test_offset += start_offsets[i+1:]
                count +=1
                if test_offset[-1] + int(nums[-1]) > len(sec):
                    break
                else:
                    offsets.append(test_offset)
    print(offsets)
        
    return 1

def check_section(secs, nums):
    possibilites = 0
    if len(secs) == 0 and len(nums) > 0:
        return 0
    if len(secs) == 0 and len(nums) == 0:
        return 1
    if secs[0] == '':
        print("hit")
        #call check section on the next section
        return check_section(secs[1:], nums)
    
    cur_len = 0
    l_nums = nums
    perm_list = [[]]

    i = 0
    #get all possible numbers that can fit in current
    while(cur_len < len(secs[0])):
        cur_len+=int(l_nums[i])
        #can't fit the number
        if cur_len > len(secs[0]):
            break
        i+=1
        perm_list.append([])
        for x in range(i):
            perm_list[-1].append(l_nums[x])
        cur_len += 1
        #that's all the numbers!
        if i > len(nums) -1: 
            break
    print(secs, nums,perm_list, i)
    total = 0
    for x in range(i+1):
        my_answer = is_possible(secs[0], nums[:x])
        if my_answer > 0:
            other_answer = check_section(secs[1:], nums[x:])
        
        #compute how many permutation this using I numbers can get in this section (myanswer)
        total += (other_answer * my_answer)
    return total
        


new_lines = []
for line in lines:
    new_lines.append("")
    toks = line.strip().split()
    row = toks[0].split(".")
    numbers = toks[1].split(",")
    max_leng = 0

    #starting from every section in the row, check section 
    new_row = []
    for section in row:
        if section != '':
            new_row.append(section)

    check_section(new_row, numbers)
    print("\n")
    # max_leng = len(section)
    f2.write(new_lines[-1])