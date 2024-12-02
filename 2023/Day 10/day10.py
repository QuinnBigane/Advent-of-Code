path = "C:\\Directory\\Advent-of-Code\\Day 10\\"
f = open(path + "input.txt", "r")
f2 = open(path + "output.txt", "w")
lines = f.readlines()

start_x = 0
start_y = 0
#find start
for y in range(len(lines)):
    for x in range(len(lines[y])):
        if lines[y][x] == "S":
            start_x = x
            start_y = y
            break

main_loop = []
for y in range(len(lines)):
    main_loop.append([])
    for x in range(len(lines[y])):
        main_loop[-1].append("0")
        
#follow the pipes
def progress(cur_y, cur_x, orientation):
    print("step", cur_y, cur_x, orientation, lines[cur_y][cur_x])
    if lines[cur_y][cur_x] == '|':
        if orientation == 'N':
            return cur_y-1, cur_x, orientation
        elif orientation == 'S':
            return cur_y+1, cur_x, orientation
        else:
            print("error1a")
    elif lines[cur_y][cur_x] == '-':
        if orientation == 'E':
            return cur_y, cur_x+1, orientation
        elif orientation == 'W':
            return cur_y, cur_x-1, orientation
        else:
            print("error2a")
    elif lines[cur_y][cur_x] == 'L':
        if orientation == 'S':
            orientation = 'E'
            return cur_y, cur_x+1, orientation
        elif orientation == 'W':
            orientation = 'N'
            return cur_y-1, cur_x, orientation
        else:
            print("error3a")
    elif lines[cur_y][cur_x] == 'J':
        if orientation == 'S':
            orientation = 'W'
            return cur_y, cur_x-1, orientation
        elif orientation == 'E':
            orientation = 'N'
            return cur_y-1, cur_x, orientation
        else:
            print("error4a")
    elif lines[cur_y][cur_x] == '7':
        if orientation == 'N':
            orientation = 'W'
            return cur_y, cur_x-1, orientation
        elif orientation == 'E':
            orientation = 'S'
            return cur_y+1, cur_x, orientation
        else:
            print("error5a")
    elif lines[cur_y][cur_x] == 'F':
        if orientation == 'N':
            orientation = 'E'
            return cur_y, cur_x+1, orientation
        elif orientation == 'W':
            orientation = 'S'
            return cur_y+1, cur_x, orientation
        else:
            print("error6a")
    elif lines[cur_y][cur_x] == 'S':
        if orientation == 'W':
            return cur_y, cur_x -1, orientation 
        else:
            return cur_y, cur_x +1, 'E' 
    else:
        print("error7a")
        print(lines[cur_y][cur_x], cur_y, cur_x, orientation)

steps = 0
cur_x = start_x
cur_y = start_y
orientation = 'W' #west for main 

main_loop[cur_y][cur_x] = lines[cur_y][cur_x]
cur_y, cur_x, orientation = progress(cur_y, cur_x,orientation)
main_loop[cur_y][cur_x] = lines[cur_y][cur_x]
steps+=1
while(lines[cur_y][cur_x] != 'S' ):
    steps+=1
    print(steps)
    cur_y, cur_x, orientation = progress(cur_y, cur_x,orientation)
    print(lines[cur_y][cur_x] != 'S')
total_steps = steps
print(total_steps)



#reset
steps = 0
cur_x = start_x
cur_y = start_y
orientation = 'W' #west for main
#Normalize the main loop to a square
while(steps != total_steps):
    steps+=1
    cur_y, cur_x, orientation = progress(cur_y, cur_x,orientation)
    main_loop[cur_y][cur_x] = lines[cur_y][cur_x]



for line in main_loop:
    f2.write("\n")
    for chr in line:
        f2.write(chr)
f2.write("\n\n")


