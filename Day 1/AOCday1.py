f = open("C:\Directory\Advent of Code 2022\Day 1\input.txt", "r")

current_calories = 0
highest_calories = [0,0,0]

for line in f.readlines():
    if line != '\n':
        current_calories += int(line.strip())
    else:
        if current_calories > highest_calories[-1]:
            highest_calories.append(current_calories)
            highest_calories.sort(reverse = True)
            highest_calories.pop()
            print(highest_calories)
        current_calories = 0

print(sum(highest_calories))

