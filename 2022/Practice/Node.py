class Node:
    def __init__(self, data = None, neighbors = []): 
        self.data = data
        self.neighbors = neighbors
    def add_neighbor(self, quantity = 1):
        while(quantity > 0):
            self.neighbors.append(Node(neighbors = self))
            quantity -=1

if __name__ == '__main__':
    node1 = Node(data = 1)
    node1.add_neighbor(quantity = 6)
    for node in node1.neighbors:
        print(node.neighbors)