"""
.......L7F7L7FJL7.FJ
........LJL7|L-7L-JF
.........F7|L--JF7FJ
"""
def progress_rat(y,x,orientation, location):
    # print(y,x,orientation, location)
    answer = []
    if location == 'NE':
        if orientation != 'S' and (main_loop[y-1][x] not in 'LF-') and (main_loop[y-1][x+1] not in 'J7-'):
            answer.append([ y-1,x,'N', location])
            # print(y,x,orientation, location, " went N")
        if orientation != 'E' and (main_loop[y][x] not in 'JL|') and (main_loop[y-1][x] not in '7F|'):
            answer.append([y,x-1,'W', location])
            # print(y,x,orientation, location, " went W")

        if orientation != 'W' and (main_loop[y][x+1] not in 'JL|') and (main_loop[y-1][x+1] not in '7F|'):
            answer.append([ y,x+1,'E', location])
            # print(y,x,orientation, location, " went E")

        if orientation != 'N' and (main_loop[y][x] not in 'LF-') and (main_loop[y][x+1] not in 'J7-'):
            answer.append([ y+1, x, 'S', location])
            # print(y,x,orientation, location, " went S")

    elif location == 'SE':
        # print("hit SE")
        if orientation != 'S' and (main_loop[y][x] not in 'LF-') and (main_loop[y][x+1] not in 'J7-'):
            answer.append([ y-1,x,'N', location])
        if orientation != 'E' and (main_loop[y][x] not in '7F|') and (main_loop[y+1][x] not in 'JL|'):
            answer.append([ y,x-1,'W', location])
        if orientation != 'W' and (main_loop[y][x+1] not in '7F|') and (main_loop[y+1][x+1] not in 'JL|'):
            answer.append([ y,x+1,'E', location ])
        if orientation != 'N' and (main_loop[y+1][x] not in 'LF-') and (main_loop[y+1][x+1] not in 'J7-'):
            answer.append([ y+1, x, 'S', location])
    elif location == 'NW':
        # print("hit NW")
        if orientation != 'S' and (main_loop[y-1][x] not in '7J-') and (main_loop[y-1][x-1] not in 'LF-'):
            answer.append([ y-1,x,'N', location])
        if orientation != 'E' and (main_loop[y][x-1] not in 'JL|') and (main_loop[y-1][x-1] not in '7F|'):
            answer.append([ y,x-1,'W', location])
        if orientation != 'W' and (main_loop[y][x] not in 'JL|') and (main_loop[y-1][x] not in '7F|'):
            answer.append([ y,x+1,'E', location])
        if orientation != 'N' and (main_loop[y][x] not in '7J-') and (main_loop[y][x-1] not in 'LF-'):
            answer.append([ y+1, x, 'S', location])
    elif location == 'SW':
        # print("hit SW")
        if orientation != 'S' and (main_loop[y][x] not in '7J-') and (main_loop[y][x-1] not in 'LF-'):
            answer.append([ y-1,x,'N', location])
        if orientation != 'E' and (main_loop[y][x-1] not in '7F|') and (main_loop[y+1][x-1] not in 'JL|'):
            answer.append([ y,x-1,'W', location])
        if orientation != 'W' and (main_loop[y][x] not in '7F|') and (main_loop[y+1][x] not in 'JL|'):
            answer.append([ y,x+1,'E', location])
        if orientation != 'N' and (main_loop[y+1][x] not in '7J-') and (main_loop[y+1][x-1] not in 'LF-'):
            answer.append([ y+1, x, 'S', location])
    else:
        print(location)
        print("error1b")
    return answer


class Node:
    def __init__(self, chr):
        self.chr = chr
        self.NW = ""
        self.SE = ""
        self.SW = ""
        self.NE = ""


