class Graph(object):
    def __init__(self, number_of_vertices):
        self.adj_list = None

        def add_vertices(number_of_vertices):
            self.vertices = {v for v in range(number_of_vertices)}
            self.adj_list = {i: list() for i in self.vertices}

        add_vertices(number_of_vertices)

    def __contains__(self, edge_pair):
        v1, v2 = edge_pair[0], edge_pair[1]
        containsEdge = False
        if v1 in self.adj_list and v2 in self.adj_list:
            containsEdge = True if v2 in self.adj_list[v1] else False
        return containsEdge

    def __str__(self):
        return str(self.adj_list)

    def add_edge(self, v1, v2):
        couldAddEdge = False
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            couldAddEdge = True
        return couldAddEdge


class Search(object):
    def __init__(self, graph):
        self.graph = graph

    def _validate_input(self,vertex1,vertex2):
        return not False in [vertex in self.graph.vertices for vertex in (vertex1,vertex2)]

    def connection(self, vertex1, vertex2):
        #dfs implementation (recursive)
        if not self._validate_input(vertex1,vertex2):
            return False
        marked = set()

        def dfs(vertex):
            if vertex not in marked:
                marked.add(vertex)
                for adj_vertex in self.graph.adj_list[vertex]:
                    dfs(adj_vertex)

        dfs(vertex1)
        return vertex1 in marked and vertex2 in marked

    def connection_1(self,vertex1,vertex2):
        #BFS implementation
        isConnection = False
        if self._validate_input(vertex1,vertex2):
            vertex_queue = list()
            marked_set = set()
            vertex_queue.append(vertex1)

            while len(vertex_queue) > 0:
                current_vertex = vertex_queue.pop()
                if current_vertex not in marked_set:
                    marked_set.add(current_vertex)
                    if current_vertex is vertex2:
                        isConnection = True
                        break
                    else:
                        [vertex_queue.append(v) for v in self.graph.adj_list[current_vertex]]
        return isConnection



def main():
    import random
    number_vertices = 100
    g = Graph(number_vertices)
    print str(g)
    edges = []
    for x in range(200):
        edge = (random.choice(range(number_vertices)),random.choice(range(number_vertices)))
        g.add_edge(edge[0],edge[1])
        edges.append(edge)
    print g

    search = Search(g)
    for edge in edges:
        print search.connection(edge[0],edge[1])
        print search.connection_1(edge[0],edge[1])
        #should all be true
    #should be false
    print search.connection_1(2000,200)

if __name__ == '__main__':
    main()
