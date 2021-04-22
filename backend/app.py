from flask import Flask, request, jsonify
from application.function import new_graph, change_graph
from application.model import Graph
import json

app = Flask(__name__)

@app.route('/', methods=['POST', ])
def handle_graph():
    request_json = request.get_json()

    data = json.load(request_json)

    graph = Graph(
                weighted=data['state']['weighted'],
                directed=data['state']['directed']
            )

    graph_dict = {}

    if data['state']['graph'] == None:
        # Since the condition is true, we can create a new Graph.
        return jsonify(new_graph(graph))

    elif 'new_edges' in data['changes'].keys():
        # Since the condition is true, we can execute the request's changes.
        return jsonify(change_graph(graph))

    elif data['changes']['adjacency']:
        # Since the condition is true, we can create a dict that's confirm if the two vertices are adjacents.
        graph.graph = data['state']['graph']
        temp = data['changes']['adjacency']
        graph_dict['adjacency'] = graph.adjacency(temp[0], temp[1])
        return jsonify(graph_dict)

    elif data['changes']['get_degree']:
        # Since the condition is true, we can create a dict with vertex's degree.
        graph.graph = data['state']['graph']
        temp = data['changes']['get_degree']
        graph_dict['degree'] = graph.get_degree(temp)
        return jsonify(graph_dict)

    elif data['changes']['get_adjacents']:
        # Since the condition is true, we can create a dict with all adjacents vertices.
        graph.graph = data['state']['graph']
        temp = data['changes']['get_adjacents']
        graph_dict['adjacents'] = graph.get_adjacents(temp)
        return jsonify(graph_dict)

if __name__ == '__main__':
    app.run(debug=True)