def try_to_escape(y,x):
    start_x = x
    start_y = y

    cur_x = start_x
    cur_y = start_y
    # print(len(main_loop[y]), cur_x)
    if cur_y < 2 or (cur_y > len(main_loop)-2) or cur_x < 2 or (cur_x > len(main_loop[y]) -3):
        # print("hit")
        return 1
    flag = 0
    possibilities = []
    test_loop = []
    for line in main_loop:
        test_loop.append([])
        for chr in line:
            test_loop[-1].append(Node(chr))
    for l in ['NE', 'SE', 'NW', 'SE']:
        for o in ['N', 'S', 'E', 'W']:
            #print(o,l)
            cur_orientation = o
            cur_location = l
            #get the first possibilities
            answers = progress_rat(cur_y,cur_x,cur_orientation,cur_location)
            for possibility in answers:
                    possibilities.append(possibility)
            while(possibilities != []):
                #print(len(possibilities))
                if len(possibilities) > 10000:
                    pass
                    #print(possibilities[-1][0],possibilities[-1][1],possibilities[-1][2],possibilities[-1][3])
                    # print(len(possibilities))
                    # possibilities = []
                    # flag =1 
                    #break
                # check the last one for new possibiliteies
                # print(possibilities)
                answers = progress_rat(possibilities[-1][0],possibilities[-1][1],possibilities[-1][2],possibilities[-1][3])
                #remove the last one
                possibilities.pop(-1)
                for i in range(len(answers)):
                    if (answers[i][0] < 1 or
                         answers[i][0] > len(main_loop)-1 or 
                         answers[i][1] < 1 or 
                         answers[i][1] > len(main_loop[0])-1 or 
                         main_loop[answers[i][0]][answers[i][1]] == '.'):
                            # print(answers[i][0],answers[i][1],cur_orientation,cur_location)
                            # print()
                            return 1                        
                #add to checks
                if answers != []:
                    for possibility in reversed(answers):
                        if possibility[3] == 'NE':
                            if possibility[2] not in test_loop[possibility[0]][possibility[1]].NE:
                                test_loop[possibility[0]][possibility[1]].NE += possibility[2]
                                possibilities.append(possibility)
                            else:
                                pass
                                #print("whoops already tried that")
                        if possibility[3] == 'NW':
                            if possibility[2] not in test_loop[possibility[0]][possibility[1]].NW:
                                test_loop[possibility[0]][possibility[1]].NW += possibility[2]
                                possibilities.append(possibility)
                        if possibility[3] == 'SE':
                            if possibility[2] not in test_loop[possibility[0]][possibility[1]].SE:
                                test_loop[possibility[0]][possibility[1]].SE += possibility[2]
                                possibilities.append(possibility)
                        if possibility[3] == 'SW':
                            if possibility[2] not in test_loop[possibility[0]][possibility[1]].SW:
                                test_loop[possibility[0]][possibility[1]].SW += possibility[2]
                                possibilities.append(possibility)
                
        #     break    
        # break
    if flag:
        return 2
    else:
        return 0

# for y in range(3):
#     for x in range(3):
#         if main_loop[y][x] == '0':
#             if try_to_escape(y,x):
#                 print(y, x, " escaped")
#                 main_loop[y][x] = '.'
#             else:
#                 print(y, x, " included")
#                 main_loop[y][x] = 'I'

# if try_to_escape(5,16):
#     print(5, 16, " escaped")
#     main_loop[y][x] = '.'
# else:
#     print(5, 16, " included")
#     main_loop[y][x] = 'I'

uncertain = 0
escaped = 0
inside = 0
for y in range(len(main_loop)):
    f2.write("\n")
    for x in range(len(main_loop[y])):
        if main_loop[y][x] == '0':
                test = try_to_escape(y,x)
                if test == 1:
                    escaped +=1
                    print(y, x, " escaped")
                    main_loop[y][x] = '.'
                    f2.write(".")
                elif test == 2:
                    uncertain +=1
                    print(y, x, " uncertain")
                    main_loop[y][x] = '?'
                    f2.write("?")
                else:
                    inside +=1
                    print(y, x, " inside")
                    main_loop[y][x] = 'I'
                    f2.write("I")
        else:
            #print(y,x, " main pipe")
            f2.write(main_loop[y][x])

print(uncertain, escaped, inside)
print(uncertain / (uncertain + escaped + inside))

f2.write("\n\n")
for line in main_loop:
    f2.write("\n")
    for chr in line:
        f2.write(chr)
#712 too high