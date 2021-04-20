from model import Graph

class Controller():
    def __init__(self, input_graph=None):
        if input_graph = None:
            self.graph = Graph()
        else:
            #TODO make graph

if __name__ == '__main__':
    graph = Graph()

    graph.add_edge('A', 'B')

    graph.print_graph()
