from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from model import Graph

app = Flask(__name__)
cors = CORS(app, resources={r'/': {"origins": "http://localhost:3000"}})

@app.route('/', methods=['POST', ])
@cross_origin()
def handle_graph():
    data = request.get_json()

    graph = Graph(
        weighted=data['state']['weighted'],
        directed=data['state']['directed'],
    )
    graph.graph = data['state']['graph'] if data['state']['graph'] else {}

    if data['changes']['new_edges']:
        if data['state']['weighted']:
            for i, j in data['changes']['new_edges']:
                graph.add_edge(i[0], i[1], j)
        else:
            for i, j in data['changes']['new_edges']:
                graph.add_edge(i[0], i[1])
        
    res = vars(graph)
    
    if data['changes']['adjacency']:
        temp = data['changes']['adjacency']
        res['adjacency'] = graph.adjacency(temp[0], temp[1])
    
    if data['changes']['get_degree']:
        temp = data['changes']['get_degree']
        res['degree'] = graph.get_degree(temp)

    if data['changes']['get_adjacents']:
        temp = data['changes']['get_adjacents']
        res['adjacents'] = graph.get_adjacents(temp)

    if data['changes']['dijkstra_table']:
        res["dijkstra_table"] = graph.dijkstra_table(
            data['changes']['dijkstra_table']
        )
        print(res['dijkstra_table'])

    res["size"] = graph.get_size()
    res["order"] = graph.get_order()
    
    return jsonify(res)
    

if __name__ == '__main__':
    app.run(debug=True)