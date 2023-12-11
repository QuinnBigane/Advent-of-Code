path = "C:\\Directory\\Advent-of-Code\\Day 7\\"
f = open(path + "input.txt", "r")

lines = f.readlines()


class Hand:
    def __init__(self, id, cards, bid):
        self.id = id
        self.cards = cards
        self.bid = bid
        self.strength = 0
        self.type = None
    def calc_strength(self):
        counts = [0,0,0,0,0,0,0,0,0,0,0,0,0]
        for card in self.cards:
            counts[self.get_card_count(card) - 2] +=1
        if counts[9] > 0:
            highest_count = 0
            highest_count_loc = -1
            for x in [0,1,2,3,4,5,6,7,8,10,11,12]:
                if counts[x] > highest_count:
                    highest_count = counts[x]
                    highest_count_loc = x
            counts[highest_count_loc] += counts[9]
            counts[9] = 0
        for count in counts:
            if count == 5:
                self.strength = 600
            if count == 4: 
                self.strength = 500
            if ((count == 3) and (self.strength == 100)) or (count == 2 and self.strength == 300):
                self.strength = 400
            if (count == 3 and self.strength == 0):
                self.strength = 300
            if (count == 2 and self.strength == 100):
                self.strength = 200
            if (count == 2 and self.strength == 0):
                self.strength = 100
        self.counts = counts 

    def check_high_card(self,hand2):
       
        for c in range(5):
            if self.get_card_strength(self.cards[c]) > hand2.get_card_strength(hand2.cards[c]):
                return 1
            if self.get_card_strength(self.cards[c]) < hand2.get_card_strength(hand2.cards[c]):
                return 0
    def get_card_count(self,c):
        if c == 'A':
            return 14
        elif c == 'K':
            return 13
        elif c == 'Q':
            return 12
        elif c == 'J':
            return 11
        elif c == 'T':
            return 10
        elif c == '9':
            return 9
        elif c == '8':
            return 8
        elif c == '7':
            return 7
        elif c == '6':
            return 6
        elif c == '5':
            return 5
        elif c == '4':
            return 4
        elif c == '3':
            return 3
        elif c == '2':
            return 2
        else:
            print("bad")
            return -10000

    def get_card_strength(self,c):
        if c == 'A':
            return 14
        elif c == 'K':
            return 13
        elif c == 'Q':
            return 12
        elif c == 'J':
            return 1
        elif c == 'T':
            return 10
        elif c == '9':
            return 9
        elif c == '8':
            return 8
        elif c == '7':
            return 7
        elif c == '6':
            return 6
        elif c == '5':
            return 5
        elif c == '4':
            return 4
        elif c == '3':
            return 3
        elif c == '2':
            return 2
        else:
            print("bad")
            return -10000
        


hands = []
id = 0
for line in lines:
    toks = line.strip().split()
    hands.append(Hand(id,toks[0], int(toks[1])))
    id+=1

for hand in hands:
    hand.calc_strength()





ordered_hands = [hands[0]]
for x in range(1, len(hands)):
    for y in range(len(ordered_hands)):
        if hands[x].strength < ordered_hands[y].strength:
            if y == len(ordered_hands) - 1:
                ordered_hands.insert(y+1,hands[x])
            continue
        if hands[x].strength > ordered_hands[y].strength:
            ordered_hands.insert(y,hands[x])
            break
        if hands[x].strength == ordered_hands[y].strength:
            if hands[x].check_high_card(ordered_hands[y]):
                ordered_hands.insert(y,hands[x])
                break
        if (y == len(ordered_hands) - 1):
            ordered_hands.insert(y+1,hands[x])

f = open(path + "output.txt", "w")

rnk = 1000
for hand in ordered_hands:
    hand.rank = rnk
    rnk -=1
for strength in [600,500,400,300,200,100,0]:
    for hand in ordered_hands:
        if hand.strength == strength:
            f.write(hand.cards + " "+str(hand.rank) + " "+ str(hand.strength) + " " + str(hand.counts)+"\n")
total = 0
for hand in ordered_hands:
   total += (hand.bid * hand.rank) 
print(total)

# nums = [4, 3, 7 ,12 , 8]
# ordered_nums = [nums[10]]

#too low 251203906