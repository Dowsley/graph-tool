class Node():
    """
    Represents the adjacency list of the node

    Input Arguments: data"""
    def __init__(self, data):
        self.vertex = data
        self.next = None

class Graph:
    def __init__(self, num_vertices):
        self.V = num_vertices
        self.graph = [None] * self.V

if __name__ == '__main__':
    print("Running test script")
