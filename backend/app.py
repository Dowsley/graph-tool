from flask import Flask
from flask import request

from application.model import Graph

app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_graph():
    request_json = request.get_json()

    return "Hello World!"

if __name__ == '__main__':
    app.run()
