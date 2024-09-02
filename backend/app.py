# backend/app.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/todos', methods=['GET'])
def get_todos():
    todos = [
        {"id": 1, "task": "Learn Docker", "done": False},
        {"id": 2, "task": "Build a React app", "done": False}
    ]
    return jsonify(todos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
