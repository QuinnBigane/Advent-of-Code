path = "C:\\Directory\\Advent-of-Code\\Day 17\\"
test = open(path + "test.txt", "r")
f = open(path + "input.txt", "r")
f2 = open(path + "output.txt", "w")

t = 0
lines = f.readlines()

t = 1
lines = test.readlines()

class Node:
    def __init__(self,val):
        self.cost = int(val)
nodes = []
for line in lines:
    nodes.append([])
    for val in list(line.strip()):
        nodes[-1].append(Node(val))

node_costs = []
for node_row in nodes:
    node_costs.append([])
    for _ in node_row:
        node_costs[-1].append(100000000000000000000)

def dijkstra(cur_row,cur_col, movements):
    order_to_search = []
    if cur_row > 0:
        #check up
        if node_costs[cur_row-1][cur_col] > node_costs[cur_row][cur_col] + nodes[cur_row-1][cur_col].cost:
            node_costs[cur_row-1][cur_col] = node_costs[cur_row][cur_col] + nodes[cur_row-1][cur_col].cost
    if cur_col > 0:
        #check left 
        if node_costs[cur_row][cur_col-1] > node_costs[cur_row][cur_col] + nodes[cur_row][cur_col-1].cost:
            node_costs[cur_row][cur_col-1] = node_costs[cur_row][cur_col] + nodes[cur_row][cur_col-1].cost
    if cur_col < len(node_costs[0]) -1:
        #check right
        if node_costs[cur_row][cur_col+1] > node_costs[cur_row][cur_col] + nodes[cur_row][cur_col+1].cost:
            node_costs[cur_row][cur_col+1] = node_costs[cur_row][cur_col] + nodes[cur_row][cur_col+1].cost
    if cur_row < len(node_costs) - 1:
        #check down
        if node_costs[cur_row+1][cur_col] > node_costs[cur_row][cur_col] + nodes[cur_row+1][cur_col].cost:
            node_costs[cur_row+1][cur_col] = node_costs[cur_row][cur_col] + nodes[cur_row+1][cur_col].cost
    for val in order_to_search:
        if val == 'S':
            dijkstra(cur_row+1, cur_col, movements)
        if val == 'S':
            dijkstra(cur_row-1, cur_col, movements)
        if val == 'S':
            dijkstra(cur_row, cur_col+1, movements)
        if val == 'S':
            dijkstra(cur_row, cur_col-1, movements)

node_costs[0][0] = nodes[0][0].cost
dijkstra(0,0,'')
print(node_costs)