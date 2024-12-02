path = "C:\\Directory\\Advent-of-Code\\Day 4\\"
f = open(path + "input.txt", "r")

lines = f.readlines()

total = 0

class Card:
    def __init__(self,ID,winning_numbers,numbers):
        self.id = ID
        self.winning_numbers = winning_numbers
        self.numbers = numbers
        self.points = 0
        self.wins = 0
        self.copies = 1
    def calculate_points(self):
        for num in self.numbers:
            if num in self.winning_numbers:
                if self.points == 0:
                    self.points = 1
                else:
                    self.points *= 2
        return self.points
    def calculate_wins(self):
        for num in self.numbers:
            if num in self.winning_numbers:
                self.wins +=1
        return self.wins

cards = []
for line in lines:
    main = line.split("|")
    temp_id = int(main[0].split(":")[0][4:])

    toks = main[0].split(":")[1].split(" ")
    temp_winning_numbers = []
    for num in toks:
        if num != "":
            temp_winning_numbers.append(int(num))
    
    toks = main[1].strip().split(" ")
    temp_numbers = []
    for num in toks:
        if num != "":
            temp_numbers.append(int(num))
    cards.append(Card(ID=temp_id, winning_numbers = temp_winning_numbers, numbers = temp_numbers))



for card in cards:
    total += card.calculate_points()
print(total)

total = 0
for card in cards:
    card.calculate_wins()

for card in cards:
    cur_id = card.id
    cur_wins = card.wins
    cur_copies = card.copies
    for c in cards:
        if c.id > cur_id and c.id <= cur_id + cur_wins:
            c.copies += cur_copies

for card in cards:
    total += card.copies
print(total)