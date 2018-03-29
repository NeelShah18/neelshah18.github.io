from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    result = {"ans": "Hello, world"}
    return jsonify(result)

@app.route('/name')
def neel():
    result = {"ans": "shah"}
    return jsonify(result)

if __name__=='__main__':
    app.run(debug=True)
