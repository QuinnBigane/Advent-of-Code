f = open("C:\\Directory\\Advent-of-Code-2022\\Day 11\input.txt", "r")

import math 

class Monkey:
    def __init__(self, items = [], operation = "", test_value = "", true_monkey = None, false_monkey = None):
        self.items = items
        self.operation = operation
        self.test_value = test_value
        self.true_monkey =true_monkey
        self.false_monkey =false_monkey
        self.count = 0
    def divide_by_3(self, item):
        return item//3
    def operate(self):
        toks = self.operation.split(" ")
        new_items = []
        for item in self.items:
            self.count+= 1
            if(toks[2] == "old"):
                new1 = item
            else:
                new1 = int(toks[2])

            
            if(toks[4] == "old"):
                new2 = item
            else:
                new2 = int(toks[4])

            if(toks[3] == '*'):
                new = new1 * new2
            elif(toks[3] == '/'):
                new = new1 / new2
            elif(toks[3] == '-'):
                new = new1 - new2
            elif(toks[3] == '+'):
                new = new1 + new2
            else:
                print("error")
            if(new / (5*2*13*7*19*11*3*17) > 1):
                new = new % (5*2*13*7*19*11*3*17)
            new_items.append(new)
        self.items = new_items
    def test(self):
        for item in self.items:
            if item % self.test_value == 0:
                self.true_monkey.items.append(item)
            else:
                self.false_monkey.items.append(item)
        self.items = []

monkeys = [Monkey(items = [61], operation="new = old * 11",test_value = 5),
        Monkey(items = [76, 92, 53, 93, 79, 86, 81], operation="new = old + 4",test_value = 2),
        Monkey(items = [91, 99], operation="new = old * 19",test_value = 13),
        Monkey(items = [58, 67, 66], operation="new = old * old",test_value = 7),
        Monkey(items = [94, 54, 62, 73], operation="new = old + 1",test_value = 19),
        Monkey(items = [59, 95, 51, 58, 58], operation="new = old + 3",test_value = 11),
        Monkey(items = [87, 69, 92, 56, 91, 93, 88, 73], operation="new = old + 8",test_value = 3),
        Monkey(items = [71, 57, 86, 67, 96, 95], operation="new = old + 7",test_value = 17)]

monkeys[0].true_monkey = monkeys[7]
monkeys[0].false_monkey = monkeys[4]

monkeys[1].true_monkey = monkeys[2]
monkeys[1].false_monkey = monkeys[6]

monkeys[2].true_monkey = monkeys[5]
monkeys[2].false_monkey = monkeys[0]

monkeys[3].true_monkey = monkeys[6]
monkeys[3].false_monkey = monkeys[1]

monkeys[4].true_monkey = monkeys[3]
monkeys[4].false_monkey = monkeys[7]

monkeys[5].true_monkey = monkeys[0]
monkeys[5].false_monkey = monkeys[4]

monkeys[6].true_monkey = monkeys[5]
monkeys[6].false_monkey = monkeys[2]

monkeys[7].true_monkey = monkeys[3]
monkeys[7].false_monkey = monkeys[1]

for round in range(10000):
    if(round % 10 == 0):
        print(round)
    for monkey in monkeys:
        monkey.operate()
        monkey.test()

for monkey in monkeys:
    print(monkey.count)