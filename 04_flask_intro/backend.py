from flask import Flask, request

app = Flask(__name__)


@app.route("/")
@app.route("/greeting")
def greet():
    _greeting = {"greeting": "Hello, world!"}
    return _greeting


@app.route("/greeting/<user>")
def greet_user(user):
    _response = {"greeting": "Hello", "user": user}
    return _response


@app.route("/math/sum", methods=["POST"])
def add_by_api():
    _to_add = request.form.getlist("add")
    _all_addable = all(n.isnumeric() for n in _to_add)
    if _all_addable and _to_add is not None:
        _sum = sum(float(n) for n in _to_add)
        return {"sum": _sum}, 200
    else:
        return 'Bad request', 400