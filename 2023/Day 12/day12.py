path = "C:\\Directory\\Advent-of-Code\\Day 12\\"
test = open(path + "test.txt", "r")
f = open(path + "input.txt", "r")
f2 = open(path + "output.txt", "w")

t = 0
lines = f.readlines()

t = 1
lines = test.readlines()

#6598 too low
# 8069 too high
def get_offsets(sec_len, nums, starting_offset):
    # print(len(nums), starting_offset, sec_len)
    # print("get_offsets",nums)
    if len(nums) == 0:
        return []
    if int(nums[0]) > sec_len or starting_offset > sec_len:
        return []
    count = 0
    offsets = []
    cur_len = 0
    offset = starting_offset + count
    cur_len = offset 
    for num_index in range(len(nums)):
        cur_len += (1)
        cur_len += int(nums[num_index])
    cur_len -=1
    while(cur_len <= sec_len):
        offsets.append(offset) 
        offset +=1
        cur_len +=1
        # count +=1
        # cur_len += nums
        # offset = starting_offset + count
        # cur_len = offset 
        # for num_index in range(len(nums)):
        #     cur_len += (1)
        #     cur_len += int(nums[num_index])
        # cur_len -=1
    main_response = []
    # print(offsets, nums[0])
    count = 0
    # print(offsets)
    for offset in offsets:
        #if there are more numbers 
        if len(nums) > 1:
            answers = get_offsets(sec_len, nums[1:],offset+int(nums[0])+1)
            # print(offset, nums[1:],offset+int(nums[0]), answers)
            if answers != -1:
                for answer in answers:
                    main_response.append([offset] + answer)
        else:
            main_response.append([offset])
        count +=1

    # print(main_response)
    return main_response

def is_possible(secs, nums):
    #
    sec = secs[0]
    print("is_possible", sec, nums)

    if nums == []:
        if "#" not in sec:
            # print("returned 1")
            return 1
        else:
            # print("returned 0")
            return 0

    offsets = get_offsets(len(sec), nums, 0)


    #convert offsets to a list
    print("offsets done")
    possible_count = 0
    for offset in offsets:
        l_sec = ""
        for i in range(len(offset)):
            count = offset[i] - len(l_sec)
            while count > 0:
                count -=1
                l_sec += "."
            count = int(nums[i])
            while(count > 0):
                l_sec += "#"
                count -=1
        while(len(l_sec) != len(sec)):
            l_sec += "."
        flag = 1
        for i in range(len(sec)):
            if sec[i] == '#' and l_sec[i] == '.':
                flag = 0
                break
        possible_count += flag
        # if flag:
            # print(l_sec)
    #         f2.write(l_sec + "\n")
    # f2.write("\n")
    # print("possible count: ",possible_count)
    return possible_count

def check_section(secs, nums):
    # print("check",secs,nums)
    possibilites = 0
    if len(secs) == 0 and len(nums) > 0:
        # print("returned 0")
        return 0
    if len(secs) == 0 and len(nums) == 0:
        # print("returned 1")
        return 1
    if len(nums) == 0:
        if "#" not in secs[0]:
            return check_section(secs[1:], nums)
        else:
            return 0
    if secs[0] == '':
        #print("hit")
        #call check section on the next section
        return check_section(secs[1:], nums)
    
    cur_len = 0
    l_nums = nums
    # perm_list = [[]]

    i = 0
    #get all possible numbers that can fit in current
    while(cur_len < len(secs[0])):
        cur_len+=int(l_nums[i])
        #can't fit the number
        if cur_len > len(secs[0]):
            break
        i+=1
        # perm_list.append([])                     perm list doesnt matter
        # for x in range(i):
        #     perm_list[-1].append(l_nums[x])
        cur_len += 1
        #that's all the numbers!
        if i > len(nums) -1: 
            break
    #print(secs, nums,perm_list, i)
    
    #start index
    e_index = i
    #get the minimum index left we need
    s_index = 0
    remaining_len = 0
    for sec in secs[1:]:
        remaining_len+= len(sec)

    s_index = 0 
    while(1):
        c_len = 0
        for num in nums[s_index:]:
            c_len += int(num)
        if c_len < remaining_len:
            break
        else:
            s_index+=1
        if s_index > e_index:
            s_index == e_index
            break
    if s_index > 0:
        s_index -=1
    total_remaining_nums = 0
    for num in nums:
        total_remaining_nums += int(num)
    print(secs[0] , secs)
    print(remaining_len, nums, total_remaining_nums)
    # for x in reversed(range(e_index+1):
    #     c_len = 0
    #     for num in nums[x:]:
    #         c_len += int(num)
    #     #print(nums[x:],c_len)
    #     if c_len > remaining_len:
    #         s_index+=1
    print(s_index, e_index)
    total = 0
    other_answer = 0
    for x in range(s_index,e_index+1):
        print("I am considering", nums[:x])

    for x in range(s_index,e_index+1):
        my_answer = is_possible(secs, nums[:x])
        if my_answer > 0:
            # print(nums)
            # print("checking deeper w/ ", nums[x:])
            other_answer = check_section(secs[1:], nums[x:])
        # f2.write(str(my_answer) + " x " + str(other_answer) + "\n")
        #compute how many permutation this using I numbers can get in this section (myanswer)
        #print("check returned: ",other_answer * my_answer, other_answer,my_answer )
        total += (other_answer * my_answer)
        # print("running total ", total)
    return total
        

total = 0

new_lines = []
for line in lines:
    new_lines.append("")
    toks = line.strip().split()
    row = (toks[0] + "?" +toks[0] + "?" +toks[0] + "?" +toks[0] + "?" +toks[0]).split(".")
    f2.write(str(row) + "\n")
    #row = toks[0].split(".")
    numbers = toks[1].split(",") + toks[1].split(",") +toks[1].split(",") +toks[1].split(",") +toks[1].split(",")
    # numbers = toks[1].split(",")
    f2.write(str(numbers) + "\n\n")
    max_leng = 0

    #starting from every section in the row, check section 
    new_row = []
    for section in row:
        if section != '':
            new_row.append(section)
    
    # f2.write(line)
    answer = check_section(new_row, numbers)
    print("---------------------------")
    print(new_row,answer)
    # f2.write(str(answer) + "\n\n\n")

    total +=answer
    if answer == 0:
        print("wrong")
        break
    # max_leng = len(section)
    

print("total ", total)
if t:
    print(0 == (total - 525152))