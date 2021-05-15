from flask import Flask, render_template, request, jsonify
from functions import plus, minus, multiply, divide
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/healthz", methods=["GET"])
def healthCheck():
    return "", 200

@app.route("/plus", methods=["GET"])
def add():
    x = request.args.get("x")
    y = request.args.get("y")
    if x.isdigit() and y.isdigit():
        result = plus(x, y)
        tmp_result = f"{x} + {y} = {result}"
        response = jsonify(tmp_result)
    else:
        response = jsonify("BAD REQUSET ERROR")
    return response
@app.route("/minus", methods=["GET"])
def substract():
    x = request.args.get("x")
    y = request.args.get("y")
    if x.isdigit() and y.isdigit():
        result = minus(x, y)
        tmp_result = f"{x} - {y} = {result}"
        response = jsonify(tmp_result)
    else:
        response = jsonify("BAD REQUSET ERROR")
    return response

@app.route("/multiply", methods=["GET"])
def multiple():
    x = request.args.get("x")
    y = request.args.get("y")
    if x.isdigit() and y.isdigit():
        result = multiply(x, y)
        tmp_result = f"{x} * {y} = {result}"
        response = jsonify(tmp_result)
    else:
        response = jsonify("BAD REQUSET ERROR")
    return response

@app.route("/divide", methods=["GET"])
def division():
    x = request.args.get("x")
    y = request.args.get("y")
    if x.isdigit() and y.isdigit():
        result = divide(x, y)
        tmp_result = f"{x} / {y} = {result}"
        response = jsonify(tmp_result)
    else:
        response = jsonify("BAD REQUSET ERROR")
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
