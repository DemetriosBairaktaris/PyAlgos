class Graph(object):


    def __init__(self,number_of_verticies):
        self.adj_list = None
        self.___addVerticies(number_of_verticies)

    def ___addVerticies(self, number_of_verticies):
        self.adj_list = {i: list() for i in range(number_of_verticies + 1)}

    def addEdge(self, v1, v2):
        couldAddEdge = False
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            couldAddEdge = True
        return couldAddEdge

    def __contains__(self, edgePairTuple):
        v1, v2 = edgePairTuple[0], edgePairTuple[1]
        containsEdge = False
        if v1 in self.adj_list and v2 in self.adj_list:
            containsEdge = True if v2 in self.adj_list[v1] else False
        return containsEdge

    def __str__(self):
        return str(self.adj_list)


class Search(object):
    def __init__(self,graph):
        self.graph = graph
        self.___marked = []

    def dfs(self):
        verticies = [v for v in graph]
        def recurse(v):
            if v not in self.___marked:
                self.___marked.append(v)
                pass #todo finish this
def main():
    g = Graph()
    g.addVerticies(10)
    print str(g)
    g.addEdge(1, 2)
    g.addEdge(2, 4)
    print g
    print (1, 2) in g
    print (2, 1) in g
    print (200, 2) in g
if __name__ == '__main__':
    main()