path = "C:\\Directory\\Advent-of-Code\\Day 15\\"
test = open(path + "test.txt", "r")
f = open(path + "input.txt", "r")
f2 = open(path + "output.txt", "w")

t = 0
lines = f.readlines()

# t = 1
# lines = test.readlines()
def get_hash(tk, c_val):

        
    c_val += ord(tk)
    c_val *=17
    c_val %= 256
    return c_val

boxes=[]
for x in range(256):
    boxes.append([])
for line in lines:
    total = 0
    toks = line.strip().split(",")
    for tks in toks:
        cur_val = 0
        index = 0
        for tk in tks:
            if tk == '-':
                #remove
                rem_index = 0
                for val in boxes[cur_val]:
                    if val.split(" ")[0] == tks[:index]:
                        boxes[cur_val].pop(rem_index)
                    rem_index +=1
            elif tk == '=':
                ins_index = 0
                flag = 1
                for val in boxes[cur_val]:
                    if val.split(" ")[0] == tks[:index]:
                        boxes[cur_val][ins_index] = tks[:index] + " "+ tks[index +1:] 
                        flag = 0
                        break
                    ins_index +=1
                if flag:
                    boxes[cur_val].append(tks[:index] + " "+ tks[index +1:] )
                
            else:
                index +=1
                cur_val = get_hash(tk, cur_val)

        for x in range(5):
            print(boxes[x])

focal_power = 0
for box_num in range(len(boxes)):
    for lens_num in range(len(boxes[box_num])):
        focal_power+=((box_num +1) * (lens_num + 1) * int(boxes[box_num][lens_num].split(" ")[1]))
print(focal_power)