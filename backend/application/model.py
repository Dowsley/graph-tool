from itertools import chain

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


if __name__ == '__main__':
    print("Running test script")

    graph = Graph(directed=False)

    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('B', 'C')

    graph.print_graph()
    print(graph.get_order())

    print(graph.get_size())

    print(graph.adjacency('E', 'A'))

    print(graph.get_degree('C'))

    print(graph.get_adjacents('A'))
