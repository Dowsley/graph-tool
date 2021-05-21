from itertools import chain
from functools import reduce

class Graph:
    """Represents a Graph using a dictionary. All of its methods
    behave differently based on whether the graph is directed/weighted or not.

    Attributes:
        graph (dictionary): Represents the graph structure. Initializes as empty dict.
        directed (bool, optional): Tells if the graph is weighted or not. Defaults to True.
        weighted (bool, optional): Tells if the graph is weighted or not. Defaults to False.
    """
    def __init__(self, directed=True, weighted=False):
        self.graph = {}
        self.directed = directed
        self.weighted = weighted

    def add_edge(self, src, dest, weight=None):
        """ Adds an edge based on source and destination nodes.

        Args:
            src (str): Source node data.
            dest (str): Destination node data.
            weight (int, optional): Weight for weighted graphs.

        Returns:
            bool: Whether if the operation was sucessful or not.
        """

        # Type guarantee
        src = str(src)
        dest = str(dest)

        # Check if it doesnt create parallels
        if dest in self.graph:
            if any(src in e for e in self.graph[dest]):
                return False

        new_edge = (dest, weight) if self.weighted else (dest,)
        try:
            # Check if destinity already exists
            if new_edge in self.graph[src]:
                return False


            # DEFAULT: Passed
            self.graph[src].append(new_edge)
        except:
            self.graph[src] = [new_edge]

        if not self.directed:
            new_edge = (src, weight) if self.weighted else (src,)
            try:
                # Check if destinity already exists
                if new_edge not in self.graph[dest]:
                    self.graph[dest].append(new_edge)
            except:
                self.graph[dest] = [new_edge]

        return True

    def print_graph(self):
        """ Prints the graph in a simplified manner.

        Args: None

        Returns: None
        """

        print('*--- {} {} GRAPH ---*'.format(
            'WEIGHTED' if self.weighted else 'NON-WEIGHTED',
            'DIRECTED' if self.directed else 'NON-DIRECTED',
        ), end='\n\n')

        for vertex, edges in self.graph.items():
            print(f'Adjacent to vertex {vertex}: ', end='')

            adjacents = [f'{a} ({b[0]})' if b else a for a, *b in edges]
            print(f'[{", ".join(adjacents)}]')

    def get_order(self):
        """ Calculates the order of the graph.

        Args: None

        Returns:
            int: Order of the graph
        """

        vertices = []
        for k, v in self.graph.items():
            vertices += map(lambda x: x[0], v)
            vertices.append(k)

        order = len(list(dict.fromkeys(vertices)))

        return order

    def get_size(self):
        """ Calculates the size of the graph.

        Args: None

        Returns:
            int: Size of the graph
        """

        sum_degrees = 0
        for v in self.graph.values():
            sum_degrees += len(v)

        return sum_degrees if self.directed else sum_degrees / 2

    def adjacency(self, v1, v2):
        """ Check whether two given vertices are adjacent or not.

        Args:
            v1 (str): Source node data.
            v2 (str): Destination node data.

        Returns:
            bool: Whether two vertices are adjacent or not.
        """

        # Type guarantee
        v1 = str(v1)
        v2 = str(v2)

        is_adjacent = False

        if v1 in self.graph:
            is_adjacent = v2 in map(lambda x: x[0], self.graph[v1])
        elif v2 in self.graph:
            is_adjacent = v1 in map(lambda x: x[0], self.graph[v2])

        return is_adjacent

    def get_degree(self, vertex):
        """ Calculates the degree of a given vertex.

        Args:
            vertex (str): Vertex data/key.

        Returns:
            Tuple (int, int:optional): If it's directed, (ingoing_degree, outgoing_degree).
                                       Else returns (total_degree, None).
        """

        # Type guarantee
        vertex = str(vertex)

        # CASE 1: Directed
        if self.directed:
            try:
                outgoing = len(self.graph[vertex])
            except:
                outgoing = 0

            ingoing = list(map(
                lambda x: x[0],
                list(chain(*self.graph.values()))
            )).count(vertex)

            return (ingoing, outgoing)

        # CASE 2: Undirected
        return (
            len(self.graph[vertex]),
            None
        )

    def get_adjacents(self, vertex):
        """ Gets the adjacent vertices of a given vertex.

        Args:
            vertex (str): Vertex data/key.

        Returns:
            Tuple (list of any, list of any:optional):
                If it's directed, (ingoing_adjacents, outgoing_adjacents).
                Else returns (all_adjacents, None).
        """

        # Type guarantee
        vertex = str(vertex)

        # CASE 1: Directed
        if self.directed:
            try:
                outgoing = list(map(lambda x: x[0], self.graph[vertex]))
            except:
                outgoing = []

            ingoing = []
            for k, v in self.graph.items():
                if any(vertex in t for t in v):
                    ingoing.append(k)

            return (ingoing, outgoing)

        # CASE 2: Undirected
        return (
            list(map(lambda x: x[0], self.graph[vertex])),
            None
        )

    def dijkstra_table(self, origin):
        """ Performs dijkstra algorithm and returns a table with the result.

        Args:
            origin (str): Vertex data/key to calculate shortest distances from.

        Returns:
            dictionary: 
                Each key will be a different vertex of the graph. The value is a list of 
                (shortest distance to origin, previous_vertex)
        """

        # STEP 0: Initialization
        visited = []
        if not self.directed:
            unvisited = list(self.graph.keys())
        else:
            unvisited = list(dict.fromkeys(
                list(self.graph.keys()) +
                [x[0] for x in list(chain(*self.graph.values()))]
            ))
        
        table = {}
        for key in unvisited:
            if key == origin:
                table[key] = [0, None]
            else:
                table[key] = [float('inf'), None] # first term is infinity


        # BEGIN PROCEDURE
        while (unvisited):
            # STEP 1: Visit the unvisited vertex with the 
            # smallest known distance from the start vertex.
            curr_v = None
            for v in unvisited:
                weight = table[v][0]
                if curr_v == None:
                    curr_v = (v, weight)
                elif weight < curr_v[1]:
                    curr_v = (v, weight)
            curr_v = curr_v[0]

            # STEP 2: For the current vertex, calculate the distance of each
            # neighbor from the start vertex. For each neighbor, if the calculated distance
            # is less than its known distance, update the neighbor's shortest distance 
            # and previous vertice. After that, set current vertex as visited. 
            if not self.directed:
                for neighbor, weight in self.graph[curr_v]:
                    calc_dist = weight + table[curr_v][0]
                    if calc_dist < table[neighbor][0]:
                        table[neighbor][0] = weight + table[curr_v][0] # update distance
                        table[neighbor][1] = curr_v # set 'previous vertice' too
            else:
                try:
                    connections = self.graph[curr_v]
                except:
                    visited.append(curr_v)
                    unvisited.remove(curr_v)
                    continue

                for neighbor, weight in connections:
                    calc_dist = weight + table[curr_v][0]
                    if calc_dist < table[neighbor][0]:
                        table[neighbor][0] = weight + table[curr_v][0] # update distance
                        table[neighbor][1] = curr_v # set 'previous vertice' too
            
            visited.append(curr_v)
            unvisited.remove(curr_v)
        
        filtered_table = {}
        for k, v in table.items():
            if v[0] != float('inf'):
                filtered_table[k] = v
        return filtered_table

if __name__ == '__main__':
    print("Running test script")

    graph = Graph(directed=True, weighted=True)

    graph.add_edge('A', 'B', 5)
    graph.add_edge('A', 'D', 1)
    graph.add_edge('B', 'C', 1)
    graph.add_edge('A', 'C', 8)
    graph.add_edge('D', 'B', 1)
    
    print(graph.graph)
    graph.print_graph()

    print(graph.get_degree('C'))
    print(graph.dijkstra_table('C'))