from flask import Flask,jsonify,request
app = Flask(__name__)

todos = [{"label":"My first task", "done":False}]

@app.route('/todos',methods=['GET'])
def hello_world():
    response = jsonify(todos)
    return response

@app.route('/todos',methods=['POST'])
def add_new_todo():
    request_body=request.json
    print("Incoming request with the following body",request_body)
    todos.append(request_body)
    response = jsonify(todos)
    return response

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:",position)
    todos.pop(position)
    response = jsonify(todos)
    return response

# These two lines should always be at the end of your app.py file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
