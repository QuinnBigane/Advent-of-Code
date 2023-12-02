path = "C:\\Directory\\Advent-of-Code\\Day 2\\"
f = open(path + "input.txt", "r")

lines = f.readlines()

#12 red cubes, 13 green cubes, and 14 blue cubes
class Game:
    def __init__(self, ident):
        self.ID = ident
        self.sets = []
        self.max_green = 0
        self.max_red = 0
        self.max_blue = 0
    def find_max_values(self):
        for set in self.sets:
            if set.Red > self.max_red:
                self.max_red = set.Red
            if set.Green > self.max_green:
                self.max_green = set.Green
            if set.Blue > self.max_blue:
                self.max_blue = set.Blue
class Set:
    def __init__(self, red, green, blue):
        self.Red = red
        self.Blue = blue
        self.Green = green

games = []
Identification = 0
for line in lines:
    Identification+=1
    games.append(Game(ident = Identification))
    
    all_local_sets = line.split(":")[1]
    local_sets = all_local_sets.split(";")
    for set in local_sets:
        r = 0
        b = 0
        g = 0
        counts = set.split(",")
        for count in counts:
            toks = count.split(" ")
            if toks[0] == "":
                toks.pop(0)
            if toks[1].strip() == "green":
                g = int(toks[0])
            elif toks[1].strip() == "red":
                r = int(toks[0])
            elif toks[1].strip() == "blue":
                b = int(toks[0])
            else:
                print(toks)
                print("error")
        games[Identification - 1].sets.append(Set(red = r, green = g, blue = b))

for game in games:
    game.find_max_values()


#12 red cubes, 13 green cubes, and 14 blue cubes

total = 0
for game in games:
    if game.max_red <= 12 and game.max_green <= 13 and game.max_blue <= 14:
        total += game.ID
    else:
        print("not this game")
print(total)

total_power = 0
for game in games:
    total_power += (game.max_red * game.max_green * game.max_blue)

print(total_power)