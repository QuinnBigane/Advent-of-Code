class HexNode:
    def __init__(self, data = 0, e = None, se = None, sw = None, w = None, nw = None, ne = None):
        self.data = data
        self.e = e
        self.se = se
        self.sw = sw
        self.w = w
        self.nw = nw
        self.ne = ne
        self.check_neighbors()
    def check_neighbors(self):
        cur_node = None
        new_node_added = 0
        if(self.e != None):
            cur_node = self.e
            if(cur_node.nw != None and self.ne == None):
                self.ne = cur_node.nw
                cur_node.sw = self
                new_node_added = 1
            if(cur_node.sw != None and self.se == None):
                self.se = cur_node.sw
                cur_node.nw = self
                new_node_added = 1
        if(self.se != None):
            cur_node = self.se
            if(cur_node.w != None and self.sw == None):
                self.sw = cur_node.w
                cur_node.ne = self
                new_node_added = 1
            if(cur_node.ne != None and self.e == None):
                self.e = cur_node.ne
                cur_node.w = self
                new_node_added = 1
        if(self.sw != None):
            cur_node = self.sw
            if(cur_node.nw != None and self.w == None):
                self.w = cur_node.nw
                cur_node.e = self
                new_node_added = 1
            if(cur_node.e != None and self.se == None):
                self.se = cur_node.e
                cur_node.nw = self
                new_node_added = 1
        if(self.w != None):
            cur_node = self.w
            if(cur_node.ne != None and self.nw == None):
                self.nw = cur_node.ne
                cur_node.se = self
                new_node_added = 1
            if(cur_node.se != None and self.sw == None):
                self.sw = cur_node.se
                cur_node.ne = self
                new_node_added = 1
        if(self.nw != None):
            cur_node = self.nw
            if(cur_node.sw != None and self.w == None):
                self.w = cur_node.sw
                cur_node.e = self
                new_node_added = 1
            if(cur_node.e != None and self.ne == None):
                self.ne = cur_node.e
                cur_node.sw = self
                new_node_added = 1
        if(self.ne != None):
            cur_node = self.ne
            if(cur_node.w != None and self.nw == None):
                self.nw = cur_node.w
                cur_node.se = self
                new_node_added = 1
            if(cur_node.se != None and self.e == None):
                self.e = cur_node.se
                cur_node.w = self
                new_node_added = 1
        if(new_node_added == 1):
            self.check_neighbors()
        return

    def flip(self):
        if(self.data == 0):
            self.data = 1
        else:
            self.data = 0

class HexGrid:
    def __init__(self, size = 10):
        self.reference_node = HexNode()
        self.current_node = self.reference_node
        self.running_total = 0

    def process(self):
        f = open("C:\Directory\Advent of Code 2022\Practice\input.txt", "r")
        for line in f.readlines():
            if(line != '\n'):
                self.current_node = self.reference_node
                while(line != '\n'):
                    line = self.process_line(line)
                self.current_node.flip()
                if(self.current_node.data == 0):
                    self.running_total -= 1
                else: 
                    self.running_total += 1
            print(self.running_total)
                

    def process_line(self, line):
        if(line[0] == 'e'):
            if(self.current_node.e == None):
                self.current_node.e = HexNode(w=self.current_node)
                self.current_node.check_neighbors()
            self.current_node = self.current_node.e
            return line[1:]
        elif(line[0] == 'w'):
            if(self.current_node.w == None):
                self.current_node.w = HexNode(e=self.current_node)
                self.current_node.check_neighbors()
            self.current_node = self.current_node.w
            return line[1:]
        elif(line[0:2] == 'se'):
            if(self.current_node.se == None):
                self.current_node.se = HexNode(nw=self.current_node)
                self.current_node.check_neighbors()
            self.current_node = self.current_node.se
            return line[2:]
        elif(line[0:2] == 'sw'):
            if(self.current_node.sw == None):
                self.current_node.sw = HexNode(ne=self.current_node)
                self.current_node.check_neighbors()
            self.current_node = self.current_node.sw
            return line[2:]
        elif(line[0:2] == 'nw'):
            if(self.current_node.nw == None):
                self.current_node.nw = HexNode(se=self.current_node)
                self.current_node.check_neighbors()
            self.current_node = self.current_node.nw
            return line[2:]
        elif(line[0:2] == 'ne'):
            if(self.current_node.ne == None):
                self.current_node.ne = HexNode(sw=self.current_node)
                self.current_node.check_neighbors()
            self.current_node = self.current_node.ne
            return line[2:]
        else:
            print('error')

if __name__ == "__main__":
   hexgrid = HexGrid()
   hexgrid.process()