import json
from model import Graph

def new_graph(Graph):
    """Creates a Graph based in a Json file with user's inputs.

    Args: 
        Graph (object): Graph Object

    Returns: 
        graph_dict (dict): Dictionary with resulting Graph 
    """
    
    if  data['state']['weighted']:
        for i,j in data['changes']['new_edges']:
            graph.add_edge(i[0], i[1], j)
    else:
        for i,j in data['changes']['new_edges']:
            graph.add_edge(i[0], i[1])

    graph_dict = vars(graph)
    graph_dict["size"] = graph.get_size()
    graph_dict["order"] = graph.get_order()
    
    return graph_dict

def change_graph(Graph):
    """Makes requested changes in an existing Graph based in a Json file.

    Args: 
        Graph (object): Graph Object

    Returns: 
        graph_dict (dict): Dictionary with resulting Graph 
    """

    graph.graph = data['state']['graph']

    if  data['state']['weighted']:
        for i, j in data['changes']['new_edges']:
            graph.add_edge(i[0], i[1], j)
    else:
        for i, j in data['changes']['new_edges']:
            graph.add_edge(i[0], i[1])

    graph_dict = vars(graph)
    graph_dict["size"] = graph.get_size()
    graph_dict["order"] = graph.get_order()
    
    return graph_dict