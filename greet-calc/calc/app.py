from flask import Flask, request

app = Flask(__name__)

@app.route('/add')
def add():
    a = int(request.args["a"])
    b = int(request.args["b"])

    result = a + b
    return f"<h1>{result}</h1>"

@app.route('/sub')
def sub():
    a = int(request.args["a"])
    b = int(request.args["b"])

    result = a - b
    return f"<h1>{result}</h1>"

@app.route('/mult')
def mult():
    a = int(request.args["a"])
    b = int(request.args["b"])

    result = a * b
    return f"<h1>{result}</h1>"

@app.route('/div')
def div():
    a = int(request.args["a"])
    b = int(request.args["b"])

    result = a / b
    return f"<h1>{result}</h1>"
