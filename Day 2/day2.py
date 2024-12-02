path = "C:\\Directory\\Advent-of-Code\\Day 2\\"
f = open(path + "input.txt", "r")


lines = f.readlines()

safe_count = 0

for line in lines:
    toks = line.strip().split()

    report = []
    for tk in toks:
        report.append(int(tk))


    prev_lvl = None
    grad_inc = None
    grad_dec = None

    safe = 1
    
    for lvl in report:
        if prev_lvl == None:
            prev_lvl = lvl
            continue          

        if prev_lvl < lvl:
            grad_inc = 1
        if prev_lvl > lvl:
            grad_dec = 1

        if (grad_dec == 1) and (grad_inc == 1):
            safe = 0
            # print("incdec",line)
            break
        if abs(prev_lvl - lvl) > 3:
            safe = 0
            # print("mag", line)
            break
        if prev_lvl == lvl:
            safe = 0
            # print("same", line)
            break 
        prev_lvl = lvl
    safe_count += safe
print(safe_count)


safe_count = 0
for line in lines:
    toks = line.strip().split()

    report = []
    for tk in toks:
        report.append(int(tk))

    print("report", report)
    for exl_index in range(len(report) + 1):
        tmp_report=[]
        for index in range(len(report)):
            if index != exl_index:
                tmp_report.append(report[index])
        
        safe = 1
        prev_lvl = None
        grad_inc = None
        grad_dec = None
        print("tmp_report", tmp_report)
        for lvl in tmp_report:
            if prev_lvl == None:
                prev_lvl = lvl
                continue          
            if prev_lvl < lvl:
                grad_inc = 1
            if prev_lvl > lvl:
                grad_dec = 1
            if (grad_dec == 1) and (grad_inc == 1):
                safe = 0
                print("incdec",line)
                break
            if abs(prev_lvl - lvl) > 3:
                safe = 0
                print("mag", line)
                break
            if prev_lvl == lvl:
                safe = 0
                print("same", line)
                break 
            prev_lvl = lvl
        if safe > 0:
            print("safe", tmp_report)
            safe_count += safe
            break

print(safe_count)